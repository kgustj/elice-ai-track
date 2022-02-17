const express = require("express");
const app = express();
const indexRouter = require("./routes/index");

app.use("/", indexRouter);

app.get("/webtoon", (req, res) => res.send("<h2>Webtoon ...</h2>"));
app.get("/profile", (req, res) => res.send("<h2>Profile ...</h2>"));
// req: request(요청). 사용자의 브라우저 정보, 질문(주소창), 로그인정보
// res: response(응답). 사이트 내용 HTML

// app.use((err, req, res, next) => {
//     console.log(err);
//     res.status(500).send(err.message);
// });

app.listen(3000, () => {
    console.log("Server is running - localhost:3000");
});
