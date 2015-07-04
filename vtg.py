import argparse

def configureParser():
	parser = argparse.ArgumentParser(description='Vimeo Thumbnail Getter')
	parser.add_argument('--videoId', required=True)
	parser.add_argument('--output', '-o', required=True, type=argparse.FileType('w'))
	parser.add_argument('--size', '-s', required=True, choices=['small', 'medium', 'large'])
	return parser

parser = configureParser()
args = parser.parse_args()
 
print 'We are going to get a ' + args.size + ' image from video ' + args.videoId