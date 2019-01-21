import sqlite3
conn = sqlite3.connect("all_to_the_bottom.db")
# cartDict = {}
cursor = conn.cursor()
# cursor.execute("SELECT id_cart, dat FROM request7")
# cartList = cursor.fetchall()
# cursor.execute("SELECT type FROM request5 WHERE category LIKE 'success%'")
# payList = cursor.fetchall()
# for i in range(len(cartList)):
# 	cartDict[cartList[i][0]] = cartDict.get(cartList[i][0], 0)
# for j in range(len(payList)):
# 	cartDict[payList[j][0]] += 1

# for key in sorted(cartDict):
#     if cartDict[key] == 0:
#     	cursor.execute("SELECT dat FROM request5 WHERE type key")
#     	dataList = cursor.fetchall()
#     	print(dataList)
    # print(key, cartDict[key], sep=' : ')

	# if cartDict[cartList[i][0]] > 1:
	# 	ans7 += 1
	# 	dataList.append(customerList[i][1])
cursor.execute("SELECT COUNT(*) FROM request5 WHERE category LIKE 'success%' ")
amount_pay = cursor.fetchall()
cursor.execute("SELECT COUNT(*) FROM request7")
add_card = cursor.fetchall()
# print(cartList)

print(int(*add_card[0]) - int(*amount_pay[0]))
# print(amount_pay)