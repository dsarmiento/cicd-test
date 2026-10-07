import click

from dsarm_test import __version__


@click.command()
def main():
    """Prints Hello, World! to the console."""
    click.echo(f"Hello, World! Version: {__version__}")


if __name__ == "__main__":
    main()
