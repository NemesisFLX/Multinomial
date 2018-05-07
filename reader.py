def readWord( file ):
    word = ''
    for chunk in iter(lambda: file.read(1), ''):
        if chunk == ' ' or chunk == '\n':
            return word
        elif chunk == '':
            return False
        else:
            word += chunk
