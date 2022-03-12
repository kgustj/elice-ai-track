import React, { useState, useEffect } from "react";
import UserEditForm from "./UserEditForm";
import UserCard from "./UserCard";
import * as Api from "../../apiMock";

function User({ portfolioOwnerId, isEditable }) {
    // useState 훅을 통해 isEditing 상태를 생성함.
    const [isEditing, setIsEditing] = useState(false);

    // useState 훅을 통해 user 상태를 생성함.
    const [user, setUser] = useState(null);

    useEffect(() => {
        // "users/유저id" 엔드포인트로 GET 요청을 하고, user를 response의 data로 세팅함.
        // 단, 이번 실습에서는 apiMock.js의 가짜 유저 정보를 이용하므로, 실제 api는 쓰지 않음.
        Api.get("users", portfolioOwnerId).then((res) => setUser(res.data));
    }, [portfolioOwnerId]);

    return (
        <>
            {isEditing ? (
                <UserEditForm user={user} setUser={setUser} setIsEditing={setIsEditing} />
            ) : (
                <UserCard user={user} setIsEditing={setIsEditing} isEditable={isEditable} /> //
            )}
        </>
    );
}

export default User;
