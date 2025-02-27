from pathlib import Path

import numpy as np
import typer
from loguru import logger

from basic_rl import basic_example

app = typer.Typer(name="app", pretty_exceptions_enable=False)

basic_example_app = typer.Typer(name="basic", add_completion=False)
app.add_typer(basic_example_app)


@basic_example_app.command("train")
def basic_example_train(
    grid_size: int,
    models_dir: Path = Path("data/models/basic_example"),
    logs_dir: Path = Path("data/models/basic_example/logs"),
    timesteps: int = 100_000,
) -> None:
    """Train the basic example model."""
    logger.info(f"Starting basic example training with {timesteps} timesteps")
    logger.info(f"Models will be saved to {models_dir}")
    logger.info(f"Logs will be saved to {logs_dir}")

    basic_example.train(
        models_dir=models_dir,
        logs_dir=logs_dir,
        grid_size=grid_size,
        total_timesteps=timesteps,
    )


@basic_example_app.command("evaluate")
def basic_example_evaluate(
    grid_size: int,
    model_path: Path = Path("data/models/basic_example/ppo_simple_env_final.zip"),
    num_episodes: int = 5,
) -> None:
    """Train the basic example model."""
    logger.info(f"Run stats for model {model_path}")
    basic_example.evaluate(model_path=model_path, grid_size=grid_size, num_episodes=num_episodes)


@basic_example_app.command("run")
def basic_example_run(
    grid_size: int,
    actor_x: int,
    actor_y: int,
    goal_x: int,
    goal_y: int,
    model_path: Path = Path("data/models/basic_example/ppo_simple_env_final.zip"),
) -> None:
    """Train the basic example model."""
    logger.info(f"Run stats for model {model_path}")
    problem_params = basic_example.ProblemParams(
        agent_pos=np.array([actor_x, actor_y]),
        goal_pos=np.array([goal_x, goal_y]),
    )
    solution = basic_example.run(model_path=model_path, grid_size=grid_size, problem=problem_params)
    logger.info(f"Solution: {solution.pretty_str()}")
