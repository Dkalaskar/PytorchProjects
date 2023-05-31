import React from 'react'
import "../style/Nav.css"



const Navbar = () => {
    return(
        <nav className='Navbar'>
        <ul className='Nav'>
        <div className='home'>
        <li>
        <a href='/'>Home</a>
        </li>
        </div>
        <div className='about'>
        <li>
        <a href='/about'>About</a>
        </li>
        </div>
        <div className='contact'>
        <li>
        <a href='/contct'>Contact</a>
        </li>
        </div>

        </ul>
        

    </nav>
   
 );
};
export default Navbar;
