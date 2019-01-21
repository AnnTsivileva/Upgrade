import sqlite3
conn = sqlite3.connect("all_to_the_bottom.db")
cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='request3'")
tab3 = cursor.fetchall()
if int(*tab3[0]) == 0:
	cursor.execute("""CREATE TABLE request3
						(dat text, 
						tim text,
						id text)
					""")
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='request4'")
tab4 = cursor.fetchall()
if int(*tab4[0]) == 0:
	cursor.execute("""CREATE TABLE request4
						(dat text, 
						tim text,
						id text,
						category text)
					""")
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='request5'")
tab5 = cursor.fetchall()
if int(*tab5[0]) == 0:
	cursor.execute("""CREATE TABLE request5
						(dat text, 
						tim text,
						id text,
						category text,
						type text)
					""")
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='request6'")
tab6 = cursor.fetchall()
if int(*tab6[0]) == 0:
	cursor.execute("""CREATE TABLE request6
						(dat text, 
						tim text,
						id text,
						category text,
						id_customer text,
						id_cart text)
					""")
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='request7'")
tab7 = cursor.fetchall()
if int(*tab7[0]) == 0:
	cursor.execute("""CREATE TABLE request7
						(dat text, 
						tim text,
						id text,
						category text,
						id_goods text,
						amount text,
						id_cart)
					""")
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='answer4'")
ans4 = cursor.fetchall()
if int(*ans4[0]) == 0:
	cursor.execute("CREATE TABLE answer4 (id, tim)")
	cursor.execute("""INSERT INTO answer4(tim, id)
						SELECT tim, id
						FROM request3"""
					)
	conn.commit()
	cursor.execute("""INSERT INTO answer4(tim, id)
						SELECT tim, id
						FROM request4"""
					)
	conn.commit()
	cursor.execute("""INSERT INTO answer4(tim, id)
						SELECT tim, id
						FROM request5"""
					)
	cursor.execute("""INSERT INTO answer4(tim, id)
						SELECT tim, id
						FROM request6"""
					)
	conn.commit()
	cursor.execute("""INSERT INTO answer4(tim, id)
						SELECT tim, id
						FROM request7"""
					)
	conn.commit()
# cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='answer6'")
# ans6 = cursor.fetchall()
# if int(*ans6[0]) == 0:
# 	cursor.execute("CREATE TABLE answer6 (dat_add, tim_add, dat_pay, tim_pay)")
# 	cursor.execute("""INSERT INTO answer6(tim, id)
# 						SELECT tim, id
# 						FROM request3"""
# 					)
