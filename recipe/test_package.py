from openff.utilities import __version__

from packaging.version import Version

assert Version(__version__) > Version("0.0.0")
print('{get_ambertools_version()=}')
