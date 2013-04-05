# Impish

A friendly helper library for the `imp` module.

![](imp.jpg)

[Source](http://49.50.242.36/images/zoom/1971-1980/1973_7_83.jpg)


## Introduction

Impish implements helper methods which wrap `imp` module 
functionality to provide a friendlier programming interface with 
nicer exception handling.  

It is MIT-licensed.

----

###Definitons

**imp** *|imp|*  
noun  
a mischievous child: *a cheeky young imp.*  
• a small, mischievous devil or sprite.  

verb [ with obj. ]  
repair a damaged feather in (the wing or tail of a trained hawk) by attaching part of a new feather.

----

**impish** *|ˈimpiSH|*   
adjective  
inclined to do slightly naughty things for fun; mischievous: *he had an impish look about him*.

DERIVATIVES  
**impishly** adverb,  
**impishness** noun  

*Source*: New Oxford American Dictionary, via Apple OS X Dictionary app.

----

## Examples

**1. Finding a module's absolute file path**

    >>> import impish
    >>> impish.find('os').filename
    /path/to/os.py

**2. `find` also accepts modules as a parameter directly**

    >>> impish.find(os).filename
    /path/to/os

**Finding a module's file object**

	>>> impish.find('os').file
	<file object>
	
	>>> impish.find(os).file
	<file object>

**3. Checking for a built-in**

	>>> impish.isbuiltin('sys')
	True
	
	>>> impish.isbuiltin('os')
	False

**4. Checking for source**

	>>> impish.issource('sys')
	False
	
	>>> impish.isbuiltin('os')
	True

----

![](cb_qr.png)
  
Impish is a **[codebrow.se](http://codebrow.se)** package written by [Michael Van Veen](http://github.com/mvanveen).
