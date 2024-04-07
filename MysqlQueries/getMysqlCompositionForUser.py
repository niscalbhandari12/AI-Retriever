import mysql.connector
import re
mydb = mysql.connector.connect(
  host="192.168.1.250",
  user="jeffreytest",
  password="SGDroid$99",
  database="boomconsole_dev_server"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT group_concat(' ',typeoftheconcept.character_value, ' has ', totheconcept.character_value, ' ' , typetotheconcept.character_value) FROM the_connections left join the_concepts as oftheconcept on oftheconcept.id =  the_connections.of_the_concepts_id left join the_concepts as typeoftheconcept on oftheconcept.type_id = typeoftheconcept.id left join the_concepts as totheconcept on totheconcept.id = the_connections.to_the_concepts_id left join the_concepts as typetotheconcept on totheconcept.type_id = typetotheconcept.id where the_connections.user_id = 10267 and the_connections.order_id = 2 group by the_connections.type_id;")

myresult = mycursor.fetchall()
count = 0
file_object = open(str(count) + ".txt", "w")

for x in myresult:
    count = count + 1
    string = str(x)
    print(string)
    newString = re.sub('[^, ./_A-Za-z0-9]+', '', string)

    file_object.write(newString)
    file_object.write("\n\n\n")
