def prime_sieve_of_Eratosthenes(self, list_size=13, print_result=True):
    numbers = [i for i in range(2, list_size + 1)]
    not_prime = set()
    prime = []
    for i in numbers:
        for j in numbers:
            mod = j % i
            if mod == 0 and j != i:
                not_prime.add(j)

    for i in numbers:
        if i not in not_prime:
            prime.append(i)

    if print_result:
        print("list = " + str(numbers))
        print("not prime" + str(not_prime))
        print("prime" + str(prime))
        print("prime_count between 2 to " + str(list_size) + " : " + str(prime.__len__()))
    return prime


if __name__ == '__main__':
    prime_sieve_of_Eratosthenes(50)