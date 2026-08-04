import whisper , json,os
#our videos and mp3 are in english so we dont need to translate, other languages must be translated to english using model of whisper. So we will use the medium model which is faster and more accurate than the small model. The large model is more accurate but it is slower and requires more resources.

model = whisper.load_model("medium")
audios = os.listdir('audios')   
for audio in audios:
    name = audio.split('- Pavan Lalwani')[0]
    print(f"Transcribing {name}")
 
    result = model.transcribe(f"audios/{audio}")
    # print(result)
    chunks = []
    for segment in result['segments']:
        chunks.append({'name': name, 'start': segment['start'], 'end': segment['end'], 'text': segment['text']})
    metachunks = {'chunks': chunks, 'text': result['text']}
    
    with open(f"transcripts/{name}.json", 'w') as f:
        json.dump(metachunks, f, indent=4)
    print(f"Finished transcribing {name}")