CREATE TABLE WORLD_CUPS(
YEAR INT NOT NULL,
COUNTRY VARCHAR(35),
WINNER VARCHAR(35),
RUNNERS_UP VARCHAR(35),
THIRD VARCHAR(35),
FOURTH VARCHAR(35),
GOALSSCORED INT,
QUALIFIEDTEAMS INT,
MATCHESPLAYED INT,
ATTENDANCE VARCHAR(9),
PRIMARY KEY (YEAR));


CREATE TABLE WORLD_CUP_MATCHES(
YEAR INT,
DATE_TIME VARCHAR(35),
STAGE VARCHAR(25),
STADIUM VARCHAR(100), 
CITY VARCHAR(60), 
HOME_TEAM_NAME VARCHAR(50), 
HOME_TEAM_GOALS INT, 
AWAY_TEAM_GOALS INT, 
AWAY_TEAM_NAME VARCHAR(50), 
WIN_CONDITIONS VARCHAR(100), 
ATTENDANCE INT,
HALF_TIME_HOME_GOALS INT,
HALF_TIME_AWAY_GOALS INT,
REFEREE VARCHAR(80), 
ASSISTANT1 VARCHAR(80),
ASSISTANT2 VARCHAR(80), 
ROUNDID INT NOT NULL, 
MATCHID INT NOT NULL, 
HOME_TEAM_INITIALS CHAR(3), 
AWAY_TEAM_INITIALS CHAR(3),
CONSTRAINT PRIME_KEY PRIMARY KEY (ROUNDID, MATCHID),
FOREIGN KEY (YEAR) REFERENCES WORLD_CUPS(YEAR)
);



CREATE TABLE WORLD_CUP_PLAYERS(
ROUNDID INT,
MATCHID INT,
TEAM_INITIALS CHAR(3),
COACH_NAME VARCHAR(80),
LINE_UP CHAR(1),
SHIRT_NUMBER INT,
PLAYER_NAME VARCHAR(80),
POSITION VARCHAR(3),
EVENT VARCHAR(50),
FOREIGN KEY (ROUNDID, MATCHID) REFERENCES WORLD_CUP_MATCHES(ROUNDID, MATCHID));
