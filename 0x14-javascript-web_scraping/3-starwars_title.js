#!/usr/bin/node

const request = require('request');
ep = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/${ep}/`;
request.get(url, (error, response, body)=>{
    console.log(JSON.parse(body).title)
});

