var fs = require("fs");

var data = fs.readFileSync('server.js');
console.log(data.toString());
console.log("Code Finish - readSync!");

fs.readFile('server.js', function (err, data) {
    if (err) return console.error(err);
    console.log(data.toString());
});

console.log("Code Finish - readAsync - callback!");
