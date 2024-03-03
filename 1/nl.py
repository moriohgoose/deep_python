import click
import sys
from sys import stdin


@click.command()
@click.argument('filename', required=False, type=click.File('r'), default=None)
@click.option('-', '--stdin', 'from_stdin', is_flag=True, help='Read from stdin instead of a file.')
def nl(filename, from_stdin):
    line_number = 1
    if from_stdin:
        file = sys.stdin
    else:
        file = filename if filename else sys.stdin

    for line in file:
        click.echo(f"{line_number}\t{line}", nl=False)
        line_number += 1

if __name__ == "__main__":
    nl()