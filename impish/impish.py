"""Impish: A friendly helper library for the `imp` module.

"""

from collections import namedtuple
import imp


Suffix = namedtuple('Suffix', 'suffix mode type')
Import = namedtuple('Import', 'file filename description')


def isbuiltin(module):
  result = find(module)
  if result.description.type == imp.C_BUILTIN:
    return True
  return False


def find(module):
  metadata = list(imp.find_module(module))
  metadata[2] = Suffix(*metadata[2])
  return Import(*metadata)
