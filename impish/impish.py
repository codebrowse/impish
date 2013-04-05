"""Impish: A friendly helper library for the `imp` module.

"""

from collections import namedtuple
import imp


Suffix = namedtuple('Suffix', 'suffix mode type')
Import = namedtuple('Import', 'file filename description')


def check_type(_import, _type):
  result = find(_import)
  if result.description.type == _type:
    return True
  return False


def isbuiltin(_import):
  return check_type(_import, imp.C_BUILTIN)


def issource(_import):
  return check_type(_import, imp.PY_SOURCE)


def iscompiled(_import):
  return check_type(_import, imp.PY_COMPILED)


def isextension(_import):
  return check_type(_import, imp.C_EXTENSION)


def ispackage(_import):
  return check_type(_import, imp.PKG_DIRECTORY)


def isfrozen(_import):
  return check_type(_import, imp.PY_FROZEN)


def find(module):
  metadata = list(imp.find_module(module))
  metadata[2] = Suffix(*metadata[2])
  return Import(*metadata)
