class StandardDeviation: 
  ROUND_DECIMALS = 2
  
  sample = []
  
  def __init__(self, sample) -> None:
    self.sample = sample

  def getUnbiasedSampleDeviation(self):
    """ return the unbiased sample deviation for a given sample with which the class
      was initialized
        Variance is the measure of how far the data is spread from the mean

    Returns:
        _type_: float
    """
    mean = self.getMean()
        
    squared_deviations = 0
    
    for s in self.sample:
      squared_deviations += (s - mean)**2
      print("deviation {}", (s - mean)**2)
      
    print("squared_deviations {}", squared_deviations / 9)
      
    return round((squared_deviations / (len(self.sample) - 1)), self.ROUND_DECIMALS)
      
    
  def getMean(self):
    return sum(self.sample) / len(self.sample)
