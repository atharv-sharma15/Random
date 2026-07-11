import json
import os

DATA_DIR = "data"

def load_all_car_data(data_dir):
    """Loop through all JSON files in the data/ folder and load them."""
    car_data = {}
    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith(".json"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    car_data[filename] = data
                except json.JSONDecodeError as e:
                    print(f"❌ ERROR parsing {filename}: {e}")
                    continue
    return car_data

def print_summary(car_data):
    print(f"Loaded {len(car_data)} files from '{DATA_DIR}/'\n")
    print("=" * 70)
    for filename, data in car_data.items():
        print(f"FILE: {filename}")
        print(f"  Model Name       : {data.get('model_name')}")
        print(f"  Segment          : {data.get('segment')}")
        price = data.get("price_range", {})
        print(f"  Price Range      : Rs. {price.get('ex_showroom_min_inr_lakh')}L - {price.get('ex_showroom_max_inr_lakh')}L")
        print(f"  Fuel Types       : {data.get('fuel_types')}")
        print(f"  Seating Capacity : {data.get('seating_capacity')}")
        print(f"  Variants         : {len(data.get('variants', []))} -> {data.get('variants')}")
        print(f"  Video ID         : {data.get('video_path')}")
        print(f"  FAQs Loaded      : {len(data.get('faqs', []))}")
        print("-" * 70)

if __name__ == "__main__":
    car_data = load_all_car_data(DATA_DIR)
    print_summary(car_data)