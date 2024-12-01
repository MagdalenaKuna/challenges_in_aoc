file = open('day3_test.txt', 'r')
image = file.read()
image = image.split('\n')
max_length = len(image)
numbers_engine = []

column_pointer = 0
pointer_start = -1
pointer_end = -1
pointer = 0


def check_specials_around(im, cc, ps, pe):
    print(ps, pe)
    checker_start = ps
    checker_end = pe
    special_here = False

    if ps != 0:
        checker_start = ps-1
    if pe != len(im[cc])-1:
        checker_end = pe+1

    for i in range(-1, 2):
        print(i)
        if cc == 0:
            continue
        if cc == max_length-1 and i == 1:
            break

        for row in im[cc+i]:
            print('checkers: ', checker_start, checker_end, type(checker_end), type(checker_start))
            for v in row[checker_start:checker_end]:
                if v.isnumeric() or v == '.':
                    continue
                else:
                    special_here = True

    return special_here


while True:
    value = image[column_pointer][pointer]
    print(value, pointer, pointer_start, pointer_end)
    if value.isnumeric():
        if pointer_start == -1:
            pointer_start = pointer
        pointer += 1
        if pointer == len(image[column_pointer]):
            print('what?')
            res = check_specials_around(image, column_pointer, pointer_start, pointer_end)
            if res:
                numbers_engine.append(int(image[column_pointer][pointer_start:pointer_end]))
            pointer = 0
            column_pointer += 1
            pointer_start = -1
            pointer_end = -1
    else:
        if pointer_start != -1 and pointer_end == -1:
            pointer_end = pointer-1
            res = check_specials_around(image, column_pointer, pointer_start, pointer_end)
            if res:
                numbers_engine.append(int(image[column_pointer][pointer_start:pointer_end]))
            pointer_start = -1
            pointer_end = -1
        pointer += 1
        if pointer == len(image[column_pointer]):
            pointer = 0
            column_pointer += 1
