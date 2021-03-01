import os
import sys

# Creating lists of possible extensions
IMAGES = ['JPEG', 'PNG', 'JPG', 'SVG']
VIDEOS = ['AVI', 'MP4', 'MOV', 'MKV']
DOCUMENTS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
MUSIC = ['MP3', 'OGG', 'WAV', 'AMR']
ARCHIVES = ['ZIP', 'GZ', 'TAR']

# Creating lists of files
images_list = list()
videos_list = list()
documents_list = list()
music_list = list()
archives_list = list()
unknown_extension_list = list()
folders_list = list()

# Print all files with extensions from a specific folder if there are any
def print_files(folder):
    # Check if we have any files
    if len(folder) > 0:
        print('Files in folder: ')
        for file in folder:
            print(file)
    else:
        print(f'No files detected in {os.listdir(sys.argv[1])}.')

# Print all extensions 
def print_extensions(file_list):
    extensions_set = set()
    try:
        for file in file_list:
            extensions_set.add(file.split('.')[1].upper())
    except IndexError:
        pass
    print(f'All extensions: {extensions_set}')

# Sorting files by category
def sort_files(folder):
    for file in folder:
        try: 
            if file.split('.')[1].upper() in IMAGES:
                images_list.append(file)
            elif file.split('.')[1].upper in VIDEOS:
                videos_list.append(file)
            elif file.split('.')[1].upper in DOCUMENTS:
                documents_list.append(file)
            elif file.split('.')[1].upper in MUSIC:
                music_list.append(file)
            elif file.split('.')[1].upper in ARCHIVES:
                archives_list.append(file)
            elif os.path.isfile(file):
                unknown_extension_list.append(file)
            elif os.path.isdir(file):
                sort_files(file)
        except IndexError:
            print('Index Error Occured')
    print(f'Images: {images_list}')
    print(f'Videos: {videos_list}')
    print(f'Documents: {documents_list}')
    print(f'Music: {music_list}')
    print(f'Archives: {archives_list}')
    print(f'Unknown fextension files: {unknown_extension_list}')
    print(f'Folders: {folders_list}')

            
def main():
    path = sys.argv[1]

    sort_files(os.listdir(path))

    print_files(os.listdir(path))
    print_extensions(os.listdir(path))

    

if __name__ == '__main__':
    main()