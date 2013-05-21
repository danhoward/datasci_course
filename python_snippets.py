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




