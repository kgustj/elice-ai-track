const http = require("http");
const fs = require("fs");

function onRequest(req, res) {
    res.writeHead(200, { "Content-Type": "text/html" });
    fs.readFile("index.html", "UTF-8", function (err, data) {
        if (err) res.writeHead(404);
        res.write(data);
        res.end();
    });
}

http.createServer(onRequest).listen(8080);

// 220215 실습
