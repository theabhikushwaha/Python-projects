# Snake Game 🐍

A basic, Nokia-style Snake game built with Python and `pygame`.
Made as a small learning/portfolio project.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Gameplay

Move the snake around the grid to eat food (red square). Each piece of food
eaten makes the snake grow by one segment and increases your score. The game
ends if the snake hits a wall or runs into itself.

## Controls

| Key                | Action        |
|--------------------|---------------|
| Arrow keys / WASD  | Move          |
| P                  | Pause/Resume  |
| R                  | Restart (after game over) |
| Esc / Q            | Quit          |

## Setup

```bash
git clone https://github.com/<your-username>/snake-game.git
cd snake-game
pip install -r requirements.txt
python snake.py
```

Requires Python 3.8+.

## Project structure

```
snake-game/
├── snake.py          # game source code
├── requirements.txt  # dependencies
└── README.md
```

## Possible improvements (ideas for later)

- Increasing speed as the score grows
- High score saved to a local file
- Different difficulty levels / grid sizes
- Sound effects

## License

MIT — feel free to fork and modify.
