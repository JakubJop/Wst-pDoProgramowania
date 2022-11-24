
def maximum(a1, *args):
    m = a1
    for a in args:
        if m < a:
            m = a
    return a

maks = maximum2( 1, 3, 4, 10, 5)
print(maks)

maks = maximum2(3)
print(maks)
