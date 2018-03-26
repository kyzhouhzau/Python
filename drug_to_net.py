
"""

Time 2018年3月10号
Author：周开银
目的：做三种数据之间的交叉并取出重叠部分。
"""
from collections import defaultdict

import sys
inp=sys.argv[1]
filename=inp
inp=inp.replace('_',', ')

with open('New_score-hotnet-significant.txt','r') as rf:
	di=defaultdict(list)
	base_diseasename=inp
	for line in rf:
		flag=line.strip().split('\t')[0]
		gene=line.strip().split('\t')[2:]
		di[flag].append(gene)
	dit=defaultdict(list)

	
	gene_net=di[inp]
	total_gene=[]	
	for lis_gene in gene_net:
		total_gene+=lis_gene
	with open(filename+'.txt','r') as f:
		for line_ in f:
			line=line_.strip()
			if line in total_gene:
				dit[base_diseasename].append(line)
	print(base_diseasename.lower()+" has following target gene {}".format(dit[base_diseasename]))

	with open('all_drug_disease_target_xx.txt','r') as rf:
		di_=defaultdict(list)
		di_1=defaultdict(set)
		result=defaultdict(list)
		finall=defaultdict(list)
		for line in rf:
			diseasename=line.strip().split('\t')[1]
			if diseasename==base_diseasename:
				genename=line.strip().split('\t')[2]
				drugname=line.strip().split('\t')[0]
				di_[diseasename].append(genename)
				di_1[drugname].add(genename)
		gene_list=dit[base_diseasename]
		gene_list_=di_[base_diseasename]
		result_gene = set([x for x in gene_list_ if x in gene_list])
		result[base_diseasename]=result_gene
		result_gene_lis=result[base_diseasename]
		print("Three file have following target gene {}".format(result_gene_lis))
		for gene in result_gene_lis:
			for key,value in di_1.items():
				if gene in value:
					finall[key].append(gene)
		with open(base_diseasename+'_result.txt','w') as wf:
			for key ,value in finall.items():
				wf.write(key+'\t'+'\t'.join(value)+'\n')










