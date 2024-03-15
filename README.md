# Oporto Races Database

This project was carried out as part of the database course and is composed by four different phases, namely design database, load data, user interaction and questions.

The data can be dowloaded [here](https://www.kaggle.com/datasets/pvlima/results-from-running-events-in-porto).

## Design database
- Draw UML diagram 
- Convert diagram to relational model
- Write a SQL script that creates the database
- Create the corresponding tables in your PostgreSQL database

## Load data
Create python script that:

- Remove all data from the database
- Read all_races.csv and populate database

## User interaction
Create a python script that:

- Prints a menu with several options (for example, search runner, show race, top runner for each distance, ...) and that allows the user to select one of these options
- Allows the user to interact with the database in a friendly interface. For example, show the progress of a single runner on a single distance throughout the years.

## Questions
- Who run the fastest 10K race ever (name, birthdate, time)?
- What 10K race had the fastest average time (event, event date)?
- What teams had more than 3 participants in the 2016 maratona (team)?
- What are the 5 runners with more kilometers in total (name, birthdate, kms)?
- What was the best time improvement in two consecutive maratona races (name,
birthdate, improvement)?
