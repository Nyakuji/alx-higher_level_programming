#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err === null) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err === null) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }
  }
});
