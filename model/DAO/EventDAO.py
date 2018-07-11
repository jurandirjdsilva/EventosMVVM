import csv
import glob
import json
from model.Event import Event
import os

def get_all_events():
	files = glob.glob('./model/saved_events/*.json')
	events = []
	for f in files:
		with open(f, 'r') as nf:
			content = nf.read()
			event = Event(name=None)
			e = json.loads(content)
			event.__dict__.update(e)
			events.append(event)
	return events

def save_event(event):
	event_json = json.dumps(event.__dict__)
	file_name = './model/saved_events/{}.json'.format(event.get_name().upper())
	with open(file_name, 'w') as f:
		f.write(event_json)

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

def update_event(event):
	save_event(event)