var fs = require("fs");
var express = require("express");
var app = express();

app.get('/help', function (req, res) {
	var commandList =    "RESTful command: \n"
			 +   "listUser    \n"
			 +   "addUser    \n"
			 +   "deleteUser \n"
			 +   ":<key>   "
        res.end( commandList );
	}
)

app.get('/listUser', function (req, res) {
       fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
   });
})

//添加的新用户数据
var newUser = {
   "user4" : {
      "name" : "mohit",
      "password" : "password4",
      "profession" : "teacher",
      "id": 4
   }
}

app.get('/addUser', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
       data = JSON.parse( data );
       data["user4"] = newUser["user4"];
       console.log( data );
       res.end( JSON.stringify(data, null, 4));
   });
})

app.get('/deleteUser', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
       data = JSON.parse( data );
       delete data["user4"];
       console.log( data );
       res.end( JSON.stringify(data, null, 4));
   });
})

app.get('/:id', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
       data = JSON.parse( data );
       console.log( "param is:  " + req.params.id );
       var user = data[req.params.id]
       console.log( user );
       res.end( JSON.stringify(user, null, 4));
   });
})


var server = app.listen(8888, function () {
		var host = server.address().address
		var port = server.address().port
		console.log("RESTful Server，link - http://%s:%s", host, port)
	 	}
)
