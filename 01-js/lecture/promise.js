//callback을 promise로 바꾸는 예제

function loginUser(id, password) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const userDB = [
                {
                    id: "paul",
                    pw: "pw1",
                },
                {
                    id: "tom",
                    pw: "pw2",
                },
                {
                    id: "gray",
                    pw: "pw3",
                },
            ];

            for (let i = 0; i < userDB.length; i++) {
                if (
                    userDB[i].id === id && //
                    userDB[i].pw === password
                ) {
                    resolve(id);
                    return;
                }
            }
            reject("아이디와 패스워드가 맞지 않습니다!");
        }, 2000); // userDB를 가져오는 시간
    });
}

function getRoles(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const roleDB = [
                { id: "paul", role: "admin" },
                { id: "tom", role: "user" },
            ];

            for (let i = 0; i < roleDB.length; i++) {
                if (roleDB[i].id === id) {
                    console.log("로그인 성공!");
                    resolve(roleDB[i]);
                    return;
                }
            }
            reject(`${id}의 role이 존재하지 않습니다!`);
        }, 1000);
    });
}

let id = "tom";
let password = "pw24";

loginUser(id, password).then(getRoles).then(console.log).catch(console.log);
