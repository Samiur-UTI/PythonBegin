while True:
    try:
        ask = int(input('What is your age?'))
        print(10/ask)
    except ValueError:
        print('You must enter a valid age.')
    except ZeroDivisionError:
        print('You must be born to play')
    else:
        print('Thank you')
        break