const express = require("express");
const User = require("../models/schema/userSchema");
const Board = require("../models/schema/boardSchema");
const Comment = require("../models/schema/commentSchema");
const router = express.Router();

/**
 * 전체 게시물을 반환합니다.
 * @return 전체 게시물
 */

router.get("/", async (req, res) => {

});

/**
 * 게시물을 작성합니다.
 * @return 성공 시 201
 */

router.post("/", async (req, res) => {

});

/**
 * 특정 아이디를 갖는 게시물의 정보를 반환합니다.
 * @param id 아이디
 * @return 게시물 정보 (댓글 포함)
 */

router.get("/:id", async (req, res) => {

});

/**
 * 특정 아이디를 갖는 게시물에 댓글을 답니다.
 * @param id 아이디
 * @return 성공시 201, 게시물이 존재하지 않을 시 404
 */

router.post("/:id/comment", (req, res) => {

});

/**
 * 특정 게시물을 삭제합니다.
 * @param id 아이디
 * @return 성공 시 200, 존재하지 않을 시 404
 */

router.delete("/:id", async (req, res) => {

});

/**
 * 특정 게시물을 대체합니다.
 * @param id 게시물의 id
 * @return 성공 시 200, 존재하지 않을 시 404
 */

router.put("/:id", async (req, res) => {

});

module.exports = router;
