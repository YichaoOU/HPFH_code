#!/hpcf/authorized_apps/rhel7_apps/R/install/3.5.1/bin/Rscript

library("edgeR")

# Rscript run_EdgeR.R input_count_table treatment_group control_group output_name
args <- commandArgs(trailingOnly=TRUE)
infile = args[1]
group1 <- as.character(unlist(strsplit(args[2], ","))) ## treatment
group2 <- as.character(unlist(strsplit(args[3], ","))) ## control
group_label <- c(rep("treatment", length(group1)), rep("control", length(group2)))
outfile = args[4]


countData = read.csv(infile,sep="\t")
mat <- countData[,-1]
rownames(mat) <- countData[,1]

group <- factor(group_label)


y <- DGEList(counts=mat,group=factor(group_label))

y <- calcNormFactors(y)

design <- model.matrix(~group)

y <- estimateDisp(y,design)


fit <- glmQLFit(y,design)

pdf(paste(outfile, ".plotQLDisp.pdf", sep=""))
plotQLDisp(fit)
dev.off()

qlf <- glmQLFTest(fit)


res=topTags(qlf,n=Inf)

write.table(res, file=paste(outfile, ".edgeR_result.tsv", sep=""),sep="\t",quote=FALSE, row.names=TRUE)


