import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5] 


y = [10, 24, 36, 40, 5] 


xyz = ['one', 'two', 'three', 'four', 'five'] #used to assign name to each bar

 
plt.bar(x, y, tick_label = xyz, 
		width = 0.8, color = ['red', 'green']) 


plt.xlabel('x - axis') 
 
plt.ylabel('y - axis') 

plt.title('bar chart!') 


plt.show()
