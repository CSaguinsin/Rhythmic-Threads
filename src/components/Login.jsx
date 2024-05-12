import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import localStorage from "../utils/localStorage";

const Login = () => {
  const [loading, setLoading] = useState(false);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const backgroundColor = "#333"; // Dark gray background color

  const navigate = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();

    setLoading(true);

    try {
      await axios
        .post("/api/auth/login", {
          username,
          password,
        })
        .then((res) => {
          localStorage.setItem("token", res.data.token);
          navigate("/landingpage");
        });
    } catch (error) {
      setLoading(false);
      console.error("Error:", error.response.data.message);
    }
  };

  return (
    <form
      onSubmit={(e) => handleLogin(e)}
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "60vh",
        backgroundColor,
      }}
    >
      <div
        style={{
          textAlign: "center",
          maxWidth: "400px",
          padding: "20px",
          backgroundColor: "#fff",
          borderRadius: "8px",
          boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)",
        }}
      >
        <h2
          style={{
            color: "#f68347",
            marginBottom: "20px",
            fontWeight: "bold",
            fontSize: "24px",
          }}
        >
          Login
        </h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "5px",
            border: "1px solid #ccc",
            borderRadius: "5px",
            backgroundColor: "#444",
            color: "#fff",
          }}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "5px",
            border: "1px solid #ccc",
            borderRadius: "5px",
            backgroundColor: "#444",
            color: "#fff",
          }}
        />
        <button
          type="submit"
          disabled={loading}
          className={loading ? "animate-pulse" : ""}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "10px",
            backgroundColor: loading ? "#444" : "#f68347",
            color: "#fff",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </div>
    </form>
  );
};

export default Login;
