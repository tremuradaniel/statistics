class StandardDeviation: 
  ROUND_DECIMALS = 2

  def getUnbiasedSampleDeviation(self, sample):
    """ return the unbiased sample deviation for a given sample
        Variance is the measure of how far the data is spread from the mean
    Args:
        sample (list): sample records

    Returns:
        _type_: float
    """
    mean = self._getMean(sample)
        
    squared_deviations = 0
    
    for s in sample:
      squared_deviations += (s - mean)**2
      print("deviation {}", (s - mean)**2)
      
    print("squared_deviations {}", squared_deviations / 9)
      
    return round((squared_deviations / (len(sample) - 1)), self.ROUND_DECIMALS)
      
    
  def _getMean(self, sample):
    return sum(sample) / len(sample)
