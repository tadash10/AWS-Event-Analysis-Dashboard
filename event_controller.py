from flask import Blueprint, request, jsonify
from event_model import Event

event_bp = Blueprint('events', __name__)

events_data = [
    Event(1, "2023-08-30 10:00:00", "user123", "server1", "escalation", "Unauthorized access"),
    # More events...
]

@event_bp.route("/", methods=["GET"])
def get_events():
    return jsonify([event.__dict__ for event in events_data])

@event_bp.route("/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = next((event for event in events_data if event.id == event_id), None)
    if event:
        return jsonify(event.__dict__)
    return jsonify({"error": "Event not found"}), 404

@event_bp.route("/", methods=["POST"])
def create_event():
    data = request.json
    if not data or not all(key in data for key in ["timestamp", "user", "resource", "action", "details"]):
        return jsonify({"error": "Invalid data"}), 400

    new_event = Event(
        id=len(events_data) + 1,
        timestamp=data["timestamp"],
        user=data["user"],
        resource=data["resource"],
        action=data["action"],
        details=data["details"]
    )
    events_data.append(new_event)
    return jsonify(new_event.__dict__), 201
