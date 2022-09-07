from tkinter import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import numpy as np

# plot function is created for
# plotting the graph in
# tkinter window
def plot():

	# the figure that will contain the plot
	fig = Figure(figsize = (10, 10),
				dpi = 100)

	# list of squares
	y = [i**3 for i in range(101)]

    
    

    

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y)

    

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,
							master = window)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,
								window)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()

# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("1000x700")

# button that displays the plot
plot_button = Button(master = window,
					command = plot,
					height = 2,
					width = 10,
					text = "Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()

