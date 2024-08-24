#!/usr/bin/node

const request = require('request');

function getObj (ar) {
  const obj = {
  };
  ar.forEach((element) => {
    if (element.completed === true) {
      if (element.userId in obj) {
        obj[`${element.userId}`] += 1;
      } else {
        obj[`${element.userId}`] = 1;
      }
    }
  });
  console.log(obj);
}

request.get(process.argv[2], (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    getObj(JSON.parse(body));
  }
});
