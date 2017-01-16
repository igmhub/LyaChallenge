import matplotlib.pyplot as plt
import numpy as np
import read_PD2013 as pd13
import theory_PD2013 as t13
import MockP1D as mP1D

# for testing
# np.random.seed(42)

dir_PD2013='../ResultsP1D/PD2013/PublishedFiles/'
data_PD2013 = pd13.PD2013(dir_PD2013)

z=3.2
k,P,eP = data_PD2013.get_power(z)

theory_PD2013 = t13.TheoryPD2013()
t = theory_PD2013.Power_kms(z,k)

C = data_PD2013.get_covariance(z)

diag=True
if diag:
  mock = mP1D.MockP1D(np.diagonal(C))
  m = mock.mock_fluctuation()
else:
  mock = mP1D.MockP1D(C)
  m = mock.mock_fluctuation()

plt.semilogy(k,k*(t+m)/3.1416,'o')
plt.errorbar(k,k*(t+m)/3.1416,yerr=2*k*eP/3.1416,fmt='ko')
plt.semilogy(k,k*t/3.1416,':')

plt.xlim(0.001,0.02)
plt.xlabel(r'k [s $\rm{km}^{-1}$]')
plt.ylabel(r'k P(k) / $\pi$')
plt.savefig('Pk_data.png')
plt.show()
exit()

