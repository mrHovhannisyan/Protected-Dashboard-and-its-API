import React, {useState} from 'react';

import './App.css';
import Login from "./components/login/Login";
import Dashboard from "./components/dashboard/Dashboard";
import useToken from "./components/services/useToken";


function App() {
    const {token, setToken} = useToken();

    return (
        <div className="App">
            {token ? <Dashboard/> : <Login setToken={setToken}/>}
        </div>
    );
}

export default App;
