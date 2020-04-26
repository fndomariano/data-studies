# -*- coding: utf-8 -*-

def str_to_second(time):

	if isinstance(time, int) or isinstance(time, float):
		return time * 60

	time = time.split(':')

	if (len(time) == 3):
		hours = int(time[0]) * 3600
		minutes = int(time[1]) * 60
		seconds = int(time[2])
		return (hours + minutes + seconds)	

	if (len(time) == 2):
		minutes = int(time[0]) * 60
		seconds = int(time[1])
		return (minutes + seconds)	

	return int(time[0]) * 60