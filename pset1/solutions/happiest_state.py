import sys
import json
from collections import defaultdict
from collections import Counter


def afin_lines_to_dict(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
        	term, score = line.split("\t") # tab-delimited file needs to be parsed
        	scores[term] = int(score) 
	return scores

def tweet_parse(twt_fp):
	full_twts_list = []
	for line in twt_fp:
        	full_twts_list.append( json.loads(line))
	return full_twts_list

def grab_location(full_tw_data):                   # this shows the logic for grabbing location data from full tweet_data	
	try:	
		if full_tw_data['user']['location'][-4:-2] == ", ":
			s = full_tw_data['user']['location']
			state = s[-2:]
			return state
	except:
		pass
	

def get_score(full_tw_data, sentiments):
	tweet_score = 0
	try:	
		tw_body = (full_tw_data['text']).encode('utf8')
		for word in sentiments:
			if word in tw_body:
				tweet_score += float(sentiments[word])
		return tweet_score
	except:
		pass
	
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	tws_data = tweet_parse(tweet_file)
	sentiment = afin_lines_to_dict(sent_file)
	state_score = Counter()	

	for i in range(len(tws_data)):
		tweet_datum = tws_data[i]
		state = grab_location(tweet_datum)                         			  # GRAB THE STATE
		try:		
			tw_score = get_score(tweet_datum, sentiment)		                  # GRAB THE TWEET SCORE
			state_score[state] += tw_score
		except:
			pass

	for ste, score in state_score.most_common(2):			# the bleow filter knowcks off the none value AFTER iteration !!
		if ste is not None:		
			print str(ste)

	sent_file.close()
	tweet_file.close()




if __name__ == '__main__':
	main()

