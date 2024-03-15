DROP TABLE IF EXISTS athlete;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS result;

CREATE TABLE team(
    team_id integer PRIMARY KEY,
	name varchar
);

CREATE TABLE athlete(
	athlete_id integer PRIMARY KEY,
	name varchar NOT NULL,
	birth_date date NOT NULL,
	sex varchar NOT NULL,
	nation varchar,
	team_id integer REFERENCES team
);

CREATE TABLE event(
	event_id integer PRIMARY KEY,
	name varchar NOT NULL,
	event_year integer NOT NULL,
	distance integer NOT NULL
);

CREATE TABLE results(
	result_id integer PRIMARY KEY,
	place integer NOT NULL,
	place_in_class integer NOT NULL,
	net_time TIME NOT NULL,
	official_time TIME NOT NULL,
	age_class varchar,
	event_id integer REFERENCES event,
	athlete_id integer REFERENCES athlete,
	team_id integer REFERENCES team,
	bib integer NOT NULL,
);