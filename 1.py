max = 0
min = 1000

def inputoutput():
    max = input('Enter a number : ')
    min = input('Enter another number : ')

def selection():
    if max>min:
        print('max is {0} , min is {1} '.format(max,min))
    else:
        max,min=min,max
        print('max is {0} , min is {1} '.format(max, min))

inputoutput()
selection()


