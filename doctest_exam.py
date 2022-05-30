
def split(line, types=None, delimiter=None):
    """Разбивает строку в список
    Пример:
    >>> split('erger 100 rfg 23.4')
    ['erger', '100', 'rfg', '23.4']
    >>> split('erger 100 rfg 23.4', [str, int, str, float])
    ['erger', 100, 'rfg', 23.4]
    >>> split('erger,100,rfg,23.4', delimiter=',')
    ['erger ', ' 100', 'rfg', '23.4']
    """

    fields = line.split(delimiter)
    if types:
        fields = [eval(ty + '(\'' + val + '\')') for ty, val in zip(types, fields)]
    return fields

line = "wefwe 34 dfge 21.2"
types = ['str', 'int', 'str', 'float']
print(split(line, types=types))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
