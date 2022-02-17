const express = require("express");
const path = require("path");
const app = express();
const router = express.Router();
const port = 3001;

router.get("/", (req, res) => {});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "/index.html"));
    // req: request(요청). 사용자의 브라우저 정보, 질문(주소창), 로그인정보
    // res: response(응답). 사이트 내용 HTML
    //   _: 안쓰는 변수.
    //  __: 시스템 환경변수. ex) dirname
});

app.get("/webtoon", (req, res) => res.send("<h2>Webtoon ...</h2>"));
app.get("/profile", (req, res) => res.send("<h2>Profile ...</h2>"));

app.use((err, req, res, next) => {
    console.log(err);
    res.status(500).send(err.message);
});

app.listen(port, () => {
    console.log(`Server is running - localhost:${port}`);
});
