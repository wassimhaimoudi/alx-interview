#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length <= 2) {
  console.log('Please provide a Movie ID as a command line argument');
  process.exit(1);
}

const movieID = process.argv[2];

request(`${API_URL}/films/${movieID}/`, (err, _, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const charactersURL = JSON.parse(body).characters;

  const charactersNamePromises = charactersURL.map(characterURL => {
    return new Promise((resolve, reject) => {
      request(characterURL, (err, _, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  Promise.all(charactersNamePromises)
    .then(names => {
      console.log(names.join('\n'));
      process.exit(0);
    })
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
});
