def ad(x):
    last = 0
    for j in x:
        last = j + last
    return last


def sub(x):
    last = 0
    for j in x:
        last = j - last
    return last

def mul(x):
    last = 1
    for j in x:
        last = j*last
    return last

def divi(x):
    last = 1
    for j in x:
        last = last/j
    return last

def mod(x):
    last = 1
    for j in x:
        last = last%j
    return last

def flo(x):
    last = 1
    for j in x:
        last = last//j
    return last

def pali(x):
    for i in x:
        if str(i)[::-1] == str(i):
            print(f'{i} is a palidrome no.')

def arm(x):
    for i in x:
        m = i
        sum = 0
        num_of_digits = len(str(i))
        while m > 0:
            digit = m % 10
            sum += digit ** num_of_digits
            m = m// 10
        if i == sum:
            print(i, "is an Armstrong number.")
        else:
            print(i, "is not an Armstrong number.")

def rev(x):
    for i in x:
        print(f'Reverse:{str(i)[::-1]}')

def prime(x):
    for num in x:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    break
                else:
                    print(num,"is a prime number")
                    break
        else:
            print(num,"is not a prime number")
        



def choice():
    print('''  
1.Add
2.Subtract
3.multiply
4.divided
5.modulus
6.floor
7.Palidrome
8.armstrong
9.reverse
10.Prime number
11.Exit
''')
    choice = int(input('Enter your Choice:'))
    num = int(input('Enter number of elements:'))
    lst = []
    for i in range(num):
        num1 = int(input('Enter the Elements:'))
        lst.append(num1)

    if choice==1:
        print('addition:',ad(lst))
        choice()


    elif choice==2:
        print('subtraction:',sub(lst))
        choice()


    elif choice==3:
        print('multiply:',mul(lst))
        choice()


    elif choice==4:
        print('division:',divi(lst))
        choice()

    elif choice==5:
        print('modulus:',mod(lst))
        choice()


    elif choice==6:
        print('floor:',flo(lst))
        choice()

    elif choice ==7:
        print(pali(lst))
        choice()

    elif choice ==8:
        arm(lst)

    elif choice==9:
        rev(lst)

    elif choice==10:
        prime(lst)


    elif choice ==11:
        exit()

    else:
        print('Please enter valid command')
        choice()
choice()







