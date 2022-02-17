const express = require("express");
const app = express();
const port = 3001;

app.get("/", (req, res) => {
    res.send("Hello, World");
});
// req: request(요청). 사용자의 브라우저 정보, 질문(주소창), 로그인정보
// res: response(응답). 사이트 내용 HTML

app.listen(port, () => {
    console.log(`Server is running - localhost:${port}`);
});
