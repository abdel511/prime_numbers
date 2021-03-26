
    number = int(input("\nGive a number to check out : "))
    for i in range(2,(number // 2)+1 ):
        if number % i == 0 :
            j = number / i
            print( "\n" + str(number) + " = " + str(i) + " * " + str(j) )
            break
    else :
        print( "\n" + str(number) + " is a prime number! ")
