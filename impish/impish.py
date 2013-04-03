"""Impish: A friendly helper library for the `imp` module.

"""

from collections import namedtuple
import imp


Suffix = namedtuple('Suffix', 'suffix mode type')
Import = namedtuple('Import', 'file filename description')


def isbuiltin():
  pass

def find(module):
  if isinstance(module, basestring):
    metadata = list(imp.find_module(module))
    metadata[2] = Suffix(*metadata[2])
    return Import(*metadata)
