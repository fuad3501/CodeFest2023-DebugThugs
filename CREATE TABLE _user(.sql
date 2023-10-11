CREATE TABLE _user(
    userId INT NOT NULL AUTO_INCREMENT,
    userType INT,
    PRIMARY KEY (userId)
);

CREATE TABLE therapistUser(
    therapistUserId INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50),
    _name VARCHAR(50),
    userID INT,
    PRIMARY KEY (therapistUserId),
    FOREIGN KEY (userId) REFERENCES _user(userId)
);

CREATE TABLE clientUser(
    clientUserId INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50),
    _name VARCHAR(50),
    userID INT,
    therapistUserId INT
    PRIMARY KEY (clientUserId),
    FOREIGN KEY (userId) REFERENCES _user(userId),
    FOREIGN KEY (therapistUserId) REFERENCES therapistUser(therapistUserId)
);

CREATE TABLE ChatLogs
(
logId INT NOT NULL AUTO_INCREMENT,
logTimestamp DATETIME,
therapistUserId INT NOT NULL,
clientUserId INT NOT NULL,
PRIMARY KEY (logId),
FOREIGN KEY (therapistUserId) REFERENCES therapistUser(therapistUserId),
FOREIGN KEY (clientUserId) REFERENCES clientUser(clientUserId)
);

