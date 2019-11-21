import MathFun_Points

def prime_sieve_of_Eratosthenes(list_size=13, print_result=True):
    numbers = [i for i in range(2, list_size + 1)]
    not_prime = set()
    primes = []
    for i in numbers:
        for j in numbers:
            mod = j % i
            if mod == 0 and j != i:
                not_prime.add(j)

    for i in numbers:
        if i not in not_prime:
            primes.append(i)

    if print_result:
        print("list = " + str(numbers))
        print("not prime" + str(not_prime))
        print("prime" + str(primes))
        print("prime_count between 2 to " + str(list_size) + " : " + str(primes.__len__()))
    return primes


def is_prime(any_number, print_result=True):
    if type(any_number) is list or type(any_number) is set:
        list_of_numbers = any_number
        for i in list_of_numbers:
            is_prime(i)

    if type(any_number) is not int:     # type check
        return False
    if any_number is 0:                 # if number is 0
        print("0 is not prime number, only natural numbers greater than 1 can be prime. 0 is not positive nor negative")
        return False
    elif any_number is 1:               # if number is 1
        print("1 is not prime number, \n" +
              "\tprime number by definition greater than 1 and it's positive divisor are one and itself.\n" +
              "\t1 is not greater than 1 and it's divisor are both one and itself")
        return False

    for i in range(2, any_number):
        tmp_cal = any_number % i
        if tmp_cal is 0:
            if print_result:
                print(str(any_number) + " is not prime number. It is dividable by " + str(i))
            return False
    print(str(any_number) + " is prime number")
    return True


def interpolation_between_2_points(a, b, steps, print_result=True):
    import math
    # a and b are points in space and ratio is a point between.
    precision_int = 2
    precision = '.' + str(precision_int) + 'f'

    values = []
    ratio = 1/steps
    for k in range(0, steps+1):
        cal = (((b-a)*(k*ratio))+a)
        cal = float(format(cal, precision))
        values.append(cal)

    if print_result:
        str_len_max = 0

        for v in values:                        # find maximum str length within values[]
            if str(v).__len__() > str_len_max:
                str_len_max = str(v).__len__()

        output_len_max = steps*str_len_max
        output_str = ""
        output_str += str(a)

        for i in range(values.__len__()-2):     # -2 because a and b are printed other way
            for j in range(str_len_max-1):
                output_str += "-"
            output_str += "|"
        for j in range(str_len_max-1):
            output_str += "-"
        output_str += str(b)
        print(output_str)   # print first line
        # - - - - - - - - - - - - - - - - - - - -
        output_str = ""
        for i in range(1, values.__len__()-1):
            for j in range(str_len_max-int(str(values[i]).__len__())):
                output_str += " "
            output_str += str(values[i])

        print(output_str)  # print second line

        print("max_str_len = " + str(output_len_max))
        print("ratio = " + str(ratio))
        print(values)







if __name__ == '__main__':
    # some tests can be done here.
    #prime_list = prime_sieve_of_Eratosthenes(50)
    #is_prime(prime_list)

    interpolation_between_2_points(0, 100, 3)


    ''' test pointer and operator overloads
    import MathFun_Points as P
    p_a = P.Point2D(3, 3)
    p_b = P.Point2D(4, 3)
    p_c = p_a / p_b
    print(p_c)
    '''


