from build_knowledge_base import collection
def search(collection, query, n_results=6):
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0]
def search_multi_vehicle(collection, query, all_vehicles, n_results_per_vehicle=4):
    query_lower = query.lower()
    mentioned = [v["model_name"] for v in all_vehicles if v["model_name"].split()[-1].lower() in query_lower]

    if len(mentioned) >= 2:
        all_chunks = []
        for model in mentioned:
            vehicle_query = f"{model} {query}"
            results = collection.query(query_texts=[vehicle_query], n_results=n_results_per_vehicle)
            all_chunks.extend(results["documents"][0])
        return all_chunks
    else:
        results = collection.query(query_texts=[query], n_results=6)
        return results["documents"][0]