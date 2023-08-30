def get_event_statistics():
    user_counts = {}
    resource_counts = {}
    action_counts = {}

    for event in events_data:
        user_counts[event.user] = user_counts.get(event.user, 0) + 1
        resource_counts[event.resource] = resource_counts.get(event.resource, 0) + 1
        action_counts[event.action] = action_counts.get(event.action, 0) + 1

    return {
        "user_counts": user_counts,
        "resource_counts": resource_counts,
        "action_counts": action_counts
    }
