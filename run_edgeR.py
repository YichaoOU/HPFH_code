import pandas as pd
import glob
import os

file = pd.read_csv("input.tsv",sep="\t",header=None)
design = pd.read_csv("GATAmotif_mutation_diffPeak_matrix.tsv",sep="\t",header=None)


df = pd.read_csv("scores_per_bed.tsv",sep="\t")
df.columns = [x.replace("'","") for x in df.columns]


for t,c,n in design.values:
	print (t,c,n)
	t_group = file[file[1]==t][0].tolist()
	c_group = file[file[1]==c][0].tolist()
	input = "%s.input.tsv"%(n)
	tmp = df[t_group+c_group]
	for c in tmp.columns:
		tmp[c] = tmp[c].astype(int)
	tmp.to_csv(input,sep="\t")
	command = "module load R/3.5.1;run_EdgeR.R %s %s %s %s &> /dev/null"%(input,",".join(t_group),",".join(c_group),n)
	os.system(command)
