# -*- coding: utf-8 -*-
################### pgpt_comp_kegg.py ############################
# AUTHOR: Sascha Patz at university of Tuebingen, 2021-09-11
# DESCRIPT: Takes accession file of all pgpt fasta sequences
#           retrieved by awk 'sub(/^>/, "")' PGPT_protein.fasta
#           and the megan pgpt.map file (format per line nodeID\tnodeName)
#           and returns a tab file in format acc/tnodeID per line.
#           The output file can be coverted to a MEGAN mappping .abin file.
#           # CMD: see python3 pgpt_acc-map2mapping.py -h
##################################################################
vers = "0.1"

# ####### #
# Modules #
# ####### #
import argparse, sys, os, io

# ######### #
# Functions #
# ######### #
def check_file_exist(file):
	print("Checking file path ...")
	if os.path.exists(file):
		if os.path.isfile(file):
			print("... single file found")
			return("F")
		elif os.path.isdir(file):
			print("... path to files found")
			return("P")
	else:
		print("ERROR: File, directory or path does not exist for:"+ file)
		sys.exit()

def readmeganmapfile(fm):
	fn = open(fm,"r").readlines() #node id to nodename (megan .map file)
	d_nod = {}
	for node in fn:
		nod_l = node.rstrip().split("\t")
		if "PGPT0" in node and nod_l[1].split("-")[0] not in d_nod:
			d_nod[nod_l[1].split("-")[0]]=nod_l[0]
	return(d_nod)

def readaccfile(fac,nodic,op,na):
	fa = open(fac,"r").readlines() #accession file of all pgpt fasta sequences retrieved by awk 'sub(/^>/, "")' PGPT_BASE_nr_Aug2021n.fasta
	fo = open(str(op+"/"+na).replace("//","/"),"a")
	for acc in fa:
		ac = acc.rstrip()
		fo.write(ac+"\t"+nodic[ac.split("-")[0]]+"\n")
	fo.close()

def main()
	# Initiate the parser
	parser = argparse.ArgumentParser(prog='pgpt_acc-map2mapping',formatter_class=argparse.MetavarTypeHelpFormatter)

	# Add long and short argument
	parser.add_argument("--accession", "-a", type=str, help="input protein accession file (one accession per line)", required=True)
	parser.add_argument("--map", "-m", type=str, help="input megan map file (nodeID\tnodeName)", required=True)
	parser.add_argument("--outpath", "-op", default = ".", type=str, help="path to output folder, def.: current directory")
	parser.add_argument("--outname", "-on", default = ".", type=str, help="output file name", required=True)
	parser.add_argument("--version", "-v", help="version", action="store_true")

	# Read arguments from the command line
	args = parser.parse_args()
	# Check for arguments
	if args.version:
		print("Version  "+vers)
	if args.accession:
		form_s = check_file_exist(args.accession)
	if args.map:
                form_s = check_file_exist(args.map)
	readaccfile(args.accession,readmeganmapfile(args.map),args.outpath,args.outname)

# #### #
# Main #
# #### #
if __name__ == "__main__":
	main()

