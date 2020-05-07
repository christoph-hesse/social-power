# Oppressive Speech Simulation

This repository holds a simulation of oppressive speech.

It is a multi-agent simulation using a 3-stratgy Nash demand game with 1) dynamic updates to bargaining power and 2) belief updates about bargaining power. Oppression is modelled as the reduction of material bargaining power. Oppressive speech, such as slurs, is modelled as updating agents' beliefs about their bargaining power such that they think they are weaker than they actually are.

The simulation's behavior can be controlled by a variety of parameters:
* The population of agents is split into two social groups, and racists who would use oppressive speech occur in only one of the two groups
* The number of racists and non-racists in the first group; the number of agents in the second group
* Bargaining power is set via disagreement points per group and subgroup: a higher disagreement point means more bargaining power


## Requirements

* Python (tested with version 3.7.4)
* Python module numpy (tested with version 1.18.1)
* Python module random
* Python module csv
* Python module os

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

[comment] <> (If you are using our simulation for research purposes, please cite the following paper:)

[comment] <> (## References)

[comment] <> (1. bla)
