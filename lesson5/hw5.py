symbol_map = {ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E', ord('Ё'): 'E', ord('Ж'): 'ZH', 
                ord('З'): 'Z', ord('И'): 'I', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
                ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'TS', ord('Ч'): 'CH',
                ord('Ш'): 'SH', ord('Щ'): 'SCH', ord('Ъ'): 'I', ord('Ы'): 'YU',ord('Ь'): 'I', ord('Э'): 'E', ord('Ю'): 'JU', ord('Я'): 'JA',
                ord('а'): 'f', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ё'): 'e', ord('ж'): 'zh',
                ord('з'): 'z', ord('и'): 'i', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
                ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts', ord('ч'): 'ch',
                ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): 'i', ord('ы'): 'yu',ord('ь'): 'i', ord('э'): 'e', ord('ю'): 'ju', ord('я'): 'ja'}


def normalize(text):
    result = ''
    for letter in text:
        if letter.isalpha():
            result += letter.translate(symbol_map)
        elif letter.isdigit():
            result += letter
        else:
            result += '_'
    return result

def main():
    pass

if __name__ == '__main__':
    main()