#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ep}/`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log(JSON.parse(body).title);
  }
});
