
# **ASCII Jetpack Joyride**

## Installation and running the code:

Download the files required.

To run the game, enter the command `python3 game.py`

## Movement:
1. W - fly up

2. A - move left

3. S - move down

4. D - move left

5. L - shoot bullets

6. SPACE - activate the shield

7. K - Summon the dragon(the one on your side)

## OOPs Features:

1. Inheritance: gameObj is a parent class of almost every object in the game. The attributes and some common methods are inherited by these objects.

2. Polymorphism: Some methods of the parent classes are overidden depending on the type of object. Also, most attributes of the parent class are overidden in the subclass.

3. Encapsulation: Using classes and subclasses meets the requirements of Encapsulation. Every obstacle in the game is an object, including the Mandalorian himself.

4. Abstraction: Various methods for each object are defined so that the user only interacts with the basic functionality. (Eg: changeX(), changeXVel() change the X position and X velocity of an object repsectively, user isn't concerned with how they work).

## Gameplay:

1. There is a time limit of the whole game, and if you don't collect baby yoda in that time, you lose the game.

2. The player has 5 lives, and collision with fire beams or boss' bullets result in the loss of one life. If the player runs out of all lives, the game ends.

3. When the shield is activated, the player is completely immune for 10 seconds, after which he needs to wait for 60 seconds for it to recharge.

4. The player can activate the dragon only ONCE in the entire game.

5. After the boss is defeated, the player has to move to baby yoda to complete the game.

