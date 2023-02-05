class StandardDeviation: 
  ROUND_DECIMALS = 2
  
  sample = []
  isPopulation = False
  isVerbose = False
  
  def __init__(self, sample, isPopulation = False, isVerbose = False) -> None:
    self.sample = sample
    self.isPopulation = isPopulation
    self.isVerbose = isVerbose
    self._setMean()
    self._setVariance()
    self._setStandardDeviation()
  
  def getMean(self):
    return self.mean
  
  def getStandardDeviation(self):
    return self.standarDeviation
  
  def getVariation(self):
    return self.variation

  def _setVariance(self):
    """ 
      return the unbiased sample deviation for a given sample with which the class
      was initialized
        Variance is the measure of how far the data is spread from the mean
    """
    
    sampleSize = len(self.sample) if self.isPopulation else len(self.sample) - 1
            
    squared_deviations = 0
    
    for s in self.sample:
      squared_deviations += (s - self.getMean())**2
      if self.isVerbose:
        print("squared_deviations - ", (s - self.getMean())**2)
    
    self.variation = round((squared_deviations / sampleSize), self.ROUND_DECIMALS)
    
    if self.isVerbose:
      print("Variation: %f" % (self.variation))

  def _setStandardDeviation(self):
    self.standarDeviation = round(self.variation**0.5, self.ROUND_DECIMALS) # square root the unbiased deviation
    
    if self.isVerbose:
      standardDeviationType = "Population" if self.isPopulation else "Sample"
      print("Standard %s Deviation: %f" % (standardDeviationType, self.standarDeviation))
      
  
  def _setMean(self):
    self.mean = sum(self.sample) / len(self.sample)
    
    if self.isVerbose:
      print("Mean ", self.mean)
