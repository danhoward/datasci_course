import sys
import json



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
	
	for i in range(len(tw)):
		score = 0
		tweet = tw[i].encode('utf8')
		for word in sentiment:	
			if word in tweet:
				score += float(sentiment[word])
		print score
	sent_file.close()
	tweet_file.close()




if __name__ == '__main__':
	main()


