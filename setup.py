from setuptools import setup, find_packages

setup(
    version="0.0.0",
    name="pystash",
    description="A terminal based secret keeper",
    author="Ben Aaron",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "appdirs~=1.4",
        "cryptography~=39.0",
        "click~=8.1",
        "pyperclip~=1.8",
    ],
    entry_points={
        "console_scripts": [
            "pystash=pystash.main:main",
        ],
    },
)
