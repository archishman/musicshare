import React from 'react';
import './bootstrap.css';
import NavBar from './navbar'

class Login extends React.Component {
  render() {
    return (
      <main>
        <NavBar/>
        <div className = "container">
            <div className="card">
                <div className="card-body">
                  <h4 class="card-title">Login</h4>
                  <h6 class="card-subtitle mb-2 text-muted">Through Spotify or Google</h6>
                </div>
            </div>
        </div>
      </main>
    )
  }
}

export default Login;