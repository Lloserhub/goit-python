import os
import sys
import shutil
import zipfile
symbol_map = {ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E', ord('Ё'): 'E', ord('Ж'): 'ZH', 
                ord('З'): 'Z', ord('И'): 'I', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
                ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'TS', ord('Ч'): 'CH',
                ord('Ш'): 'SH', ord('Щ'): 'SCH', ord('Ъ'): 'I', ord('Ы'): 'YU',ord('Ь'): 'I', ord('Э'): 'E', ord('Ю'): 'JU', ord('Я'): 'JA',
                ord('а'): 'а', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ё'): 'e', ord('ж'): 'zh',
                ord('з'): 'z', ord('и'): 'i', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
                ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts', ord('ч'): 'ch',
                ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): 'i', ord('ы'): 'yu', ord('ь'): 'i', ord('э'): 'e', ord('ю'): 'ju', ord('я'): 'ja'}
# Creating lists of possible extensions
IMAGES = ['JPEG', 'PNG', 'JPG', 'SVG']
VIDEOS = ['AVI', 'MP4', 'MOV', 'MKV']
DOCUMENTS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
MUSIC = ['MP3', 'OGG', 'WAV', 'AMR']
ARCHIVES = ['ZIP', 'GZ', 'TAR']

def isFile(filename):
    try:
        if filename.find('.') != -1:
            return True
        else: 
            return False
    except:
        print('Unknown Exception Caught. Function isFile()')


def isDir(filename):
    try:
        if filename.find('.') == -1:
            return True
        else:
            return False
    except:
        print('Unknown Exception Caught. Function: isDir()')


def normalize(text):
    result = ''
    for letter in text:
        if letter.isalpha():
            result += letter.translate(symbol_map)
        elif letter.isdigit():
            result += letter
        elif letter == '.':
            result += '.'
        else:
            result += '_'
    return result


def move_file(filename):
    if isFile(filename):
        if filename.split('.')[1].upper() in IMAGES:
            print(f'{filename} is being put into images folder.')

            shutil.move(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\images\\{filename}')

            os.rename(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\images\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\images\\{normalize(filename)}')
        elif filename.split('.')[1].upper() in VIDEOS:
            print(f'{filename} is being put into videos folder.')

            shutil.move(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\video\\{filename}')

            os.rename(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\video\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\video\\{normalize(filename)}')
        elif filename.split('.')[1].upper() in DOCUMENTS:
            print(f'{filename} is being put into documents folder.')

            shutil.move(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\documents\\{filename}')

            os.rename(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\documents\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\documents\\{normalize(filename)}')
        elif filename.split('.')[1].upper() in MUSIC:
            print(f'{filename} is being put into music folder.')

            shutil.move(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\audio\\{filename}')

            os.rename(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\audio\\{filename}',
            f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\audio\\{normalize(filename)}')
        elif filename.split('.')[1].upper() in ARCHIVES:
            print(f'{filename} is being unpacked in archives folder.')

            with zipfile.ZipFile(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\{filename}', 'r') as zip_ref:
                zip_ref.extractall(f'C:\\Users\\38066\\Documents\\python\\goit-python\\lesson6\\testFiles\\archives\\{filename}')

        else:
            print(f'{filename} is not being put in any category.')
    else:
        print(f'{file} is not a File.')


def print_files(folder):
    print('+==============================================+')
    print('Files in folder: ')
    for file in folder:
        if isFile(file):
            print(f'  +--{normalize(file)} is a File.')
            move_file(file)
        elif isDir(file):
            pass
        else:
            print(f'{file} is a Special File.')
    print('+==============================================+')
    


def main():
    path = sys.argv[1]
    print_files(os.listdir(path))


if __name__ == '__main__':
    main()