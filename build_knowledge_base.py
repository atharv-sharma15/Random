import json
import os
import chromadb

client = chromadb.Client()
collection = client.create_collection(name="vehicles")

data_folder = "data"
doc_id_counter = 1

for filename in os.listdir(data_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(data_folder, filename)
        with open(filepath, "r") as file:
            vehicle = json.load(file)

        chunks = [
            f"{vehicle['model_name']} price range is {vehicle['price_range']}",
            f"{vehicle['model_name']} mileage is {vehicle['mileage']}",
            f"{vehicle['model_name']} engine options are {vehicle['engine_options']}",
            f"{vehicle['model_name']} seating capacity is {vehicle['seating_capacity']}",
            f"{vehicle['model_name']} features include {', '.join(vehicle['key_features'])}"
        ]

        for chunk in chunks:
            collection.add(documents=[chunk], ids=[f"doc{doc_id_counter}"])
            doc_id_counter += 1

print("Knowledge base built. Total documents:", doc_id_counter - 1)