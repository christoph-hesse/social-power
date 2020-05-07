# Oppressive Speech Simulation

This repository holds a simulation of oppressive speech implemented in Python.

It is a multi-agent simulation using a 3-strategy Nash demand game with 1) dynamic updates to bargaining power and 2) belief updates about bargaining power. Oppression is modelled as the reduction of material bargaining power. Oppressive speech, such as slurs, is modelled as updating agents' beliefs about their bargaining power such that they think they are weaker than they actually are, which results in modified behavior.

## Requirements

* Python 3 (tested with version 3.7.4)
* Python module numpy (tested with version 1.18.1)
* Python module random
* Python module csv
* Python module os

## Simulation Parameters

The simulation's behavior can be controlled through a variety of parameters:
* The population of agents is split into two social groups, and agents who would use oppressive speech (*racists*) occur in only one of the two groups
* The number of racists and non-racists in the first group; the number of agents in the second group
* Bargaining power is set via disagreement points per group and subgroup: a higher disagreement point means more bargaining power
* Groups' propensity for using racist slurs
* How popular the different groups are. More popular agents have more say in updates of bargaining power

When setting the parameters above to characterize and initialize a population of agents, you can choose from four sampling methods to assign individual parameter values to agents:
* constant value
* sampled from a random normal distribution
* sampled from a power distribution
* sampled from a uniform random distribution

For instance, you could assign a random propensity for racism while assigning normally distributed, initial disagreement points.


* How many past interactions agents remember (memory length)
* The reward associated with the 3 possible demands: low, medium, high
* The number of interactions per simulation run (number of trials)
* Whether the outcome of each interaction is printed

* Whether a final summary of the simulation is printed
* Who agents can interact with

* number of jurors

## Usage

1. Set the simulation parameters in ```par.py```.

2. Also in ```par.py``` decide how much output you want to print to your Python console.
*  ```print_rounds = Bool``` prints a line for each interaction containing the following information: number of round, agents' indices, their group membership, their memories, their payoff vector, their best response, their disagreement point before and after the interaction, the increase/decrease in disagreement point prescribed by the jury, whether a slur occured.

* ```print_rewards = Bool``` prints a summary at the end of one simulation run containing the following information: the number of times that members of each group made a low, medium or high demand in the game, what best responses they chose based on whether they acted with in-group agents (group 1 amongst themselves ```gr1|1```, group 2 amongst themselves ```gr2|2```) or out-group agents (interaction between group 1 and group 2 ```gr1/2```), the median disagreement points that members of each group hold about their own group and the other group (```d1/2 gr1```, ```d1/2 gr2```), the median demand of racist agents and their disagreement points, the median disagreement points that members of each group hold at the end of the simulation, and their beliefs that they hold about their disagreement point at the end of the simulation, the Nash strategy they have arrived at at the end of the simulation

* ```print_results = Bool``` prints a tabulated summary of what is written to the ```.csv``` output file containing the following columns: number of agents per group and subgroup, initial disagreement points, slur strength, strength of jurors, the Nash strategy agents in each group arrived at at the end of the simulation, final disagreement points, final beliefs about disagreement points

3. Decide whether you want to run the simulation once or multiple times

* For a single run of the simulation run this in your Python console. No ```.csv``` output file will be saved:
```python
simulate(par)
```

* For multiple simulations, set the number of simulation runs and a name for your ```.csv``` file, and call this line in your Python console:
```python
multi_sim2(par,number_of_runs,'filename_of_csv',False,True)
```
In the root folder of the simulation create a subfolder called ```csv``` where all ```.csv``` output files will be saved. If you want to test run multiple simulation without actually saving a ```.csv``` file yet, use
```python
multi_sim2(par,number_of_runs,'filename_of_csv',True,False)
```
with some dummy filename. Keep in mind that ```.csv``` files of the same name will be overwritten.

## License and Citation

The simulation and its associated code are released under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. You can find a human-readable summary of the licence agreement here:

https://creativecommons.org/licenses/by-nc-sa/4.0/

If you are using our simulation for research purposes, please cite the following paper:

## References

1. bla
