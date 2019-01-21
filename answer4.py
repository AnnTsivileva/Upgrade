import sqlite3
hour = 4
conn = sqlite3.connect("all_to_the_bottom.db")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE answer4 (id, tim)")
# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request3"""
# 				)
# conn.commit()
# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request4"""
# 				)
# conn.commit()
# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request5"""
# 				)
# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request6"""
# 				)
# conn.commit()
# cursor.execute("""INSERT INTO answer4(tim, id)
# 					SELECT tim, id
# 					FROM request7"""
# 				)
# conn.commit()
if hour == 0:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '00:%' ")
elif hour == 1:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '01:%' ")
elif hour == 2:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '02:%' ")
elif hour == 3:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '03:%' ")
elif hour == 4:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '04:%' ")
elif hour == 5:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '05:%' ")
elif hour == 6:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '06:%' ")
elif hour == 7:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '07:%' ")
elif hour == 8:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '08:%' ")
elif hour == 9:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '09:%' ")
elif hour == 10:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '10:%' ")
elif hour == 11:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '11:%' ")
elif hour == 12:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '12:%' ")
elif hour == 13:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '13:%' ")
elif hour == 14:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '14:%' ")
elif hour == 15:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '15:%' ")
elif hour == 16:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '16:%' ")
elif hour == 17:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '17:%' ")
elif hour == 18:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '18:%' ")
elif hour == 19:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '19:%' ")
elif hour == 20:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '20:%' ")
elif hour == 21:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '21:%' ")
elif hour == 22:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '22:%' ")
elif hour == 23:
	cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE '23:%' ")
# cursor.execute("SELECT COUNT(*) FROM answer4 WHERE tim LIKE 'hour:%' ESCAPE 'hour'")
ans4 = cursor.fetchall()
print(int(*ans4[0]) / 14)
conn.close()