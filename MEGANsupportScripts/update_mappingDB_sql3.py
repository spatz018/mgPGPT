import sys, sqlite3

fsql = sys.argv[1]
fupd_l = open(sys.argv[2], "r").readlines()

up_d = {}

for line in fupd_l:
	li_l = line.rstrip().split("\t")
	up_d[li_l[1]] = li_l[3]

#up_s = "UPDATE mappings SET PGPT = 5000 WHERE Accession = 'ABZ93083';"
conn = sqlite3.connect(fsql)
cur = conn.cursor()
for k in sorted(up_d.keys()):
	up_s = "UPDATE mappings SET PGPT = " + str(up_d[k]) + " WHERE Accession = '"+ k +"';"
	cur.execute(up_s)
	conn.commit()
	#cur.execute("SELECT * FROM mappings WHERE accession = 'ABZ93083';")
	#print(cur.fetchall())
conn.close()
