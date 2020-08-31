# pip: 20.2.2
# python: 3.8.3
# pytest 6.0.1

import pytest
from MaxLimitedSumOfConsPrimes import MaxLimitedSumOfConsPrimes
from PrimeService import PrimeService


@pytest.fixture()
def instance():
    yield MaxLimitedSumOfConsPrimes(None)


class TestClass:

    def test_positive_given_limit_return_highest_prime_num_and_primes_cons_seq(self, instance):
        limit = 100
        instance.primes_array = PrimeService.get_primes_array(limit, list())
        maxSum, primesArray = instance.longest_length_prime_sum(limit)
        assert type(maxSum) is int
        assert maxSum == 41
        assert all([actualPrime == expectedPrime
                    for actualPrime, expectedPrime in zip(primesArray, [2, 3, 5, 7, 11, 13, 17, 19, 23])])
        print("\nPrimes sequence: {}".format(primesArray))
        print("Maximal number, lower than {} with longest consecutive primes sequence is: {}".format(limit, maxSum))

    def test_negative_given_illegal_limit_expect_value_error(self, instance):
        limit = 1
        with pytest.raises(ValueError):
            instance.primes_array = PrimeService.get_primes_array(limit, list())
            instance.longest_length_prime_sum(limit)
