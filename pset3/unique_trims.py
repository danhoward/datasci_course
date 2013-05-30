import MapReduce
import sys

"""
Implementing a method for trimming final 10 bases from a hypothetical gene sequence then outputting unique sequences
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:: sequence minus final 10 bases
    # value: gene identifier
    key = record[1][:-10]
    value = record[0]
    mr.emit_intermediate(key, record)

def reducer(key, record_list):
    # key: unique sequences
			mr.emit((key))
	
		
		


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)



