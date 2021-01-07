import matplotlib.pyplot as plt 


x = [1,2,3,4,5,6] 

y = [2,4,1,5,2,6] 


plt.plot(x, y, color='blue', linestyle='dotted', linewidth = 4, 
		marker='X', markerfacecolor='black', markersize=12) 


plt.ylim(1,8) 
plt.xlim(1,8) ## optional


plt.xlabel('x - axis') 

plt.ylabel('y - axis') 


plt.title('Some cool customizations!') 


plt.show()
