import MapReduce
import sys

"""
Implementing a simple "friend count" function for [user, friend] tuples
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:: person (user)
    # value: user's friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, record_list):
    # key: user
    # value: list of all friends
   count = 0
   for record in record_list:
   	count += 1
   mr.emit((key, count))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)



