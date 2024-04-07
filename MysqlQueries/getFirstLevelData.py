import mysql.connector
import re
mydb = mysql.connector.connect(
  host="192.168.1.250",
  user="jeffreytest",
  password="SGDroid$99",
  database="boomconsole_dev_server"
)


def getFirstLevelData(subjectId, type):
    mycursor = mydb.cursor()
    token = ""
    parsedData = "select concat( relatedconceptstype.character_value, ' is ', relatedconcepts.character_value) from the_concepts  inner join the_connections as con1 on con1.to_the_concepts_id = the_concepts.id left join the_connections as compconnections on compconnections.type_id = con1.type_id  inner join the_concepts as relatedconcepts on relatedconcepts.id = compconnections.to_the_concepts_id inner join the_concepts as relatedconceptstype on relatedconcepts.type_id = relatedconceptstype.id where the_concepts.id = " + str(subjectId) + " and relatedconceptstype.character_value LIKE '%" + type +"%'  LIMIT 10;"
    mycursor.execute(parsedData)

    myresult = mycursor.fetchall()
    print(parsedData)

    for x in myresult:
        token = x[0]
        print(token)
    return token

# getFirstLevelData(100619566)
