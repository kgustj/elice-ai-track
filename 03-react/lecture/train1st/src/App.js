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
                {articleList.map((value, index) => (
                    <li>
                        <a href="/" onClick={clickHandler(index)}>
                            {value.title}
                        </a>
                    </li>
                ))}
            </ol>
        </nav>
    );
}
// properties -> props
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
