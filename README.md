# Oppressive Speech Simulation

This repository holds a simulation of oppressive speech implemented in Python.

It is a multi-agent simulation using a 3-strategy Nash demand game with 1) dynamic updates to bargaining power and 2) dynamic updates to agents' beliefs about their bargaining power. Oppression is modelled as the reduction of material bargaining power. Oppressive speech, such as slurs, is modelled as updating agents' beliefs about their bargaining power such that they think they are weaker than they actually are, which results in modified behavior.

There are two versions of the simulation contained in this repository: ```dynamic_update_1.py``` is a simulation of material racism where racists can take away actual, material power from the oppressed. ```dynamic_update_2.py``` is a simulation of oppressive speech where racists can only use slurs to intimidate the oppressed thereby indirectly modifying their behavior.

## Requirements

* Python 3 (tested with version 3.7.4)
* Python module numpy (tested with version 1.18.1)
* Python module random
* Python module csv
* Python module os

## Simulation Parameters

The simulation's behavior can be controlled through a variety of parameters:
* The number of interactions per simulation run (number of ```trials```)
* ```print_rounds = Bool``` sets whether the outcome of each interaction is printed
* ```print_rewards = Bool``` sets whether a final summary of the simulation is printed

The population of agents is split into two social groups, and agents who would use oppressive speech (*racists*) occur in only one of the two groups. You can control:

* The number of racists (```N3```) and non-racists (```N1```) in the first group; the number of agents in the second group (```N2```)
* Bargaining power is set via disagreement points per group and subgroup (```d1``` for group 1, ```d2``` for group 2, ```d3``` for group 3) relative to the reward associated with the 3 possible demands low ```L```, medium ```M```, and high ```H```: a higher disagreement point, closer to one of the possible rewards, means more bargaining power because then agents have less to loose 
* ```r1```, ```r2```, ```r3``` is groups' propensity for using racist slurs
* ```pop1```, ```pop2```, ```pop3``` is how popular the different groups are. More popular agents have more say in updates of bargaining power

When setting the parameters above to characterize and initialize a population of agents, you can choose from four sampling methods to assign individual parameter values to agents (```d_sampling```, ```r_sampling```, ```pop_sampling```):

* constant values
* values sampled from a random normal distribution
* values sampled from a power distribution
* values sampled from a uniform random distribution

For instance, you could assign random racist tendencies while assigning normally distributed, initial disagreement points.

Furthermore, you can set:

* How many past interactions agents remember (memory length ```m```)
* Whether agents have separate memories for in-group and out-group interactions (```group_mem = Bool```)
* Who agents can interact with: 1) only with out-group agents (```method = 'inter'```) or 2) with both in-group and out-group agents (```method = 'both'```)

Those agents with racist tendencies (```r3 > 0```) insult out-group agents with odds proportional to their racist tendencies. The simulation has the following parameters for slurring:

* How much a slur updates agents' beliefs about their bargaining power (```slur_str```)
* Whether slurring happens before agents decide their best response (```slurring = 'before'```) or after (```slurring = 'after'```)

An audience witnesses each interaction and acts as a jury with the power to increase or decrease agents' bargaining power based on their behavior in the interaction:

* ```audience_size``` controls the number of jurors
* ```aud_str``` controls the strength of the jury to reward or sanction agents' behavior

## Usage

1. Set the simulation parameters in the ```class par```.

2. Decide how much output you want to print to your Python console.
*  In the ```class par```, ```print_rounds = Bool``` prints a line for each interaction containing the following information: number of round, agents' indices, their group membership, their memories, their payoff vector, their best response, their disagreement point before and after the interaction, the increase/decrease in disagreement point prescribed by the jury, whether a slur occured.

* In the ```class par```, ```print_rewards = Bool``` prints a summary at the end of one simulation run containing the following information: the number of times that members of each group made a low, medium or high demand in the game, what best responses they chose based on whether they acted with in-group agents (group 1 amongst themselves ```gr1|1```, group 2 amongst themselves ```gr2|2```) or out-group agents (interaction between group 1 and group 2 ```gr1/2```), the median disagreement points that members of each group hold about their own group and the other group (```d1/2 gr1```, ```d1/2 gr2```), the median demand of racist agents and their disagreement points, the median disagreement points that members of each group hold at the end of the simulation, and their beliefs that they hold about their disagreement point at the end of the simulation, the Nash strategy they have arrived at at the end of the simulation

* When calling the ```multi_sim``` function (see below) set ```print_results``` to ```True``` to print a tabulated summary of what is written to the ```.csv``` output file containing the following columns: number of agents per group and subgroup, initial disagreement points, slur strength, strength of jurors, the Nash strategy agents in each group arrived at at the end of the simulation, final disagreement points, final beliefs about disagreement points

3. Decide whether you want to run the simulation once or multiple times.

* For a single run of the simulation run this in your Python console. No ```.csv``` output file will be saved!
```python
simulate(par)
```

* For multiple simulations, set the number of simulation runs and decide on a name for your ```.csv``` file. Then call this line in your Python console:
```python
multi_sim(par,number_of_runs,'filename_of_csv',False,True)
```
In the root folder of the simulations ```dynamic_update_1.py``` and ```dynamic_update_2.py``` create a subfolder called ```csv``` where all ```.csv``` output files will be saved. If you want to test run multiple simulations without actually saving a ```.csv``` file yet, use
```python
multi_sim(par,number_of_runs,'dummy_filename',True,False)
```
with some dummy filename. Keep in mind that ```.csv``` files of the same name will be overwritten!

4. Load the ```.csv``` files into your favorite statistics software. If you are using R, the repository contains an ```.r``` markdown file called ```stats.r``` to get you started.

## License and Citation

The simulation and its associated code are released under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. You can find a human-readable summary of the licence agreement here:

https://creativecommons.org/licenses/by-nc-sa/4.0/

The ```.csv``` data files contained in this repository are supplementary material, to be used only for instruction and non-commercial educational or academic purposes, and may not be reproduced in any medium without the expressed permission of the authors.

If you are using our simulation for research purposes, please cite the following paper:

## References

1. placeholder
