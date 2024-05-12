import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import localStorage from "../utils/localStorage";
import Navbar from "./Navbar";

const Login = () => {
  const [loading, setLoading] = useState(false);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

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
    <>
      <Navbar />

      <div className="hero relative min-h-full bg-[url('/LandingpagePics/callToAction.png')] bg-cover bg-center">
        <form
          onSubmit={(e) => handleLogin(e)}
          className="flex items-center justify-center py-20"
        >
          <div className="max-w-[400px] rounded-xl bg-gray-50 p-12 text-center shadow-lg dark:bg-gray-800">
            <h2
              style={{
                color: "#f68347",
                marginBottom: "20px",
                fontWeight: "bold",
                fontSize: "24px",
              }}
            >
              Sign in the get started
            </h2>
            <input
              type="text"
              placeholder="Username"
              value={username}
              autoComplete="username"
              onChange={(e) => setUsername(e.target.value)}
              className="my-1 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              autoComplete="current-password"
              onChange={(e) => setPassword(e.target.value)}
              className="my-1 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              required
            />

            <div className="flex w-full flex-row items-center justify-between align-middle">
              {/* remember me */}
              <span>
                <input
                  type="checkbox"
                  id="rememberMe"
                  name="rememberMe"
                  className="mr-2"
                />
                <label htmlFor="rememberMe">Remember me</label>
              </span>

              <button
                type="submit"
                disabled={loading}
                className="btn my-3 rounded-full border-0 px-12 text-white shadow-sm"
                style={{ backgroundColor: "#f68347" }}
              >
                {loading ? "Logging in..." : "Login"}
              </button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
};

export default Login;
