import click

from dsarm_test import __version__


@click.command()
def main():
    """Prints Hello, World! to the console."""
    click.echo(f"Hello, World! Version: {__version__}")


@click.command()
def random_number():
    """Prints a random number between 1 and 100."""
    import random

    num = random.randint(1, 100)
    click.echo(f"Your random number is: {num}")


# Optionally add the command to a group for multi-command CLI
@click.group()
def cli():
    pass


cli.add_command(main)
cli.add_command(random_number)


if __name__ == "__main__":
    cli()
