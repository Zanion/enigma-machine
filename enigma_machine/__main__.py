# -*- coding: utf-8 -*-
import sys
import click
from enigma_machine.conf import defaults
from enigma_machine.enigma_app import EnigmaApp


ENIGMA_OPT = {}


@click.command()
def cli():
    # Set all provided arguments to configuration
    # ...

    app = EnigmaApp(**ENIGMA_OPT)
    app.run()
    sys.exit(0)
