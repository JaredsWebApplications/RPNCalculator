"""
This is the driver code for the RPN
caclulator
"""

from flask.cli import FlaskGroup

from webapplication.bauer import app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
