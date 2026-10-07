import click

from dsarm_test import __version__


# Optionally add the command to a group for multi-command CLI
@click.group()
def cli():
    pass


@cli.command()
def main():
    """Prints Hello, World! to the console."""
    click.echo(f"Hello, World! Version: {__version__}")


@cli.command()
def random_number():
    """Prints a random number between 1 and 100."""
    import random

    num = random.randint(1, 100)
    click.echo(f"Your random number is: {num}")


@cli.command()
@click.argument("name", required=False, default="World")
def greet(name):
    """Greets the user by name."""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()
