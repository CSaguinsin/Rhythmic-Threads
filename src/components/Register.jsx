import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import Navbar from "./Navbar";

const Register = () => {
  const [loading, setLoading] = useState(false);

  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();

  const handleRegister = async (event) => {
    event.preventDefault();

    setLoading(true);

    if (password !== confirmPassword) {
      setErrorMessage("Passwords don't match");
      return;
    }

    try {
      await axios
        .post("/api/auth/register", {
          name,
          username,
          password,
        })
        .then(() => {
          navigate("/login");
        });
    } catch (error) {
      setLoading(false);
      console.error("Error: ", error.response);
    }
  };

  return (
    <>
      <Navbar />

      <div className="hero relative min-h-full bg-[url('/LandingpagePics/heroPic.png')] bg-cover bg-center">
        <form
          onSubmit={(e) => handleRegister(e)}
          className="flex items-center justify-center py-20"
        >
          <div className="max-w-[400px] rounded-xl bg-gray-50 p-12 text-center shadow-lg dark:bg-gray-800">
            <h2 className="mb-8 text-2xl font-bold text-[#f68347]">
              Create your Account
            </h2>

            <label
              htmlFor="name"
              className="block text-left text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Full Name
            </label>
            <input
              id="name"
              className="my-2 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              type="text"
              placeholder="John Doe"
              name="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />

            <label
              htmlFor="email"
              className="block text-left text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Email
            </label>
            <input
              id="email"
              className="my-2 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              type="email"
              placeholder="john.doe@gmail.com"
              name="username"
              autoComplete="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />

            <label
              htmlFor="password"
              className="block text-left text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Password
            </label>
            <input
              className="my-2 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              type="password"
              placeholder="********"
              value={password}
              name="password"
              autoComplete="new-password"
              onChange={(e) => setPassword(e.target.value)}
              required
            />

            <label
              htmlFor="confirmPassword"
              className="block text-left text-sm font-medium text-gray-700 dark:text-gray-200"
            >
              Confirm Password
            </label>
            <input
              className="my-2 w-full rounded-lg border-2 border-gray-300 p-3 dark:bg-gray-700 dark:text-white"
              type="password"
              placeholder="********"
              autoComplete="new-password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />

            {errorMessage && (
              <p className="mx-0 font-semibold text-red-500">{errorMessage}</p>
            )}

            <button
              type="submit"
              disabled={loading}
              className="btn my-3 w-full rounded-full border-0 px-12 text-white shadow-sm"
              style={{ backgroundColor: "#f68347" }}
            >
              {loading ? "Creating account..." : "Create Account"}
            </button>

            <p className="mt-2 text-gray-500 dark:text-gray-400">
              Already have an account?{" "}
              <a href="/login" className="text-[#f68347]">
                Login
              </a>
            </p>
          </div>
        </form>
      </div>
    </>
  );
};

export default Register;
