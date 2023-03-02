import click

from pystash import config, crypt, store

STORE = store.Store(config.ROOT_PATH)
CRYPT = crypt.Crypt(config.ROOT_PATH)


@click.group()
def main():
    pass


@main.command()
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="password to unlock vault.",
)
def init(password: str):
    click.echo("setting up vault...")
    if CRYPT.exists():
        click.echo("vault already configured, exiting without changes")
        return
    CRYPT.record_key_hash(CRYPT.make_key_from_password(password))
    click.echo("vault configured, please remember your passkey")


@main.command()
@click.argument(
    "secret",
    type=click.STRING,
    nargs=1,
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=False,
    help="password to unlock vault.",
)
def get():
    click.echo("getting secret")


@main.command()
@click.argument(
    "secret",
    type=click.STRING,
    nargs=1,
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=False,
    help="password to unlock vault.",
)
def put():
    click.echo("putting secret")


@main.command()
@click.argument(
    "secret",
    type=click.STRING,
    nargs=1,
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=False,
    help="password to unlock vault.",
)
def delete():
    click.echo("deleting secret")
