import matplotlib.pyplot as plt
import pylab
import decimal
import read_Irsic2017 as i17
import read_PD2013 as pd13

def onedec(x) :
  if x<1 : return "{:.2g}".format(x)
  if x<10 : return "{:.2g}".format(decimal.Decimal(x))
  return int(x)

dir_I2017='../ResultsP1D/Irsic2017/PublishedFiles/'
data_I2017 = i17.Irsic2017(dir_I2017)
dir_PD2013='../ResultsP1D/PD2013/PublishedFiles/'
data_PD2013 = pd13.PD2013(dir_PD2013)

zs = data_I2017.get_zs()
#zs = data_PD2013.get_zs()
Nz=len(zs)
for iz in range(Nz):
  z=zs[iz]
  col=pylab.cm.gist_rainbow(iz/float(Nz))
  k,P,eP=data_I2017.get_power(z)
  plt.semilogy(k,k*P/3.1416,'-',label='z='+onedec(z),color=col)
  plt.semilogy(k,k*P/3.1416,'o',color=col)
  plt.errorbar(k,k*P/3.1416,yerr=k*eP/3.1416,fmt='ko',color=col)
  k,P,eP=data_PD2013.get_power(z)
  plt.semilogy(k,k*P/3.1416,'-',color=col)
  plt.semilogy(k,k*P/3.1416,'o',color=col)
  plt.errorbar(k,k*P/3.1416,yerr=k*eP/3.1416,fmt='ko',color=col)

plt.legend()
plt.xlim(0.001,0.03)
plt.xlabel('k [s/km]')
plt.ylabel('k P(k) / PI')
plt.savefig('Pk_data.png')
plt.show()
exit()

