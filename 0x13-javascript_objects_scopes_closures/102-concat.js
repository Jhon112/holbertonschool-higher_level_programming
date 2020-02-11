#!/usr/bin/node

const fs = require('fs');

process.argv.forEach((element, index) => {
  if (index >= 2 && index < 4) {
    fs.readFile(process.argv[index], function (err, data) {
      if (err) throw err;

      fs.appendFile(process.argv[4], data, function (err) {
        if (err) throw err;
      });
    });
  }
});
