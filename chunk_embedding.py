import json , os, requests
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embeddings(text_list):
    r= requests.post("http://localhost:11434/api/embed", json={
                          'model': "bge-m3",
                          'input': text_list
    })
    embedding = r.json()['embeddings']
    return embedding

json_files = os.listdir('transcripts')
chunk_data = []
chunk_id = 0
for json_file in json_files:
    print(f"Creating embeddings for {json_file}")
    with open(f"transcripts/{json_file}", 'r') as f:
        chunks = json.load(f)
        chunk_list = [chunk['text'] for chunk in chunks['chunks']]
        embeddings = create_embeddings(chunk_list)
    for i, chunk in enumerate(chunks['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_data.append(chunk)
        chunk_id += 1
        
    print(f"Finished creating embeddings for {json_file}")
    
# Create a DataFrame from the chunk data and save it to a joblib file
df = pd.DataFrame.from_records(chunk_data)
# print(df)
joblib.dump(df, 'chunk_embeddings.joblib')
