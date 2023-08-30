def delete_event(event_id):
    event = find_event_by_id(event_id)
    if event:
        events_data.remove(event)
        return True
    return False
