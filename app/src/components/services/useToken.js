import {useState} from "react";

export default function useToken() {
    const getToken = () => {
        const tokenString = sessionStorage.getItem('token');
        const userToken = JSON.parse(tokenString);
        return userToken?.access_token
    };

    const [token, setToken] = useState(getToken());

    const removeToken = () => {
        sessionStorage.removeItem('token');
        window.location.href = '/';
    };

    const saveToken = userToken => {
        sessionStorage.setItem('token', JSON.stringify(userToken));
        setToken(userToken.access_token);
    };

    return {
        setToken: saveToken,
        removeToken,
        token
    };
}
