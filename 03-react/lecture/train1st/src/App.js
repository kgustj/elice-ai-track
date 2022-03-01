import { useState } from "react";

const articleList = [
    { title: "HTML", body: "HTML is Hyper-Text Markup Language" },
    { title: "CSS", body: "CSS defines the style of page" },
    { title: "JS", body: "Javascript defines the action of page" },
];

function HeaderTag() {
    return (
        <header>
            <h1>React Sample Page</h1>
        </header>
    );
}

function Nav(props) {
    function clickHandler(postId) {
        return (event) => {
            event.preventDefault();
            props.setPostId(postId);
        };
    }
    return (
        <nav>
            <ol>
                <li>
                    <a href="/" onClick={clickHandler(0)}>
                        HTML
                    </a>
                </li>
                <li>
                    <a href="/" onClick={clickHandler(1)}>
                        CSS
                    </a>
                </li>
                <li>
                    <a href="/" onClick={clickHandler(2)}>
                        JavaScript
                    </a>
                </li>
            </ol>
        </nav>
    );
}

function Article(props) {
    const article = articleList[props.postId];
    return (
        <article>
            <h2>{article.title}</h2>
            {article.body}
        </article>
    );
}

function App() {
    const [id, setId] = useState(0);
    return (
        <>
            <HeaderTag></HeaderTag>
            <Nav setPostId={setId}></Nav>
            <Article postId={id}></Article>
        </>
    );
}

export default App;
