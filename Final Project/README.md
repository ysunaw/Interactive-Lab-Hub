# Final Project - Connect Four

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19

## Description
In our final project, we used Raspeberry Pi to simulate the Connect Four game. The game features two players - each has their own set of boards and chesses - playing the game remotely. 

## Deliverables

1. Documentation of design process
2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)
4. Reflections on process (What have you learned or wish you knew at the start?)

### Design Process

#### System design



#### Chessboard design

We used a two 6*5 board. 

#### Functional design

We separated the code into two separate files for each player (`connect-4-O.py` and `connect-4-X.py`). The one playing the chess O will be the one that makes the first move. 

- Communication

The `on_connect` and `on_message` functions are used for communicating what move they are making. Each side acts as both the sender and the receiver: they send a message right after a valid move is made (i.e. a touch sensor representing a column that is not full is triggered), and they keep monitoring the messages and get informed when their opponent has made a move. 

- Update opponent's move

Once the opponent has made a move, the player needs to update their board accordingly. This is accomplished by displaying what the other player has placed their move on the screen. After the player has updated the board, the player need to 


### Video


## Reflection

The cutting took awfully long time, and we spent quite some amount of time figuring out how to make the board. 
On the coding side, ... 

## Our Team

Yanjun Zhou
Yimeng Sun
Renzhi Hu






