from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import numpy

def onclick(event):
	plt.plot([event.xdata], [event.ydata], marker='x', markersize=3, color='black')
	fig.canvas.draw()
	data.append([event.xdata, event.ydata])

if __name__ == '__main__':
	#Picked points:
	data = []
	fig, ax = plt.subplots()
	#If you do not set axes limits, draw will put auto set and jump around.
	#Set any x/y lim for consistency:
	ax.set_xlim(0,10)
	ax.set_ylim(0,10)
	fig.canvas.mpl_connect('button_press_event', onclick)
	print('Click some points and close the window.')
	
	plt.show()
	#plot closed...
	for C in range(2,10):
		X = numpy.array(data)
		model = KMeans(n_clusters=C, random_state=0)#, verbose=True)
		model.fit(X)
		#print(model.labels_) #Different number for each "cluster" found.
		centroids = model.cluster_centers_
		#Separate xs [:, 0], ys [:,1] and scatter plot:
		plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=170, zorder=10, c='m')
		
		#print(centroids.size)
		plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
		# %d is int, %f is for float:
		print('For %d clusters the average silhouette score is %f' % (C, silhouette_score(X, model.labels_)))
		plt.show()
		
