# Snake Game (Pygame)

A simple 2D Snake game implemented in Python using Pygame. The project follows a modular architecture with clear separation of concerns, making it easy to extend and maintain.

---

## Features

- Snake movement in a grid-based environment  
- Food generation outside the snake's body  
- Snake length increases when food is eaten  
- Game over on wall or self-collision  
- Game over screen with a "Restart" button  

---

## Project Structure

- `main.py`: Entry point and game loop  
- `game_logic.py`: Core game mechanics (snake movement, collisions, food, reset)  
- `renderer.py`: Rendering of game elements (snake, food, game over screen)  
- `input.py`: Keyboard input handling and direction validation  
- `models.py`: Data structures (`Point`, `Direction`) and utility classes  
- `config.py`: Centralized game constants (screen size, grid, cell size)  
- `color_palette.py`: Color definitions for the game UI  

---


## How to Run

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Run the game:  
   ```bash
   python main.py
   ```

---

## Controls

- Arrow keys (`↑`, `↓`, `←`, `→`) to control the snake's direction  
