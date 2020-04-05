num1 = [x for x in range(0,100)]

num2 = [x for x in range(0,10)]

result = []

def multiplication():
    i = 0
    j = 0
    while i < 101:
        while j < 11:
            j += 1
            print(j)

        i += 1
        
        result = i * j
        print(result, i, j)
        return result

    # for i in range(0,101):
    #     for j in range(0,11):
    #         j += 1
    #     i += 1
    #     result =  i * j
    #         # print(result)

    # return result
            


def integer_division(num1, num2):
    remainder = num1 % num2

    if remainder == 0:
        return True
    else:
        print(remainder)
        return False


def prime_number(num):
    if divisors == [1, num]:
        pass
    else:
        print('The number {} isn\'t prime'.format(num))

if __name__=='__main__':
    multiplication()
    print(result)