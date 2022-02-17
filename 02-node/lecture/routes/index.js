const express = require("express");
const path = require("path");
const router = express.Router();

router.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../index.html"));
    //   _: 안쓰는 변수.
    //  __: 시스템 환경변수. ex) dirname
});

module.exports = router;
