const http = require("http");

http.createServer((req, res) => {
    console.log(req.url, req.headers.cookie);
    res.writeHead(200, { "Set-Cookie": "mycookie=123qwe" });
    res.end("Welcome to our service.");
}).listen(8003, () => console.log("Web server start."));
