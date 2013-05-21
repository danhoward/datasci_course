import sys
import json




def tweet_parse(twt_fp):
	twts = []
	txt = []	
	for line in twt_fp:
        	twts.append( json.loads(line))
	#for twt in range(len(twts)):	
	#	txt.append(twts[twt]['text'])
	return twts

def main():
	tweet_file = open(sys.argv[1])
	tw = tweet_parse(tweet_file)

	for i in range(len(tw)):
		tweet = tw[i] #.encode('utf8')
		print tweet['user']['location']
	tweet_file.close()




if __name__ == '__main__':
	main()

