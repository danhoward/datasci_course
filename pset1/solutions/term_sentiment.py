import sys
import json
from collections import defaultdict


def afin_lines_to_dict(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
        	term, score = line.split("\t") # tab-delimited file needs to be parsed
        	scores[term] = int(score) 
	return scores

def tweet_parse(twt_fp):
	twts = []
	txt = []	
	for line in twt_fp:
        	twts.append( json.loads(line))
	for twt in range(len(twts)):	
		txt.append(twts[twt]['text'])
	return txt

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	tw = tweet_parse(tweet_file)
	sentiment = afin_lines_to_dict(sent_file)
	new_terms = defaultdict(int)	

	for i in range(len(tw)):
		tweet_score = 0
		tweet = tw[i].encode('utf8')
		tokens = tweet.split()
		for word in tokens:	
			if word in sentiment:
				tweet_score += float(sentiment[word])
		for word in tokens:
			if word not in sentiment:
				new_terms[word] += tweet_score
		for x in new_terms:
			print x, new_terms[x]
							

	sent_file.close()
	tweet_file.close()




if __name__ == '__main__':
	main()


"""
need to create dict of terms in tweet not in AFIN dict then apply score of total tweet to these words?



new_terms[term] += tweet_score

frequencies = defaultdict(int)
	for i in range(len(tw)):
		tweet = tw[i].encode('utf8')
		tokens = tweet.split()
		for word in tokens:
			frequencies[word] += 1
			count += 1
	
	for x in frequencies:
		print x, (frequencies[x] / float(count))
	tweet_file.close()

"""






