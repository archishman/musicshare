import React from 'react';
import './bootstrap.min.css';
import { Link } from "react-router-dom";

class NavBar extends React.Component {
    render() {
        return(
            <nav className="navbar bg-dark">
                <div className="container-fluid">
                    <div className="navbar-header">
                        <Link to="/" className="navbar-brand"> Home </Link>
                    </div>
                    <ul className="nav navbar-nav mr-auto">
                        <li className="active"><Link to="/feed/" className="nav-link">Feed</Link></li>
                    </ul>
                    <ul className="nav navbar-nav ml-auto">
                        <li className="active"><Link to="/login/" className="nav-link">Login</Link></li>
                    </ul>
                </div>
            </nav>
        )
    }
}


export default NavBar