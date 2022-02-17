const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
    res.render("index");
    //   _: 안쓰는 변수.
    //  __: 시스템 환경변수. ex) dirname
});

module.exports = router;
