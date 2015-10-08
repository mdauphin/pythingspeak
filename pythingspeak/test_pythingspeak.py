#-*- coding: utf-8 -*-
import pythingspeak
import unittest


class TestPyThingSpeak(unittest.TestCase):
	def test_update(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.update( [ 1, 2 ] )
		self.assertTrue(results)

	def test_feeds(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.feeds()
		self.assertTrue(results)

	def test_last(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.last()
		self.assertTrue(results)		

	def test_entry(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.entry(1)
		self.assertTrue(results)	

	def test_fields(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.fields(1)
		self.assertTrue(results)			

	def test_fields(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.fields(1)
		self.assertTrue(results)			

	def test_last_field(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.last_field(1)
		self.assertTrue(results)	
		
	def test_status_update(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.status_update()
		self.assertTrue(results)	

	def test_list_public_channels(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.list_public_channels()
		self.assertTrue(results)			

	def test_list_my_channels(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.list_my_channels()
		self.assertTrue(results)				

	def test_view_channel(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.view_channel()
		self.assertTrue(results)			

	def test_create_channel(self):
		ts = pythingspeak.ThingSpeak( channel_id=59596, api_key='ISXCEH1JHRQR85O4' )
		results = ts.create_channel()
		self.assertTrue(results)	
		
if __name__ == '__main__':
    unittest.main()		