import sqlite3
conn = sqlite3.connect("all_to_the_bottom.db")
countDict = {}
dateDict = {}
ans7 = 0
dataList = []

cursor = conn.cursor()
cursor.execute("SELECT id_customer, dat FROM request6")
customerList = cursor.fetchall()
for i in range(len(customerList)):
	countDict[customerList[i][0]] = countDict.get(customerList[i][0], 0) + 1
	if countDict[customerList[i][0]] > 1:
		ans7 += 1
		dataList.append(customerList[i][1])

for date in dataList:
	dateDict[date] = dateDict.get(date, 0) + 1

# кол-во пользователей совершили покупки повторно за все время
# print(ans7)

for key in sorted(dateDict):
    print(key, dateDict[key], sep=' : ')