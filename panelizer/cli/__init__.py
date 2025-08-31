"""
panelizer.cli
===================

This package contains all UI-related components for interacting with the user.
Initially, it's CLI-based (Rich/Textual), helping users select input/output
directories and flowing through the processing pipeline.

Public cli:
- pick_directory()
"""

from .core import PanelizerCli
from .dir_picker import pick_directory

__all__ = ["PanelizerCli", "pick_directory"]