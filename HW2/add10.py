# credit to jaredjxyz

import arff
import random

attribute = 'preg'
filename = 'diabetes.arff'

def main():
	partg()
	parth()

def partg():
	data = arff.load(open(filename))

	# find the attribute index
	for attribute_index in range(len(data['attributes'])):
		if data['attributes'][attribute_index][0] == attribute:
			break

	if attribute_index == len(data['attributes']):
		print("The given attribute name does not exist.")
		exit(1)

	attribute_type = data['attributes'][attribute_index][1]

	# Add attribute 10 times
	for i in range(10):
		# Add a new attribute
		data['attributes'].insert(0, (attribute + str(i), attribute_type))

		# Append a copy to each piece of data
		for j in range(len(data['data'])):
			data['data'][j].insert(0, data['data'][j][attribute_index])

	# Write a new file
	p4g_file = open('partg-' + filename, 'w')
	p4g_file.write(arff.dumps(data))

def parth():
	data = arff.load(open(filename))

	for i in range(20):
		data['attributes'].insert(0, ('RANDOM' + str(i), 'NUMERIC'))
		for j in range(len(data['data'])):
			data['data'][j].insert(0, random.random())

	p4h_file = open('parth-' + filename, 'w')
	p4h_file.write(arff.dumps(data))



if __name__ == '__main__':
	main()