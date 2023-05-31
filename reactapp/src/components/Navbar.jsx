import React,{useState} from 'react'
import "../style/Nav.css"



const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);
  
    const handleToggle = () => {
      setIsOpen(!isOpen);
    };
  
    return (
      <nav className="navbar">
        <div className="navbar-logo">
          <h1>Logo</h1>
        </div>
        <div className={`navbar-links ${isOpen ? 'active' : ''}`}>
          <a href="/">Home</a>
          <a href="About">About</a>
          <a href="Model">Model</a>
          <a href="Contact">Contact</a>
        </div>
        <div className="navbar-toggle" onClick={handleToggle}>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </nav>
    );
  };
  
  export default Navbar;
