# Impish

A friendly helper library for the `imp` module.

----

**imp** *|imp|*  
noun  
a mischievous child: *a cheeky young imp.*  
• a small, mischievous devil or sprite.  

verb [ with obj. ]  
repair a damaged feather in (the wing or tail   of a trained hawk) by attaching part of a new feather.

-----

**impish** *|ˈimpiSH|*   
adjective  
inclined to do slightly naughty things for fun; mischievous: *he had an impish look about him*.

DERIVATIVES  
**impishly** adverb,  
**impishness** noun  

*Source*: New Oxford American Dictionary, via Apple OS X Dictionary app.

----

## Introduction

This is a small helper library

## Examples

**Finding a module's absolute file path**

    >>> import impish
    >>> impish.find('os')
    /path/to/os.py

    >>> impish.find(os)
    /path/to/os
    
**TODO**: determine if I can get shared code object (e.g. `.so` file)
    
    >>> impish.find(__import__)
    TypeError: `__import__` is built-in.

**Checking for a built-in**

	>>> impish.isbuiltin('__import__')
	True
	
	>>> impish.isbuiltin('os')
	False

**Finding a module's file object**

	>>> impish.find_file('os')
	<file object>
	
	>>> impish.find_file(os)
	<file object>

