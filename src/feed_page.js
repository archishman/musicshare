import React from 'react';
import './bootstrap.css';
import NavBar from './navbar';

class Feed extends React.Component {
    render() {
        return (
        <main>
            <NavBar/>
            <div className = "container">
            <div className="card">
                <div className="card-body">
                  <h4 class="card-title">Feed</h4>
                  <h6 class="card-subtitle mb-2 text-muted">Here's the feed</h6>
                </div>
            </div>
            </div>
        </main>
        )
    }
}

export default Feed;