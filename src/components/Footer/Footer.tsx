import "./Footer.css";
import MyLocationIcon from "@mui/icons-material/MyLocation";
import MailIcon from "@mui/icons-material/Mail";
import LocalPhoneIcon from "@mui/icons-material/LocalPhone";
import FacebookIcon from "@mui/icons-material/Facebook";
import InstagramIcon from "@mui/icons-material/Instagram";
import TwitterIcon from "@mui/icons-material/Twitter";
import LinkedInIcon from "@mui/icons-material/LinkedIn";

function Footer() {
  const date = new Date();
  const year = date.getFullYear();

  return (
    <footer className="footer">
      <div className="footercontainer">
        <div className="footerrow">
          <div className="footer-left">
            {/* Logo Image  */}
            <a className="company-logo" href="#">
              <h1>SecretsShare</h1>{" "}
            </a>
            <p className="slogan">Secure Secret Sharing</p>
          </div>

          <div className="footer-col">
            <h4>Services</h4>
            <ul>
              <li>
                <a href="/secrets">Secrets</a>
              </li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Contact Information</h4>
            <ul>
              <li>
                {" "}
                <a href="https://maps.app.goo.gl/18b2L1ALboRrGkVE8">
                  {" "}
                  <MyLocationIcon
                    style={{
                      fontSize: "1em",
                      marginTop: "3px",
                      marginRight: "4px",
                    }}
                  />
                  Bazerkan Bldg., Beirut, Lebanon
                </a>{" "}
              </li>
              <li>
                <a href="mailto:issa.makki@lau.edu">
                  {" "}
                  <MailIcon
                    style={{ marginTop: "0px", fontSize: "1em" }}
                  />{" "}
                  E-mail
                </a>
              </li>
              <li>
                <a>
                  {" "}
                  <LocalPhoneIcon style={{ fontSize: "1em" }} /> +961 01 444 777
                </a>
              </li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Follow Us</h4>
            <div className="social-links">
              <a href="#">
                {" "}
                <FacebookIcon style={{ fontSize: "1.5em" }} />{" "}
              </a>
              <a href="#">
                {" "}
                <InstagramIcon />{" "}
              </a>
              <a href="#">
                {" "}
                <TwitterIcon />{" "}
              </a>
              <a href="#">
                {" "}
                <LinkedInIcon />{" "}
              </a>
            </div>
          </div>
        </div>
      </div>

      <p className="copyright">Copyright ⓒ {year} SecretsShare</p>
    </footer>
  );
}

export default Footer;
