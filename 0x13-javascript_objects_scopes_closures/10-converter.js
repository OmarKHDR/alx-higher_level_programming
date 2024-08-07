#!/usr/bin/node

exports.converter = function (base) {
  function convert (numb) {
    return numb.toString(base);
  }
  return convert;
};
