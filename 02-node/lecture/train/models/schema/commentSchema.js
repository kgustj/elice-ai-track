const mongoose = require("mongoose");

// 1. 댓글에는 무엇이 들어가야 할까요?
const commentSchema = new mongoose.Schema(
    {
        content: { type: String, required: true },
        ownerId: mongoose.Schema.Types.ObjectId,
        boardId: mongoose.Schema.Types.ObjectId,
    },
    {
        timpStamps: true,
    },
);

// 2. 어떻게 내보내야 할까요?
module.expores = mongoose.model("Comment", commentSchema);
