const panel = document.querySelector(`.panel`);
let axis = 15,
    turn = 1,
    map = [];

let blank = 0;

// 2차원 배열로 DB 만들기
// 승리 조건 분석할 때 필요한 공간 + 4
function data() {
    for (let i = 0; i < axis + 4; i++) {
        const arr = [];
        arr.length = axis + 4;
        map.push(arr.fill(0, 0, axis + 4));
    }
}

// turn 박스 만들기
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

// turn 박스 초기화
function initTurn() {
    const img = document.querySelector("img");
    if (turn === 2) {
        img.setAttribute("src", "./img/black.png");
        turn = 1;
    } else {
        img.setAttribute("src", "./img/white.png");
        turn = 2;
    }
}

// 승리 시 초기화
function initBoard() {
    for (let i = 0; i < axis; i++) {
        for (let j = 0; j < axis; j++) {
            map[i][j] = 0;
            panel.querySelectorAll(".row")[i].querySelectorAll(".col")[j].classList.remove("white", "black");
        }
    }
    blank = 0;
    turn = 2;
    initTurn();
}

function initWin() {
    if (turn === 1) {
        setTimeout(() => {
            console.log("Black WIN!");
            alert("Black WIN!");
            initBoard();
        });
    } else {
        setTimeout(() => {
            console.log("White WIN!");
            alert("White WIN!");
            initBoard();
        });
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
                    this.classList.add("black");
                } else {
                    this.classList.add("white");
                }
                // 콘솔 로그 기록
                console.log(`${turn === 1 ? "Black" : "White"} clicked ${alphabet.charAt(j)}${axis - i}, ${blank} ${blank === 1 ? "move" : "moves"}.`);
                console.groupCollapsed("Map");
                for (let i = 0; i < axis; i++) {
                    console.log(axis - i < 10 ? `0${axis - i}` : `${String(axis - i)}`, map[i].slice(0, 15));
                }
                console.groupEnd("Map");
            } else {
                // 돌이 이미 놓아진 자리를 클릭하면 턴 넘어가지 않게
                if (turn === 2) {
                    turn = 1;
                } else {
                    turn = 2;
                }
            }

            for (let i = 0; i < axis; i++) {
                for (let j = 0; j < axis; j++) {
                    if (turn === map[i][j] && turn === map[i][j + 1] && turn === map[i][j + 2] && turn === map[i][j + 3] && turn === map[i][j + 4]) {
                        initWin();
                        break;
                    } else if (turn === map[i][j] && turn === map[i + 1][j] && turn === map[i + 2][j] && turn === map[i + 3][j] && turn === map[i + 4][j]) {
                        initWin();
                        break;
                    } else if (turn == map[i][j] && turn == map[i + 1][j + 1] && turn == map[i + 2][j + 2] && turn == map[i + 3][j + 3] && turn == map[i + 4][j + 4]) {
                        initWin();
                        break;
                    } else if (turn == map[i][j + 4] && turn == map[i + 1][j + 3] && turn == map[i + 2][j + 2] && turn == map[i + 3][j + 1] && turn == map[i + 4][j]) {
                        initWin();
                        break;
                    } else {
                        // pass
                    }
                }
            }

            // 바둑판이 전부 채워졌을 시 초기화
            if (blank == axis ** 2) {
                initBoard();
            } else {
                // pass
            }

            // 턴 바꾸기
            initTurn();
        }
        colTag.addEventListener("click", handleClick);
    }
}

data();
makeTurn();
