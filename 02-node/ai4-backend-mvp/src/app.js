const express = require("express");
const app = express();
const createError = require("http-errors");
const passport = require("passport");
const dotenv = require("dotenv").config();
const path = require("path");
const cookieParser = require("cookie-parser");
const session = require("express-session");
const logger = require("morgan");
const dayjs = require("dayjs");

const loginRequired = require("./middlewares/login-required");
const getUserFromJWT = require("./middlewares/get-user-from-jwt");

const indexRouter = require("./routes");
const postsRouter = require("./routes/posts");
const usersRouter = require("./routes/users");
const authRouter = require("./routes/auth");
require("./passport")();

const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/crudboard");
const db = mongoose.connection;
db.on("error", (error) => console.log("❌ DB Error:", error));
db.once("open", () => console.log("✅ Connected to DB"));

app.locals.formatDate = (date) => {
    return dayjs(date).format("YYYY-MM-DD HH:mm:ss");
};

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use(passport.initialize());
app.use(getUserFromJWT);

app.get("/", (req, res) => {
    res.json({ status: "OK" });
});

app.use("/", indexRouter);
app.use("/posts", loginRequired, postsRouter);
app.use("/users", loginRequired, usersRouter);
app.use("/auth", authRouter);

app.use((err, req, res, next) => {
    // render the error page
    res.json({ error: err.message }).status(err.status || 500);
});

const PORT = process.env.PORT;

app.listen(PORT, () => {
    console.log(`✅ Running on http://localhost:${PORT} 🚀`);
});
