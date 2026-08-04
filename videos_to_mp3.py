import os , subprocess
files = os.listdir('videos')
os.makedirs('audios', exist_ok=True)
for file in files:
    name = file.split('.mp4')[0]
    print(name)
    subprocess.run(['ffmpeg', '-i', f'videos/{file}',  f'audios/{name}.mp3'])