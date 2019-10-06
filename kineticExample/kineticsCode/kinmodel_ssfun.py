from oct2py import octave
octave.addpath('/home/asifc/mhgp_model/kineticsCode/')
import numpy as np

data = np.array([
        [[0, 1.000, 0.000],
        [1, 0.504, 0.416],
        [2, 0.186, 0.489],
        [3, 0.218, 0.595],
        [4, 0.022, 0.506],
        [5, 0.102, 0.493],
        [6, 0.058, 0.458],
        [7, 0.064, 0.394],
        [8, 0.000, 0.335],
        [9, 0.082, 0.309]],
        
        [[0, 1.000, 0.000],
        [1, 0.415, 0.518],
        [2, 0.156, 0.613],
        [3, 0.196, 0.644],
        [4, 0.055, 0.444],
        [5, 0.011, 0.435],
        [6, 0.000, 0.323],
        [7, 0.032, 0.390],
        [8, 0.000, 0.149],
        [9, 0.079, 0.222]]            
    ])
	
def ssfun(theta):
   t = np.empty([8])
   t[0:4] = theta[0:4]   
   t[4] = 300.00000
   t[7] = 0.00000
   temps = [283.00000, 313.00000]
   ss = 0.0
   for i in range(2):
      t[5] = temps[i]
      t[6] = theta[4+i]
      ymodel = octave.boxoMpy(data[i], t)
      ydata = data[i][:,1:]
      ssi = np.sum(np.power(ydata - ymodel, 2))
      #print(ssi)
      ss += ssi
   return ss

