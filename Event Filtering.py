def filter_events(criteria):
    filtered_events = []
    for event in events_data:
        if all(getattr(event, key) == value for key, value in criteria.items()):
            filtered_events.append(event)
    return filtered_events
