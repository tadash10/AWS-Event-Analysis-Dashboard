def is_valid_event_data(data):
    return data and all(key in data for key in ["timestamp", "user", "resource", "action", "details"])
