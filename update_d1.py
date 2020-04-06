# Power by Association
# Travis LaCroix, Cailin O'Connor (2018)
# using the Nash demand game (1950)

# in power by association for their in-group and a bargaining disadvantage for their out-group
# disagreement point = consulation prize

# rational choice
# Nash's solution, 4 axioms to follow:
# 1) Pareto efficiency (zero-sum, one's loss is anothers gain)
# 2) Symmetry (players are equal, interchangeable)
# 3) Invariance to affine transformations (independence of sequential bargaining)
# 4) Independence of irrelevant alternatives (decision made because of payoff, not relevant to lesser alternatives)

# payoffs u1 and u2 for player 1 and 2, with disagreement points d1 and d2 = consulation prizes for player 1 and 2, respectively
# players maximize (u1-d1)(u2-d2)

# Nash (1953) reinterprets disagreement points as threat, i.e. what the other player stands to loose should bargaining break down
# bargaining breakdown = if the summed payoffs exceed the available resource

# Whoever has the ability to issue a more credible threat, based on their personal situation, can lower their opponent’s disagreement point further and reap the benefits in the subsequent bargain. Even without this threat interpretation, though, the disagreement point captures something relevant about the power of an individual—those with more secure fall-back positions are in a better, more powerful place with respect to bargaining in general.

# social conventions according to Lewis (1969)
# conventions arise because of an "accident of history" which becomes reinforced over time
# over time the tags come to bear social significance, and the population is divided into a class system that depends upon these (now) discriminatory tags

# winner take all is not possible in the Nash demand game because it assumes that the other player willingly demands nothing

# replicator dynamic = a very common dynamic from evolutionary game theory which supposes that strategies yielding above average payoffs proliferate while those that yield below average payoffs diminish and go extinct

# power(asrepre- sented by disagreement points) translates to a bargaining advantage in evolutionary models as well as rational-choice ones. Therefore, in both types of models, it pays to be powerful. However, the reason is not the same: in the evolutionary models, the disagreement points influence the population dynamics such that the predicted, population-wide equilibrium is changed, whereas in the rational-choice models the disagreement points influence the actual choices of individuals.



# mixed strategies in Nash demand game
# => when in dought, compromize
# => if certain go for pure strategy

# ====================================
# THE MODEL
# ====================================

class par:
	# population size N
	N = 10# 10, 20, 40, 100
	N1 = 4#N/2
	N2 = 5#N/2
	N3 = 1# powerful individuals / racists

	# disagreement points (consulation prizes) for player 1 and 2
	d1 = 3
	d2 = 3
	d3 = 4.5
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

	# memory length m
	m = 4# 5, 10, 15, 20

	# total resource R
	R = 10

	# diviation from M
	di = 1

	# possible demands
	H = R/2 + di
	M = R/2
	L = R/2 - di
	# {4,5,6}, {3,5,7}, {2,5,8}

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

	trials = 100
	r = 0
	print_rounds = True
	print_rewards = True

	method = 'both'# 'both' = agents from population regardless of group membership, 'inter' one agent from each group
	group_mem = True

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

	slurring = 'before'# if slurring happens, it happens before/after selecting the best response; set to 'none' to deactivate slurring
	slur_str = 0.# slur strength = the amount by which the disagreement point of the agent insulted is reduced

	audience_size = N-2
	aud_str = 0.5# strength of audience scores on disagreement point updates

# agents begin with empty memories
# determine first strategy at random

# player1's memory of what player2 has played
# player2's memory of what player1 has played

import numpy as np
import random
import csv

#strategies[random.randint(0,2)][random.randint(0,2)]

# generate a population of agents
# each agent is a set of attributes which characterize it:
# 0) an index which identifies group membership
# 1) the first move, which initially (before learning) is random
# 2) the expected payoff, which initially is random
# 3) the memory of what they themselves did in the past m interactions, which initially has the random starting move
# 4) the memory of what the other agents did in the past m interactions, which has the random starting move
# 5) power groups (1 = non-powerful g1, 2 = g2, 3 = powerful individuals g3)
# 6) the memory of what other in-group agents did in the past m interactions
# 7) the memory of what out-group agents did in the past m interactions

# 8) the likelihood of racism (between 0 = not racist and 1 = racist)
# racists are more likely to slur; a slur is a performative utterance which reduces the disagreement point of the one insulted

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

#d1s = [par.d1 for n in range(0,par.N1)]# [norm(par,3) for n in range(0,par.N1)]# [par.d1 for n in range(0,par.N1)]
	#d2s = [par.d2 for n in range(0,par.N2)]# [norm(par,2) for n in range(0,par.N2)]# [par.d2 for n in range(0,par.N2)]
	#d3s = [par.d3 for n in range(0,par.N3)]# [norm(par,3) for n in range(0,par.N3)]# [par.d3 for n in range(0,par.N3)]
	#r1s = [par.r1 for n in range(0,par.N1)]# racism likelihood, i.e. propensity to slur, of blue agents
	#r2s = [par.r2 for n in range(0,par.N2)]# racism likelihood red agents
	#r3s = [par.r3 for n in range(0,par.N3)]# racism likelihood 
	#pop1s = [par.pop1 for n in range(0,par.N1)]
	#pop2s = [par.pop2 for n in range(0,par.N2)]
	#pop3s = [par.pop3 for n in range(0,par.N3)]

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

def test1(par,t):
	count = 0
	total = 0
	for x in range(1,t+1):
		total = total + 1
		v = pick_agents1(par)
		if v[0] == v[1]:
			count = count + 1
	return(count/total)

def pick_agents2(par):
	l = [item for item in range(0,par.N)]
	i = random.randint(0,int(par.N1)+int(par.N3)-1)
	j = random.randint(int(par.N1)+int(par.N3),int(par.N1)+int(par.N2)+int(par.N3)-1)
	l = [item for item in l if item not in [i,j]]
	return([i,j,l])

def test2(par,t):
	g1 = []
	g2 = []
	for x in range(1,t+1):
		v = pick_agents2(par)
		g1.append(v[0])
		g2.append(v[1])
	print(min(g1),max(g1),'|',min(g2),max(g2))
	return(g1,g2)

# when a blue agent insults a red agent, that's lowering d2
def disagreement_update(agent,update):# g1 = 1, g2 = 2
	group = agent[0]
	L = agent[6][0][0][0][0]
	M = agent[6][0][1][0][0]
	H = agent[6][0][2][0][0]
	d1 = agent[6][2][2][2][0]# agent's own current disagreement point
	d2 = agent[6][2][2][2][1]# opponent's current disagreement point
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

	# update agents' memories with the bids/moves/demandsjust made
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

	# agent_i & agent_j may have been updated; the electorate is unaffected
	# we update the entire population of agents by putting the (changed) agent_i and agent_j together with their electorate
	agents = [agent_i]+[agent_j]+electorate

	# log for print-out
	agent_i_new_ds = str([agent_i[6][2][2][2][0],agent_i[6][2][2][2][1]])
	agent_j_new_ds = str([agent_j[6][2][2][2][0],agent_j[6][2][2][2][1]])

	if par.print_rounds == True:
		print('R',str(par.r),'Pl('+str(v[0])+','+str(v[1])+')','Gr('+str(agent_i[0])+','+str(agent_j[0])+')','M',str(mem_p1),str(mem_p2),'Pa',agent_i_payoff,agent_j_payoff,'BR('+agent_i_best_response+agent_j_best_response+')','dO',agent_i_old_ds,agent_j_old_ds,'dN',agent_i_new_ds,agent_j_new_ds+slur_print)
	# ,str(agent_i_payoff),str(agent_j_payoff),'Best response',str(agent_i_best_response),str(agent_j_best_response),'d1/2',str(agent_i_old_ds),str(agent_j_old_ds)
	return(agents)

def weighted_average(ratings,weights):
	w_avrg = sum([ratings[i]*weights[i] for i in range(0,len(ratings))])/sum(weights)
	return(w_avrg)

def audience_score(agent_i,agent_j,audience,agent_i_move,agent_j_move,par):
		i_ratings, j_ratings = [], []
		for a in audience:
			if random.uniform(0,1) < a[9]:# racist audience members side with their own kind
				#if agent_i[0] == a[0] and agent_j[0] == a[0]:
				#	mat = a[0]-1
				#	mem = 7
				#elif agent_i[0] == a[0] and agent_j[0] != a[0]:
				#	pass
				#elif 
				if agent_i[0] == 1 and agent_j[0] == 1:
					mat = 0
					mem = 7
				elif agent_i[0] == 2 and agent_j[0] == 2:
					mat = 1
					mem = 7
				elif agent_i[0] == 1 and agent_j[0] == 2:
					mat = 2# racists' higher disagreement point results in more aggressive bargaining
					mem = 8
				elif agent_i[0] == 2 and agent_j[0] == 1:
					mat = 3# racists' higher disagreement point results in more aggressive bargaining
					mem = 8
			else:# treat out-group as in-group
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

# blue H red L = taking advantage of superior position = abuse of power
# blue L red H = boldly standing up & challenging
# blue M red M = compromise is good
# the moral thing would be to treat out-group agnets as if they were in-group agents
# value risk taking
# look at probable moves based on memory prob(memory) to gauge likely blue / red behaviour
# compare to how you would behave in that situation; best response

# in-group memories and behaviour
#e_agent_i_move = e_agent_j_move = [par.L,par.M,par.H][int(best_response(audience[0][6][0],audience[0][0]-1,audience[0][7])[0])]
#e_i_rating = e_agent_i_move - agent_i_move# amount by which disagreement point of agent_i should be raised/lowered
#e_j_rating = e_agent_j_move - agent_j_move# amount by which disagreement point of agent_j should be raised/lowered
# out-group memories and behaviour
#[par.L,par.M,par.H][int(best_response(electorate[0][6][2],0,electorate[0][8])[0])]

# audience members side with their kind
#e_agent_i_move | agent_i_move | rating

# a racist insulting a red agent is chipping away at their selfesteem
# slur strength is set to the same value as the strength of audience scores,
# i.e. an audience without any racists should be able to undo the effect of sluring on a red agent

#i_ratings = [-0.9,-0.5,-0.5,0,0.5]
#j_ratings = [0.75,0.5,0.5,0,-0.5]
# more popular audience member get a bigger say
#weights = [member[10] for member in audience]
# weighted average, weighted according to popularity
#i_rating = weighted_average(i_ratings,weights)
#j_rating = weighted_average(j_ratings,weights)

#agent_i_memory
#agent_j_memory

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

	agents = create_pop(par)# create a population of agents
	for t in range(0,par.trials):# make the agents interact for par.trials
		par.r += 1
		agents = interact(par,agents)
	if par.print_rewards == True:
		print('Best responses group1',str([sum([1 for x in par.resp_hist_g1 if x == i]) for i in [par.L,par.M,par.H]]),
			'group2',str([sum([1 for x in par.resp_hist_g2 if x == i]) for i in [par.L,par.M,par.H]]))
		print('Best responses group1|group1','('+str(len(par.resp_hist_g1_g1))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [y for x in par.resp_hist_g1_g1 for y in x] if z == i]) for i in [par.L,par.M,par.H]]),
			'group2|group2','('+str(len(par.resp_hist_g2_g2))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [y for x in par.resp_hist_g2_g2 for y in x] if z == i]) for i in [par.L,par.M,par.H]]),
			'group1/group2','('+str(len(par.resp_hist_g1_g2))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for z in [x[0] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]),str([sum([1 for z in [x[1] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]),
			'd1/2 group1',str([np.median(par.g1_d1_hist),np.median(par.g1_d2_hist)]),
			'd1/2 group2',str([np.median(par.g2_d1_hist),np.median(par.g2_d2_hist)])
			)
		if par.N3 > 0:
			print('Powerful',str(np.median(par.resp_hist_g3)),'('+str(len(par.resp_hist_g3))+'/'+str(len(par.resp_hist_g1_g1)+len(par.resp_hist_g2_g2)+len(par.resp_hist_g1_g2))+')',str([sum([1 for x in par.resp_hist_g3 if x == i]) for i in [par.L,par.M,par.H]]),
				'd1/2 group3',str([np.median(par.g3_d1_hist),np.median(par.g3_d2_hist)])
				)

#[[y for x in l] for y in x]
#[sum([1 for z in [y for x in par.resp_hist_g1_g1 for y in x] if z == i]) for i in [par.L,par.M,par.H]]
#[val for sublist in par.resp_hist_g1_g1 for val in sublist]

#[sum([1 for z in [x[0] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]

def multi_sim(par,number,filename,print_results,save_results):
	output = []
	for n in range(0,number):
		simulate(par)
		output.append([[sum([1 for z in [x[0] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]],[sum([1 for z in [x[1] for x in par.resp_hist_g1_g2] if z == i]) for i in [par.L,par.M,par.H]]])
	print('Done!')
	if print_results == True:
		print('b_max'+'\t'+'b_L'+'\t'+'b_M'+'\t'+'b_H'+'\t'+'r_max'+'\t'+'r_L'+'\t'+'r_M'+'\t'+'r_H')
		for i in output:
			print(str(i[0].index(max(i[0])))+'\t'+str(i[0][0])+'\t'+str(i[0][1])+'\t'+str(i[0][2])+'\t'+str(i[1].index(max(i[1])))+'\t'+str(i[1][0])+'\t'+str(i[1][1])+'\t'+str(i[1][2]))
	if save_results == True:
		header = ['b_max','b_L','b_M','b_H','r_max','r_L','r_M','r_H']
		with open('Mihaela/simulations/ich/csv/'+str(filename)+'.csv', 'wt') as f:
		    csv_writer = csv.writer(f,delimiter=',')
		    csv_writer.writerow(header) # write header
		    for i in output:
		    	row = [i[0].index(max(i[0])),i[0][0],i[0][1],i[0][2],i[1].index(max(i[1])),i[1][0],i[1][1],i[1][2]]
		    	csv_writer.writerow(row)


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

# iter_value(par,'d1',[0,4.5,0.5])
# iter_value(par,'m',[1,10,1])
# iter_value(par,'d3',[0,4.5,0.5])
# iter_value(par,'d3',[0,5.5,0.5])

# count how many L, M, H in memory
#sum_L = sum([1 for x in memory if x == par.L])
#sum_M = sum([1 for x in memory if x == par.M])
#sum_H = sum([1 for x in memory if x == par.H])

#L_move = 0
#M_move = 1
#H_move = 2

#prob_L = sum_L/len(memory)
#prob_M = sum_M/len(memory)
#prob_H = sum_H/len(memory)

#(payoff_agent_i - par.d1) * (payoff_agent_j - par.d2)

#moves[]
#4*sum_L+5*sum_M+6*sum_H+
#5*sum_L+5*sum_M+par.d1*sum_H+
#6*sum_L+par.d1*sum_M+par.d1*sum_H

#4*4,1*5,0*6			4*4,4*5,4*6
#4*4,0*5,0*6			4*4,4*5,4*6

#4*4,,

#strategies, moves = [
#		[[4,4],[4,5],[4,6]],
#		[[5,4],[5,5],[d1,d2]],
#		[[6,4],[d1,d2],[d1,d2]]
#	]

# best respond of player2 to player1's move L is H because
# max([moves[0][x][1] for x in [0,1,2]])
# best respond of player2 to player1's move M is M because
# max([moves[1][x][1] for x in [0,1,2]])
# best respond of player2 to player1's move H is L because
# max([moves[2][x][1] for x in [0,1,2]])

# best respond of player1 to player2's move L is H because
# max([moves[x][0][0] for x in [0,1,2]])
# best respond of player1 to player2's move M is M because
# max([moves[x][1][0] for x in [0,1,2]])
# best respond of player1 to player2's move H is L because
# max([moves[x][2][0] for x in [0,1,2]])

# player1 remembers player2s playing [M,H,H,H]
# so the probability of player2s playing L = 0, M = 1/4, H = 3/4
# player2 remembers player1s playing [L,L,L,L]
# so the probability of player1s playing L = 4/4 = 1, M = 0, H = 0

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

#mem_p1 = [par.M,par.H,par.H,par.H]
#mem_p2 = [par.L,par.L,par.L,par.L]

#payoffs_p1 = [expected_payoff(agent,2,0,mem_p1,action) for action in [0,1,2]]
#payoffs_p2 = [expected_payoff(agent,2,1,mem_p2,action) for action in [0,1,2]]

def best_response(moves,player,memory):# returns a tuple: index of best response (0 = L, 1 = M, 2 = H) and expected payoffs for L,M,H
	payoffs = [expected_payoff(moves,player,memory,action) for action in [0,1,2]]# player 1 (index 0), player 2 (index 1 in par.strategies)
	indices = [i for i, x in enumerate(payoffs) if x == max(payoffs)]# multiple bids/demands might have the same expected payoff
	best_response = indices[random.randint(0,len(indices)-1)]# if multiple bids/demands have equal expected payoff, choose at random
	return(best_response,payoffs)

#best_response(moves,0,mem_p1)
#best_response(moves,1,mem_p2)

#best_move_p1 = best_response(moves,0,mem_p1)[0]
#best_move_p2 = best_response(moves,1,mem_p2)[0]

#normal = np.random.normal(1.0, 0.005, 100)# 100 samples of normal dist w/ mean 1.0 and standard deviation 0.005

#normal_g1 = np.random.normal(3.0, 1, 1)
#normal_g2 = np.random.normal(2.0, 1, 1)

def norm(par,mean,sd):
	n = np.random.normal(mean, sd, 1)[0]
	while not(n >= 0 and n <= 4.5):
		n = np.random.normal(mean, sd, 1)[0]
	return(n)

def test3(par,mean,samples):
	n = []
	for s in range(0,samples):
		n.append(norm(par,mean))
	return(min(n),max(n))


# When the disagreement points differ AND interactions are restricted to inter-group interactions (not within-group) only,
# then the group with the higher disagreement point (the powerful group) will bet H all the time, forcing the inferior group to always bet L
# in order for the inferior group not to risk communication breakdown.

# However, if intra-group interactions, alongside with inter-group interactions, are allowed
# agents from the same group turn against each other, and sometimes play L and sometimes play H.
# This in turn results agents to also oscillate between L or H bids in inter-group interactions,
# even when a higher disagreement point for one of the groups makes that group more powerful than the other.
# Half of the interactions are inter-group, half intra-group (evenly split between interactions amongs group 1 and interactions amongs group 2).

# With both inter-group interactions and intra-group interactions, when both groups have the same disagreement point,
# agents from both groups converge on the fair strategy (M), regardless of whether they are interaction with an in-group agent or out-group agent.




# give each agent a seprate memory for within-group interactions and another for between-group interactions
# signal H in conjunction with group membership
# slurs as performative actions which bring about lowering in disagreement point of insulted agent
# conditional signal of playing H conditioned on group membership S(H|blue)
# Anton's model adds the signalled H to the memories of all red agents, but not to the blue agents
# so the blue agents playing H are reacting to the red agents playing L
# if you have many more red agents than blue agents, then it could force the blue agents to play L, allowing the red agents to play H
# what happens if the red group has the powerful agents, but the blue group still has the power of signaling
# O'Conner: even powerful individuals in the less powerful group cannot give them a ighting chance
