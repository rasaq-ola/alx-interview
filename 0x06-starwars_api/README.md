# 0x06. Star Wars API - Star Wars Characters

## Description
This project involves writing a Node.js script that prints all characters of a Star Wars movie using the Star Wars API. The script will take a movie ID as a positional argument and display each character's name in the order they appear in the movie.

### Star Wars API
The Star Wars API (SWAPI) provides a wealth of data from the Star Wars universe, including information on characters, planets, species, starships, and films. The script fetches data from the `/films/` endpoint.

## Task 0: Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- **Positional Argument**: The first positional argument passed is the Movie ID. For example, if you pass `3`, it refers to “Return of the Jedi.”
- **API**: You must use the Star Wars API `https://swapi-api.alx-tools.com/api/films/:id/` where `:id` is the Movie ID.
- **Output**: Print one character name per line in the same order as the characters list in the `/films/` endpoint.
- **Module**: You must use the `request` module in Node.js to make HTTP requests.

#### Example
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
