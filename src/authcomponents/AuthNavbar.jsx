/* eslint-disable react/prop-types */
import { memo } from "react";
import Logo from "/public/webSystemLogo.png";
import { useNavigate } from "react-router-dom";

const AuthNavbar = memo(function AuthNavbar({ user }) {
  const navigate = useNavigate();

  const signOut = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div className="navbar sticky top-0 z-10 bg-white px-[70px]">
      <div className="">
        <div className="dropdown">
          <div
            tabIndex={0}
            role="button"
            className="btn btn-ghost lg:hidden"
          ></div>
        </div>
      </div>

      <div className="navbar-center hidden space-x-[24px] lg:flex">
        <a href="/landingpage">
          <img src={Logo} className="h-[4rem] w-[4rem]" />
        </a>

        {/* Search bar */}
        <label className="input input-bordered flex w-[500px] items-center gap-2">
          <input
            type="text"
            className="grow"
            placeholder="Search products..."
          />
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 16 16"
            fill="currentColor"
            className="h-4 w-4 opacity-70"
          >
            <path
              fillRule="evenodd"
              d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
              clipRule="evenodd"
            />
          </svg>
        </label>
      </div>

      {user ? (
        <div className="navbar-end space-x-3">
          {/* Cart */}
          <a href="/cart" className="btn btn-ghost">
            <img src="/icons/cart.png" className="h-6 w-6" />
          </a>

          {/* User Dropdown */}
          <details className="dropdown">
            <summary className="btn glass m-1 flex items-center pe-1 text-sm">
              <img
                className="me-2 h-8 w-8 rounded-full p-1"
                src={user?.image_url ?? "/imgs/avatar.png"}
                alt="user photo"
              />
              {user.name}
              <svg
                className="ms-3 h-2.5 w-2.5"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 10 6"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="m1 1 4 4 4-4"
                />
              </svg>
            </summary>
            <ul className="menu dropdown-content z-[1] w-max rounded-box bg-base-100 p-2 shadow">
              <div className="px-4 pt-3 text-sm text-gray-900 dark:text-white">
                <div className="font-medium ">{user?.name}</div>
                <div className="truncate">{user?.username}</div>
              </div>

              <div className="divider my-1" />

              <ul
                className="pb-2 text-sm text-gray-700 dark:text-gray-200"
                aria-labelledby="dropdownInformdropdownAvatarNameButtonationButton"
              >
                <li>
                  <a
                    href="#"
                    className="block rounded-md px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  >
                    Dashboard
                  </a>
                </li>
                <li>
                  <button
                    type="button"
                    className="block rounded-md px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white"
                    onClick={() => signOut()}
                  >
                    Sign out
                  </button>
                </li>
              </ul>
            </ul>
          </details>
        </div>
      ) : (
        <div className="navbar-end space-x-3">
          <a href="/login" className="btn px-8">
            Login
          </a>

          <a
            href="/register"
            className="btn px-8 text-white"
            style={{ backgroundColor: "#F68347" }}
          >
            Create an account →
          </a>
        </div>
      )}
    </div>
  );
});

export default AuthNavbar;
