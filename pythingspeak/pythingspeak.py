#-*-coding: utf-8-*-
import requests

class Channel(object):
	def __init___(self, channel_id=None):
		self.channel_id = channel_id

class ThingSpeak(object):
	RESPONSE_FORMAT = { 'TEXT' : '', 'JSON' : '.json', 'XML' : '.xml' }
	def __init__(self,
		channel_id=None,
		api_key=None, 
		url='http://api.thingspeak.com'):
		self.channel_id = channel_id
		self.api_key = api_key
		self.url = url
		self.response_format = self.RESPONSE_FORMAT['JSON']
		
	def convertListToDico(self, data):
		arr = {}
		for i in range(len(data)):
			arr[ 'field%d' % (i+1) ] = data[i]
		return arr
		
	def update(self, data):
		arr = {}
		if isinstance(data, (list, tuple)):
			arr = self.convertListToDico(data)
		arr['api_key'] = self.api_key
		results = requests.post( self.url + "/update", params=arr )
		return results
		
	def feeds(self, results=100):
		''' retrieve an HTML page containing JSON Channel feed '''
		params = { 'api_key' : self.api_key, 'results' : results }
		results = requests.get( "%s/channels/%d/feeds%s" % (self.url,self.channel_id,self.response_format), params=params )
		return results
		
	def last(self):
		''' get the last entry in a Channel feed '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d/feeds/last%s" % (self.url,self.channel_id,self.response_format), params=params )
		#print results.text
		return results
		
	def entry(self, entry_id):
		''' To get a specific entry in a Channel's feed '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d/feeds/%d%s" % 
		(self.url,self.channel_id,entry_id,self.response_format), params=params )
		#print results.text
		return results
		
	def fields(self, field):
		''' To view a Channel's field feed '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d/fields/%d%s" % 
		(self.url,self.channel_id,field,self.response_format), params=params )
		#print results.text
		return results		
		
	def last_field(self, field):
		''' To view a Channel's field feed '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d/fields/%d/last%s" % 
		(self.url,self.channel_id,field,self.response_format), params=params )
		#print results.text
		return results			
		
	def status_update(self):
		''' To view a Channel's status updates '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d/status%s" % 
		(self.url,self.channel_id,self.response_format), params=params )
		#print results.text
		return results		

	def list_public_channels(self):
		''' To view a list of public Channels '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/public%s" % 
		(self.url,self.response_format), params=params )
		return results		

	def list_public_channels(self):
		''' To view a list of your Channels '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels%s" % 
		(self.url,self.response_format), params=params )
		return results			
		
	def view_channel(self):
		''' To view a specific Channel '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels/%d%s" % 
		(self.url,self.channel_id,self.response_format), params=params )
		return results		

	def create_channel(self):
		''' To create a new Channel '''
		params = { 'api_key' : self.api_key  }
		results = requests.get( "%s/channels%s" % 
		(self.url,self.channel_id,self.response_format), params=params )
		return results			