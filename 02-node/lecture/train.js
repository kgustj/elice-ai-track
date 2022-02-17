const express = require("express");
const app = express();
const index = require("./routes/train");

app.use("/routes", index);

app.listen(4000, () => console.log("Server ON!"));

// 220217 실습
