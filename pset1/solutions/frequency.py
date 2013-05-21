import sys
import json
from collections import defaultdict


def tweet_parse(twt_fp):
	twts = []
	txt = []	
	for line in twt_fp:
        	twts.append( json.loads(line))
	for twt in range(len(twts)):	
		txt.append(twts[twt]['text'])
	return txt

def main():
	count = 0
	tweet_file = open(sys.argv[1])
	tw = tweet_parse(tweet_file)
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


if __name__ == '__main__':
	main()

