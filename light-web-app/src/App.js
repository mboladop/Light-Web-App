import React, { Component } from 'react';
import logo from './logo.svg';
import Readings from './Readings';
import './App.css';




class App extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      months: [],
      cociente: 0.5,
    };
    
  }  
  
  componentDidMount(){
    const d = new Date();
    const n = d.getMonth()+1;
    const y = d.getFullYear();
    const prevArray = [{month:n,year:y}, {month:(n===1)?12:n-1, year:(n===1)? y-1:y}];
    this.setState({
      months: prevArray
    });
    
  }
  render() {
    
    return (
      <div className="App">
       
       <container>
         <h1>Light Web App</h1>
       </container>
       <hr/>
      
       <card>
       <h4>Mes en curso</h4>
       
       <p>{
        this.state.months && this.state.months.map((item)=>{
          return <Readings cociente = {this.state.cociente} month={item.month} year={item.year}/>;
        })
      }</p>
       </card>

       <hr/>

       <card>
       <h4>Graphs y Consumo</h4>
       </card>
      </div>
    );
  }
}

export default App;
