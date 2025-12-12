from openff.utilities import __version__, get_ambertools_version

from packaging.version import Version

assert Version(__version__) > Version("0.0.0"), f"FOUND VERSION {__version__}"
print("{get_ambertools_version()=}")
