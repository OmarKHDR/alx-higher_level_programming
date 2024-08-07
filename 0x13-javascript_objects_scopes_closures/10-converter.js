#!/usr/bin/node

exports.converter = function (base) {
  b = base;
  function convert(numb) {
    return numb.toString(b);
  }
  return convert;
}
