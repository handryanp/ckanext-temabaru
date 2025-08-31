import click


@click.group(short_help="temabaru CLI.")
def temabaru():
    """temabaru CLI.
    """
    pass


@temabaru.command()
@click.argument("name", default="temabaru")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [temabaru]
