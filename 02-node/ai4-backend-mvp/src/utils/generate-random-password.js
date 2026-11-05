module.exports = () => {
    return Math.floor(Math.random() * 10 ** 8) // 1~100000000
        .toString() // int to str
        .padStart(8, "0"); // 문자열이 지정된 길이에 도달할 때까지 현재 문자열을 다른 문자열로 채움
};
