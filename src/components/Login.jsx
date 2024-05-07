import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const backgroundColor = '#333'; // Dark gray background color

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://localhost:5000/login', { username, password });
            console.log(response.data.message);
        } catch (error) {
            console.error('Error:', error.response.data.message);
        }
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh', backgroundColor }}>
            <div style={{ textAlign: 'center', maxWidth: '400px', padding: '20px', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)' }}>
                <h2 style={{ color: '#f68347', marginBottom: '20px', fontWeight: 'bold', fontSize: '24px' }}>Login</h2>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} style={{ width: '100%', padding: '10px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '5px', backgroundColor: '#444', color: '#fff' }} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} style={{ width: '100%', padding: '10px', marginTop: '5px', border: '1px solid #ccc', borderRadius: '5px', backgroundColor: '#444', color: '#fff' }} />
                <button onClick={handleLogin} style={{ width: '100%', padding: '10px', marginTop: '10px', backgroundColor: '#f68347', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>Login</button>
            </div>
        </div>
    );
};

export default Login;
