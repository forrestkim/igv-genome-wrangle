
# Automated UCSC Genome Wrangler for IGV 

# Input genome ID
genome_id = input("Print Genome ID: ")

#make new dir
import os
try:
    os.mkdir(genome_id)
except FileExistsError:
    os.chdir(genome_id)

# wget all the necessary files
import subprocess

# Fasta
fasta_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/bigZips/%s.fa.gz' % (genome_id, genome_id)
subprocess.run(['wget', '%s' % (fasta_url)])
subprocess.run(['gunzip','%s.fa.gz' % (genome_id)])
subprocess.run(['samtools','faidx','%s.fa' % (genome_id)])

# Cytoband
cytoband_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/database/cytoBandIdeo.txt.gz' % (genome_id) 
subprocess.run(['wget', '%s' % (cytoband_url)])

# Gene
gene_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/database/refGene.txt.gz' % (genome_id)
subprocess.run(['wget', '%s' % (gene_url)])
subprocess.run(['gunzip','refGene.txt.gz'])
subprocess.run(['bgzip','refGene.txt'])
subprocess.run(['tabix','refGene.txt.gz'])
