import invoke


@invoke.task
def install(context):
    """Install production requirements."""
    context.run("poetry install --only main")


@invoke.task
def install_dev(context):
    """Install development requirements."""
    context.run("poetry install")
    context.run("poetry run pre-commit install")
    context.run(
        """
        echo "Generating pyrightconfig.json";
        echo "{\\"venv\\": \\".\\", \\"venvPath\\": \\"$(poetry env info -p)\\", \\"exclude\\": [\\"tests\\"], \\"include\\": [\\"basic_rl\\"]}" > pyrightconfig.json
    """,
    )


@invoke.task
def check_style(context):
    """Run style checks."""
    context.run("ruff .")


@invoke.task
def tests(context):
    """Run pytest unit tests."""
    context.run("pytest -x -s")


@invoke.task
def tests_coverage(context, output="xml"):
    """Run pytest unit tests with coverage."""
    context.run(f"pytest --cov=basic_rl -x --cov-report={output}")
