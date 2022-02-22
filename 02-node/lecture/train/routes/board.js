const express = require("express");
const User = require("../models/schema/userSchema");
const Board = require("../models/schema/boardSchema");
const Comment = require("../models/schema/commentSchema");
const router = express.Router();

/*
 * 전체 게시물을 반환합니다.
 * @return 전체 게시물
 */
router.get("/", async (req, res) => {
    const boards = await Board.find({});
    res.status(200).json(boards);
});

/*
 * 게시물을 작성합니다.
 * @return 성공 시 201
 */
// TODO: name, content 받는다.
router.post("/", async (req, res) => {
    const { name, content } = req.body;
    const board = new Board({
        name,
        content,
    });
    // * save 를 통해 데이터를 저장 -> 반환 값: 넣은 값
    // * 새로운 데이터를 생성 -> 201 CREATED
    board
        .save()
        .then((savedResult) => {
            res.status(201).json({
                result: "OK",
                data: savedResult,
            });
            console.log(savedResult);
        })
        .catch((err) => {
            res.status(500).send(err.message);
        });
});

/*
 * 특정 아이디를 갖는 게시물의 정보를 반환합니다.
 * @param id 아이디
 * @return 게시물 정보 (댓글 포함)
 */

router.get("/:id", async (req, res) => {});

/*
 * 특정 아이디를 갖는 게시물에 댓글을 답니다.
 * @param id 아이디
 * @return 성공시 201, 게시물이 존재하지 않을 시 404
 */
router.post("/:id/comment", (req, res) => {
    const { id } = req.params;
    const { content } = req.body;
    const board = Board.findById(id);
    if (!board) {
        res.status(404).json({
            result: "Not Found",
        });
    }
    const comment = new Comment({
        content,
        boardId: id,
    });
    comment
        .save()
        .then((savedResult) => {
            res.status(201).json({
                result: "OK",
                data: savedResult,
            });
            console.log(savedResult);
        })
        .catch((err) => {
            res.status(500).send(err.message);
        });
});

/*
 * 특정 게시물을 삭제합니다.
 * @param id 아이디
 * @return 성공 시 200, 존재하지 않을 시 404
 */
router.delete("/:id", async (req, res) => {
    const id = req.params.id;
    // findByIdAndDelete -> findById에서 나온 결과 삭제
    // findByIdAndDelete.then() -> then의 매개변수는 삭제한 결과
    // findByIdAndDelete.then(output.n) -> n은 데이터의 수
    Board.findByIdAndDelete(id).then((output) => {
        if (output.n === 0) {
            return res.status(404).json({
                result: "Not Found",
            });
        }
        res.status(200).json({
            result: "OK",
        });
    });
});

/*
 * 특정 게시물을 대체합니다.
 * @param id 게시물의 id
 * @return 성공 시 200, 존재하지 않을 시 404
 */
router.put("/:id", async (req, res) => {
    const id = req.params.id;
    const { name, content } = req.body;
    // 첫 번째 매개변수 id, 두 번째 매개변수 바뀔 값
    Board.findByIdAndUpdate(id, {
        name,
        content,
    }).then((output) => {
        if (output.n === 0) {
            return res.status(404).json({
                result: "Not Found",
            });
        }
        res.status(200).json({
            result: "OK",
        });
    });
});

module.exports = router;
