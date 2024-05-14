import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import Products from "../components/Products";

const AuthLandingPage = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();
  const token = JSON.parse(localStorage.getItem("token"));

  useEffect(() => {
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

    if (!user?.id) {
      navigate("/landingpage");
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  return <>{user && <Products user={user} />}</>;
};

export default AuthLandingPage;
