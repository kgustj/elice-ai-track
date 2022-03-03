import TodoInput from "./components/TodoInput";
import TodoList from "./components/TodoList";
import { useEffect, useState } from "react";
import useAxios from "./tools/useAxios";
import axios from "axios";

const initialList = [
    { id: 1, content: "상쾌하게 기상하기", isCompleted: true },
    { id: 2, content: "엘리스 이론 강의 듣기", isCompleted: true },
    { id: 3, content: "간지나게 점심 먹기", isCompleted: true },
    { id: 4, content: "엘리스 실습 강의 듣기", isCompleted: false },
    { id: 5, content: "고풍스럽게 저녁 먹기", isCompleted: false },
    { id: 6, content: "누구보다도 꿀잠 자기", isCompleted: false },
];

function App() {
    const [loading, setLoading] = useState(true);
    const [toDoList, setToDoList] = useState(initialList);

    useEffect(() => {
        useAxios.setup();
        async function fetch() {
            const resp = await axios.get("/");
            return resp.data.records;
        }

        fetch().then((v) => {
            const fetchedList = v.map((v) => {
                return {
                    id: v.id,
                    content: v.fields.Name,
                    isCompleted: v.fields.isCompleted || false,
                };
            });
            setToDoList(fetchedList);
            setLoading(false);
        });
    }, []);

    function handleToggle(id) {
        const mapped = toDoList.map((todo) => {
            if (todo.id === id) return { ...todo, isCompleted: !todo.isCompleted };
            else return { ...todo };
        });
        console.log(mapped);
        setToDoList(mapped);
    }

    async function handleSubmit(content) {
        const resp = await axios.post("/", {
            records: [
                {
                    fields: {
                        Name: content,
                        isCompleted: false,
                    },
                },
            ],
        });
        // console.log(resp);

        let copied = [
            ...toDoList,
            ...resp.data.records.map((v) => {
                return {
                    id: v.id,
                    content: v.fields.Name,
                    isCompleted: v.fields.isCompleted || false,
                };
            }),
        ];
        setToDoList(copied);
    }

    if (loading) return <div>Loading...</div>;
    return (
        <div>
            <TodoInput submitHandler={handleSubmit}></TodoInput>
            <TodoList toDoList={toDoList} toggleHandler={handleToggle}></TodoList>
        </div>
    );
}

export default App;
