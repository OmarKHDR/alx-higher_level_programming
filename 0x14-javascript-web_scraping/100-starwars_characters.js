#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const ep = process.argv[2];

request.get(url + `${ep}/`, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).characters.forEach(element => {
      request(element, (error, res, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
