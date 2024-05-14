import Logo from "/public/webSystemLogo.png";

const AuthNavbar = () => (
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
        <input type="text" className="grow" placeholder="Search products..." />
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
  </div>
);

export default AuthNavbar;
