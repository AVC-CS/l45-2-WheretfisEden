import random


def main():
    total = 0
    numbers = [0]* 100
    index  = 0
    
    while total <= 100:
        num =  random.randint(1,100)
        numbers[index] = num
        total += num
        index += 1
        
    numbers = numbers[:index]
    for i in range(index -1):
        total += numbers[i]
    for n in numbers:
        print (n, end= ' ')
    


    #print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
