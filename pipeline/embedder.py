from sentence_transformers import SentenceTransformer

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to embed chunks of text
def embed_chunks(chunks):
    
    # Extract the text from each chunk
    texts = [chunk['text'] for chunk in chunks]

    # Generate embeddings for the texts
    embeddings = model.encode(texts)

    # Add the embeddings back to the chunks
    return embeddings