import sys
import json
from collections import defaultdict
from collections import Counter

""" 
THIS SCRIPT SHOULD TAKE IN TWEETS THEN COUNT MOST FREQUENT HASHTAGS
PRINT TO STD OUT:  " HASHTAG  COUNT"
"""

def tweet_parse(twt_fp):
	full_twts_list = []
	for line in twt_fp:
        	full_twts_list.append( json.loads(line))
	return full_twts_list

def grab_hashtag(full_tw_data):                  	
	try:	
		tags = full_tw_data['entities']['hashtags']   
	except:
		pass  
	try:                     
		if tags != []:
			if tags[0]['text'] != "":			
				return tags[0]['text']
	except: 
		pass
	
def main():
	tweet_file = open(sys.argv[1])
	tws_data = tweet_parse(tweet_file)
	tw_tags_count = Counter()	

	for i in range(len(tws_data)):
		tweet_datum = tws_data[i]
		x =  grab_hashtag(tweet_datum)
		if x is not None:					
			tw_tags_count[x] += 1

	for text, count in tw_tags_count.most_common(10):
		print text, float(count)

	tweet_file.close()


if __name__ == '__main__':
	main()
	

