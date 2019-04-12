# Module with functions for extracting special numbers.

def get_naturals(init_list, sort=False):
    '''
        Returns list with natural numbers. 
        If sorted list needed: get_naturals(list, sort=True).
    '''
        
    naturals = []
    for num in init_list:
        try:
            natural = int(num)
            if natural > 1: naturals.append(natural)
        except: pass
    
    if sort: naturals.sort()

    return naturals

def get_primes(upper_range):
    '''
        Returns list with prime numbers based on given range, using sieve Erastothenes 
        algorithm.
    '''

    num_list = list(range(2, upper_range))
    i = 0

    while i < len(num_list):
        for prime in num_list:
            # Not prime. Delete from list.
            if num_list[i] % prime == 0 and num_list[i] is not prime:
                del num_list[i]
                break
            # Is prime.    
            elif num_list[i] == prime: 
                i += 1
                break

    return num_list

def is_prime(num):
    '''Returns True if number is a prime number, else False.'''

    for number in range(2,num):
        if num % number == 0: return False
    return True

def _test():
    # naturals_test = ['abc', '2', 7, 39, 40.5, -5, '-3', list(range(10)), 0, 's', '4']
    # print(get_naturals(naturals_test,sort=True))
    
    # print(get_primes(10000))
    
    # print(is_prime(1006533))
    
    pass

if __name__ == "__main__":
    _test()