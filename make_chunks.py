import whisper , json,os
#our videos and mp3 are in english so we dont need to translate
#my laptop will fuck up if i use better model so i will use medium model
model = whisper.load_model("medium")
audios = os.listdir('audios')   
for audio in audios:
    name = audio.split('- Pavan Lalwani')[0]
    print(f"Transcribing {name}")
    # result = model.transcribe(f"audios/1.0 Excel 2025 Complete Course From Beginner to Advanced Full Microsoft Excel Tutorial - Pavan Lalwani (720p, h264).mp4.mp3")
    result = model.transcribe(f"audios/{audio}")
    # print(result)
    chunks = []
    for segment in result['segments']:
        chunks.append({'name': name, 'start': segment['start'], 'end': segment['end'], 'text': segment['text']})
    metachunks = {'chunks': chunks, 'text': result['text']}
    
    with open(f"transcripts/{name}.json", 'w') as f:
        json.dump(metachunks, f, indent=4)
    print(f"Finished transcribing {name}")