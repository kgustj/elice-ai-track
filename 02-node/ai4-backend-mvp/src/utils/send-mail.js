const nodemailer = require("nodemailer");

const user = "bbulbum@gmail.com";
const pass = "<GMAIL_APP_PASSWORD>";

const transport = nodemailer.createTransport({
    service: "Gmail",
    auth: {
        user,
        pass,
    },
});

module.exports = (to, subject, text) =>
    new Promise((resolve, reject) => {
        const message = {
            from: user,
            to,
            subject,
            text,
        };

        transport.sendMail(message, (err, info) => {
            if (err) {
                reject(err);
                return;
            }

            resolve(info);
        });
    });
