#Opening and reading from files line by line
#This will work with HUGE files too without having to read the whole thing into memory at once.

with open(sys.argv[1]) as f:  
    for line in f:
        print line # do something with each line  

#Strings and substrings:

mystring = "The quick, brown fox jumped over the lazy dog."

#Does a word exist in a string?

word = "quick"
word in mystring # returns True

#How about a phrase?

phrase = "the lazy dog"
phrase in mystring # returns True 

#Words or phrases can be removed from strings by replacing the word or phrase with an empty string

mystring.replace(phrase,"")

#A string can be split into a list of words

mylist = mystring.split() # splits on whitespace  

#Or split on any other character or string you like

mylist = mystring.split(',')

#A list can be joined back into a string

" ".join(mylist)

#Join using any character or string you like

",".join(mylist) # words seperated by commas

#Or no character at all

"".join(mylist) # no space between words

#You can append an item to a list

mylist.append("newword")

#Lists are ordered and can be sorted

mylist.sort() 

#They can be reversed too

mylist.reverse()

#Sorting a list by item length is useful if it's a list of strings

mylist.sort(key = len)

#Dictionaries: A new empty dictionary

d = {}

#Add an item to the dictionary

d[key] = value

#Get an item from the dictionary

value = d[key] # error if key does not exist

#Get an item with default value if key does not exist

value = d.get(key, defvalue) # value = defvalue if key not in dict

#Increment value if key exists otherwise new value = 1

d[key] = d.get(key, 0) + 1 

#Iterate through the keys of a dictionary

for key in mydict:
    # do something with each key or value

#This can be handy for histograms and things

for tok in tokens:
    d[tok] = d.get(tok, 0) + 1

#You can get a list of the dictionary keys

mykeys = mydict.keys()

#Access dictionary values in order based on its values instead of its keys e.g.  get a list of keys sorted by dictionary values

sorted_keys = sorted(mydict, key=mydict.get)

#Or if the values are strings, maybe sorted by their length

sorted_keys = sorted(mydict, key=lambda k : len(mydict[k]))



"""
EXTENDED TUTORIAL FOLLOWS
"""
""" 
I got bored and decided to write an attempt at a bare-minimum Python tutorial for this class. I'm subscribed by email and pretty free today, so I'll check back if anyone has any questions. I'm no pro, but I've been coding in Python recreationally for a couple years now (and I actually try to keep up with what actual pros are saying) so I have some idea what I'm doing. I did this assignment in a few hours, including at least 45 minutes of which was kludging my way around Unicode problems that I'm not used to dealing with because Python 3 wouldn't have had them.

For knowledge levels, I'm aiming for "already knows a few things about programming", but I'm actually trying to give a snowball's chance to people who've only programmed from an IDE, or run a bunch of MATLAB code without ever touching a command line or similar. I won't explain things like what if or for means for the people who didn't notice the class specified "some programming knowledge". That said, anyone who's in this class and hasn't given up yet, I'm interested in any feedback (and hope the staff for this class notices as well). Same for people who want to yell at me and tell me I'm wrong. I also sometimes mention things without explaining them. Many of these things are "useful if you know what this means, but confusing if you don't." If you understand only 80% of this you might get along just fine with only that 80% for now.

I try to link to documentation where relevant. You'll notice I give almost no logic specific to the assignment; I'm just trying to tell you exactly which parts of Python you need to know before trying to figure out what to do with it. I skip over explaining stuff like print that you can figure out from context for the same reason. I often mention something and immediately say "don't do this". What I mean is, "this is generally a bad idea, but I think you should know it exists. Avoid it for now and look it up if you're that curious."

I'd normally wait a day and edit before posting something this massive, but we don't have that kind of time. Sorry in advance for any errors.

This Tutorial's Conventions
The code samples below are going to contain a combination of running programs and interactive typing in the Python shell. If you see a line starting with $, that means "you should be at the command line and type this in if you want to see it run yourself". If it starts with >>>, try it from within the Python shell (which you can get to by running "python" with no other options). If a code block starts with some_file_name.py, you can put all of the code in a file and save the file to try running it.

If a code sample has no shown output or filename, then I'm just explaining something without showing a full running example. I'll try not to do this often.

# denotes a comment. Same for any string surrounded with '''.

The Setup
Python is easy enough to set up that I refuse to even look at the virtual machine. If you prefer to use it, and you can get it up and running, then skip to the next section, but if you want help getting it set up, someone else will have to make that post.

If you don't already have it, go here and download Python 2.7.4 (or use your package manager if you both have one and know what that is). I like Python 3 better than Python 2, but Python 3 won't work with the code in this class and 2.7.4 is the newest and best Python 2.

If you don't already know what your command line is, it's time to get started. The provided examples from the class are in a Unix terminal. The teachers are probably using Linux, but if you are on a Mac, you also have a Unix command line. Windows users don't, but you go "Start->Run" and type "cmd" to get a Windows command prompt. You can run the programs themselves in Windows just fine as long as you stick to "python" and related commands, although the Unix native stuff like "ls" won't work. You can get by without it for now, or you can install Cygwin if you really want a Unix shell, or maybe some other nice person will make a detailed post about the Windows command prompt.

In both operating systems, the most important command is "cd" to change directories until you get to the one your program is in. If you can figure out "cd to my program directory, then python [file]" you can do enough to get through the first assignment. In all operating systems that I know of, the following all work:

$ cd [full directory path] # go to full directory path
$ cd / # go to top level directory
$ cd directory # go to directory contained in the current directory
If you want to see what's in your current directory, you can use "ls" in Unix and "dir" in Windows.

Github
Git is kind of tricky to get used to and if you've never used source control before you're not going to figure it out in the next day while also figuring out the assignment. You can try to run the code without using github for now; just download the ZIP file from the project page and extract it wherever. It's also fine to start using Git later when you have more time to figure it out.

Installing Packages
Even this first assignment requires third-party modules, so you might as well get this out of the way. The first thing I would recommend installing is pip, because pip makes it a lot easier to install other Python things. Get it here.

When installing a module, try these steps:

Look for a binary installer
$ pip install [module name]
Download the archive, extract it wherever you want it installed, then $ python setup.py install in whatever directory has setup.py in it.

For any remotely popular library, one of those things should work.

Editing and Running Code
Python comes with a programming environment called IDLE. It hasn't been updated since the dark ages, is slow, and has gross incompatibilities even with some code running only Python standard libraries. It's awful.

If you have a favorite plaintext editor, use that. If you don't have a favorite or don't know what that is, go download gedit.

To create a Python program, save it in a text file (it's standard to end this file with .py). Then run it by typing this from your program directory:

$ python my_program.py
Syntax and Whitespace
Python is highly unusual in that whitespace is syntactically significant. If you're used to a language with braces, it wouldn't be far off to say that anything that would be enclosed in braces is now newline+indent instead. (As an aside, if you know how to replace tabs with spaces in your editor, do so; you don't want invisible syntax errors). One corollary of significant indentation is that you can't indent otherwise, or you'll get SyntaxErrors.

If you ever need an empty block, Python has pass, a no-op keyword. You don't need an empty block.

I was very careful to mind my indentation here; all examples should be indented exactly as they are shown.

Finally, if you really want a one-line block, you can do this:

if condition(x): do_something()

Importing Outside Code
If you need code from a library, you can use import:

>>> import math
>>> math.sqrt(4)
2.0
If you need a specific function or variable only, you can use from:

>>> from math import sqrt
>>> sqrt(4)
2.0
(from math import * also works. Don't do that.)

If and Conditionals
Python if statements take the form:

if condition:
    # code here
elif condition2: # optional
    # more code here
else: # also optional
    # default code here
There can be any number of elifs. There is no switch. If if/elif/else is too unwieldy, you probably want a dictionary.

There is no &&, ||; you use the words and and or (there is no xor). The bitwise versions like & still exist.

Test equality with ==. There is an is keyword; don't use it.

You can easily test most collections for objects using the in keyword. For instance:

>>> a = [1,2,3]
>>> 3 in a
>>> True
>>> 'dog' in a
>>> False
Python is pretty liberal about coercing things to booleans; True and False are just special names for 1 and 0. Generally, containers are falsy if empty and truthy otherwise, and numbers are falsy if 0 and truthy otherwise. The special value None is falsy.

Functions
Functions are defined using the def keyword:

def square(x):
    return x*x
Note, by the way, the need for an explicit return statement. If you don't have one, Python won't warn you; it returns None, a null value. If you get mysterious errors referring to NoneType, this is one of the things to look for.

When calling functions, you can pass arguments positionally or by name:

>>> square(3)
9
>>> square(x=5)
25
Python supports default arguments and variable numbers of arguments, though you don't need them for this assignment. If you do decide to start playing with such things, read this first.

Python functions are first-class objects.

Lists
A list is essentially a dynamic array, and the literal syntax for it looks a lot like arrays in other languages:

a = [1,2,3]
You can get any given element by index:

>>> print a[2]
3
By the way, Python zero-indexes everything:

>>> print a[3]
Traceback (most recent call last):
    File "<stdin>", line 1, in 
IndexError: list index out of range
There is also an easy syntax for slicing (ranges of indices):

>>> print a[1:3]
[2,3]
You can also omit endpoints; empty slice argument default to the beginning and end of the list:

>>> a[:1], a[1:], a[:]
([1], [2,3], [1,2,3])
That last one is a handy way to copy a list so you can mutate the copy without changing the original. Can be particularly important if you're passing lists to functions.

There are two other data types similar to lists that are worth knowing if you write a lot of Python code:

tuple: Essentially an immutable list. They use parens instead of brackets like (1,2,3) and you can basically treat them like lists as long as you don't try to modify them.

set: Based on mathematical sets, they're sort of a cross between a list and a hash table. They discard all duplicates, can only contain hashable values, and make no effort to preserve the order of elements. Very fast because its restrictions allow it to be.

If none of that last part made sense, forget it for now. Just use lists.

Dictionaries and JSON
For dictionaries, think "hash table" if you know what that means. A dictionary associates values to keys:

>>> d = {1: 'cat', 2: 'dog', 7: ['chicken', 'geese']}
>>> d[1]
'cat'
Note that you look things up by key, not value:

>>> d['dog']
Traceback (most recent call last):
    File "", line 1, in 
KeyError: 'dog'
This is also true in for loops, as you'll see below.

As seen above, if you try to get a key that doesn't exist you will get a KeyError. There are several ways to handle this. The most straightforward would be to just check for the key first:

if k in D:
    x = D[k]
If you have a sensible default to fall back on, you could also use the .get method:

x = D.get(k, default_value)
You could also just handle the exception:

try:
    x = D[k1][k2]
    y = x[k3]
except KeyError:
    # If you want to handle all of the above missing keys the same way
Finally, the collections module has some dictionary variants that handle common cases like "a dictionary that always returns a default value for missing keys" and "a dictionary whose keys are things I'm counting".

The first assignment uses something called JSON, which stands for JavaScript Object Notation; it's a common format for sending data to be readable by multiple languages. Now that you know what a Python dictionary is, I can tell you that Python's json library parses a JSON string to a dictionary. So, for instance, the JavaScript object '{"legs": 4, "hungry", true}' would get parsed to {'legs': 4, 'hungry': True}. Yes, the translation is frequently that obvious because JavaScript objects are almost the same thing as Python dictionaries. This also means that you can just look at the JSON data from this assignment and tell what keys you're supposed to be looking for by inspection.

Strings
Strings are immutable. They can be indexed like lists.

>>> s = 'dog'
>>> s[0]
'd'
>>> s[0] = 'c'
Traceback (most recent call last):
    File "", line 1, in 
TypeError: 'str' object does not support item assignment
There is no char data type; a one-character string is still a string.

Strings can be delimited by ' or ". All my examples use the former because I hate the Shift key. Triple quotes allow literal (well, more literal...super-literal?) strings that can even include things like newlines and other normally-escaped characters. Such strings are often used for documentation.

Python strings use backslash escaping, although note that if your string is surrounded with ' you don't have to escape " and vice-versa.

If you know C-style string formatting ("%d" and such) you can do that. Python strings also have a .format() method with its own syntax that I forget approximately every other week. The basic version where you just need to stuff variable values in a string is pretty easy though:

>>> print 'I have {} dogs!'.format(3)
I have 3 dogs!

>>> print 'You can also {1}, {2}, or {1} things with {0}!'.format('indices', 'repeat', 'rearrange')
You can also repeat, rearrange, or repeat things with indices!
Python 2 has serious difficulties with Unicode that I'm not going to get into because I don't know that much about it and the class instructions already go into it better than I could.

Looping
Python while is extremely straightforward:

whileloop.py

x = 0
L = []

while x < 10:
    x += 1
    L.append(x)
   
print L

$ python whileloop.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
There is no do-while construct in Python.

for is a little different from what you might be used to. It can only be used as what some languages would call foreach:

forloop.py 

for x in 'dog':
    print x

$ python forloop.py
d
o
g
Note that for  iterates over the values, not the indices in most cases. The major exception is the dictionary:

forloopdict.py

D = {'a': 3, 'b': 10, 'x': 19}

for k in D:
    print k

$ python forloopdict.py
a
x
b
(Dictionaries make no guarantees about what order you get the keys in, but you will get them all.)

Python for essentially always takes the for guy in thing: form, with thing determining the exact behavior. Another important thing to know about is a file object, which lets you iterate line by line:

# This just prints a file

thing = open('thing.txt')
for line in thing:
    print(line)
By the way, you can only iterate over a file object once. Delete that lines function from the class code. It "uses up" the file object.

The standard counting for loop (0, 1, 2...) takes the form for i in range(N) (but use xrange instead if N is large)

The Python Shell and Why It's Great
You can get into the Python shell using $ python (with no filename). This lets you type in code and see the results immediately so you can quickly try things:

>>> for i in range(3):
...        print i
...
    0
    1
    2
>>>
Thanks to built-in documentation, the Python shell is actually a really cool way to get used to Python once you get past the most basic syntax. For example, let's say I don't remember what I can do to a list. So I initialize an empty list:

>>> a = []
Then I get a list of a's methods...

>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
By the way, ignore the methods that start and end with underscores (__). Not just for lists, but for everything. They're for overloading and you should basically never call them directly. Now, let's say I'm not sure what "insert" does, so I just ask:

>>> help(a.insert)
insert(...)
    L.insert(index, object) -- insert object before index
So, instead of thumbing through documentation trying to find the exact parts you want, you can just look stuff up as you start using it.

You can also make it so that your programs stay in a python shell instead of immediately bailing out by adding a "-i" option. In other words:

$ python -i foo.py
Will run foo.py, then put you in a Python REPL. And the best part is, Python remembers all the code it ran so you can check the values of variables this way! So, for instance:

badprogram.py

a = [1,2,3]
x = a.pop()
print a[2]

$ python -i badprogram.py
Traceback (most recent call last):
    File "", line 1, in 
IndexError: list index out of range
>>> 
Notice that even though my program failed entirely, I'm in a working Python shell. So now I check what a is:

>>> a
[1,2]
By the way, there is something that the sample homework does, but I haven't been doing. This is extremely on purpose. The provided files are structured like this:

def main():
    # main program code

if __name__ == '__main__':
    main()
This construct has its good points in general, but in the context of this assignment I think it is wrong. The reason you write code like the above is to make your code more "import safe"...that is, to write code that other people can import without immediately and automatically running it. This doesn't matter to us because we are uploading these files one at a time without any guarantee that they'll be able to see each other, so no one will ever import this code. And the downside of code like this is that it's harder to interactively debug:

worseprogram.py

def main():
    a = [1,2,3]
    x = a.pop()
    print a[2]

    if __name__ == '__main__':
        main()

$ python -i worseprogram.py
Traceback (most recent call last):
    File "", line 1, in 
IndexError: list index out of range
>>> a
Traceback (most recent call last):
    File "", line 1, in 
NameError: name 'a' is not defined
(For those who know Python, yes, I'm aware you can still get the variables out of main if you really want to. That's still a lot of typing we're doing to solve a problem we won't have. EDIT: actually, upon further reflection I'm pretty sure you can't without a separate debugger)

Comprehensions and Generators (bonus)
This section is optional, but worth it in my opinion. You can do everything in this section without this last bit, but I think these are useful first steps toward writing good Python code instead of code badly ported from some language that isn't Python.

If you're used to for in other languages, you may have been surprised at the apparently lack of flexibility in Python's for. This is because Python inverts the script a bit; instead of having for decide what to do to things, the things themselves dictate what for should do. Without getting into the gory details, for just asks an object for things until the object stops giving things.

This is surprisingly easy to write yourself. For example, I mentioned above that range(N) is bad for large N. This is because range in Python 2 returns a list:

>>> range(5)
[0, 1, 2, 3, 4]
This means that all those numbers are in memory at once, so if you write for i in range(100000), you have a huge list in memory. If, on the other hand, you just want a counter, you can easily make one:

def xrange(N):
    '''Don't actually use this in real code; Python 2 has a better one built in and Python 3 doesn't need it'''
    x = 0
    while x < N:
        yield x
        x += 1
The new part here is yield, which is the only piece of syntax that tells Python that it's defining a generator instead of a function. yield essentially means "return this value, but save my current state until something asks for the next value from me". We can then write something like this:

for i in xrange(3):
    print i
or even...

xranges.py

# pretend my xrange code from above is here

a = xrange(3)

for i in a:
    print i

for i in a:
    print i


$ python xranges.py
0
1
2
Surprised it only printed once? Remember when I said you can only iterate over a file object once? Here's why: a = xrange(3) creates a new generator. But once a runs its course, it is essentially "used up" and we need to create a new xrange to start from the beginning again. And this is why you can't iterate over the same file object twice; open(file) creates an object that can give you every line in the file, but only once. If you want the file again, you have to reload it. This is also why you should delete or comment out that "lines" file from the class sample code once you've started trying to manipulate the file yourself.

It is also possible to create one-line generators. For instance, let's say that I want to iterate over i squared instead of i:

squares = (k**2 for k in range(10))
Some other possibilities:

(f(x) for x in L)
(x for x in L if is_g(x))
Functional programming people: yes, that is Python's map and filter (map and filter also exist, but the performance is generally worse because Guido Van Rossum hates FP). By the way, all of the above can create lists too, if you don't want something more persistent than a one-time generator; just replace the outer parens with [] like so:

[f(x) for x in L] # This is a list, so you can run through it more than once, index it, etc
You can read more about comprehension syntax here.

By the way, if you're not used to dynamic typing, this whole discussion is a good reason to close your eyes and get used to it. This post was in part inspired by someone on another forum complaining about getting confused by how many type conversions are going on in this problem. To be fair, there are a lot! But you mostly don't have to worry about it if you just iterate over it and let the language figure it out. For instance, what does string.split() return? It's a list, but you don't normally need to care, since you're presumably writing something like:

for word in string.strip().split():
The builtin sorted returns a list, but reversed returns a generator. That annoys me on principle, but in practice it almost never comes up for the same reason.

I'm looking over my assignment now, and few of my functions are above five lines (including main functions). About 1/3 of them are generators and the rest are mostly single for loops. Things merrily switch from strings to lists to generator comprehensions, and I never had to care about any of this while I was writing it.
"""
