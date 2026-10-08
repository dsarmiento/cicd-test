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


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a, b):
    """Adds two numbers and prints the result."""
    result = a + b
    click.echo(f"The sum of {a} and {b} is: {result}")


@cli.command()
def another():
    """Prints a message from the 'another' command."""
    click.echo("This is another command!")


@cli.command()
@click.argument("text")
def reverse(text):
    """Reverses the given text and prints the result."""
    click.echo(text[::-1])


@cli.command()
def version():
    """Print the installed package version."""
    click.echo(__version__)


if __name__ == "__main__":
    cli()
