import random


def main():
    total = 0
    numbers = [0]* 100
    index  = 0
    sum = 0
    
    while sum <= 100:
        num =  random.randint(1,10)
        numbers[index] = num
        sum += num
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
