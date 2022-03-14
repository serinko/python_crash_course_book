# Alien Invasion

In alien invasion, the player controls a rocket ship that appears at the bottom
center of the screen. The player can move the ship right and left using the
arrow keys and shoot bullets using the spacebar. When the game begins, a fleet
of aliens fills the sky and moves accross and down on the screen. If the player
shoots all the aliens, a new fleet appears that moves faster than the previous
fleet. If any alien hits the player's ship, or reaches the bottom of the
screen, the player loses a ship. If player looses three ships, the game ends.

## Dependencies

- pygame module

## New Syntaxes Introduced

| PYGAME MODULE                             | EXPLANATION                                       |
|-------------------------------------------|---------------------------------------------------|
| .display.set_mode()                       | setting screen size                               |
| .display.set_caption()                    | setting caption on top                            |
| .event.get()                              | respond to keypresses and mouse events            |
| .event.type == pygame.QUIT                | clicking on quit or pressing quit keys            |
| .display.fill(x)                          | redraw the screen with x                          |
| .display.get_rect()                       | load rectangular                                  |
| .load()                                   | import a file                                     |
| .display.blint(x)                         | draw x at a current location on top of the screen |
| event.key == pygame.KEYDOWN               | register keypress                                 |
| event.type == pygame.KEYUP                | register key release                              |
| .display.set_mode((0,0),pygame.FULSCREEN) | firure out the window size to fill the screen     |
| `super()__init__()`                       | help inherit properly from Sprite                 |
| add(x)                                    | append() for pygame groups                        |

| OTHER SYNTAX | EXPLANATION                  |
|--------------|------------------------------|
| sys.exit()   | kill the program             |
| float()      | convert x value to a decimal |