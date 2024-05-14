import Logo from "/webSystemLogo.png";

const Navbar = () => {
  return (
    <div className="navbar bg-white md:px-36">
      <div className="navbar-start">
        {/* Mobile menu */}
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

        <a href="/">
          <img
            src={Logo}
            className="h-[6rem] w-[6rem]"
            alt="Welcome to Rhythmic Threads"
          />
        </a>
      </div>

      <div className="navbar-center hidden lg:flex">
        <ul className="menu menu-horizontal px-1 uppercase">
          <li className="font-inter font-semibold">
            <a href="/">Home</a>
          </li>
          <li className="font-inter font-semibold">
            <a href="/products?q=men">Men</a>
          </li>
          <li className="font-inter font-semibold">
            <a href="/products?q=women">Women</a>
          </li>
          <li className="font-inter font-semibold">
            <a href="/products?q=kids">Kids</a>
          </li>
        </ul>
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
};

export default Navbar;
