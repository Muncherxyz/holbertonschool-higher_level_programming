#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const wedgeAntillesMovies = movies.filter(movie => {
      return movie.characters.some(character => character.includes(characterId));
    });
    console.log(wedgeAntillesMovies.length);
  }
});
