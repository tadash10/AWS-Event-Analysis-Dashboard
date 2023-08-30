def update_event(event_id, updated_data):
    event = find_event_by_id(event_id)
    if event:
        for key, value in updated_data.items():
            setattr(event, key, value)
        return event
    return None
