import ToDoInput from "./components/ToDoInput";
import ToDoList from "./components/ToDoList";
import { useState } from "react";

const initialList = [
    { id: 1, content: "상쾌하게 기상하기", isCompleted: true },
    { id: 2, content: "엘리스 이론 강의 듣기", isCompleted: true },
    { id: 3, content: "간지나게 점심 먹기", isCompleted: true },
    { id: 4, content: "엘리스 실습 강의 듣기", isCompleted: false },
    { id: 5, content: "고풍스럽게 저녁 먹기", isCompleted: false },
    { id: 6, content: "누구보다도 꿀잠 자기", isCompleted: false },
];

function App() {
    const [toDoList, setToDoList] = useState(initialList);

    const handleToggle = (id) => {
        const mapped = toDoList.map((todo) => {
            if (todo.id === id) return { ...todo, isCompleted: !todo.isCompleted };
            else return { ...todo };
        });
        console.log(mapped);
        setToDoList(mapped);
    };

    return (
        <div>
            <ToDoInput></ToDoInput>
            <ToDoList toDoList={toDoList} toggleHandler={handleToggle}></ToDoList>
        </div>
    );
}

export default App;
