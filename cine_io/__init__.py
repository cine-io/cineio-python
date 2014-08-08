"""
cineio
=======

See http://cine.io/ for documentation.

:copyright: (c) 2014 by cine.io
:license: MIT, see LICENSE for more details

"""

from .cine_io import Client, Project, Stream, StreamRecording, requests

from .version import __version__
__all__ = [Client, Project, Stream, StreamRecording, requests]
__author__ = 'cine.io engineering'
__copyright__ = 'Copyright 2014 cine.io'
__license__ = 'MIT'
__title__ = 'cineio'
__version_info__ = tuple(int(i) for i in __version__.split('.'))
