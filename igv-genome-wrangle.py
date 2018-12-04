# Automated UCSC Genome Wrangler for IGV 

# Can use a list instead of raw input
#id_list = []
#for genome_id in id_list:

# Input genome ID
genome_id = input("Print Genome ID: ")

# Create a new directory, if it doesn't exist
# If identical files exist within the genome id directory, files will be overwritten
import os
try:
    os.mkdir(genome_id)
    os.chdir(genome_id)
except FileExistsError:
    os.chdir(genome_id)

# Download and Index necessary files
import subprocess

# Fasta download and indexing
fasta_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/bigZips/%s.fa.gz' % (genome_id, genome_id)
subprocess.run(['wget', '%s' % (fasta_url), '-O', '%s.fa.gz' % (genome_id)])
subprocess.run(['gunzip','%s.fa.gz' % (genome_id)])
subprocess.run(['samtools','faidx','%s.fa' % (genome_id)]) # indexes fasta

# Cytoband download
cytoband_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/database/cytoBandIdeo.txt.gz' % (genome_id) 
subprocess.run(['wget', '%s' % (cytoband_url), '-O', 'cytoBandIdeo.txt.gz'])

# Gene download and indexing
gene_url = 'http://hgdownload.soe.ucsc.edu/goldenPath/%s/database/refGene.txt.gz' % (genome_id)
subprocess.run(['wget', '%s' % (gene_url), '-O', 'refGene.txt.gz'])
subprocess.run(['gunzip','refGene.txt.gz'])
subprocess.run(['bgzip','refGene.txt'])
subprocess.run(['tabix','refGene.txt.gz']) #indexes gene list 