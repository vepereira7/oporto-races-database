--question a)
SELECT A.name, A.birth_date, R.official_time
FROM results R
JOIN athlete A ON a.athlete_id=R.athlete_id
JOIN event E ON E.event_id=R.event_id
WHERE E.distance = 10
ORDER BY R.official_time ASC
LIMIT 1

--question b)
SELECT E.event_year, E.name, AVG(R.official_time) as ot_avg
FROM event E
JOIN results R ON E.event_id=R.event_id
WHERE E.distance = 10
GROUP BY E.event_id
ORDER BY ot_avg ASC

--question c)
SELECT T.name as team, COUNT(T.name)
FROM team T
JOIN results R ON T.team_id=R.team_id
JOIN event E on E.event_id=R.event_id
WHERE E.name = 'maratona' AND E.event_year = 2016
GROUP BY T.name
HAVING COUNT(T.name)>3

--question d)
SELECT A.name, A.birth_date, SUM(E.distance)
FROM event E
JOIN results R ON E.event_id=R.event_id
JOIN athlete A ON R.athlete_id=A.athlete_id
GROUP BY A.name, A.birth_date
ORDER BY SUM(E.distance) DESC
LIMIT 5




