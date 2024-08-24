#!/usr/bin/node

const request = require('request');

url = 'https://alx-intranet.hbtn.io/status';
request.get(url, (error, response, body) => {
  console.log(response.statusCode);
});
