import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)

        # Run he game in full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # run it pre set default screen
        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width, self.settings.screen_height
        # ))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to safe game statistics and
        # create a scoreboards

        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color
        self.bg_color = (0, 17, 26)

        # Make the Play button
        self.play_button = Button(self, "Play")

    def _start_game(self):
        """Starts the game"""

        # Game starts with clicking the Play button or pressing P on inactive
        # Or restarts on pressing R at any point

        # Reset the game settings.
        self.settings.initialize_dynamic_settings()

        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid off any remaining aliens or bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _create_fleet(self):
        """Create the fleet of aliens"""

        # Create an alien and find a number of aliens fitting a row
        # Spacing between each = width of one alien
        # Make an alien
        alien = Alien(self)
        # self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        # counts # fitting aliens per row
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # // sgn is a floor division, drops off all the reminder.
        # Always returns an integer

        # Determine the number of aliens
        ship_height = self.ship.rect.height
        available_space_y = \
            (self.settings.screen_height - (3 * alien_height) - ship_height)

        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            # Create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

                # Two nested loops when one make a row from an alien
                # Another makes a plot of rows from one row

    def _create_alien(self, alien_number, row_number):
        """Create alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        # Adds to the group aliens in Sprite (in __init__)

    def _check_fleet_edges(self):
        """Respond appropriatelly if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Threat this the same as if the ship got hit.
                self._ship_hit()
                break
                # once any alien hits the ship no need to check for others
                # so - break the loop

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update position of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(
                self.ship, self.aliens
        ):
            self._ship_hit()

        # Lookk  for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_events(self):
        # _method() is known as a helper method
        """Respond to key-presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the playes clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        # Ensure button can be clicked only when game not active
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to key-press"""
        # event.type are pygame methods
        # .ship refers to our ship class

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._exit_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
        elif event.key == pygame.K_r:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # Limiting the number of bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid off old bullets."""
        self.bullets.update()

        # Get rid off the disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_alien_colisions()

    def _check_bullet_alien_colisions(self):
        """Respond to a bullet-alien colisions."""
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        # True arguments tell Python to delete the given attributes

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            # Colissions is a dictionary
            # If the disctionary is called we loop through all the values
            # Each value is a list of aliens hit by a single bullet
            # We multiply the value of each alien with the len of the list
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            # method empty() removes all remaining sprites

            # scale up the speed with a new fleet
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # empty () method re,pves a;; s[rites from a group

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            # Wne 0 ships (lives) left, de-activate the game
            self.stats.game_active = False

            # Make cursor visible
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # Ship on top of the background
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Draw the scre information
        self.sb.show_score()

        # Draw the Play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _exit_game(self):
        """Function storing high score and quiting the game"""

        t_p = self.stats.top_pl
        self.stats.store_high_score(t_p)

        self.stats.exit_message()
        sys.exit()

    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                # Those are needed only when the game runs

            self._update_screen()

        # Check events and upd scrn is needed at all times in the program


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
