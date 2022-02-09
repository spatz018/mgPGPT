

MEGAN support files:
1. Create pgpt.map file by using the PGPT Ontology file
2. Create pgpt.tre file by using the PGPT Ontology file
3. Create a mapping file for the PGPT diamond database

	a) take the current pgpt diamond database fasta file (uncompressed)
	
	b) retrieve fasta header without ">" by e.g.:  awk 'sub(/^>/, "")' PGPT_protein.fasta > PGPT_protein_accessions.txt
	
	c) run (with -op define outputpath):  python3 pgpt_acc-map2mapping.py -a PGPT_protein_accessions.txt -m pgpt.map -on pgptID2nodeID.tab
	
	d) now take file and convert to abin by applying: convert-accessionmap2abin -i pgptID2nodeID.tab -o mgPGPT_mapping.abin
	
	
