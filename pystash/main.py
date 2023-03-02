import click

from pystash import config, crypt, store

STORE = store.Store(config.ROOT_PATH)
CRYPT = crypt.Crypt(config.ROOT_PATH)


@click.group()
@click.argument(
    "secret",
    type=click.STRING,
    nargs=1,
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="password to unlock vault.",
)
def main():
    pass


@main.command()
def get():
    click.echo("getting secret")


@main.command()
@click.argument("name", type=click.STRING)
@click.option("-v", type=click.STRING, help="Secret to store")
@click.option(
    "-f",
    type=click.File("r"),
    help="File to store",
)
@click.option("-e", type=click.STRING, help="Environment variable to store")
def put():
    click.echo("putting secret")


@main.command()
def delete():
    click.echo("deleting secret")
