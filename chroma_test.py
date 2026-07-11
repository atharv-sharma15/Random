import chromadb

client = chromadb.Client()
collection = client.create_collection(name="vehicles")

collection.add(
    documents=[
        "XUV700 has a mileage of 18 kmpl",
        "Scorpio-N has a mileage of 15 kmpl",
        "Thar has a mileage of 14 kmpl",
        "Bolero has a mileage of 16 kmpl",
        "XUV700 price range is 13.99 to 24.94 Lakh"
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["what is the mileage of Bolero"],
    n_results=1
)

print(results["documents"])