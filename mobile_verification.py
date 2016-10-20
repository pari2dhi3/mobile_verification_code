import csv
import re
import mysql.connector as sqlcon
import dbConfig

# Open database connection
cnx = sqlcon.connect(user=dbConfig.USER, password=dbConfig.PWD,
                     host=dbConfig.HOST, database=dbConfig.DATABASE)
# prepare a cursor object using cursor() method
cursor = cnx.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "Sample Query --> SELECT work_phone, personal_phone \
FROM Table"

x=["Id","Work Mob No.","Personal Mob No.","Reason of invalidation"]

# Execute the SQL command
cursor.execute(sql)
resultFile = open("fileName.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(x)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
	cm_id = row[0]
	work_phone = row[1]
	personal_phone = row[2]

	#regex expression is used to find invalid / test case work mobile numbers
	if re.search("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$", work_phone):		
		if re.search("9{10}|8{10}|7{10}", work_phone):
			x=[cm_id, work_phone, personal_phone, "Work Mob. No is a test case"]
			wr.writerow(x)
		else:
			continue
	else :
		x=[Id, work_phone, personal_phone, "Work Mob. No is invalid"]
		wr.writerow(x)
	#regex expression is used to find invalid / test case personal mobile numbers 
	if re.search("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$", personal_phone):
		if re.search("9{10}|8{10}|7{10}", personal_phone):
			x=[cm_id, work_phone, personal_phone, "Personal Mob. No is a test case"]
			wr.writerow(x)
		else:
			continue
	else : 
		x=[Id, work_phone, personal_phone, "Personal Mob. No is invalid"]
		wr.writerow(x)
# disconnect from server
cnx.close()
