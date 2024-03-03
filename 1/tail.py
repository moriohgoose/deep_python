import click
import sys
from sys import stdin

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def tail(files):
    if not files:
        lines = sys.stdin.readlines()
        start_index = max(0, len(lines) - 17)
        for line in lines[start_index:]:
            click.echo(line, nl=False)
    else:
        for file in files:
            with open(file, 'r') as f:
                lines = f.readlines()
                if len(files) > 1:
                    click.echo(f"==> {file} <==")
                start_index = max(0, len(lines) - 10)
                for line in lines[start_index:]:
                    click.echo(line, nl=False)
            if len(files) > 1:
                click.echo()

if __name__ == "__main__":
    tail()