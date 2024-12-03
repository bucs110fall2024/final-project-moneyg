
# WAKE UP!!
## CS110 Final Project  Fall, 2024

## Team Members

Monica Gnajewski

***

## Project Description

My project uses a movable character object controlled by the player that dodges falling "z"s to avoid falling asleep in class. There will also be falling collectables that allow the player to recover once they hit a falling "z". Once the player is hit three times in a row with no collectables, the game is over.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design
Classes
1. Player
- creates player character
- allows for user to move character up, down, left, and right using keyboard keys

2. Customer
- creates customer NPCS
- moves customer left to counter
- creates customer "order" (task completed by player)



### Features

1. moveable character
2. different screens
3. collectable items
4. falling obstacles
5. background music


### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Test Case 1: Player Movement
Test Description: Verify that player is able to move the character left and right using the arrow keys.
| Step                 |Procedure                                     |Expected Results                   |
|----------------------|:--------------------------------------------:|----------------------------------:|
|  1                   | Start the game.                              |GUI window appears with count = 0  |
|  2                   | Press right arrow key.                       | display changes to count = 1      |
|  3                   | Verify that the player character moves right.|                                   |
|  4                   | Press left arrow key.                        |                                   |
|  5                   | Verify that the player charcter moves left.  |                                   |

Test Case 2: Enemy Detection
Test Description: Verify that enemy dissappears and player life count is decreased when colliding with an enemy.
| Step                 |Procedure                                                   |Expected Results                   |
|----------------------|:----------------------------------------------------------:|----------------------------------:|
|  1                   | Start the game.                                            |GUI window appears with count = 0  |
|  2                   | Move player charcter to collide with falling enemy.        | display changes to count = 1      |
|  3                   | Verify that enemy dissappears when player is hit.          |                                   |
|  4                   | Verify that life counter decreases by 1 when player is hit.|                                   |

Test Case 3: Collectable Detection
Test Description: Verify that collectable dissappears and player life count is increased when colliding with a collectable.

| Step                 |Procedure                                                   |Expected Results                   |
|----------------------|:----------------------------------------------------------:|----------------------------------:|
|  1                   | Start the game.                                            |GUI window appears with count = 0  |
|  2                   | Move player charcter to collide with falling collectable.  | display changes to count = 1      |
|  3                   | Verify that collectable dissappears when player is hit.    |                                   |
|  4                   | Verify that life counter increases by 1 when player is hit.|                                   |

Test Case 4: Game Over
Test Description: Verify that gameplay ends when player loses their three lives.
| Step                 |Procedure                                              |Expected Results                   |
|----------------------|:-----------------------------------------------------:|----------------------------------:|
|  1                   | Start the game.                                       |GUI window appears with count = 0  |
|  2                   |Play until all three lives are lost.                   | display changes to count = 1      |
|  3                   | Verify that player can no longer move their character.|                                   |
|  4                   | Verify that "game over" message is displayed.         |                                   |

Test Case 5: Exit
Test Description: Verify that clicking "x" in upper right corner closes the game. 
| Step                 |Procedure                                              |Expected Results                   |
|----------------------|:-----------------------------------------------------:|----------------------------------:|
|  1                   | Start the game.                                       |GUI window appears with count = 0  |
|  2                   | Click "x" in upper right corner.                      | display changes to count = 1      |
|  3                   | Verify that player can exit game without error.       |                                   |


