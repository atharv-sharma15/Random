from build_knowledge_base import collection
def search(collection, query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0]
