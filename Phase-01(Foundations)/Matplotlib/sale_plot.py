import matplotlib.pyplot as plt 

x=['Mon','Tues','Wed','Thur','Fri'] #x-axis
y=[10,15,7.5,20,5]

plt.plot(x,y)

plt.title('Bekery Sales This Week')

plt.xlabel("Day of the Week")
plt.ylabel("sales Per Day")

plt.show()