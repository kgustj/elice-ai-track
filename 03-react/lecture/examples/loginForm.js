import { useState } from "react";
import { Form, Button } from "react-bootstrap";

function FormWithCondition() {
    // email, password, confirmPassword, name 변수 및 세팅함수를 useState 훅을 통해 생성
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [name, setName] = useState("");

    // isPasswordValid, isPasswordSame,  isNameValid,  isFormValid의 4개 조건 변수 생성
    const isPasswordValid = password.length >= 4;
    const isPasswordSame = password === confirmPassword;
    const isNameValid = name.length >= 2;
    const isFormValid = isPasswordValid && isPasswordSame && isNameValid;

    const handleSubmit = (e) => {
        e.preventDefault();
        const message = `이메일: ${email}, 비밀번호: ${password}, 확인 비밀번호: ${confirmPassword}, 이름: ${name} 입니다. `;
        alert(message);
    };

    return (
        <Form onSubmit={handleSubmit} className="w-25">
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>이메일</Form.Label>
                <Form.Control type="email" placeholder="abc@example.com" autoComplete="off" value={email} onChange={(e) => setEmail(e.target.value)} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>비밀번호</Form.Label>
                <Form.Control type="password" placeholder="비밀번호" value={password} onChange={(e) => setPassword(e.target.value)} />
                {!isPasswordValid && <Form.Text className="text-danger">비밀번호는 4글자 이상입니다.</Form.Text>}
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicConfirmPassword">
                <Form.Label>비밀번호 확인</Form.Label>
                <Form.Control type="password" placeholder="비밀번호 확인" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
                {!isPasswordSame && <Form.Text className="text-danger">비밀번호가 일치하지 않습니다.</Form.Text>}
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicName">
                <Form.Label>이름</Form.Label>
                <Form.Control type="text" placeholder="엘리스" value={name} onChange={(e) => setName(e.target.value)} />
                {!isNameValid && <Form.Text className="text-danger">이름은 2글자 이상입니다.</Form.Text>}
            </Form.Group>
            <Button variant="primary" type="submit" className="mt-4" disabled={!isFormValid}>
                제출
            </Button>
        </Form>
    );
}

export default FormWithCondition;
