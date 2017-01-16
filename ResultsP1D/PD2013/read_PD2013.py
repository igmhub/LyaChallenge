import pylab
import numpy as np

class PD2013(object):
  """Class to read P1D results from Palanque-Delabrouille et al. (2013).
  Wavenumbers and power in units of km/s."""
  def __init__(self,basedir='PublishedFiles',use_FFT=False):
    """If use_FFT=True, use FFT results instead of Likelihood results."""
    self.basedir=basedir
    self.use_FFT=use_FFT
    self.Nz=12
    if self.use_FFT:
      self.Nk=35
    else:
      self.Nk=32
    self._read_power()
    # by default, do not read covariance matrices
    self.covar=[]

  def _read_power(self):
    if self.use_FFT:
      fname=self.basedir+'table4a.dat'
    else:
      fname=self.basedir+'table5a.dat'
    i,j,z,k,P,P_stat,P_noise,P_metal,P_syst=pylab.loadtxt(fname,unpack=True)
    self.all_z=z
    self.all_k=k
    self.all_P=P
    self.all_errP=P_stat
  
  def _read_covariance(self,iz):    
    if self.use_FFT:
      fname=self.basedir+'cct4b'+str(iz+1)+'.dat'
    else:
      fname=self.basedir+'cct5b'+str(iz+1)+'.dat'
    # files contain correlation matrix
    corr=pylab.loadtxt(fname)
    # rescale with statistical error
    z=self.get_zs()[iz]
    _,_,errP = self.get_power(z)
    C = np.multiply(np.transpose(np.multiply(corr,errP)),errP)
    return C
  
  def _read_covariances(self):
    for iz in range(self.Nz):
      C = self._read_covariance(iz)
      self.covar.append(C)

  def get_zs(self):
    return np.unique(self.all_z)

  def get_power(self,z):
    filter=(self.all_z==z)
    return self.all_k[filter],self.all_P[filter],self.all_errP[filter]

  def get_covariance(self,z):
    if not self.covar:
      self._read_covariances()
    zs=self.get_zs()
    if z in zs:
      zbin=np.where(zs==z)[0][0]
      return self.covar[zbin]
    else:
      print z,"not in zs",zs

