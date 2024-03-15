import psycopg2

try:
    con = psycopg2.connect(
        database = 'fced_vitor_pereira',
        user = 'fced_vitor_pereira',
        password = 'vepdatabase77',    #postgres postgres
        host = 'dbm.fe.up.pt',
        port = '5433',
        options='-c search_path=public'
    )
except (Exception,psycopg2.DatabaseError) as error:
    print(error,'You must be connected to FEUP VPN')
    quit()
else:
    print('Connection sucessful!')


def menu():
    print('\n[1] Athletes')
    print('[2] Events')
    print('[3] Results')
    print('[0] Quit menu.')

cur = con.cursor()
menu()

option = int(input('\nInsert your option: '))

while option != 0:
    if (option == 1):
        athlete_name = str(input("\nAthlete name?: "))
        cur.execute(f"""\nSELECT A.name , R.net_time, R.official_time, R.place, E.name, E.event_year 
        FROM results R 
        JOIN athlete A ON A.athlete_id=R.athlete_id
        JOIN event E ON E.event_id=R.event_id
        WHERE A.name = '{athlete_name}'""")
        print(f'\nHere are all {athlete_name} records')
        for record in cur.fetchall():
            print(record)
        break
    elif (option == 2):
        event_name = str(input('\nWhich event?: ')).lower()
        try:
            event_year = int(input('\nWhich year?: '))
        except ValueError:
            event_year = None
        if event_year == None:
            cur.execute(f"""SELECT DISTINCT E.name, E.distance, E.event_year
            FROM event E
            JOIN results R ON R.event_id=E.event_id
            WHERE E.name = '{event_name}'
            ORDER BY E.event_year ASC""")
            print(f'There are all {event_name} contained in this database.')
            print('\nYou must insert year to see more detailed results from each event.')
            for eventrecord in cur.fetchall():
                print(eventrecord)
        else:
            cur.execute(f"""SELECT A.name, E.name, E.event_year, R.official_time, E.distance
            FROM results R
            JOIN event E ON E.event_id=R.event_id
            JOIN athlete A ON A.athlete_id=R.athlete_id
            WHERE E.name = '{event_name}' AND E.event_year = '{event_year}'
            ORDER BY R.official_time ASC""")
            print(f'\n2These are all records from {event_year} in {event_name}')
            for eventrecord in cur.fetchall():
                print(eventrecord)
        break
    elif (option == 3):
        print("""\nInsert event name to see best times all in that event.
        \nInsert event year to see best times of the year in all events.
        \nInsert event name and year to best of the year in that specific event.""")
        try:
            results = (input("\nFrom which event?: ")).lower()
        except ValueError:
            results = ''
            print(results)
        try:
            results_year = int(input('\nFrom which year?: '))
        except ValueError:
            results_year = ''
        if results_year == '' and results == '':
            print('\nYou must insert one of these choices.')
        elif results_year == '':
            cur.execute(f"""SELECT R.place, A.name, R.official_time, E.name, E.event_year
            FROM results R
            JOIN event E ON E.event_id=R.event_id
            JOIN athlete A ON A.athlete_id=R.athlete_id
            WHERE E.name = '{results}' AND R.place = '1'""")
            print(f'There are {results} best results')
            for ryear in cur.fetchall():
                print(ryear)
        elif results == '':
            cur.execute(f"""SELECT R.place, A.name, R.official_time, E.name, E.event_year
            FROM results R
            JOIN event E ON E.event_id=R.event_id
            JOIN athlete A ON A.athlete_id=R.athlete_id
            WHERE E.event_year = '{results_year}' AND R.place = '1'""")
            print(f'These are best results of {results_year} in all events')
            for eyear in cur.fetchall():
                print(eyear)
        else:
            cur.execute(f"""SELECT R.place, A.name, R.official_time, E.name, E.event_year
            FROM results R
            JOIN event E ON E.event_id=R.event_id
            JOIN athlete A ON A.athlete_id=R.athlete_id
            WHERE E.event_year = '{results_year}' AND E.name = '{results}' AND R.place = '1'""")
            print(f'This is the best result of {results_year} in {results}.')
            for allres in cur.fetchall():
                print(allres)
        break
    elif (option == 0):
        quit()
    else:
        print('\nInvalid option, you should choose one option from the previously menu.')
        break
print('\nThank you!')        

