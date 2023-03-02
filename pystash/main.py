import click

from pystash import config, crypt, store

STORE = store.Store(config.ROOT_PATH)
CRYPT = crypt.Crypt(config.ROOT_PATH)


@click.group()
def main():
    print(STORE.dir)
    print(CRYPT.dir)
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
def get(secret: str, password: str):
    if not CRYPT.check_key_hash(CRYPT.make_key_from_password(password)):
        click.echo("invalid password")
        return
    encrypted_secret = STORE[secret]
    secret = CRYPT.decrypt_with_password(encrypted_secret, password)
    click.echo(secret)


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
@click.option(
    "--val",
    "-v",
    prompt=True,
    hide_input=True,
    help="secret to store in pystash",
)
def put(secret: str, password: str, val: str):
    if not CRYPT.check_key_hash(CRYPT.make_key_from_password(password)):
        click.echo("invalid password")
        return
    encrypted_secret = CRYPT.encrypt_with_password(bytes(val, "utf-8"), password)
    STORE[secret] = encrypted_secret
    return


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
