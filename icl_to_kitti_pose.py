import os
import glob
# from evo.core.transformations import quaternion_matrix
import sys

if __name__ == '__main__':
	filename = sys.argv[1]
	outputname = sys.argv[2]
	fd = open(outputname, 'w')
	res = []
	with open(filename, 'r') as f:
		cnt = 0
		temp_res = []
		for line in f:
			temp_res += [float(i) for i in line.strip().split(" ")]
			cnt = (cnt+1)%4
			if(cnt==0):
				res.append(temp_res)
				temp_res = []
	for i in res:
		fd.write(' '.join([str(x) for x in i][:12])+'\n')
	fd.close()
