import matplotlib.pyplot as plt 


ages = [2,5,70,40,32,20,19,30,45,50,45,43,40,44,88,87,79, 
		60,60,50,53,51,7,13,57,18,90,77,32,21,20,40,98,99,91] 


range = (0, 100) 
bins = 10


plt.hist(ages, bins, range, color = 'red', 
		histtype = 'bar', rwidth = 0.8) 

 
plt.xlabel('age') 

plt.ylabel('No. of people') 

plt.title('My histogram') 


plt.show()
