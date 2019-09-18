from util import get_data, plot_image
	
X = get_data()
for im in X:
	plot_image(im)
	y = input("Type 'q' to quit: ")
	if y == 'q':
		break
	
