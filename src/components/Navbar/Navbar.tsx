import "./Navbar.css";
import { useState } from "react";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";

function Navbar() {
  const [clicked, setClicked] = useState(false);

  function handleClick() {
    setClicked(!clicked);
  }


  const menuItems = [
    {
      title: "Home",
      url: "/",
      cName: "nav-links",
    },
    {
      title: "Secrets",
      url: "/secrets",
      cName: "nav-links",
    },
 
  ];

  return (
    <nav className="navbarItems">
      <h1 className="navbar-logo">
        SecretsShare {" "}
      </h1>
      <div className="menu-icon" onClick={handleClick}>
        {clicked ? (
          <CloseIcon style={{ color: "white" }} />
        ) : (
          <MenuIcon style={{ color: "white" }}>
            <CloseIcon />
          </MenuIcon>
        )}
      </div>
      <ul className={clicked ? "nav-menu active" : "nav-menu"}>
       {  menuItems.map((item, index) => (
              <a key={index} href={item.url} className={item.cName}>
                {item.title}
              </a>
            ))
       }
      </ul>

   
    </nav>
  );
}

export default Navbar;
