#Matrix Addition

m1  =  [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]

m2  =  [[10, 11, 12],
	[13, 14, 15],
	[16, 17, 18]]

res =  [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

for i in range(len(m1)):
	for j in range(len(m1[0])):
		res[i][j] = m1[i][j] + m2[i][j]

		
for r in res:
	print(r)
