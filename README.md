
# HPFH_code

This repository provides code for the following two analyses. 

- Differential peak analysis

Reads were first normalized using S3Norm (https://github.com/guanjue/S3norm), then normalized scores for each peak is calculated using DeepTools. Result is provided in `scores_per_bed.tsv`. Next, run `python run_edgeR.py`.


- Motif analysis

The idea of this in silico motif mutation analysis is to all the sequences with one mismatch to the reference sequence, e.g., `TGACCAATAGCC`. Then use FIMO to calculate motif mapping p-value.

To generate one mismatch, run

```
python create_one_mismatch_seq.py TGACCAATAGCC > TGACCAATAGCC.mis.fa

```

Run FIMO, and then parse its output:

```
python get_score.py

```

# Dependency

Pandas

# Note

For ATAC-seq, ChIP-seq, and HiC analyses, please go to https://github.com/YichaoOU/HemTools. 

