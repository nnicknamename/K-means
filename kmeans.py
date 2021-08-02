#!/usr/bin/python
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import random
import math
import point
import csv
data_points=[]

def load_data(n,dimentions):
	for i in range(n):
		coordinates=[]
		for j in range(dimentions):
			coordinates.append(random.rand()*100)
		data_points.append(point.point(coordinates))

def load_data_csv(file,colls):
	with open(file,'r')as read:
		reader=csv.DictReader(read)
		list_dict=list(reader)
		for i in range(len(list_dict)):
			coordinates=[]
			for j in range(len(colls)):
				coordinates.append(float(list_dict[i][colls[j]]))
			data_points.append(point.point(coordinates))


def generate_centers(k,points):
	centers=[]
	for i in range(k):
		coordinates=[]
		index=random.random_integers(points[0].dimentions()+1)
		for j in range(points[index].dimentions()):
			coordinates.append(points[index].get_dimention(j))
		centers.append(point.point(coordinates))
	return centers

def closest_center(centers,p):
	min_distance=p.distance(centers[0])
	index=0
	#for each center
	for i in range(1,len(centers)):
		distance=p.distance(centers[i])
		if(distance<min_distance):
			min_distance=distance
			index=i
	return index

def group_middle_point(points,grouping,group):
	dimentions=[]
	points_in_group=0
	for i in range(points[0].dimentions()):
		dimentions.append(0)

	for i in range(len(points)):
		if(grouping[i]==group):
			points_in_group+=1
			for j in range(points[i].dimentions()):
				dimentions[j]+=points[i].get_dimention(j)
	if(points_in_group!=0):
		for i in range(points[0].dimentions()):
			dimentions[i]=dimentions[i]/points_in_group
	return point.point(dimentions)

def recalculate_centers(centers,grouping,points):
	for i in range(len(centers)):
		centers[i]=group_middle_point(points,grouping,i)
					
def reformat(data_p,dimentions):
	data=[]
	for j in range(dimentions):
		data.append([])
		for i in range(len(data_p)):
			data[j].append(data_p[i].get_dimention(j))
	return data

def grouping_to_color_3D(grouping):
	colors=[[175/255,0,105/255],[9/255,1/255,95/255],[85/255,179/255,177/255],[246/255,192/255,101/255]]
	color=[]
	for i in range(len(grouping)):
		color.append(colors[grouping[i]])
	return color 

def grouping_to_color_2D(grouping):
	color=[]
	for i in range(len(grouping)):
		color.append("C"+str(grouping[i]+1))
	return color 

def compare(arr1, arr2):
	for i in range(len(arr1)):
		if(arr1[i]!=arr2[i]):
			return False
	return True

def k_means(k,points ,centers=None,grouping=None):
	if(centers==None):
		centers=generate_centers(k,points)
	if(grouping==None):
		grouping=[]
	#for each point
	for i in range(0,len(points)):
		grouping.append(closest_center(centers,points[i]))
	recalculate_centers(centers,grouping,points)
	return [grouping,centers]

def plot_2D(result,data):
	grouping=result[0]
	centers=result[1]
	plt.scatter(data[0],data[1],color=grouping_to_color_2D(grouping))
	data=reformat(centers,2)
	colors=[]
	for i in range(len(data[0])):
		colors.append("C"+str(i+1))
	plt.scatter(data[0],data[1],marker='^',color=colors)
	plt.show()

def plot_3D(result,data):
	grouping=result[0]
	centers=result[1]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	color=grouping_to_color_3D(grouping)
	for i in range(len(data[0])):
		ax.scatter(data[0][i],data[1][i],data[2][i],c=color[i],depthshade=True)
	data=reformat(centers,3)
	for i in range(len(data[0])):	
		colors=[[175/255,0,105/255],[9/255,1/255,95/255],[85/255,179/255,177/255],[246/255,192/255,101/255]]
		ax.scatter(data[0][i],data[1][i],data[2][i],marker='X',c=colors[i],depthshade=True)
	plt.show()

file="cars.csv"

#load_data(80,2)
load_data_csv(file,['drat','disp','hp'])
result=k_means(3,data_points)
cpt=0
while(cpt<100):
	cpt+=1
	result=k_means(3,data_points,result[1],result[0])

data=reformat(data_points,3)
plot_3D(result,data)