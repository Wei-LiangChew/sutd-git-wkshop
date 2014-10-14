import csv
import sys
import copy
def parse():

	daydict = {}
	resultdict = {}

	with open('./data/Monday.csv') as file:

		resultdict['Monday'] = copy.deepcopy(processday(file))

	with open('./data/Tuesday.csv') as file:

		resultdict['Tuesday'] = copy.deepcopy(processday(file))

	with open('./data/Wednesday.csv') as file:

		resultdict['Wednesday'] = copy.deepcopy(processday(file))


	with open('./data/Thursday.csv') as file:

		resultdict['Thursday'] = copy.deepcopy(processday(file))


	with open('./data/Friday.csv') as file:

		resultdict['Friday'] = copy.deepcopy(processday(file))

	return resultdict
			

def processday(file):
	daydict = {}
	reader = csv.reader(file, delimiter=',')

	classrooms = reader.next();
	for room in range(1,len(classrooms)):
		daydict[classrooms[room]] = {}
	for row in reader:
		for i in range(len(row)):
			if row[i] == '0':
				daydict[classrooms[i]][row[0]] = False
			elif row[i] == '1':
				daydict[classrooms[i]][row[0]] = True

	return daydict



def getRoomList():
	with open('./data/Monday.csv') as file:
		reader = csv.reader(file, delimiter=',')
		classrooms = reader.next();
		return classrooms[1:-1]
