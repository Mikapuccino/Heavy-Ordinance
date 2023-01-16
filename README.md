# Project 3 - Fundamentos de Programação 2022/23 
# Heavy Ordinance

Project 3 by Daniela Gameiro nº 21901681 and Nelson Milheiro nº 21904365.

[Git repository](https://github.com/Mikapuccino/Heavy-Ordinance.git)

##  Project credits
* Daniela Gameiro

  1. Gameplay - Cannon (player rotation)
  2. Gameplay - Boats (collison and spawn frequency)
  3. Game Score
  4. Game Over
  5. `READ.md` project report

* Nelson Milheiro

  1. Gameplay - Cannon (Shoot, cannonball physics)
  2. Gameplay - Boats (Movement and spawn positions)
  3. Gameplay - HeavyOrdinance Class (Main loop, main menu, input logic, draw)
  4. Leaderboard - Leaderboard reading, writing and editing
  5. Sprites - All sprites used
  6. Background - Background image
  7. Sfx - All sound effects used (BoatDanger, BoatHit, CannonShot, GameOver)
  8. Music - Music used in the game (pirate)
  9. Additional Functions - All additional functions (load_sprite, text, text_in_line, text_in_pos)

## Solution architecture

The `Main.py` is where the function `HeavyOrdinance()` are called to start the game.

`Classes.py` ➞ Is responsible for defining the `HeavyOrdinance` class: encompassing the game loop, player inputs, game logic and screens. Also, it has the `Player`, `Cannonball` and `Boat` classes that inherit the `GameObject` class, which has an essential function for all game objects.

`Functions.py` ➞ Is responsible for loading the sprites (images) and rendering the texts of the menus.

## References

* [Random module](https://docs.python.org/3/library/random.html) used for calculations that required random values in the project, such as `spawn_interval` and `random_size`, both boat variables (enemies).