import os , subprocess
files = os.listdir('videos')

for file in files:
    name = file.split('.')[0]
    print(name)
    subprocess.run(['ffmpeg', '-i', f'videos/{file}',  f'audios/{name}.mp3'])