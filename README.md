# AWS-Event-Analysis-Dashboard

The Event Analysis Dashboard is a web-based tool for visually presenting detected privilege escalation events. It offers an interactive user interface to display event statistics, trends, and details. The dashboard also includes filtering, search capabilities, and the ability to trigger actions directly from the interface.
Installation

    Clone this repository to your local machine:

    bash

git clone https://github.com/your-username/event-analysis-dashboard.git

Navigate to the project directory:

bash

cd event-analysis-dashboard

Create a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate

Install the required packages:

bash

    pip install -r requirements.txt

Usage
Starting the Server

    Start the backend server by running the following command:

    bash

    python app.py

    This will start the Flask development server, and the API will be accessible at http://localhost:5000.

CLI Commands

The following CLI commands are available:

    create_event: Create a new event.
    list_events: List all events.
    get_event: Get details of a specific event.
    update_event: Update details of an event.
    delete_event: Delete an event.
    export_to_csv: Export events data to a CSV file.

To use these commands, make sure the backend server is running.

bash

python cli.py <command> [options]

Examples:

    Create a new event:

    bash

python cli.py create_event --timestamp "2023-08-30 12:00:00" --user "user456" --resource "server2" --action "escalation" --details "Unauthorized access"

List all events:

bash

python cli.py list_events

Get details of a specific event:

bash

python cli.py get_event 1

Update details of an event:

bash

python cli.py update_event 1 --user "user789"

Delete an event:

bash

python cli.py delete_event 1

Export events data to a CSV file:

bash

    python cli.py export_to_csv events.csv

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
License

This project is licensed under the MIT License.
