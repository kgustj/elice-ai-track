const ToDo = ({ value, toggleHandler }) => {
    // props -> props.value
    const { id, content, isCompleted } = value;
    const clickHandler = (event) => {
        // toggle
        toggleHandler(id);
    };

    return (
        <li>
            <label>
                <input type="checkbox" checked={isCompleted} onChange={clickHandler}></input>
                {content}
            </label>
            <button>삭제</button>
        </li>
    );
};

export default ToDo;
