# Basic RL

## Installation

To setup project, you need to install:
- [poetry](https://python-poetry.org/)
- [invoke](https://www.pyinvoke.org/)
- [pre-commit](https://pre-commit.com/)

To install all dependencies and generate pre-commit hook files, use the command:
```bash
invoke install-dev
```

To see logs with [tensorboard](https://www.tensorflow.org/tensorboard), you need to install it:
```bash
pip install tensorboard
```

## Basic example

For now, this project contains only one example - basic example with the following parameters:

- the environment is a simple 2D square grid world
- the agent is a simple agent that can move in the grid
- the agent can move in 4 directions: up, down, left, right
- the goal is to reach the target cell

```
 . . . . G . . . . .   A - agent
 . . . . . . . . . .   G - goal
 . . . . . . . . . .
 . . A . . . . . . .
 . . . . . . . . . .
 . . . . . . . . . .
 . . . . . . . . . .
 . . . . . . . . . .
 . . . . . . . . . .
 . . . . . . . . . .
```

### Project structure

This project contains the following files:

- `custom_env.py` - contains the environment class and additional classes, like `ProblemParams` and `Solution`
- `train.py` - contains the training script
- `inference.py` - contains the script to evaluate model, and also run it of the real input from the user

### Train, evaluate and run

In the `cli.py` file described all the commands that you can run. To see all available commands, run the following command:

```bash
poetry run app --help
poetry run app basic --help
```

Some parameters are predefined, so you can just call the following command:

```bash
poetry run app basic train 10 # here 10 is the number of grid size
poetry run app basic evaluate 10
poetry run app basic run 10 5 5 3 8 # here 10 is the number of grid size, 5 5 is the start position, 3 8 is the target position
```

To see tesorboard logs, run the following command:

```bash
tensorboard --logdir=./data/models/basic_example/logs
```
