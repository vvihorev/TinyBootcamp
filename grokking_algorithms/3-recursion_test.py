def inner(known):
    print("Inner started")
    print(known)
    print("Inner is done")


def outer(known, unknown):
    print("Outer started")
    print(known, unknown)
    inner(known)
    print("Outer is done")


outer(1, 2)
