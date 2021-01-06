def exp(base, sup):
    result = 1
    for index in range(sup):
        result = result * base
    print("The answer is " + str(result))

exp(10,4)