import urllib2
import json
import time
import datetime

APIKEY = 'APIkey'

def http_put():
        file = open("/home/pi/iot/temp_data.txt")
	distance= float(file.read())
	CurTime = datetime.datetime.now()
	url='http://api.heclouds.com/devices/设备ID/datapoints'
        values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":distance}]}]}

	print "the time is: %s" %CurTime.isoformat()
	print "The upload distance value is: %.3f" %distance

	jdata = json.dumps(values)
	print jdata
	request = urllib2.Request(url, jdata)
        request.add_header('api-key', APIKEY)
	request.get_method = lambda:'POST'
	request = urllib2.urlopen(request)
	return request.read()

time.sleep(5)
resp = http_put()
print "OneNET result:\n %s" %resp
file.closes
