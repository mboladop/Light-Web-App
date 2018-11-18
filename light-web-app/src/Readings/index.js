import React, { Component } from 'react';
import './style.css';


class Readings extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          data: [],
          consumo: 0
        };
      }
        
      componentDidMount() {
        fetch('http://127.0.0.1:5000/getreadings/'+this.props.year+'/'+this.props.month)
          .then(response => response.json())
          .then(data => this.averageReading(data))
          .then(data => this.setState({ data }));

      }

      averageReading(data){
        
        const counters = [];
        data.map((item)=>{
            counters.push(item.counter);
        })
        
        counters.sort();
       
        const average = counters[counters.length-1] - counters[0];
        
        this.setState({
            consumo: average * this.props.cociente
        });
        
        return data;
    }
    render() {
        console.log(this.state.data);
        
        return (
            <div className={(this.props.reading>500?'higher':'lower')}>
                <p>{this.props.month} - {this.props.year} //{this.state.consumo}</p>
                {this.state.data && this.state.data.map((item)=>{
          return <p>{item.counter}</p>;
        })}
            </div>
        );
    }

}

export default Readings;