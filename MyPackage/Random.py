import os
import time


class Random:
    """
    A simple random number generator class based on the linear congruential generator algorithm.

    Attributes:
        weight (int): Multiplier for the random number generation formula.
        bias (int): Additive constant for the random number generation formula.
        m (int): Modulus for the random number generation formula.
        x1 (int): Current random number.
    """
    
    def __init__(self, weight=65432, bias=0, m=2 ** 31 - 1, seed=None):
        """
        Initialize the random number generator.

        Parameters:
            weight (int): Multiplier for the random number generation formula. Default is 65432.
            bias (int): Additive constant for the random number generation formula. Default is 0.
            m (int): Modulus for the random number generation formula. Default is 2^31-1.
            seed (int): Seed value for initializing the random number generator. If None, a default seed is used.
        """
        self.weight = weight
        self.bias = bias
        self.m = m
        if seed is None:
            self.x0 = time.time() + 30000 * os.getpid() + 12345678
        else:
            self.x0 = seed
        
        self.x1 = (self.weight * self.x0 + self.bias) % self.m
    
    def randomInt(self, num_range=None) -> int:
        """
        Generate a random integer within a specified range or from 0 to m - 1.

        Parameters:
            num_range (tuple or list or range): Optional parameter specifying the range [a, b] for the random number generation.

        Returns:
            int: Random integer within the specified range.
        """
        self.x1 = (self.weight * self.x1 + self.bias) % self.m
        
        if num_range is None:
            return self.x1
        else:
            scalar = self.x1 / (self.m - 1)  # create a number in the range [0, 1)
            return int(scalar * (num_range[-1] - num_range[0]) + num_range[0])
    
    def random(self, num_range=None) -> float:
        """
        Generate a random float within a specified range or from 0 to 1.

        Parameters:
            num_range (tuple or list or range): Optional parameter specifying the range [a, b] for the random number generation.

        Returns:
            float: Random float within the specified range.
        """
        self.x1 = (self.weight * self.x1 + self.bias) % self.m
        
        if num_range is None:
            return self.x1
        else:
            scalar = self.x1 / (self.m - 1)  # create a number in the range [0, 1)
            return scalar * (num_range[-1] - num_range[0]) + num_range[0]


if __name__ == '__main__':
    def testRandomInt():
        """
        Test function to generate random integers and display their frequencies.
        """
        random_generator = Random()
        
        ls = []
        for i in range(0, 100001):
            ls.append(random_generator.randomInt([1, 101]))
        
        ref = [n for n in range(1, 101)]
        element_counts = {num: ls.count(num) for num in ref}
        
        ls_len = len(ls)
        for num, count in element_counts.items():
            print(f"Frequent of {num:>3}: {count:>6} || Probability of it: {100 * count / ls_len:>10.6f}%")
    
    
    def testRandom():
        """
        Test function to generate random floats until a value between 1 and 2 is obtained.
        """
        random_generator = Random()
        count = 0
        num = 0
        while not (1 < num < 2):
            count += 1
            num = random_generator.random([1, 101])
            print(num)
        
        print(f'---\n{count} iterations to finish')
    
    
    testRandomInt()
    # testRandom()
