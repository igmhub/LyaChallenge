import numpy as np

class MockP1D(object):
  """Class to make mock P1D measurements, given covariance 
  (either dense matrix or diagonal)"""

  def __init__(self,covar):
    self.diagonal = (covar.ndim==1)
    self.covar=covar
    if self.diagonal: self.N=len(covar)
    else: self.N,_=covar.shape

  def mock_fluctuation(self):
    m = np.random.normal(size=self.N)
    if self.diagonal:
      return m * np.sqrt(self.covar)
    else:
      L = np.linalg.cholesky(self.covar)
      return np.dot(L,m)

