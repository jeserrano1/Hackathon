import random

def obtener_tecla_adyacente(tecla):
    """ Obtener una tecla random adyactente a la tecla. """

    teclas_adyacentes = {
        '1': ['2'],
        '2': ['1', '3'],
        '3': ['2', '4'],
        '4': ['3', '5'],
        '5': ['4', '6'],
        '6': ['5', '7'],
        '7': ['6', '8'],
        '8': ['7', '9'],
        '9': ['8', '0'],
        '0': ['9'],
        'q': ['w', 'a', 's'],
        'w': ['q', 'a', 's', 'e'],
        'e': ['w', 's', 'd', 'r'],
        'r': ['e', 'd', 'f', 't'],
        't': ['r', 'f', 'g', 'y'],
        'y': ['t', 'g', 'h', 'u'],
        'u': ['y', 'h', 'j', 'i'],
        'i': ['u', 'j', 'k', 'o'],
        'o': ['i', 'k', 'l', 'p'],
        'p': ['o', 'l'],
        'a': ['q', 'w', 's', 'z'],
        's': ['q', 'w', 'e', 'a', 'd', 'z', 'x'],
        'd': ['w', 'e', 'r', 's', 'f', 'x', 'c'],
        'f': ['e', 'r', 't', 'd', 'g', 'c', 'v'],
        'g': ['r', 't', 'y', 'f', 'h', 'v', 'b'],
        'h': ['t', 'y', 'u', 'g', 'j', 'b', 'n'],
        'j': ['y', 'u', 'i', 'h', 'k', 'n', 'm'],
        'k': ['u', 'i', 'o', 'j', 'l', 'm'],
        'l': ['i', 'o', 'p', 'k'],
        'z': ['a', 's', 'x'],
        'x': ['s', 'd', 'z', 'c'],
        'c': ['d', 'f', 'x', 'v'],
        'v': ['f', 'g', 'c', 'b'],
        'b': ['g', 'h', 'v', 'n'],
        'n': ['h', 'j', 'b', 'm'],
        'm': ['j', 'k', 'n']
    }

    return random.choice(teclas_adyacentes.get(tecla, [tecla]))

def same(semilla):
    return semilla

def typo(semilla):
    pass
