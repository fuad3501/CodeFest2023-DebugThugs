# Import flask and datetime module for showing date and time
import datetime
import sqlite3
from sqlite3 import Error
from flask import Flask

 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)

con=None
 
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
#get each message, get all the data
     
# Running app




def create_connection(db_file):
    """ create a database connection to a SQLite database """
    con = sqlite3.connect(db_file)
    return con

def alterTable():
    cur = con.cursor()
    cur.executescript("""
    ALTER TABLE ChatLogs ADD SenderType INTEGER;
    """)

def insertData():
    cur = con.cursor() 
  
    cur.executescript(""" 
    INSERT INTO _user (userId, userType)
VALUES (1, 1),
       (2, 2),
       (3, 1);

INSERT INTO therapistUser (therapistUserId, username, _name, userId)
VALUES (1, 'therapist1', 'John Doe', 1),
       (3, 'therapist2', 'Jane Smith', 2);

INSERT INTO clientUser (clientUserId, username, _name, userId, therapistUserId)
VALUES (2, 'client1', 'Alice Johnson', 3, 1),

INSERT INTO ChatLogs (logId, logTimestamp, therapistUserId, clientUserId, message)
VALUES (1, """ """, 1, 1, 'Hello, how are you?'),
       (2, '2023-10-11 10:15:00', 1, 2, 'I'm doing well, thanks!'),
       (3, '2023-10-11 10:30:00', 2, 1, 'How can I help you today?');
""")

def createTables():
    cur = con.cursor() 
  
    cur.executescript(""" 
        CREATE TABLE _user (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    userType INTEGER
);

CREATE TABLE therapistUser (
    therapistUserId INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    _name TEXT,
    userId INTEGER,
    FOREIGN KEY (userId) REFERENCES _user(userId)
);

CREATE TABLE clientUser (
    clientUserId INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    _name TEXT,
    userId INTEGER,
    therapistUserId INTEGER,
    FOREIGN KEY (userId) REFERENCES _user(userId),
    FOREIGN KEY (therapistUserId) REFERENCES therapistUser(therapistUserId)
);

CREATE TABLE ChatLogs (
    logId INTEGER PRIMARY KEY AUTOINCREMENT,
    logTimestamp DATETIME,
    therapistUserId INTEGER,
    clientUserId INTEGER,
    message TEXT,
    FOREIGN KEY (therapistUserId) REFERENCES therapistUser(therapistUserId),
    FOREIGN KEY (clientUserId) REFERENCES clientUser(clientUserId)
);

ALTER TABLE ChatLogs ADD SenderType INTEGER;



        
        """) 
if __name__ == '__main__':
    con=create_connection("data.db")
    alterTable()
    app.run(debug=True)


    "CREATE TABLE User(userID INTEGER primary key, name TEXT, username TEXT);"
    "CREATE TABLE TherapistUser(therapistuserID INTEGER primary key references User(userID));"
    "CREATE TABLE ClientUser(userID INTEGER primary key foreign key references User(userID), TherapistUserID foreign key references TherapistUser(TherapistUserID));"



