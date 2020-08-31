class MaxLimitedSumOfConsPrimes:

    def __init__(self, primes_array):
        self.primes_array = primes_array

    def longest_length_prime_sum(self, n):
        if n < 2:
            raise ValueError("Invalid argument received.")
        consec_length = 0
        largest_primes_sum = 0
        last_index_needed = len(self.primes_array)
        for i in range(len(self.primes_array)):
            for j in range(i + consec_length, last_index_needed):
                result = sum(self.primes_array[i:j])
                if result < n:
                    if result in self.primes_array:
                        consec_length = j-i
                        largest_primes_sum = result
                else:
                    last_index_needed = j+1
                    primes_subarr = self.primes_array[i:j]
                    break
        return largest_primes_sum, primes_subarr

    # #Find the maximal num (not necessarily prime)
    # def longest_length(self, n):
    #     if n < 2:
    #         raise ValueError("Negative argument received.")
    #     limited_primes_array = PrimeService.get_primes_array(n, list())
    #     if self.primes_array:
    #         max_length = 0
    #         curr_sum = 0
    #         for i in range(0, n):
    #             if curr_sum + self.primes_array[i] > n:
    #                 break
    #             curr_sum += self.primes_array[i]
    #             max_length = i
    #         return curr_sum, self.primes_array[0:max_length]
    #     return 0, []