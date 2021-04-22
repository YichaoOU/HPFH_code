import pandas as pd
import numpy as np
df = pd.read_csv("one_mis.fimo",sep="\t")
df = df.sort_values("p-value")
df['name'] = df['#pattern name']+df['sequence name']
df = df.drop_duplicates('name')
df.shape
df.head()
df['-logP'] = [-np.log10(x) for x in df['p-value']]
df.head()
def check_diff_pos(s,x):
	for i in range(len(s)):
		if x[i] != s[i]:
			return i+1
ref="TGACCAATAGCC"
df['variant_pos']=[check_diff_pos(ref,x) for x in df['sequence name']]
df.head()
df = df.sort_values(['#pattern name','variant_pos','sequence name'])
df2 = df[['#pattern name','variant_pos','sequence name','p-value','-logP']]
df2.head()
df2.to_csv('WT_distal.all_one_mismatch.score.tsv',sep="\t",index=False)
