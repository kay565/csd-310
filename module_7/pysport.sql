
CREATE TABLE Team (
    Team_ID INT NOT NULL AUTO_INCREMENT, 
    Team_Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Team_ID));

CREATE TABLE Player (
    Player_ID INT NOT NULL AUTO_INCREMENT,
    First_Name VARCHAR(50) NOT NULL,
    Fk_Team_ID INT,
    INDEX Par_ing (Player_ID),
    CONSTRAINT Fk_Player FOREIGN KEY (Team_ID) ON DELETE CASCADE ON UPDATE CASCADE);

INSERT INTO Team(Team_Name, Mascot) VALUES 
('King','Tiger'), 
('Mighty', 'Hawks');

INSERT INTO Player (First_Name, Last_Name, Fk_Team_ID) VALUES
('Jerry','White',1),
('Garry','Miller',1),
('Perry','Barcia'2),
('Henry','Williams',2),
('John','Davis',1),
('Jack','Smith',2);


