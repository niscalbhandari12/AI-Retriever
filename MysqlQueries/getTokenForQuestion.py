import mysql.connector
import re
mydb = mysql.connector.connect(
  host="192.168.1.250",
  user="jeffreytest",
  password="SGDroid$99",
  database="boomconsole_dev_server"
)


def getToken(string):
    token = 0
    mycursor = mydb.cursor()
    parsedData = "select count(*) as totalcount,to_the_concepts_id from the_connections where to_the_concepts_id IN (select the_concepts.id from the_concepts where character_value = '" + str(string) + "' group by the_concepts.type_id) group by to_the_concepts_id order by totalcount desc;"
    print(parsedData)
    
    mycursor.execute(parsedData)
    myresult = mycursor.fetchall()


    for x in myresult:
        token = x[1]
        exit
    return token

# print(getToken(9860086391))
