import argparse
import json
import urllib2

def configureParser():
	parser = argparse.ArgumentParser(description='Vimeo Thumbnail Getter')
	parser.add_argument('--videoId', required=True)
	parser.add_argument('--output', '-o', required=True, type=argparse.FileType('w'))
	parser.add_argument('--thumbnailSize', '-s', required=True, choices=['small', 'medium', 'large'])
	return parser

def buildUrl(videoId, output):
	return "http://vimeo.com/api/v2/video/{videoId}.{output}".replace('{videoId}', videoId).replace('{output}', output)

def getVideoJson(videoId):
	url = buildUrl(videoId, 'json')
	print 'The url is ' + buildUrl(args.videoId, 'json')
	request = urllib2.urlopen(url)
	content = request.read();
	request.close()
	return content

def downloadThumbnail(url, path):
	request = urllib2.urlopen(url)
	image = request.read()
	request.close()
	path.write(image)
	path.close()

parser = configureParser()
args = parser.parse_args()
 
print 'We are going to get a ' + args.thumbnailSize + ' image from video ' + args.videoId
videoInfo = getVideoJson(args.videoId)
data = json.loads(videoInfo)[0]
key = 'thumbnail_' + args.thumbnailSize

if (key in data):
	thumbnailUrl = data[key]
	print 'The thumbnail url is ' + thumbnailUrl
	downloadThumbnail(thumbnailUrl, args.output)
else:
	print "Video " + args.videoId + " does not contains a " + args.thumbnailSize + " thumbnail"