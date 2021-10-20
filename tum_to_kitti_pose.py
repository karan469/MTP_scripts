import os
import glob
from evo.core.transformations import quaternion_matrix
import sys

def main(a):
	temp = [float(i) for i in a.split(" ")]
	quat = temp[-4:]
	t = temp[1:4]
	# print('quat: ', quaternion_matrix(temp))
	# print('translation: ', t)
	temp = quaternion_matrix(temp)
	temp[:-1, 3] = t
	# print('R|t: ', temp)
	temp = temp.reshape(1,-1)
	return ' '.join([str(i) for i in temp[0]][:12])

if __name__ == '__main__':
	filename = sys.argv[1]
	outputname = sys.argv[2]
	fd = open(outputname, 'w')
	with open(filename, 'r') as f:
		for line in f:
			out = main(line.strip())
			fd.write(out+'\n')
	fd.close()
