/* eslint-disable react/prop-types */
import { Outlet } from "react-router-dom";
import AuthNavbar from "../authcomponents/AuthNavbar";
import { useEffect, useState } from "react";
import axios from "axios";
import localStorage from "../utils/localStorage";

export default function Products() {
  const [user, setUser] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    // fetch user from api
    (async () => {
      await axios
        .get("/api/auth/profile", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((res) => {
          localStorage.setItem("user", JSON.stringify(res.data));
          setUser(res.data);
        });
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);
  return (
    <>
      <AuthNavbar user={user} />

      <Outlet />
    </>
  );
}
