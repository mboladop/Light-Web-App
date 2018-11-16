import React, { Component } from 'react';
import logo from './logo.svg';
import Demo from './Demo.js';
import './App.css';
const dummy = [{title:'titleXX', reading:223}, {title:'title2', reading:898}, {title:'title3', reading:600}];
const months = [{month:11, year:2018},{month:10, year:2018}]
class App extends Component {
  render() {
    return (
      <div className="App">
       
       <container>
         <h1>Light Web App</h1>
       </container>
       <hr/>
      {
        // dummy.map((item)=>{
        //   return <Demo title={item.title} reading={item.reading} />;
        // })
      }
      {
        months.map((item)=>{
          return <Demo month={item.month} year={item.year} />;
        })
      }

       <card>
       <h4>Mes en curso</h4>
       <p>Reading:</p>
       </card>

       <hr/>
       <card>
       <h4>Mes anterior</h4>
       <p>Reading:</p>
       
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
