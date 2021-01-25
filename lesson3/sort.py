import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

text_files = []
video_files = []
image_files = []
music_files = []
unknown_files = []

for file in files:
    if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt'):
        text_files.append(file)
    elif file.endswith('.avi') or file.endswith('.mp4') or file.endswith('.mov'):
        video_files.append(file)
    elif file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
        image_files.append(file)
    elif file.endswith('.mp3') or file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.amr'):
        music_files.append(file)
    else:
        unknown_files.append(file)

print(f'Text files >> {text_files}')
print(f'Video files >> {video_files}')
print(f'Image files >> {image_files}')
print(f'Music files >> {music_files}')
print(f'Unknown files >> {unknown_files}')