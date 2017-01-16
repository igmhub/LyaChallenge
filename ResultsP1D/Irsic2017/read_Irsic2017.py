import pylab
import numpy as np

class Irsic2017(object):
  """Class to read P1D results from Irsic et al. (2017).
  Wavenumbers and power in units of km/s."""
  def __init__(self,basedir='PublishedFiles'):
    self.Nz=7
    self.Nk=19
    self.basedir=basedir
    self._read_power()

  def _read_power(self):
    self.fname=self.basedir+'Pk_XQ100_Irsic.txt'
    z,k,P,P_stat,_=pylab.loadtxt(self.fname,unpack=True)
    self.all_z=z
    self.all_k=k
    self.all_P=P
    self.all_errP=P_stat

  def get_power(self,z):
    filter=(self.all_z==z)
    return self.all_k[filter],self.all_P[filter],self.all_errP[filter]

  def get_zs(self):
    return np.unique(self.all_z)
