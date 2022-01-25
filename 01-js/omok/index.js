function omok() {
    const panel = document.querySelector(`.panel`);
    let axis = 15,
        turn = 1,
        map = [];

    let blank = 0;

    // 2차원 배열로 DB 만들기
    // 승리 조건 분석할 때 공간이 필요해서 + 4
    function data() {
        for (let i = 0; i < axis + 4; i++) {
            const arr = [];
            arr.length = axis + 4;
            map.push(arr.fill(0, 0, axis + 4));
        }
    }

    function makeTurn() {
        // <div id="turn">
        //     <div class="text">Turn</div>
        //     <div class="img"></div>
        // </div>;
        const turn = document.createElement("div"),
            text = document.createElement("div"),
            img = document.createElement("img");
        panel.appendChild(turn);
        turn.appendChild(text);
        turn.appendChild(img);
        turn.id = "turn";
        text.classList.add("text");
        text.innerText = "Turn";
        img.setAttribute("src", "./img/black.png");
    }

    function initTurn() {
        const img = document.querySelector("img");
        if (turn === 1) {
            img.setAttribute("src", "./img/black.png");
        } else {
            img.setAttribute("src", "./img/white.png");
        }
    }

    // 화면에 바둑판 출력
    for (let i = 0; i < axis; i++) {
        const rowTag = document.createElement("div");
        rowTag.classList.add("row");
        panel.appendChild(rowTag);

        for (let j = 0; j < axis; j++) {
            const colTag = document.createElement("div");
            colTag.classList.add("col");
            rowTag.appendChild(colTag);

            function handleClick() {
                const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                if (map[i][j] === 0) {
                    // 돌 놓기, DB와 화면에 출력
                    map[i][j] = turn;
                    blank += 1;
                    if (map[i][j] === 1) {
                        colTag.classList.add("black");
                    } else {
                        colTag.classList.add("white");
                    }
                    // 콘솔 로그 기록
                    console.log(`${turn === 1 ? "Black" : "White"} clicked ${alphabet.charAt(j)}${axis - i}, ${blank} ${blank === 1 ? "move" : "moves"}.`);
                    console.groupCollapsed("Map");
                    for (let i = 0; i < axis; i++) {
                        console.log(axis - i < 10 ? `0${axis - i}` : `${String(axis - i)}`, map[i].slice(0, 15));
                    }
                    console.groupEnd("Map");
                    // 돌이 이미 놓아진 자리를 클릭하면 턴 넘어가지 않게
                } else {
                    if (turn === 2) {
                        turn = 1;
                    } else {
                        turn = 2;
                    }
                }

                // 승리에 필요한 조건
                for (let i = 0; i < axis; i++) {
                    for (let j = 0; j < axis; j++) {
                        if (turn === map[i][j] && turn === map[i][j + 1] && turn === map[i][j + 2] && turn === map[i][j + 3] && turn === map[i][j + 4]) {
                            console.log(`${turn == 1 ? "Black" : "White"} WIN!`);
                            alert(`${turn === 1 ? "Black" : "White"} WIN!`);
                            break;
                        } else if (turn === map[i][j] && turn === map[i + 1][j] && turn === map[i + 2][j] && turn === map[i + 3][j] && turn === map[i + 4][j]) {
                            console.log(`${turn == 1 ? "Black" : "White"} WIN!`);
                            alert(`${turn === 1 ? "Black" : "White"} WIN!`);
                            break;
                        } else if (turn == map[i][j] && turn == map[i + 1][j + 1] && turn == map[i + 2][j + 2] && turn == map[i + 3][j + 3] && turn == map[i + 4][j + 4]) {
                            console.log(`${turn == 1 ? "Black" : "White"} WIN!`);
                            alert(`${turn === 1 ? "Black" : "White"} WIN!`);
                            break;
                        } else if (turn == map[i][j + 4] && turn == map[i + 1][j + 3] && turn == map[i + 2][j + 2] && turn == map[i + 3][j + 1] && turn == map[i + 4][j]) {
                            console.log(`${turn == 1 ? "Black" : "White"} WIN!`);
                            alert(`${turn === 1 ? "Black" : "White"} WIN!`);
                            break;
                        } else {
                            // pass
                        }
                    }
                }

                if (blank == axis ** 2) {
                    for (let i = 0; i < axis; i++) {
                        for (let j = 0; j < axis; j++) {
                            map[i][j] = 0;
                            panel.querySelectorAll(".row")[i].querySelectorAll(".col")[j].classList.remove("white", "black");
                        }
                    }
                    blank = 0;
                } else {
                    // pass
                }

                // 턴 바꾸기
                if (turn === 2) {
                    turn = 1;
                } else {
                    turn = 2;
                }
                initTurn();
            }
            colTag.addEventListener("click", handleClick);
        }
    }
    data();
    makeTurn();
}

omok();
