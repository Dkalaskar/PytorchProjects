import React from 'react'
import "../style/Nav.css"

const Navbar = () => {
    return(
        <nav className='Navbar'>
        <ul className='Nav'>
        <li>
        <a href='/'>Home</a>
        </li>
        <li>
        <a href='/about'>About</a>
        </li>
        <li>
        <a href='/contct'>Contact</a>
        </li>

        </ul>
        

    </nav>
 );
};
export default Navbar;
