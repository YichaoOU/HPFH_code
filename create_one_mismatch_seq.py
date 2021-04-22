
import sys
seq = sys.argv[1]
out = open("%s.mis.fa"%(seq),"wb")
from copy import deepcopy as dp
for i in range(len(seq)):
	x = dp(seq)
	for j in ['A','C','G','T']:
		if j == seq[i]:
			continue
		x = seq[:(i)]+j+seq[(i+1):]
		print >>out,">%s\n%s"%(x,x)

