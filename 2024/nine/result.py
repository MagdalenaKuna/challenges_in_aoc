
file = open('showed_input.txt')

def use_comprehension_with_zip(a):
    b, c = zip([(x, y) for n, x in a if n%2 else y])
    return (list(b),list(c))

blocks, free_spaces = use_comprehension_with_zip(file.read())
print(blocks)
print(free_spaces)