import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Menthol-Silver1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))
    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

mycursor = db.cursor()
mycursor.execute("SELECT Team_ID, Team_Name, Mascot FROM Team")

teams = mycursor.fetchall()
print("\n-- DISPLAYING TEAM RECORDS --", end="")
for team in teams:
    print("\nTeam ID: ", team[0],) 
    print("Team Name: ", team[1])
    print("Mascot: ", team[2])

print("\n-- DISPLAYING TEAM RECORDS --", end= "")
mycursor.execute("SELECT Player_ID, First_Name, Last_Name FROM Player")
players = mycursor.fetchall()
for player in players:
    print("\nPlayer ID: ", player[0])
    print("First Name: ", player[1])
    print("Last Name: ", player[2])