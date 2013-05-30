import MapReduce
import sys

"""
Implementing a method for multiplying matricies represented in sparse form (row, col, val)
This will look for user's friends who are not friends with said user (asymmetric friendship)

i = row
j = colum

k = row
l = column

final:
i by l matrix with 0,0 filled by dot product value from matrix A row 1 and matrix B column 1, etc. for other indicies



"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:: row and "target column" in final matrix (from matrix a); "target column" and column from matrix b
    # value: source matrix, source col or row (for a, b), value
    for i in range(0,5):
	if record[0] == 'a':
    		key = (record[1], i)
   		value = ('a', record[2], record[3]) # second value in tuple allows tuples to be "matched up" in reduce phase
		mr.emit_intermediate(key, value)
    for i in range(0,5):	
	if record[0] == 'b':
		key = (i, record[2])
		value = ('b', record[1], record[3])
		mr.emit_intermediate(key, value)
       

def reducer(key, values):
    # key: coordinate from above ("target coordinate" in resultant matrix)
    # value: all values (from a and b) mapped to said coordinate
	# want something that basically says: for values if there exist 2 values with the same index # (ist number in tuple) , then multiply the two
	total = 0	
	for value in values:
		z = value
		for val in values:
			if z[1] == val[1] and z[0] == 'a' and val[0] == 'b':
				total += (z[2] * val[2])
	key = list(key)
	key.append(total)
	mr.emit((tuple(key)))  # will produce a three-tuple with coordinate and value in sparse matrix format
		


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)



