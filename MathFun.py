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
    if type(any_number) is list:
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


if __name__ == '__main__':
    prime_list = prime_sieve_of_Eratosthenes(50)
    is_prime(prime_list)



