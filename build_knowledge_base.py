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

        price = vehicle['price_range']
        chunks = [
            f"{vehicle['model_name']} price range is Rs. {price['ex_showroom_min_inr_lakh']} - {price['ex_showroom_max_inr_lakh']} Lakh ({price['currency']}, ex-showroom)",
            f"{vehicle['model_name']} mileage is {vehicle['mileage']}",
            f"{vehicle['model_name']} seating capacity is {vehicle['seating_capacity']}",
            f"{vehicle['model_name']} features include {', '.join(vehicle['key_features'])}"
        ]

        for engine in vehicle.get('engine_options', []):
            chunks.append(
                f"{vehicle['model_name']} {engine['fuel_type']} engine: {engine['engine_name']}, "
                f"{engine['displacement_cc']}cc, {engine['power_bhp']} bhp, {engine['torque_nm']} Nm, "
                f"transmission options: {', '.join(engine['transmission'])}, "
                f"drivetrain: {', '.join(engine['drivetrain'])}"
            )

        for faq in vehicle.get('faqs', []):
            chunks.append(f"{faq['question']} {faq['answer']}")

        for chunk in chunks:
            collection.add(documents=[chunk], ids=[f"doc{doc_id_counter}"])
            doc_id_counter += 1

print("Knowledge base built. Total documents:", doc_id_counter - 1)