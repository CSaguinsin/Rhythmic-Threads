import Logo from "/webSystemLogo.png";

const Navbar = () => {
  return (
    <div className="navbar bg-white md:px-36">
      <div className="navbar-start">
        <div className="dropdown">
          <div
            tabIndex={0}
            role="button"
            className="btn btn-ghost lg:hidden"
          ></div>
          <ul
            tabIndex={0}
            className="menu dropdown-content menu-sm z-[1] mt-3 w-52 rounded-box bg-base-100 p-2 shadow"
          >
            <li>
              <a>Home </a>
            </li>
            <li>
              <a>Parent</a>
              <ul className="p-2">
                <li>
                  <a>Submenu 1</a>
                </li>
                <li>
                  <a>Submenu 2</a>
                </li>
              </ul>
            </li>
            <li>
              <a> MEN</a>
            </li>
          </ul>
        </div>

        <img src={Logo} className="h-[6rem] w-[6rem]" />
      </div>

      <div className="navbar-center hidden lg:flex">
        <ul className="menu menu-horizontal px-1">
          <li className="font-inter font-semibold">
            <a>HOME</a>
          </li>
          <li className="font-inter font-semibold">
            <a>MEN</a>
          </li>
          <li className="font-inter font-semibold">
            <a>WOMEN</a>
          </li>
          <li className="font-inter font-semibold">
            <a>KIDS</a>
          </li>
        </ul>
      </div>

      <div className="navbar-end space-x-3">
        <a className="btn">Login</a>

        <button
          className="btn text-white"
          style={{ backgroundColor: "#F68347" }}
        >
          Create an account →
        </button>
      </div>
    </div>
  );
};

export default Navbar;
