from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated data for detected privilege escalation events
events_data = [
    {
        "id": 1,
        "timestamp": "2023-08-30 10:00:00",
        "user": "user123",
        "resource": "server1",
        "action": "escalation",
        "details": "User gained unauthorized access to server1"
    },
    # More events...
]

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events_data)

@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = next((event for event in events_data if event["id"] == event_id), None)
    if event:
        return jsonify(event)
    return jsonify({"error": "Event not found"}), 404

@app.route("/events", methods=["POST"])
def create_event():
    if not request.json or "timestamp" not in request.json or "user" not in request.json or \
       "resource" not in request.json or "action" not in request.json or "details" not in request.json:
        return jsonify({"error": "Invalid data"}), 400

    new_event = {
        "id": len(events_data) + 1,
        "timestamp": request.json["timestamp"],
        "user": request.json["user"],
        "resource": request.json["resource"],
        "action": request.json["action"],
        "details": request.json["details"]
    }
    events_data.append(new_event)
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
