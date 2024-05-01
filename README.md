# AlgorithmicProblemsolving

## D&D Matching magic-items with players

### Story:


## Hungarian alogrithm problem
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
Hungarian matching algorithm <br/>
The hungarian matching algorithm works for square matrixes (where there are an equal amount of row and columns) which is not necessarily what we want. This can be fixed using 'dummy' items and characters in the implemntation or change the problem to have the exact amount of items as characters can assign to themselves. 





## Ford Fulkerson problem
### Algorithm:
Make use of a network-flow alogrithm to maximize the amount of items the party can atune to
A player can use up to a maximum of 3 attuneable-items but may use as many normal items as they like but a player can only use 1 item per type

### Input
number of players `n`, `m` number of items and `t` number of item-types<br/>
`n` names of players <br/>
A single line break <br/>
`m` items with some players who can atune to the item with format `t A player1 player2 ...` Where `t` is the type as an integer, `A` is either the character 'A' or 'N' indicating whether the item must be attuned or not, and `player(n)` being the names of the players that can use the item

### Output
How many items can the party leave with as an integer

### Sample:

##### IN:
```
2 5 4
Thordak
Galroc

0 A Thordak
0 A Thordak Galroc
1 A Thordak
2 A Thordak
3 N Thordak
```
##### OUT:
```
5
```
<br/>

##### IN:
```
2 5 4
Thordak
Galroc

0 A Thordak
0 A Thordak Galroc
1 A Thordak
2 A Thordak
2 N Thordak
```
##### OUT:
```
4
```
<br/>


##### IN:
```
2 5 4
Thordak
Galroc

0 A Thordak
0 A Thordak Galroc
1 A Thordak
2 A Thordak
3 A Thordak
```
##### OUT:
```
4
```