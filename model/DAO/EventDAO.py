import csv
import glob
import json
from model.Event import Event
import os
from datetime import date as dt_date


def select_all_events():
	files = glob.glob('./model/saved_events/*.json')
	events = []
	for f in files:
		with open(f, 'r') as nf:
			content = nf.read()
			event = Event(name=None)
			e = json.loads(content)

			if e['_Event__start_date'] is not None:
				d_start = e['_Event__start_date']
				d_start = list(map(int, d_start.split('/')))
				d_start.reverse()
				e['_Event__start_date'] = dt_date(*d_start)

			if e['_Event__end_date'] is not None:
				d_end = e['_Event__end_date']
				d_end = list(map(int, d_end.split('/')))
				d_end.reverse()
				e['_Event__end_date'] = dt_date(*d_start)

			event.__dict__.update(e)
			events.append(event)
	return events


def select_event(event_name):
	if event_name in os.listdir('./model/saved_events/'):
		file_name = './model/saved_events/{}.json'.format(event_name)
		with open(file_name, 'r') as f:
			content = f.read()
			event = Event(name=None)
			e = json.loads(content)
			event.__dict__.update(e)
		return event
	else:
		print('Evento não encontrado!!!')


def select_by_period(start=None, end=None):
	start = start if start is not None else dt_date.min
	end   = end if end is not None else dt_date.max

	if isinstance(start, dt_date) and isinstance(end, dt_date):
		events = [e for e in select_all_events() if start <= e <= end]
	else:
		raise TypeError("start e end devem ser do tipo date (de datetime)!!!")
	return events



def save_event(event):
	if event.get_start_date() is not None:
		event._Event__start_date = '{}/{}/{}'.format(event.get_start_date().day,
		                                             event.get_start_date().month,
		                                             event.get_start_date().year)

	if event.get_end_date() is not None:
		event._Event__end_date = '{}/{}/{}'.format(event.get_end_date().day,
		                                             event.get_end_date().month,
		                                             event.get_end_date().year)

	event_json = json.dumps(event.__dict__)
	file_name = './model/saved_events/{}.json'.format(event.get_name().upper())
	with open(file_name, 'w') as f:
		f.write(event_json)


def update_event(event):
	save_event(event)
