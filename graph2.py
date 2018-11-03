import matplotlib.pyplot as plt 
#cordinates of left sides of the bar
left=[1,2,3,4,5]
#heights of bar
height=[10,25,35,40]
#label for bars
tick_label=['one','two','three','four','five']
#ploting a bar chart
plt.bar(left, height, tick_label=tick_label,
		width=0.8, color=['red','green'])
#naming the x axis
pit.xlabel('x-axis')
#naming the y axis
plt.ylabel('y-axis')
#plot title
plt.title('my first bar graph')
#function to show the plot
plt.show()