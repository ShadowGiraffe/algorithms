import unittest
from decimal import Decimal
from bucket import RateLimiter

class TestGap(unittest.TestCase):

    def test_of_acquire(self):
        RL = RateLimiter(5)
        packets = [Decimal('0.1'), Decimal('0.3'), Decimal('0.5'),
                   Decimal('0.7'), Decimal('0.8'), Decimal('0.9')]
        results = [RL.acquire(each) for each in packets]
        self.assertEqual(
            results, [True, True, True, True, True, False])

if __name__ == '__main__':
    unittest.main()
