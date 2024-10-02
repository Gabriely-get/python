#scope doesnt change var value

x = "Theirs"

def not_changeable_value():
    x = "Mine"
    print(f'Variable x is {x}')

not_changeable_value()
print(f'Variable x is {x}\n')


#global does
    #global y -> here does not works okay?

def changeable_value():
    global y
    y = "Now you see me"

changeable_value()
print(y)

z = "Z"

def changeable_too():
    global z
    z = 'Now you see me too'

changeable_too()
print(z)
