import math
import uuid

min = int(input('Valor de início: ') or 1)
max = int(input('Valor final: ') or 10)
step = int(input('Step: ') or 1)
columns = int(input('Colunas: ') or 1)
spaces = int(input('Espaços: ') or 10)

title = ''

if step == 1: title = f'TABUADA DO {min} AO {max}'
else: title = f'TABUADA DO {min} AO {max}, DE {step} EM {step}'

print(f'\n\n{title}\n\n')

def calculate(min=1, max=10, step=1, columns=1, spaces=10):
    array = [[]]

    if min != 0 and step != 1: step = step - 1

    num_elements = math.ceil(((max + 1 - min) / step) / columns)

    for j, i in enumerate(range(min, max + 1, step), min):
        array[len(array) - 1].append(f'{i} x {i} = {i * i}')
        if i != max and j % num_elements == 0: array.append([])

    def make_text():
        text = ''
        max_len = len(array[-1][-1])

        i = 0
        
        while True:
            for j, el in enumerate(array, 1):
                if i == len(array[0]): return text
                if i > len(el) - 1: break

                spaces_str = ''
                num_spaces = spaces + ((max_len + spaces) - (len(el[i]) + spaces))

                for _ in range(num_spaces): spaces_str += '_'

                if j == len(array): text += f'{el[i]}'
                else: text += f'{el[i]}{spaces_str}'

            text += '\n'
            i += 1
    
    text = make_text()
    print(text)

    file = open(f'tabuada_{uuid.uuid1()}.txt', 'w')
    file.write(text)
    file.close()

calculate(min, max, step, columns, spaces)

input('\n\nPressione qualquer tecla para fechar')