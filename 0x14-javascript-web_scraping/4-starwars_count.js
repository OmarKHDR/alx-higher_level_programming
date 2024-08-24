#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const car = `https://swapi-api.alx-tools.com/api/people/${id}`;
const pattern = new RegExp(car, 'i');
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const res = JSON.parse(body);
    res.results.forEach(element => {
      element.characters.forEach(ele => {
        if (pattern.test(ele)) {
          count++;
        }
      }

      );
    });
    console.log(count);
  }
});
