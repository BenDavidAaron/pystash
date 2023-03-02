import click
import os
import pathlib
import pyperclip

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
    help="Password to unlock vault.",
)
@click.option(
    "--val",
    "-v",
    prompt=True,
    prompt_required=False,
    hide_input=True,
    help="Manual entry to store in pystash.",
)
@click.option(
    "--env",
    "-e",
    help="Env Var to fetch and store."
)
@click.option(
    "--file",
    "-f",
    type=pathlib.Path,
    help="File to read and store.",
)
@click.option(
    "--clipboard",
    "-c",
    type=bool,
    help="Fetch secret from clipboard and store",
)
def put(
    secret: str,
    password: str,
    val: str,
    env: str,
    file: pathlib.Path,
    clipboard: bool
):
    if not CRYPT.check_key_hash(CRYPT.make_key_from_password(password)):
        click.echo("invalid password")
        return

    inputs = [
            int(bool(i))
            for i in
            [val, env, file, clipboard]
    ]
    if sum(inputs) > 1:
        click.echo("You may only submit one type of secret at a time")
        return
    if sum(inputs) < 1:
        click.echo("You must submit one of -v -e -f or -c to store")
        return

    if val is not None:
        secret_val = val

    if env is not None:
        secret_val = os.environ.get(env)
        if secret_val is None:
            click.echo(f"Env Var {env} not found")
            return

    if file is not None:
        secret_val = file.read_bytes()

    if clipboard:
        secret_val = pyperclip.copy()

    encrypted_secret = CRYPT.encrypt_with_password(
        bytes(secret_val, "utf-8"), password)
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
