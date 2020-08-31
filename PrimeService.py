class PrimeService:

    @classmethod
    def get_primes_array(cls, max_limit, limited_primes_array):
        # Use Sieve Of Eratosthenes to retrieve all primes within a range (0,max_limit]
        try:
            primes_array = [True for i in range(max_limit + 1)]
            primes_array[0] = False
            primes_array[1] = False
            current_prime = 2
            while pow(current_prime, 2) <= max_limit:
                # If prime[current_prime] is not changed, then it is a prime
                if primes_array[current_prime]:
                    # Update all multiples of current_prime within range(start, end, delta=multiples))
                    for i in range(current_prime * 2, max_limit + 1, current_prime):
                        primes_array[i] = False
                current_prime += 1

            for current_prime in range(max_limit + 1):
                if primes_array[current_prime]:
                    limited_primes_array.append(current_prime)
            return limited_primes_array
        except Exception as err:
            print("Encountered exception: {}".format(err))
            return None
