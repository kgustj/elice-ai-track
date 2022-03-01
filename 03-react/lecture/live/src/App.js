import "./App.css";
import { useState } from "react";
function Article(props) {
    return (
        <article>
            <h2>{props.title}</h2>
            {props.body}
        </article>
    );
}
function Header(props) {
    function clickHandler(event) {
        event.preventDefault();
        props.onChangeMode();
    }
    return (
        <header>
            <h1>
                <a href="/" onClick={clickHandler}>
                    {props.title}
                </a>
            </h1>
        </header>
    );
}
function Nav(props) {
    function clickHandler(event) {
        event.preventDefault();
        props.onChangeMode(Number(event.target.id));
    }
    let lis = [];
    for (let i = 0; i < props.topics.length; i++) {
        let t = props.topics[i];
        lis.push(
            <li key={t.id}>
                <a href={"/read/" + t.id} id={t.id} onClick={clickHandler}>
                    {t.title}
                </a>
            </li>,
        );
    }

    return (
        <nav>
            <ol>{lis}</ol>
        </nav>
    );
}
function App() {
    console.log("App render");
    let topics = [
        { id: 1, title: "html", body: "html is ..." },
        { id: 2, title: "css", body: "css is ..." },
        { id: 3, title: "js", body: "js is ..." },
    ];
    const [mode, setMode] = useState("WELCOME");
    const [id, setId] = useState(null);
    console.log("id", id);
    function onChangeModeHeader() {
        setMode("WELCOME");
    }
    function onChangeModeNav(selectedId) {
        setMode("READ");
        setId(selectedId);
    }
    let articleTag = "";
    if (mode === "WELCOME") {
        articleTag = <Article title="Welcome" body="Hello, React"></Article>;
    } else if (mode === "READ") {
        for (let i = 0; i < topics.length; i++) {
            let t = topics[i];
            if (t.id === id) {
                articleTag = <Article title={t.title} body={t.body}></Article>;
                break;
            }
        }
    }
    return (
        <>
            <Header title="React" onChangeMode={onChangeModeHeader}></Header>
            <Nav topics={topics} onChangeMode={onChangeModeNav}></Nav>
            {articleTag}
        </>
    );
}

export default App;
