import unittest
import StandardDeviation

class TestStandardDeviation(unittest.TestCase):
  def testSampleStandardDeviationClass(self):
    sample = [43, 35, 38, 56, 29, 33, 46, 63, 49, 40]
    sd = StandardDeviation.StandardDeviation(sample, False)
    self.assertEqual(sd.getMean(), 43.2)
    self.assertEqual(sd.getVariation(), 111.96)
    self.assertEqual(sd.getStandardDeviation(), 10.58)

if __name__ == '__main__':
    unittest.main()