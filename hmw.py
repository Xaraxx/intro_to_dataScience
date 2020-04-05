
name1 = input('Write your name ')
age1 = int(input('Please write your age '))

name2 = input('Write your name ')
age2 = int(input('Please write your age '))

def whos_older(age1, name1, age2, name2):
    if age1 > age2:
        print('{} is older than {}'.format(name1, name2))
    elif age1 < age2:
        print('{} is older than {}'.format(name2, name1))
    else:
        print('{} and {} have the same age.'.format(name2, name1))
        

if __name__ == '__main__':
    whos_older(age1, name1, age2, name2)
    

