import json
import os

def load_all_vehicles(data_folder="data"):
    vehicles = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".json"):
            with open(os.path.join(data_folder, filename), "r") as f:
                vehicles.append(json.load(f))
    return vehicles

def get_video_path(user_query, vehicles):
    query_lower = user_query.lower()
    for vehicle in vehicles:
        if vehicle["model_name"].lower() in query_lower:
            video_id = vehicle.get("video_path")
            if video_id:
                return f"https://www.youtube.com/watch?v={video_id}"
    return None