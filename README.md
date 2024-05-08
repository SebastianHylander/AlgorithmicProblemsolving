# AlgorithmicProblemsolving

## Magic Item Mayhem

### Story:
Your party has finally completed your latest quest and saved the town, but during the fight, that pesky monster destroyed all of your magic items!
Luckily, a local lord has taken pity on you and decided to allow you to take as many magic items as you can carry from his own private collection, on the condition that each item is worn and attuned to by a member of the party.

As it turns out, the lord's collection is quite unique, and not only does every item require attunement, but most of the magic items have very specific requirements for the user.
You decide sort the items into `5` categories - helmets, armor, cloaks, shields, and weapons - and label each item with the names of the players who meet the requirements to use it.
It takes a bit of work, but after all the trouble you went through, you feel the right to be a little greedy.

While doing this, you have managed to clearly define your rules:

- A player can wear at most `1` item from each of the `5` categories.
- A player can attune to at most `3` items at once.
- A player can only attune to items which they meet the requirements for.

All that is left to do now, is figure out how you can distribute the items to get as many as possible...

### Input
The first line contains two integers `N` and `M`, indicating the number of players in the party and the number of magic items in the collection, respectively.<br/>
After this comes `N` lines, containing the names of the players in the party.<br/>
The following `M` lines contain:

- An integer `c`, indicating the category of the item.
- A list of names, indicating the people in your party who meet the requirements to use the item.

### Output
Output the maximum number of items which the party can take.

### Sample:

##### IN:
```
2 5
Thordak
Galroc
1 Thordak
2 Thordak Galroc
2 Thordak
4 Thordak
1 Thordak
```
##### OUT:
```
4
```

## D&D Matching magic-items with players (Simplest)

### Story:
Your party has finally completed your latest quest and saved the town, but during the fight, that pesky monster destroyed all of your magic items!
Luckily, a local lord has taken pity on you and decided to allow you to take as many magic items as you can carry from his own private collection, on the condition that every item you take is attuned to by a member of the party.

As it turns out, the lord's collection is quite unique, and not only does every item require attunement, but most of the magic items have very specific requirements for the user.
To make it easier on yourselves, you decide to label each item with the names of the players who meet the requirements to use it.
It takes a bit of work, but after all the trouble you went through, you feel the right to be a little greedy.

By now, you know the rules for attunement by heart:

- A player can attune to at most `3` items.
- A player can only attune to items which they meet the requirements for.

All that is left to do now, is figure out how you can distribute the items to get as many as possible...

### Input
The first line contains two integers `N` and `M`, indicating the number of players in the party and the number of magic items in the collection, respectively.<br/>
After this comes `N` lines, containing the names of the players in the party.<br/>
The following `M` lines each represent an item, containing a list of names, indicating the people in your party who meet the requirements to use the item.

### Output
Output the maximum number of items which the party can take.

### Sample:

##### IN:
```
2 5
Thordak
Galroc
Thordak
Thordak Galroc
Thordak
Thordak
Thordak
```
##### OUT:
```
4
```

## D&D Matching magic-items with players (With categories)

### Story:
Your party has finally completed your latest quest and saved the town, but during the fight, that pesky monster destroyed all of your magic items!
Luckily, a local lord has taken pity on you and decided to allow you to take as many magic items as you can carry from his own private collection, on a few conditions:

- Every item you take must be worn by a player who can use it, and
- every item which requires attunement must be attuned to.

As it turns out, the lord's collection is quite unique, and most of the magic items have very specific requirements for the user.
You decide sort the items into `5` categories - helmets, armor, cloaks, shields, and weapons - and label each item with the names of the players who meet the requirements to use it.
It takes a bit of work, but after all the trouble you went through, you feel the right to be a little greedy.

While doing this, you have managed to clearly define your rules:

- A player can take at most `1` item from each of the `5` categories.
- A player can take at most `3` items which require attunement.
- A player can only take items which they can use.

All that is left to do now, is figure out how you can distribute the items to get as many as possible...

### Input
The first line contains two integers `N` and `M`, indicating the number of players in the party and the number of magic items in the collection, respectively.<br/>
After this comes `N` lines, containing the names of the players in the party.<br/>
The following `M` lines contain:

- An integer `c`, indicating the category of the item.
- The character 'A', if the item requires attunement, or the character '-' if it does not.
- A list of names, indicating the people in your party who meet the requirements to use the item.

### Output
Output the maximum number of items which the party can take.

### Sample:

##### IN:
```
2 5
Thordak
Galroc
1 - Thordak
2 A Thordak Galroc
2 - Thordak
4 A Thordak
1 A Thordak
```
##### OUT:
```
4
```


## Hungarian alogrithm problem
### Algorithm:
Make use of a network-flow alogrithm to maximize the amount of magic-items the party can atune to, prioritize items of higher rarity
A player can atune to a maximum of 3 items

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