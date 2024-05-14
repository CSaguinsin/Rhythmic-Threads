/* eslint-disable react/prop-types */
import { Outlet } from "react-router-dom";
import AuthNavbar from "../authcomponents/AuthNavbar";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Products() {
  const [user, setUser] = useState(null);
  const token = JSON.parse(localStorage.getItem("token"));

  useEffect(() => {
    // fetch user from api
    (async () => {
      await axios
        .get("/api/auth/profile", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((res) => setUser(res.data));
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
