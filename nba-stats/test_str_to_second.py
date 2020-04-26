# -*- coding: utf-8 -*-

import unittest
from str_to_second import str_to_second

class TestConvertDate(unittest.TestCase):

	def test_with_hour_minute_and_secod(self):		
		convertion = str_to_second('01:00:62')
		self.assertTrue(convertion == 3662)

	def test_with_minute_and_second(self):
		convertion = str_to_second('60:60')		
		self.assertTrue(convertion == 3660)

	def test_with_second(self):
		convertion = str_to_second('26')		
		self.assertTrue(convertion == 1560)

	def test_with_integer(self):
		convertion = str_to_second(4)
		self.assertTrue(convertion == 240)

	def test_with_float(self):
		convertion = str_to_second(8.0)
		self.assertTrue(convertion == 480)