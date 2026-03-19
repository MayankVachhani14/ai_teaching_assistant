import faiss
import numpy as np
import pickle

def save_index(embeddings, chunks):
    vectors = np.array(embeddings).astype("float32")
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)
    faiss.write_index(index, "data/index.faiss")
    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def search_index(query_embedding, top_k=3):
    index = faiss.read_index("data/index.faiss")
    with open("data/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, top_k)
    results = [chunks[i] for i in indices[0]]
    return results