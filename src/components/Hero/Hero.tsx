import "./Hero.css";
import Main from "../../assets/videos/main.mp4";

function Hero() {
  return (
    <div className="hero">
      <div className="headerContainer">
        <video className="vid" autoPlay loop muted>
          <source src={Main} type="video/mp4" />
        </video>
        <h1>Upload Your Secrets</h1>
        <p>Get things off your chest</p>
        <a
          href= "/secrets"
        >
          <button className="btn btn--primary">Try Out the App</button>
        </a>
      </div>
    </div>
  );
}

export default Hero;
