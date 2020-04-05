name = input('Please write your name ')

def number_of_characters(name):
    greatings = 'Hello {}, nice to meet you!'.format(name)
    number_of_characters = len(greatings)
    print(number_of_characters)
    return print('The total number of characters in the sentece is {}'.format(number_of_characters))

if __name__ == '__main__':
    number_of_characters(name)
