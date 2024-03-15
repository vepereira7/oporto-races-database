import psycopg2
import pandas as pd
import numpy as np
from datetime import datetime
from sqlalchemy import create_engine
import psycopg2.extras as extras

#load dataset
df = pd.read_csv('all_races2.csv', low_memory=False, delimiter=',')

#teams table
dfteam = df[['team']].copy()
teams = dfteam.drop_duplicates().reset_index(drop=True)
teams['team_id'] = np.arange(1, 1 + len(teams))

#athlete table
dfathletes = df[['name', 'birth_date', 'sex', 'nation', 'team']].copy().drop_duplicates(subset=['name', 'birth_date', 'sex', 'nation']).reset_index(drop=True)
dfathletes['athlete_id'] = np.arange(1, 1 + len(dfathletes))
dfathletes = pd.merge(dfathletes, teams, on='team', how='left')
athletes = dfathletes.drop(columns=['team'])

#event table
dfevents = df[['event', 'event_year', 'distance']].copy()
events = dfevents.drop_duplicates().reset_index(drop=True)
events['event_id'] = np.arange(1, len(events) + 1)

#results table
df2 = athletes
dfresults = df.drop_duplicates().reset_index(drop=True)
results = dfresults
results['net_time'] = results['net_time'].replace(np.nan, '00:00:00', regex=True)
results = pd.merge(results, df2, on=['name', 'birth_date', 'sex', 'nation'], how='left')
results = pd.merge(results, events, right_on=['event', 'event_year', 'distance'], left_on=['event', 'event_year', 'distance'], how='left')
results = results.drop(columns=['name', 'birth_date', 'team', 'sex', 'nation', 'event', 'event_year', 'distance'])
results['result_id'] = np.arange(1, 1 + len(results))

#rename this two tables
teams = teams.rename(columns={"team":"name"})
events = events.rename(columns={"event":"name"})

#connect to database
try:
    con = psycopg2.connect(
        database = 'fced_vitor_pereira',
        user = 'fced_vitor_pereira',
        password = 'vepdatabase77',
        host = 'dbm.fe.up.pt',
        port = '5433',
        options='-c search_path=public'
    )
except:
    print('You must be connected to FEUP VPN')
else:
    print('Connection sucessful!')

#delete existing data
cur = con.cursor()
cur.execute("""DELETE FROM athletes;
DELETE FROM team;
DELETE FROM event;
DELETE FROM results;""")
con.commit()
print('Data deleted.')

#load teams table
cur = con.cursor()
for row in teams.itertuples():
    cur.execute(f"INSERT INTO team (name, team_id) VALUES (%s, %s)",
    (row.name, row.team_id))
con.commit()
print('Teams completed!')

#load athlete table
cur = con.cursor()

for row in athletes.itertuples():
    cur.execute(f"INSERT INTO athlete (athlete_id, name, birth_date, sex, nation, team_id) VALUES (%s, %s, %s, %s, %s, %s)",
    (row.athlete_id, row.name, row.birth_date, row.sex, row.nation, row.team_id))
con.commit()

print('Athlete completed!')

#load event table
cur = con.cursor()
for row in events.itertuples():
    cur.execute(f"INSERT INTO event (name, event_year, distance, event_id) VALUES (%s, %s, %s, %s)",
    (row.name, row.event_year, row.distance, row.event_id))
con.commit()
print('Event completed!')

#load results table
cur = con.cursor()
for row in results.itertuples():
    cur.execute(f"""INSERT INTO results (result_id, place, place_in_class, net_time, official_time, age_class,
    event_id, athlete_id, bib, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (row.result_id, row.place, row.place_in_class, row.net_time, row.official_time, row.age_class, row.event_id,
    row.athlete_id, row.bib, row.team_id))
con.commit()
con.close()
print('Results Completed!')