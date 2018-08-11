from matplotlib import pyplot, style

style.use('fivethirtyeight')

x = [5,6,7,8]
y = [7,3,8,3]

pyplot.plot(x,y)

#pyplot.grid(True)


pyplot.title('Epic Chart')
pyplot.ylabel('Y axis..')
pyplot.xlabel('X axis..')


pyplot.show()
