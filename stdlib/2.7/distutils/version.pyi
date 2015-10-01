# Stubs for distutils.version (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Version:
    def __init__(self, vstring=None): ...

class StrictVersion(Version):
    version_re = ... # type: Any
    version = ... # type: Any
    prerelease = ... # type: Any
    def parse(self, vstring): ...
    def __cmp__(self, other): ...

class LooseVersion(Version):
    component_re = ... # type: Any
    def __init__(self, vstring=None): ...
    vstring = ... # type: Any
    version = ... # type: Any
    def parse(self, vstring): ...
    def __cmp__(self, other): ...