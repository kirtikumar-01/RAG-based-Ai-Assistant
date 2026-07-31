import json , os, requests
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
def create_embeddings(text_list):
    r= requests.post("http://localhost:11434/api/embed", json={
                          'model': "bge-m3",
                          'input': text_list
    })
    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r= requests.post("http://localhost:11434/api/generate", json={
                          'model': "llama3.2",
                          'prompt': prompt,
                          'stream': False,
    })
    response = r.json()['response']
    return response

df = joblib.load('chunk_embeddings.joblib')
query = input("Enter your query: ")
query_embedding = create_embeddings([query])[0]
similarity_scores = cosine_similarity([query_embedding], df['embedding'].tolist()).flatten()
# print(similarity_scores)
top_results = 3
top_indices = np.argsort(similarity_scores)[::-1][:top_results]  # Get top 3
# print("Top indices:", top_indices)
df_similar = df.iloc[top_indices]
# print("Top 3 similar chunks:")
# for index, row in df_similar.iterrows():
#     print(index, row['name'], row['text'],row['start'], row['end'])
#create a prompt for the LLM with the top 3 similar chunks and the query
prompt = f'''Here is the top video transcript chunks that are most similar to the query:
{df_similar[['name','start','end', 'text']].to_json(orient='records')}
--------------------------------------------------------------------------------------
"{query}"
The given question was asked in the context of the above video transcript chunks. Please answer the question based on the information provided in the video transcript chunks and aswer like a human. If the answer is not present in the video transcript chunks, please respond with "I know only what is present in the video transcript chunks. I do not have any additional information." Please provide a detailed answer to the question.
'''
with open('prompt.txt', 'w') as f:
    f.write(prompt)

response = inference(prompt)
with open('response.txt', 'w') as f:
    f.write(response)