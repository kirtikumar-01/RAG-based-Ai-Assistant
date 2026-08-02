# This is a free RAG based AI assistant based on open source resources to help you with your studies
## Step1 
Save your videos in the videos folder.
Then Run the videos_to_mp3.py file to convert videos to mp3...
All mp3s will be stored in audios folder
(you can tweak it according to the names,language and type of the video files)

## Step2
Run the transcripting_mp3.py file to store your preprocessed json chunks of your mp3s.
Then Run joining_chunks.py file
Chunks of each mp3 will be stored in transcripts folder

## Step3
Run the chunk_embedding.py file to have the embedding of all your chunks.
It will be stored as a pandas dataframe in chunk_embeddings.joblib as joblib pickle for faster execution.

## Step4
Run Query_response_generation.py file to ask a query and get a response from model.
We have used llama3.2 model, you change the model according to your need.
Response will be stored/viewed in the response.txt file.