# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
IRAF replacement / command line tools collection.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    from .example_mod import *
    from .hselect import *
