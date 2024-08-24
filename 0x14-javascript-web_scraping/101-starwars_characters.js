#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const ep = process.argv[2];

const arr = [];
let len = 1;

request.get(url + `${ep}/`, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body).characters;
    len = list.length;
    //   console.log(len)
    list.forEach(element => {
      request(element, (error, res, body) => {
        if (error) {
          console.log(error);
        } else {
          arr.push(JSON.parse(body).name);
        }
        if (arr.length === len) {
          arr.forEach((ele) => console.log(ele));
        }
      });
    });
  }
});
