import os
import unittest

import impish

class ImpishTest(unittest.TestCase):
  def setUp(self):
    self._os = impish.find('os')

  def test_find_type(self):
    assert isinstance(self._os, impish.Import), 'Expected an Import namedtuple'

  def test_suffix_type(self):
    assert isinstance(self._os.description, impish.Suffix), 'Expected a Suffix namedtuple.'

  def test_file(self):
    assert isinstance(self._os.file, file), 'Exepcted file object.'

  def test_filename(self):
    assert 'os.py' == os.path.split(self._os.filename)[-1], 'got wrong filename, expected `os.py`.'

  def test_description_suffix(self):
    assert self._os.description.suffix == '.py', 'Expected suffix to be `.py`.'

  def test_description_mode(self):
    assert self._os.description.mode == 'U', 'Expected mode to be `U`.'

  def test_description_type(self):
    assert self._os.description.type == 1
