# Azul Information and Implementation	

## General Azul knowledge

## Anatomy of an Azul board

### Bag
The bag holds all of the tiles that are not currently in play. At the beginning, the bag contains 100 tiles - 20 each of the colors Blue, Yellow, Red, Black, and Cyan. These are referred to as "colored tiles".

The bag is represented as a tuple of values in the following order:
{#Blue, #Yellow, #Red, #Black, #Cyan}

### Center
The center contains five factory circles that each hold four colored tiles and a 'pile' of tiles that starts the round with the white tile. As the round progresses, tiles that are not taken from the factories gather in the 'pile'. 

The center is represented as a 6x6 grid, where each row represents the grouping of tiles and each column represents a color. In this scheme, each cell represents the count of a certain color at a certain location.
| Location | #Blue | #Yellow | #Red | #Black | #Cyan | #White |
|--|--|--|--|--|--|--|
| Factory 1 | 1 | 2 | 0 | 0 | 1 | 0 |
| Factory 2 | 3 | 0 | 0 | 0 | 1 | 0 |
| Factory 3 | 0 | 0 | 1 | 1 | 2 | 0 |
| Factory 4 | 3 | 1 | 0 | 0 | 0 | 0 |
| Factory 5 | 0 | 1 | 1 | 1 | 1 | 0 |
| Center | 0 | 0 | 0 | 0 | 0 | 1 |


### Player board

There is one board per player. Each board is broken up into three parts.
![Board Image](https://i.imgur.com/Ai9kaRd.jpg)

#### Pattern Lines (Upper left)
Five empty lines that can hold an increasing number of tiles of the same color. Tiles that are taken from the center during a round are placed in this section of the player board.

The pattern lines is represented as a tuple of values in the following order:
 - Max size {1, 2, 3, 4, 5}
 - Current color value {None, Blue, Yellow, Red, Black, Cyan}
 - Current tile count {0, 1, 2, 3, 4, 5}

#### Floor line (Bottom)
The floor line holds any tiles that the player is forced to take and any 'overflow' tiles from the pattern lines. 

Every filled square in the floor line will subtract points from the player at the end of every round. These point values are {1, 1, 2, 2, 2, 3, 3}. The floor line is cleared at the end of each round after scoring.

The floor line is represented as a single value in the neural network - the number of tiles it contains.

#### Wall (Upper right)
The wall is a 5x5 grid that persists throughout the entire game. Each cell can only be filled by one color. 

The wall is represented as a 5x5 grid of boolean values. True indicates that a tile is present in that cell. False indicates otherwise.

## Implementation notes
### Action counting
Actions are defined as incrementing values in the framework. Every integer corresponds with a single unique action taken by a player.

In the case of Azul, a unique move is a unique conbination of the following values:
 - Location of tiles taken from (Factory 1 - 5 or center)
 - Color of tile taken (Excl. White)
 - Placement of tiles on board (Pattern line 1 - 5 or floor line)

This results in an action space of 6 * 5 * 6 == 180.

0 - 29: Factory 1
    0 - 5: Blue
        0: Line 1
        1: Line 2
        2: Line 3
        3: Line 4
        4: Line 5
        5: Floor
    6 - 11: Yellow
    12 - 17: Red
        12: Line 1
        13: Line 2
        14: Line 3
        15: Line 4
        16: Line 5
        17: Floor
    18 - 23: Black
    24 - 29: Cyan
30 - 59: Factory 2 
60 - 89: Factory 3 
90 - 119: Factory 4 
120 - 149: Factory 5 
150 - 179: Center

To convert from action -> int: location * 30 + Color * 6 + Line * 1

To convert from int -> action:
Location: num / 30
Color: num = num % 30 -> num / 6
Line: num = num % 30 -> num % 6


