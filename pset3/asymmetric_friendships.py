import MapReduce
import sys

"""
Implementing a method for viewing asymmetric friend relationships in [user, friend] tuples
This will look for user's friends who are not friends with said user (asymmetric friendship)

Issue: need to identify users which have friends who do not friend them back
suggested step is to organize by key = friend value = users who have friended them

we have user, friend sets - want to look for freind - user relationship

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:: 'user' and friend
    # value: friend and user (friended)
    value = (record[1])  # friend
    if record[0] < record[1]:
    	key = ((record[0], record[1]))  # user that has the friend
    elif record[1] < record[0]:
	key = ((record[1], record[0]))
       
    mr.emit_intermediate(key, value)

def reducer(key, record_list):
    # key: user
    # value: asymmetric friends
	if len(record_list) == 1:
		mr.emit((key[0], key[1]))
		mr.emit((key[1], key[0]))  # will produce the friend and users who friended that friend
		
# [record[0] for record in record_list]

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)



