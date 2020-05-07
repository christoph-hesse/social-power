# =====================================================================
# Oppressive Speech Simulation
# Author: Christoph Hesse (Apr 2020)
# 3-strategy Nash demand game with dynamic disagreement point updates
# Based on the Nash demand game (1950) and inspired by
# Travis LaCroix & Cailin O'Connor (2018)
# =====================================================================

# A population of agents is initialized for each run of the simulation.
# Each agent is a set of attributes which characterize it:
# 0) an index which identifies group membership
# 1) the first move, which initially (before learning) is random
# 2) the expected payoff, which initially is random
# 3) the memory of what they themselves did in the past m interactions, which initially has the random starting move
# 4) the memory of what the other agents did in the past m interactions, which has the random starting move
# 5) power groups (1 = non-racist g1, 2 = g2, 3 = racist individuals g3)
# 6) the memory of what other in-group agents did in the past m interactions
# 7) the memory of what out-group agents did in the past m interactions

# 8) the likelihood of racism (between 0 = not racist and 1 = racist)
# racists are more likely to slur; a slur is a performative utterance which reduces the disagreement point of the one insulted
# 9) popularity which is the weight that agent has as a juror/audience member

# =====================================================================
# Simulation parameters
# =====================================================================
class par:
	trials = 100# number of interaction rounds per simulation
	r = 0# round counter init
	print_rounds = False# print output for each interaction
	print_rewards = False# print summary output at the end of simulation

	# population size N
	N = 10# 10, 20, 40, 100
	N1 = 4#N/2
	N2 = 5#N/2
	N3 = 1# powerful individuals / racists

	# disagreement points (consulation prizes) for player 1 and 2
	d1 = 4# 3
	d2 = 4# 3
	d3 = 4# 4.5
	d_sampling = 'constant'# sampling method: constant value, normal distribution with mean, power function
	d_sd = 1.5# standard deviation for when disagreement points are normally random samples

	# groups' propensity for racism
	r1 = 0
	r2 = 0
	r3 = 1
	r_sampling = 'constant'# sampling method: constant value, normal distribution with mean, power function
	r_sd = 1.5# standard deviation for when rs are normally random samples

	# groups' popularity
	pop1 = 1
	pop2 = 1
	pop3 = 1
	pop_sampling = 'constant'# sampling method: constant value, normal distribution with mean, power function
	pop_sd = 1.5# standard deviation for when popularity indices are normally random samples

	# total resource R
	R = 10

	# diviation from M
	di = 1

	# possible demands
	H = R/2 + di
	M = R/2
	L = R/2 - di

	# memory length m
	m = 4# 5, 10, 15, 20
	group_mem = True# whether agents have separate memories for in-group and out-group interactions

	method = 'both'# 'both' = agents from population regardless of group membership, 'inter' one agent from each group

	slur_str = 0.5# slur strength = the amount by which the disagreement point of the agent insulted is reduced
	slurring = 'before'# if slurring happens, it happens before/after selecting the best response; set to 'none' to deactivate slurring

	audience_size = N-2
	aud_str = 1# strength of audience scores on disagreement point updates

	# Other things that need to be initialized: Payoff matices and everything for logging data for export to csv later
	strategies = [
		[# g1/g1
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d1,d1]],
			[[H,L],[d1,d1],[d1,d1]]
		],
		[# g2/g2
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d2,d2]],
			[[H,L],[d2,d2],[d2,d2]]
		],
		[# g1/g2
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d1,d2]],
			[[H,L],[d1,d2],[d1,d2]]
		],
		[# g2/g1
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d2,d1]],
			[[H,L],[d2,d1],[d2,d1]]
		]
	]	

	# best response history
	resp_hist_g1 = []
	resp_hist_g2 = []
	resp_hist_g3 = []
	resp_hist_g1_g1 = []# when the two agents interacting are both from group 1
	resp_hist_g2_g2 = []# when they are both from group 2
	resp_hist_g1_g2 = []# from different groups; first agent in vector is always group 1, other group 2
	g1_d1_hist = []
	g1_d2_hist = []
	g2_d1_hist = []
	g2_d2_hist = []
	g3_d1_hist = []
	g3_d2_hist = []
	agent_pop0 = []# population of agents at the beginning of the simulation
	agent_pop1 = []# population of agents at the end of the simulation

# =====================================================================
# Actual simulation
# =====================================================================
import numpy as np
import random
import csv

def matrix(L,M,H,d1,d2):
	moves = [
		[# g1/g1
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d1,d1]],
			[[H,L],[d1,d1],[d1,d1]]
		],
		[# g2/g2
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d2,d2]],
			[[H,L],[d2,d2],[d2,d2]]
		],
		[# g1/g2
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d1,d2]],
			[[H,L],[d1,d2],[d1,d2]]
		],
		[# g2/g1
			[[L,L],[L,M],[L,H]],
			[[M,L],[M,M],[d2,d1]],
			[[H,L],[d2,d1],[d2,d1]]
		]
	]
	return(moves)

def sampling(value,sd,group_size,method):
	if method == 'constant':
		y = [value for n in range(0,group_size)]
	if method == 'normal':
		y = [norm(par,value,sd) for n in range(0,group_size)]
	if method == 'power':
		y = [value for n in range(0,group_size)]
	if method == 'uniform':
		y = [random.uniform(value,sd) for n in range(0,group_size)]
	return(y)

def create_pop(par):
	agents = []
	d1s = sampling(par.d1,par.d_sd,par.N1,par.d_sampling)
	d2s = sampling(par.d2,par.d_sd,par.N2,par.d_sampling)
	d3s = sampling(par.d3,par.d_sd,par.N3,par.d_sampling)
	r1s = sampling(par.r1,par.r_sd,par.N1,par.r_sampling)
	r2s = sampling(par.r2,par.r_sd,par.N2,par.r_sampling)
	r3s = sampling(par.r3,par.r_sd,par.N3,par.r_sampling)
	pop1s = sampling(par.pop1,par.pop_sd,par.N1,par.pop_sampling)
	pop2s = sampling(par.pop2,par.pop_sd,par.N2,par.pop_sampling)
	pop3s = sampling(par.pop3,par.pop_sd,par.N3,par.pop_sampling)
	for x in range(0,int(par.N1)):# blue agents
		a = 1# 1 = blue, 2 = red, 3 = racists
		d1 = (d1s+d3s)[x]# par.d1
		d2 = d2s[x]
		r = r1s[x]
		pop = pop1s[x]
		moves = matrix(par.L,par.M,par.H,d1,d2)
		agents.append([a,[par.L,par.M,par.H][random.randint(0,2)],[par.L,par.M,par.H][random.randint(0,2)],[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],1,moves,[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],r,pop])
	for z in range(0,int(par.N3)):# powerful individuals
		a = 1
		d1 = d3s[z]# par.d3
		d2 = d2s[par.N1+z]
		r = r3s[z]
		pop = pop3s[z]
		moves = matrix(par.L,par.M,par.H,d1,d2)
		agents.append([a,[random.randint(0,2)],[random.randint(0,2)],[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],3,moves,[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],r,pop])
	for y in range(0,int(par.N2)):# red agents
		a = 2
		d1 = (d1s+par.N3*[par.d1])[y]# (d1s+d3s)[y]
		d2 = d2s[y]# par.d2
		r = r2s[y]
		pop = pop2s[y]
		moves = matrix(par.L,par.M,par.H,d1,d2)
		agents.append([a,[random.randint(0,2)],[random.randint(0,2)],[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],2,moves,[[par.L,par.M,par.H][random.randint(0,2)]],[[par.L,par.M,par.H][random.randint(0,2)]],r,pop])
	return(agents)

def pick_agents1(par):
	l = [item for item in range(0,par.N)]
	i = random.randint(0,par.N-1)
	l = [item for item in l if item not in [i]]
	j = random.randint(0,par.N-1)
	l = [item for item in l if item not in [j]]
	if len(l) == par.N-2:
		return([i,j,l])
	else:
		while len(l) == par.N-1:
			j = random.randint(0,par.N-1)
			#print(i,j)
			l = [item for item in l if item not in [j]]
		return([i,j,l])

def pick_agents2(par):
	l = [item for item in range(0,par.N)]
	i = random.randint(0,int(par.N1)+int(par.N3)-1)
	j = random.randint(int(par.N1)+int(par.N3),int(par.N1)+int(par.N2)+int(par.N3)-1)
	l = [item for item in l if item not in [i,j]]
	return([i,j,l])

# when a blue agent insults a red agent, that's lowering d2
def disagreement_update(agent,update):# g1 = 1, g2 = 2
	group = agent[0]
	L = agent[6][0][0][0][0]
	M = agent[6][0][1][0][0]
	H = agent[6][0][2][0][0]
	d1 = agent[6][2][2][2][0]# group1's disagreement point
	d2 = agent[6][2][2][2][1]# group2's disagreement point
	moves = agent[6]
	if group==1 and d1>0 and (d1+update)>0:
		moves = matrix(L,M,H,d1+update,d2)
	if group==2 and d2>0 and (d2+update)>0:
		moves = matrix(L,M,H,d1,d2+update)
	new_agent = agent[0:6]+[moves]+agent[7:len(agent)]
	return(new_agent)

def interact(par,agents):
	# interaction method either 1 = 'both' or 2 = 'inter'
	# select two different agents at random, regardless of group membership (method = 1, 'both')
	# select two different agents at random, one from each group (method = 2, 'inter')
	if par.method == 'both':
		v = pick_agents1(par)
	else:
		v = pick_agents2(par)
	agent_i = agents[v[0]]
	agent_j = agents[v[1]]
	electorate = [agents[e] for e in v[2]]
	# the audience is selected from the electorate
	# the electorate is the population minus agent_i and agent_j

	# log for print-out
	agent_i_old_ds = str([agent_i[6][2][2][2][0],agent_i[6][2][2][2][1]])
	agent_j_old_ds = str([agent_j[6][2][2][2][0],agent_j[6][2][2][2][1]])

	# if slurring happens before the best response is looked up, slurring affects the best response
	# decide whether to slur or not based on how successful it was in the past or with social standing in mind
	# propensity for racism x posterior success of sluring x repocussions for social standing
	# slurring means degrading the disagreement point of the one insulted
	slur_print = ''
	if par.slurring == 'before':
		if agent_i[0] == 1 and agent_j[0] == 2 and random.uniform(0,1) < agent_i[9]:
			agent_j = disagreement_update(agent_j,-par.slur_str)
			slur_print = ' slur'
		elif agent_i[0] == 2 and agent_j[0] == 1 and random.uniform(0,1) < agent_j[9]:
			agent_i = disagreement_update(agent_i,-par.slur_str)
			slur_print = ' slur'

	# retrieve agents' move strategies
	if agent_i[0] == 1 and agent_j[0] == 1:
		moves_i = agent_i[6][0]
		moves_j = agent_j[6][0]
	elif agent_i[0] == 2 and agent_j[0] == 2:
		moves_i = agent_i[6][1]
		moves_j = agent_j[6][1]
	elif agent_i[0] == 1 and agent_j[0] == 2:
		moves_i = agent_i[6][2]
		moves_j = agent_j[6][2]
	elif agent_i[0] == 2 and agent_j[0] == 1:
		moves_i = agent_i[6][3]
		moves_j = agent_j[6][3]

	# retrieve agents' memories
	if par.group_mem == True:# separate memories for in-group and out-group interactions
		if agent_i[0] == 1 and agent_j[0] == 1:
			mem_p1 = agent_i[7]
			mem_p2 = agent_j[7]
		elif agent_i[0] == 2 and agent_j[0] == 2:
			mem_p1 = agent_i[7]
			mem_p2 = agent_j[7]
		elif agent_i[0] == 1 and agent_j[0] == 2:
			mem_p1 = agent_i[8]
			mem_p2 = agent_j[8]
		elif agent_i[0] == 2 and agent_j[0] == 1:
			mem_p1 = agent_i[8]
			mem_p2 = agent_j[8]
	else:
		mem_p1 = agent_i[4]
		mem_p2 = agent_j[4]

	# make a bid/move/demand
	agent_i_move = [par.L,par.M,par.H][int(best_response(moves_i,0,mem_p1)[0])]# g1
	agent_j_move = [par.L,par.M,par.H][int(best_response(moves_j,1,mem_p2)[0])]# g2

	# log for print-out
	agent_i_payoff = str(best_response(moves_i,0,mem_p1)[1])
	agent_j_payoff = str(best_response(moves_j,1,mem_p2)[1])
	agent_i_best_response = str(['L','M','H'][int(best_response(moves_i,0,mem_p1)[0])])
	agent_j_best_response = str(['L','M','H'][int(best_response(moves_j,1,mem_p2)[0])])
	agent_i_slur_ds = str([agent_i[6][2][2][2][0],agent_i[6][2][2][2][1]])
	agent_j_slur_ds = str([agent_j[6][2][2][2][0],agent_j[6][2][2][2][1]])

	# update agents' memories with the bids/moves/demands just made
	if par.group_mem == True:# separate memories for in-group and out-group interactions
		if agent_i[0] == 1 and agent_j[0] == 1:
			agent_i[7] = update_memory(mem_p1,agent_j_move)
			agent_j[7] = update_memory(mem_p2,agent_i_move)
		elif agent_i[0] == 2 and agent_j[0] == 2:
			agent_i[7] = update_memory(mem_p1,agent_j_move)
			agent_j[7] = update_memory(mem_p2,agent_i_move)
		elif agent_i[0] == 1 and agent_j[0] == 2:
			agent_i[8] = update_memory(mem_p1,agent_j_move)
			agent_j[8] = update_memory(mem_p2,agent_i_move)
		elif agent_i[0] == 2 and agent_j[0] == 1:
			agent_i[8] = update_memory(mem_p1,agent_j_move)
			agent_j[8] = update_memory(mem_p2,agent_i_move)
	else:
		agent_i[4] = update_memory(mem_p1,agent_j_move)
		agent_j[4] = update_memory(mem_p2,agent_i_move)

	# record reward histories
	if agent_i[5] == 1:
		par.resp_hist_g1.append(agent_i_move)
	elif agent_i[5] == 2:
		par.resp_hist_g2.append(agent_i_move)
	elif agent_i[5] == 3:
		par.resp_hist_g3.append(agent_i_move)
	if agent_j[5] == 1:
		par.resp_hist_g1.append(agent_j_move)
	elif agent_j[5] == 2:
		par.resp_hist_g2.append(agent_j_move)
	elif agent_j[5] == 3:
		par.resp_hist_g3.append(agent_j_move)
	if agent_i[0] == 1 and agent_j[0] == 1:
		par.resp_hist_g1_g1.append([agent_i_move,agent_j_move])
	elif agent_i[0] == 2 and agent_j[0] == 2:
		par.resp_hist_g2_g2.append([agent_i_move,agent_j_move])
	elif agent_i[0] == 1 and agent_j[0] == 2:# first agent in vector is always group 1, other group 2
		par.resp_hist_g1_g2.append([agent_i_move,agent_j_move])
	elif agent_i[0] == 2 and agent_j[0] == 1:# first agent in vector is always group 1, other group 2
		par.resp_hist_g1_g2.append([agent_j_move,agent_i_move])

	if par.slurring == 'after':
		if agent_i[0] == 1 and agent_j[0] == 2 and random.uniform(0,1) < agent_i[9]:
			agent_j = disagreement_update(agent_j,-par.slur_str)
		elif agent_i[0] == 2 and agent_j[0] == 1 and random.uniform(0,1) < agent_j[9]:
			agent_i = disagreement_update(agent_i,-par.slur_str)

	# an audience is selected and they judge agents' behaviour in the interaction
	audience = random.sample(electorate,par.audience_size)	
	# each audience member compares how they think agent_i & agent_j should have behaved to how they actually behaved
	# the audience scores for agent_i and agent_j then are used to update their disagreement points in order to influence their future behaviour
	agent_i = disagreement_update(agent_i,audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par)[0])
	agent_j = disagreement_update(agent_j,audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par)[1])

	agent_i_score = audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par)[0]
	agent_j_score = audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par)[1]

	#if par.print_rounds == True:
	#	print('d pl1',str(agent_i[6][2][2][2]),'d pl2',str(agent_j[6][2][2][2]))
	# record (updated) disagreement points
	if agent_i[5] == 1:
		par.g1_d1_hist.append(agent_i[6][2][2][2][0])
		par.g1_d2_hist.append(agent_i[6][2][2][2][1])
	elif agent_i[5] == 2:
		par.g2_d1_hist.append(agent_i[6][2][2][2][0])
		par.g2_d2_hist.append(agent_i[6][2][2][2][1])
	elif agent_i[5] == 3:
		par.g3_d1_hist.append(agent_i[6][2][2][2][0])
		par.g3_d2_hist.append(agent_i[6][2][2][2][1])
	if agent_j[5] == 1:
		par.g1_d1_hist.append(agent_j[6][2][2][2][0])
		par.g1_d2_hist.append(agent_j[6][2][2][2][1])
	elif agent_j[5] == 2:
		par.g2_d1_hist.append(agent_j[6][2][2][2][0])
		par.g2_d2_hist.append(agent_j[6][2][2][2][1])
	elif agent_j[5] == 3:
		par.g3_d1_hist.append(agent_j[6][2][2][2][0])
		par.g3_d2_hist.append(agent_j[6][2][2][2][1])

	agents[v[0]] = agent_i
	agents[v[1]] = agent_j

	# log for print-out
	agent_i_new_ds = str([agent_i[6][2][2][2][0],agent_i[6][2][2][2][1]])
	agent_j_new_ds = str([agent_j[6][2][2][2][0],agent_j[6][2][2][2][1]])

	if par.print_rounds == True:
		print('R',str(par.r),'Pl('+str(v[0])+','+str(v[1])+')','Gr('+str(agent_i[0])+','+str(agent_j[0])+')',
			#'M',str(mem_p1),str(mem_p2),'Pa',agent_i_payoff,agent_j_payoff,
			'BR('+agent_i_best_response+agent_j_best_response+')',
			'dO',agent_i_old_ds,agent_j_old_ds,'dN',agent_i_new_ds,agent_j_new_ds,
			'AS('+str(agent_i_score)+','+str(agent_j_score)+')'# audience score of agent_i, agent_j
			+slur_print)
	return(agents)

def weighted_average(ratings,weights):
	w_avrg = sum([ratings[i]*weights[i] for i in range(0,len(ratings))])/sum(weights)
	return(w_avrg)

def audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par):
		i_ratings, j_ratings = [], []
		for a in audience:
			if random.uniform(0,1) < a[9]:# racist audience members side with their own kind with the same likelihood as slurring
				if agent_i[0] == 1 and agent_j[0] == 1:
					mat = 0
					mem = 7
				elif agent_i[0] == 2 and agent_j[0] == 2:
					mat = 1
					mem = 8#7
				elif agent_i[0] == 1 and agent_j[0] == 2:
					mat = 2# racists' higher disagreement point results in more aggressive bargaining
					mem = 8
				elif agent_i[0] == 2 and agent_j[0] == 1:
					mat = 3# racists' higher disagreement point results in more aggressive bargaining
					mem = 8
			else:# non-racists treat out-group as in-group
				if a[0] == 1:
					mat = 0
				else:
					mat = 1
				mem = 7
			e_agent_i_move = [par.L,par.M,par.H][int(best_response(a[6][mat],0,a[mem])[0])]
			e_agent_j_move = [par.L,par.M,par.H][int(best_response(a[6][mat],1,a[mem])[0])]
			e_i_rating = e_agent_i_move - agent_i_move# amount by which disagreement point of agent_i should be raised/lowered
			e_j_rating = e_agent_j_move - agent_j_move# amount by which disagreement point of agent_j should be raised/lowered
			i_ratings.append(par.aud_str*e_i_rating)
			j_ratings.append(par.aud_str*e_j_rating)
		weights = [member[10] for member in audience]# more popular audience member get a bigger say
		# weighted average, weighted according to popularity
		i_rating = weighted_average(i_ratings,weights)
		j_rating = weighted_average(j_ratings,weights)
		return(i_rating,j_rating)

def update_memory(memory,new):
	memory = memory + [new]
	if len(memory) > int(par.m):
		memory = memory[1:int(par.m)+1]
	return(memory)

def simulate(par):# run one simulation, i.e. par.trials number of interactions amongs a population of agents
	par.resp_hist_g1 = []
	par.resp_hist_g2 = []
	par.resp_hist_g3 = []
	par.resp_hist_g1_g1 = []
	par.resp_hist_g2_g2 = []
	par.resp_hist_g1_g2 = []
	par.g1_d1_hist = []
	par.g1_d2_hist = []
	par.g2_d1_hist = []
	par.g2_d2_hist = []
	par.g3_d1_hist = []
	par.g3_d2_hist = []
	par.r = 0
	par.agent_pop0 = []
	par.agent_pop1 = []

	agents = create_pop(par)# create a population of agents
	par.agent_pop0 = agents
	for t in range(0,par.trials):# make the agents interact for par.trials
		par.r += 1
		agents = interact(par,agents)
		par.agent_pop1 = agents
	if par.print_rewards == True:
		print('Best responses gr1',str([sum([1 for x in par.resp_hist_g1 if x == i]) for i in [par.L,par.M,par.H]]),
			'gr2',str([sum([1 for x in par.resp_hist_g2 if x == i]) for i in [par.L,par.M,par.H]]))
		print('Best responses gr1|gr1','('+str(len(par.resp_hist_g1_g1))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [y for x in par.resp_hist_g1_g1 for y in x] if z == i]) for i in [par.L,par.M,par.H]]),
			'gr2|2','('+str(len(par.resp_hist_g2_g2))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [y for x in par.resp_hist_g2_g2 for y in x] if z == i]) for i in [par.L,par.M,par.H]]),
			'gr1/2','('+str(len(par.resp_hist_g1_g2))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [x[0] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]),str([sum([1 for z in [x[1] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]),
			'd1/2 gr1',str([np.median(par.g1_d1_hist),np.median(par.g1_d2_hist)]),
			'd1/2 gr2',str([np.median(par.g2_d1_hist),np.median(par.g2_d2_hist)])
			)
		if par.N3 > 0:
			print('Powerful',str(np.median(par.resp_hist_g3)),'('+str(len(par.resp_hist_g3))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for x in par.resp_hist_g3 if x == i]) for i in [par.L,par.M,par.H]]),
				'd1/2 gr3',str([np.median(par.g3_d1_hist),np.median(par.g3_d2_hist)])
				)
			print('Final disagreement points: gr1',str(disagreement_points(par.agent_pop1)[0]),'('+str(sum(disagreement_points(par.agent_pop1)[0])/len(disagreement_points(par.agent_pop1)[0]))+','+str(np.median(disagreement_points(par.agent_pop1)[0]))+')','gr2',str(disagreement_points(par.agent_pop1)[1]),'('+str(sum(disagreement_points(par.agent_pop1)[1])/len(disagreement_points(par.agent_pop1)[1]))+','+str(np.median(disagreement_points(par.agent_pop1)[1]))+')','gr3',str(disagreement_points(par.agent_pop1)[2]),'('+str(sum(disagreement_points(par.agent_pop1)[2])/len(disagreement_points(par.agent_pop1)[2]))+','+str(np.median(disagreement_points(par.agent_pop1)[2]))+')')
		else:
			print('Final disagreement points: gr1',str(disagreement_points(par.agent_pop1)[0]),'('+str(sum(disagreement_points(par.agent_pop1)[0])/len(disagreement_points(par.agent_pop1)[0]))+','+str(np.median(disagreement_points(par.agent_pop1)[0]))+')','gr2',str(disagreement_points(par.agent_pop1)[1]),'('+str(sum(disagreement_points(par.agent_pop1)[1])/len(disagreement_points(par.agent_pop1)[1]))+','+str(np.median(disagreement_points(par.agent_pop1)[1]))+')')
		print('Strategies: gr1/2('+str(np.median(par.resp_hist_g1[-10:]))+','+str(np.median(par.resp_hist_g2[-10:]))+')')

def disagreement_points(population):
	gr1, gr2, gr3 = [], [], []
	for a in population:
		if a[0]==1 and a[-2]!=1:# if group1: non-racist blue
			gr1.append(a[6][2][2][2][0])
		elif a[0]==2 and a[-2]!=1:# if group2: red
			gr2.append(a[6][2][2][2][1])
		else:# if group3: racist
			gr3.append(a[6][2][2][2][0])
	return(gr1,gr2,gr3)

def multi_sim(par,number,filename,print_results,save_results):
	output = []
	for n in range(0,number):
		simulate(par)
		output.append([par.N1,par.N2,par.N3,# group sizes
			par.d1,par.d2,par.d3,# initial disagreement points
			par.slur_str,# slur strength
			par.aud_str,# audience strength
			int(np.median(par.resp_hist_g1[-10:])),int(np.median(par.resp_hist_g2[-10:])),# Nash equilibrium
			np.median(disagreement_points(par.agent_pop1)[0]),np.median(disagreement_points(par.agent_pop1)[1]),np.median(disagreement_points(par.agent_pop1)[2])# final disagreement points
			])
	print('Done!')
	if print_results == True:
		print('N1'+'\t'+'N2'+'\t'+'N3'+'\t'+'ini_d1'+'\t'+'ini_d2'+'\t'+'ini_d3'+'\t'+'sl_str'+'\t'+'aud_str'+'\t'+'strat1'+'\t'+'strat2'+'\t'+'fin_d1'+'\t'+'fin_d2'+'\t'+'fin_d3')
		for i in output:
			print(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\t'+str(i[6])+'\t'+str(i[7])+'\t'+str(i[8])+'\t'+str(i[9])+'\t'+str(i[10])+'\t'+str(i[11])+'\t'+str(i[12]))
	if save_results == True:
		header = ['N1','N2','N3','ini_d1','ini_d2','ini_d3','sl_str','aud_str','strat1','strat2','fin_d1','fin_d2','fin_d3']
		with open('csv/'+str(filename)+'.csv', 'wt') as f:
		    csv_writer = csv.writer(f,delimiter=',')
		    csv_writer.writerow(header) # write header
		    for row in output:
		    	csv_writer.writerow(row)
	#return(output)

def iter_value(par,value,iterations):# run a simulation per iteration of a parameter (iterations = [x,y,z], x = start value, y = end value, z = step size)
	ty = type(getattr(par,str(value)))
	for i in [float(x)/(1/iterations[2]) for x in range(int(iterations[0]),int(iterations[1]*(1/iterations[2]))+1)]:
		if ty is int:
			setattr(par,str(value),int(i))
		if ty is float:
			setattr(par,str(value),float(i))
		print(str(value),'=',str(i))
		simulate(par)
	print('Done!')

def prob(memory):# compute the likelihood of L, M, and H bids/moves/demands based on memory of bids/moves/demands so far
	return([sum([1 for x in memory if x == i])/len(memory) for i in [par.L,par.M,par.H]])

#return([sum([1 for x in memory if x == i])/len(memory) for x in memory for i in [par.L,par.M,par.H] if x == i])

def expected_payoff(moves,player,memory,action):# returns payoffs for 4 future moves (cf. Caitlin O'Conner paper, Tab. 2)
	# reasoning under uncertainty over oppenent's demand y
	if player == 0:# player should be 0 (player1) or 1 (player2)
		payoff = len(memory)*sum([prob(memory)[y]*moves[action][y][player] for y in [0,1,2]])
	else:
		payoff = len(memory)*sum([prob(memory)[y]*moves[y][action][player] for y in [0,1,2]])
	return(payoff)

def best_response(moves,player,memory):# returns a tuple: index of best response (0 = L, 1 = M, 2 = H) and expected payoffs for L,M,H
	payoffs = [expected_payoff(moves,player,memory,action) for action in [0,1,2]]# player 1 (index 0), player 2 (index 1 in par.strategies)
	indices = [i for i, x in enumerate(payoffs) if x == max(payoffs)]# multiple bids/demands might have the same expected payoff
	best_response = indices[random.randint(0,len(indices)-1)]# if multiple bids/demands have equal expected payoff, choose at random
	return(best_response,payoffs)

def norm(par,mean,sd):
	n = np.random.normal(mean, sd, 1)[0]
	while not(n >= 0 and n <= 4.5):
		n = np.random.normal(mean, sd, 1)[0]
	return(n)
