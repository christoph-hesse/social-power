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

## Usage

Change directory where the .csv file is saved.
```python
import numpy as np
```

```python
multi_sim2(par,100,'filename',False,True)
```

## License and Citation

The simulation and its associated code are released under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. You can find a human-readable summary of the licence agreement here:

https://creativecommons.org/licenses/by-nc-sa/4.0/

If you are using our simulation for research purposes, please cite the following paper:

## References

1. bla
