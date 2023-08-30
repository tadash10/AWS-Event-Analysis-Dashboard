from event_model import Event

def find_event_by_id(event_id):
    return next((event for event in events_data if event.id == event_id), None)
