# 🐍 Snake Game

A simple console-based Snake game written in Python using the `curses` library.

## 🎮 How to Play
- Use arrow keys (`↑`, `↓`, `←`, `→`) to control the snake.
- Eat food (`⬛`) to grow.
- Avoid hitting the walls or yourself.
- The game gets faster as you score higher!

## 🛠️ Requirements
- Python 3.x 
- `curses` module (included in standard library for Linux/macOS, installable for Windows) 
  
## 🚀 Installation & Run 
```sh   
# Clone the repository   
git clone https://github.com/yourusername/snake-game.git  
cd snake-game
    
# Run the game  
python snake.py 
``` 
  
## 🏆 Features
- Smooth snake movement
- Increasing difficulty
- Game-over detection
- Classic retro console look

## 🤖 GitHub Actions (Automated Testing)
This project includes automated tests using GitHub Actions to ensure the game runs correctly.

### Workflow Setup
A GitHub Actions workflow is included to automatically test the game:

```yaml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      
      - name: Install Dependencies
        run: |
          pip install pytest
      
      - name: Run Tests
        run: pytest test_snake.py
```

## 📜 License
This project is licensed under the MIT License. Enjoy coding! 🚀
