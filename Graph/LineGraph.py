import matplotlib.pyplot as plt 
import numpy as np # numpy is used to handle array

 
x = np.arange(0, 2*(np.pi), 0.1) 

y = np.sin(x) 


plt.plot(x, y) 


plt.show()
