import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AuthLandingPage = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();
  const token = JSON.parse(localStorage.getItem("token"));

  useEffect(() => {
    // fetch user from api
    const getUser = async () => {
      await axios
        .get("/api/auth/profile", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((res) => setUser(res.data));
    };

    getUser();

    // redirect to products page if there is a user
    if (!user?.id) {
      navigate("/products");
    } else {
      navigate("/login");
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);
};

export default AuthLandingPage;
