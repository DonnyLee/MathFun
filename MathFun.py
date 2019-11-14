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


def linear_interpolation_1D(a, b, ratio, print_result=True):
    # a and b are points in space and ratio is a point between.
    cal = ((b-a)+a)*ratio
    if print_result:
        print_width = 10           # change this value to scales output string, recommended value 10 and 100
        a_len = str(a).__len__()
        r_cnt = int(print_width*ratio)
        output = str(a)
        for i in range(r_cnt-1):
            output = output+"-"
        output = output+"|"
        for i in range(print_width-r_cnt-1):
            output = output + "-"
        output = output + str(b) + "\n"

        for i in range(int(((a_len/2)+r_cnt-1))):
            output = output + " "
        output = output + str(cal)

        print(output)
        return cal
    else:
        return cal


def linear_interpolation_2D_plane(para_point_a, para_point_b, para_point_c, para_point_d, ratio_x, ratio_y, print_result=True):
    # a,b,c,d builds a shape.
    #     c----------d
    #     |          |
    #     |          |
    #     |          |
    #     a----------b
    # ratio_x and ratio_y determine a relative position in this geometry.

    # initialisation
    import MathFun_Points as Points
    if type(para_point_a) is list:
        point_a = Points.Point2D(para_point_a[0], para_point_a[1])
    else:
        point_a = para_point_a
    if type(para_point_b) is list:
        point_b = Points.Point2D(para_point_b[0], para_point_b[1])
    else:
        point_b = para_point_b
    if type(para_point_c) is list:
        point_c = Points.Point2D(para_point_c[0], para_point_c[1])
    else:
        point_c = para_point_c
    if type(para_point_d) is list:
        point_d = Points.Point2D(para_point_d[0], para_point_d[1])
    else:
        point_d = para_point_d
    print(point_a)
    print(point_b)
    print(point_c)
    print(point_d)





    '''
    if print_result:
        print_width = 10           # change this value to scales output string, recommended value 10 and 100
        a_len = str(a).__len__()
        r_cnt = int(print_width*ratio)
        output = str(a)
        for i in range(r_cnt-1):
            output = output+"-"
        output = output+"|"
        for i in range(print_width-r_cnt-1):
            output = output + "-"
        output = output + str(b) + "\n"

        for i in range(int(((a_len/2)+r_cnt-1))):
            output = output + " "
        output = output + str(cal)

        print(output)
        return cal
    else:
        return cal
    '''



if __name__ == '__main__':
    # some tests can be done here.
    #prime_list = prime_sieve_of_Eratosthenes(50)
    #is_prime(prime_list)
    #linear_interpolation_1D(221, 333, 0.0)
    #linear_interpolation_1D(221, 333, 0.25)
    #linear_interpolation_1D(221, 333, 0.50)
    #linear_interpolation_1D(221, 333, 0.75)
    #linear_interpolation_1D(221, 333, 1.0)
    linear_interpolation_2D_plane([0,0], [0,1], [1,0], [1,1], 0.9, 0.8)


