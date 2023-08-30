def export_events_to_csv(file_path):
    import csv
    with open(file_path, mode="w", newline="") as csv_file:
        fieldnames = ["id", "timestamp", "user", "resource", "action", "details"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for event in events_data:
            writer.writerow(event.__dict__)
