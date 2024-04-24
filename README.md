# AlgorithmicProblemsolving

## D&D Matching magic-items with players

### Story:


### Algorithm:
Make use of a network-flow alogrithm to maximize the amount of magic-items the party can atune to, prioritize items of higher rarity
A player can atune to a maximum of 3 items

### Input
number of players `n` and `m` number of items<br/>
`n` names of players <br/>
`m` different items each with a rarity and some players who can atune to the item
### Output
The sum of the rarity of items

### Sample:

##### IN:
```
2 5
Thordak
Galroc
1 Thordak
2 Thordak Galroc
1 Thordak
3 Thordak
1 Thordak
```
##### OUT:
```
7
```

### Notes:
Minimum cost matching <br/>
Hungarian matching algorithm