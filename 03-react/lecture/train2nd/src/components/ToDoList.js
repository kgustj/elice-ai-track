import ToDo from "./ToDo";

const ToDoList = ({ toDoList, toggleHandler }) => {
    return (
        <ul>
            {toDoList.map((v) => (
                <ToDo value={v} toggleHandler={toggleHandler}></ToDo>
            ))}
        </ul>
    );
};

export default ToDoList;
