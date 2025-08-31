"""
Main CLI entrypoint for panelizer-cli
Run this directly to launch the app.
"""

from panelizer.cli import PanelizerCli

def cli_entry():
    app = PanelizerCli()
    app.run()

if __name__ == "__main__":
    cli_entry()