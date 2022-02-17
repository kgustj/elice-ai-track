const express = require("express");
const path = require("path");
const router = express.Router();

router.get("/", (req, res) => {
    res.send("안녕!");
});

// Q. 어떤 수를 받아서 우리가 이 수가 짝수인지, 홀수인지 알고 싶다.
// params : 주소에 추가적으로 들어오는 매개변수

router.get("/is_odd/:id", (req, res) => {
    console.log(req.params.id);
    res.send(req.params.id);
});

router.get("/count-form", (req, res) => {
    res.sendFile(path.join(__dirname, "../static/get.html"));
});

router.get("/count", (req, res) => {
    const number = parseInt(req.query.number);
    if (number % 2 === 0) {
        res.send("짝수입니다.");
    } else {
        res.send("홀수입니다.");
    }
});

router.get("/count", (req, res) => {
    const number = parseInt(req.query.number);
    if (number % 2 === 0) {
        res.send("짝수입니다.");
    } else {
        res.send("홀수입니다.");
    }
});

module.exports = router;

// 220217 실습
