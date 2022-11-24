
def maximum(, *args):
    if len(args) == 0:
        return None
    m = args[0]
    for a in args[1:]:
        if m < a:
            m = a
    return a

maks = maximum( 1, 3, 4, 10, 5)
print(maks)

maks = maximum ()
print(maks)
