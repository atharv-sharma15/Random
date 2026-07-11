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
import difflib

def correct_vehicle_names_in_query(query, all_vehicles):
    known_names = []
    for v in all_vehicles:
        known_names.append(v["model_name"])
        known_names.append(v["model_name"].split()[-1])  # e.g. "Thar", "Neo", "700"

    words = query.split()
    corrected_words = []
    for word in words:
        clean_word = word.strip(".,?!").lower()
        matches = difflib.get_close_matches(
            clean_word, [n.lower() for n in known_names], n=1, cutoff=0.6
        )
        if matches:
            match_index = [n.lower() for n in known_names].index(matches[0])
            corrected_words.append(known_names[match_index])
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)