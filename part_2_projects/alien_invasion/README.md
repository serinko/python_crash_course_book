# Alien Invasion

In alien invasion, the player controls a rocket ship that appears at the bottom
center of the screen. The player can move the ship right and left using the
arrow keys and shoot bullets using the spacebar. When the game begins, a fleet
of aliens fills the sky and moves accros and down on the screen. If the player
shoots all the aliens, a new fleet appears that moves faster than the previous
fleet. If any alien hits the player's ship, or reaches the bottom of the
screen, the player loses a ship. If player looses three ships, the game ends.

## Dependencies

- pygame

| NEW SYNTAX - PYGAME    | EXPLANATION                            |
|------------------------|----------------------------------------|
| .display.set_mode()    | setting screen size                    |
| .display.set_caption() | setting caption on top                 |                 
| .event.get()           | respond to keypresses and mouse events |
|.event.type == pygame.QUIT | clicking on quit or pressing quit keys|

| NEW SYNTAX | EXPLANATION      |
|------------|------------------|
| sys.exit() | kill the program |
| 