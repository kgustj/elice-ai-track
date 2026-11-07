const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const index = require("./routes/train");

app.use(bodyParser.urlencoded({ extended: false }));

app.use("/routes", index);

let func1 = (req, res) => console.log("ㅋㅋㅋ");

app.get("/", (req, res, next) => {
    res.send("Hello World!");
    next();
});

app.use(func1);

app.listen(4000, () => console.log("Server ON!"));

// 220217 실습
