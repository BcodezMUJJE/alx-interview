#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api';
const filmsEndpoint = `${baseUrl}/films/`;

request(filmsEndpoint + movieId + '/', function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('An error occurred while requesting the API:', error);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  if (charactersUrls.length === 0) {
    console.error(`No characters found for movie ID ${movieId}`);
    process.exit(1);
  }

  const namesPromises = charactersUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error || response.statusCode !== 200) {
          reject(`An error occurred while fetching character data from ${url}: ${error}`);
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  Promise.all(namesPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
});
