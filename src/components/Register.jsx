import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();

  const backgroundColor = "#333"; // Dark gray background color

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      setErrorMessage("Passwords don't match");
      return;
    }

    try {
      await axios
        .post("/api/auth/register", {
          username,
          password,
        })
        .then(() => {
          navigate("/login");
        });
    } catch (error) {
      console.error("Error:", error.response.data.message);
    }
  };

  return (
    <form
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
          Register
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
        <input
          type="password"
          placeholder="Confirm Password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
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
        {errorMessage && (
          <p style={{ color: "red", marginTop: "5px" }}>{errorMessage}</p>
        )}
        <button
          onClick={handleRegister}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "10px",
            backgroundColor: "#f68347",
            color: "#fff",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Register
        </button>
      </div>
    </form>
  );
};

export default Register;
