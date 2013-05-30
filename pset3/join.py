import MapReduce
import sys

"""
Implementing equivalent to SQL Relational Join in the Simple Python MapReduce Framework 
given bag of 'line items' and 'orders', join on 'order_id' attribute
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:: 'join element' - an int that stands for order_id
    # value: entire tuple containing order_id
    key = record[1]
    value = record
    mr.emit_intermediate(key, record)

def reducer(key, record_list):
    # key: order_id
    # value: whole tuple
   x = record_list[0]
   for record in record_list:
	try:	
		if record != record_list[0]:
			y = record
   			mr.emit((x+y))
	except:
		pass

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)



