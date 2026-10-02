# Snake Game in Python 

A classic Snake Game built with **Python and Turtle Graphics**, demonstrating object-oriented programming, keyboard event handling, game logic and collision detection.

The project is structured using separate classes for the snake, food and scoreboard, making the code modular and easier to maintain.

##  Game Overview

The player controls the snake using the arrow keys.

The objective is to collect the red food, increase the snake's length and achieve the highest possible score without colliding with the walls or the snake's own tail.

##  Features

* Snake starts with three segments
* Arrow-key controls
* Continuous snake movement
* Snake grows when food is collected
* Randomly positioned food
* Score tracking
* Wall collision detection
* Tail collision detection
* Game Over message
* Separate classes for the Snake, Food and Scoreboard
* Object-oriented design

##  Technologies Used

* **Python**
* **Turtle Graphics**
* Object-Oriented Programming (OOP)
* Inheritance
* Lists
* Functions and methods
* Lambda functions
* Keyboard event handling
* Collision detection
* Random number generation

## Project Structure

```text
Snake_game_in_python/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
└── README.md
```

### `main.py`

Contains the main game loop and coordinates the different components of the game.

### `snake.py`

Contains the `Snake` class and manages:

* Creating the snake
* Moving the snake
* Changing direction
* Adding new segments
* Keyboard controls

### `food.py`

Contains the `Food` class.

The food inherits from Python's `Turtle` class and is randomly positioned on the game screen.

### `scoreboard.py`

Contains the `Scoreboard` class and manages:

* Displaying the current score
* Increasing the score
* Displaying the Game Over message

##  Controls

| Key           | Action     |
| ------------- | ---------- |
| ↑ Up Arrow    | Move Up    |
| ↓ Down Arrow  | Move Down  |
| ← Left Arrow  | Move Left  |
| → Right Arrow | Move Right |

The game prevents the snake from immediately reversing direction into itself.

##  Snake Movement

The snake consists of multiple Turtle objects stored in a Python list:

```python
self.all_snakes = []
```

Each segment follows the position of the segment in front of it.

```text
HEAD → BODY → BODY → TAIL
```

The segments are moved from the tail towards the head so that each segment can follow the previous position of the segment in front of it.

## Food and Growth

When the snake's head gets close to the food:

```python
if snake.head.distance(food) < 15:
```

the food is moved to a new random position:

```python
food.refresh()
```

A new snake segment is then added:

```python
snake.extend()
```

and the score is increased:

```python
scoreboard.increase_score()
```

## Collision Detection

### Wall Collision

The game checks whether the snake's head has moved outside the game boundaries.

If the snake hits a wall, the game ends and the Game Over message is displayed.

### Tail Collision

The game checks the snake's head against the remaining snake segments:

```python
for segment in snake.all_snakes[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
```

The `[1:]` slice excludes the head and checks only the body and tail.

If the head collides with its own body, the game ends.

##  Scoreboard

The `Scoreboard` class inherits from the Turtle class:

```python
class Scoreboard(Turtle):
```

The score is stored as an object attribute and updated whenever the snake eats food.

The scoreboard also displays the Game Over message when the game ends.

## Key Python Concepts

This project demonstrates:

* Classes and objects
* Object-oriented programming
* Inheritance
* `super().__init__()`
* Class attributes
* Methods
* Lists of objects
* List slicing
* Loops
* Conditional statements
* Lambda functions
* Keyboard event handling
* Random number generation
* Collision detection
* Game loops
* Modular Python code

## How to Run

Clone the repository:

```bash
git clone https://github.com/vanitatech/Snake_game_in_python.git
```

Navigate to the project:

```bash
cd Snake_game_in_python
```

Run the game:

```bash
python main.py
```

A Turtle graphics window will open and the game will start.

## Future Improvements

* Add a persistent high-score system
* Increase difficulty as the score increases
* Add sound effects
* Add a restart option
* Prevent food from appearing on the snake
* Add different game levels
* Improve the visual design
