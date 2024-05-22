# Tetris with Python

## Description

This repository hosts a simple Tetris game implemented in Python using the Pygame library. Tetris is a classic tile-matching puzzle video game where players manipulate falling tetrominoes (geometric shapes composed of four square blocks) to create complete horizontal lines. When a line is completed, it disappears, and the player earns points.

## Features

- **Basic Tetris Gameplay:** Players can control the falling tetrominoes using arrow keys to move left, right, rotate, or accelerate their descent.
- **Scoring System:** Points are awarded for completing lines, with additional points for clearing multiple lines simultaneously, and the game keeps track of the high score in the current game session
- **Additional shape tiles** U, plus sign ,stair(hill) -**Dark mode/Light mode** We have different color schematics for each preference -**Hard mode/Easy mode:** Adjusts the falling speed of the figure accordingly
- **Game Over State:** The game ends when the stack of tetrominoes reaches the top of the playfield, triggering a game over state.
- **Graphics and UI:** The game features simple graphics and a user interface displaying the current score. Pygame's drawing functions are used to render the game elements.

## Repository Structure

- `game.py`: The main script that initializes the Pygame environment and implements the game loop.
- `tetris.py`: Contains the `Tetris` class responsible for managing the game logic, including tetromino movement, collision detection, scoring, and game state.
- `shape.py`: Defines the `Shape` class representing individual tetrominoes, along with their shapes, colors, and rotation.
