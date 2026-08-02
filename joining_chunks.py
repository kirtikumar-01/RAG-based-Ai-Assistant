#this code is for joining the chunks of transcripts json files and adds in modified_transcripts folder as json files
import os,json,math
n= 5
for file in os.listdir('transcripts'):
    file_path = os.path.join('transcripts', file)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        new_chunks = []
        num_chunks = len(data['chunks'])
        num_groups = math.ceil(num_chunks / n)
        for i in range(num_groups):
            start_index = i * n
            end_index = min((i + 1) * n, num_chunks)
            group_chunks = data['chunks'][start_index:end_index]
            new_chunks.append({
                'chunk_id': i + 1,
                'name':group_chunks[0]['name'],
                'text': ' '.join(chunk['text'] for chunk in group_chunks),
                'start': group_chunks[0]['start'],
                'end': group_chunks[-1]['end']
            })
        # Save the modified data to a new JSON file
        os.makedirs('modified_transcripts', exist_ok=True)
        with open(os.path.join('modified_transcripts', file), 'w', encoding='utf-8') as f:
            json.dump({'chunks': new_chunks}, f, ensure_ascii=False, indent=4)

