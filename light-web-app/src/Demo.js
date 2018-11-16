
import React, { Component } from 'react';
import './Demo.css';
class Demo extends Component {

    render() {
        return (
            <div className={(this.props.reading>500?'higher':'lower')}>
                <p>{this.props.month} - {this.props.year}</p>
            </div>
        );
    }

}

export default Demo;