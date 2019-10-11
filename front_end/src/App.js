// App.js
import React, { Component, Fragment } from 'react';

class App extends Component {

  state = {
    menitems: [],
  };
  
  sortNumbersAsc(attr) {
    this.setState(prevState => (
      this.state.menitems.sort((a, b) => (a[attr] - b[attr]))
  ));
  }

  sortNumbersDesc(attr) {
    this.setState(prevState => (
      this.state.menitems.sort((a, b) => (b[attr] - a[attr]))
  ));
  }
  
  sortStringsAsc(attr) {
    this.setState(prevState => (
      this.state.menitems.sort((a, b) => (a[attr].localeCompare(b[attr])))
  ));
  }

  sortStringsDesc(attr) {
    this.setState(prevState => (
      this.state.menitems.sort((a, b) => (b[attr].localeCompare(a[attr])))
  ));
  }  
  
  sortRows(event) {
    var order = event.target.getAttribute('data-order');
    var attr = event.target.textContent.toLowerCase();
    
    if (order === "ASC") {
      event.target.setAttribute("data-order", "DESC");
      if (order === "price") {
        this.sortNumbersAsc(attr);
      } else { 
        this.sortStringsAsc(attr);
      }
    } else { 
      event.target.setAttribute("data-order", "ASC");
      if (order === "price") {
        this.sortNumbersDesc(attr);
      } else { 
        this.sortStringsDesc(attr);
      }      
    }    
  }  
  
  async doSearch(event) {
    event.preventDefault();
    var txt = document.getElementById('searchText').value;
    const res = await fetch('http://127.0.0.1:8000/api/menu/?search='+txt);
    const menitems = await res.json();
    this.setState({
      menitems,
    });
  }  
  
  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/menu/');
      const menitems = await res.json();
      this.setState({
        menitems,
      });
      this.sortNumbersAsc = this.sortNumbersAsc.bind(this);
      this.sortNumbersDesc = this.sortNumbersDesc.bind(this);
      this.sortStringsAsc = this.sortStringsAsc.bind(this);
      this.sortStringsDesc = this.sortStringsDesc.bind(this);      
      this.doSearch = this.doSearch.bind(this); 
    } catch (e) {
      console.log(e);
    }
  }


render() {
  return (
     <Fragment>
     <div>
     <form>
       <input type="text" placeholder="Search.." name="search" id="searchText"/>
       <button type="submit" onClick={(e) => this.doSearch(e)} >
        <i className="fa fa-search"></i>
       </button>
     </form>
    </div>  
    <table>
      <thead>
        <tr>
          <th>
            <a onClick={(e) => this.sortRows(e)} data-order="ASC">
              Name
            </a>
          </th>
          <th>
            <a onClick={(e) => this.sortRows(e)} data-order="ASC">
              Price
            </a>
          </th>
        </tr>
      </thead>
      <tbody>
      {this.state.menitems.map(item => (
        <tr key={item.id}>
          <td>{item.name}</td>
          <td>{item.price}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </Fragment>
  );
}
}

export default App;