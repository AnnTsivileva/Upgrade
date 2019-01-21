import pars
import tables
import sqlite3
inFile = open('logs.txt', 'r')
conn = sqlite3.connect("all_to_the_bottom.db")
cursor = conn.cursor()
for line in inFile:
	res = pars.parsim(line)
	# print(res)
	if len(res) == 3:
		cursor.execute("INSERT INTO request3 VALUES (?,?,?)", res)
		conn.commit()

	elif len(res) == 4:
		cursor.execute("INSERT INTO request4 VALUES (?,?,?,?)", res)
		conn.commit()

	elif len(res) == 5:
		cursor.execute("INSERT INTO request5 VALUES (?,?,?,?,?)", res)
		conn.commit()

	elif len(res) == 6:
		cursor.execute("INSERT INTO request6 VALUES (?,?,?,?,?,?)", res)
		conn.commit()

	elif len(res) == 7:
		cursor.execute("INSERT INTO request7 VALUES (?,?,?,?,?,?,?)", res)
		conn.commit()

# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request4"""
# 				)
# conn.commit()
#answer4:

conn.close()