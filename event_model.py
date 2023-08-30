class Event:
    def __init__(self, id, timestamp, user, resource, action, details):
        self.id = id
        self.timestamp = timestamp
        self.user = user
        self.resource = resource
        self.action = action
        self.details = details
