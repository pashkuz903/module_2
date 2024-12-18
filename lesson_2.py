#name = input('Введите Ваше имя: ')
#if name == 'Pavel':
#    print('Здравствуйте, администратор')
#if name == 'Liza':
#    print('Здравствуйте, королева')
#else:
#    print('Привет,', name)
number = int(input('Введите число: ')) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Xi-Xi')
