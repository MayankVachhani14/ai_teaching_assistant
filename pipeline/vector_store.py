import faiss
import numpy as np
import pickle
import os

def save_index (embeddings, chunks):

    vector = np.array(embeddings).astype('foat32')

    dimension = vector.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vector)

    faiss.write_index(index, 'faiss_index.index')

    with open('chunks.pkl', 'wb') as f:
    pickle.dump(chunks, f)


def search_index(query_embedding, top_k=5):

    index = faiss.read_index('faiss_index.index')

    with open('chunks.pkl', 'rb') as f:
        chunks = pickle.load(f)

    query_vector = np.array(query_embedding).astype('float32')

    distances, indices = index.search(query_vector, top_k)

    results = [chunks[i] for i in indices[0]]

    return results
