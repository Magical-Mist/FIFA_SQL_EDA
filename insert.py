import pandas as pd
import numpy as np
import cx_Oracle

# Oracle database connection details
oracle_username = 'YOUR_USERNAME'
oracle_password = 'YOUR_PASSWORD'

# Excel file path
excel_files = ["./datasets/WorldCups.csv", "./datasets/WorldCupMatches.csv", "./datasets/WorldCupPlayers.csv"]

# Connect to Oracle database
oracle_connection = cx_Oracle.connect(
    user=oracle_username,
    password=oracle_password
)

# Create a cursor
cursor = oracle_connection.cursor()

# Read data from Excel file
for file in excel_files:
	df = pd.read_csv(file)
	# NaN value is not translated to NULL in SQL. Hence converting all NaN values to None
	df = df.where(pd.notnull(df), None).copy()
	print("file:", file)
	# Iterate through the DataFrame and insert rows into the Oracle table in required format
	if file == "WorldCups.csv":
		df['Attendance'] = df['Attendance'].apply(lambda x: x.replace('.',''))
		for index, row in df.iterrows():
			cursor.execute("""INSERT INTO WORLD_CUPS(YEAR, COUNTRY, WINNER, RUNNERS_UP, THIRD, FOURTH, GOALSSCORED, QUALIFIEDTEAMS, MATCHESPLAYED, ATTENDANCE) VALUES( :year, :country, :winner, :runner, :third, :fourth, :goals, :qualification, :matchno, :attend)""", row)
		oracle_connection.commit()
	elif file == "WorldCupMatches.csv":
		# Drop all rows with duplicate primary key and rows having NaN in Primary key
		df = df.drop_duplicates(subset=['RoundID','MatchID']).copy()
		df = df.dropna(subset=['RoundID','MatchID']).copy()
		for index, row in df.iterrows():
			cursor.execute("""INSERT INTO WORLD_CUP_MATCHES(YEAR, DATE_TIME, STAGE, STADIUM, CITY, HOME_TEAM_NAME, HOME_TEAM_GOALS, AWAY_TEAM_GOALS, AWAY_TEAM_NAME, WIN_CONDITIONS, ATTENDANCE, HALF_TIME_HOME_GOALS, HALF_TIME_AWAY_GOALS, REFEREE, ASSISTANT1, ASSISTANT2, ROUNDID, MATCHID, HOME_TEAM_INITIALS, AWAY_TEAM_INITIALS) VALUES(:year, :datime, :stage, :stad, :city, :home, :homegoal, :away, :awayname, :win, :attend, :halfgoal, :halfawaygoal, :referee, :assista, :assistb, :roundid, :matchid, :homeinit, :awayinit)""", list(row.values))
		oracle_connection.commit()
	elif file=="WorldCupPlayers.csv":
		for index, row in df.iterrows():
			cursor.execute("""INSERT INTO WORLD_CUP_PLAYERS(ROUNDID, MATCHID, TEAM_INITIALS, COACH_NAME, LINE_UP, SHIRT_NUMBER, PLAYER_NAME, POSITION, EVENT) VALUES(:roundid, :matchid, :teaminit, :coach, :lineup, :shirtno, :player, :pos, :event)""", row)
		# Commit the changes
		oracle_connection.commit()

# Close the cursor and connection
cursor.close()
oracle_connection.close()
