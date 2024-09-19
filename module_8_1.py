def add_everything_up(a, b):
    try:
        ev_up = a+b
        return ev_up
    except TypeError:
        err = str(a)+str(b)
        return err


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))