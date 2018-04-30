import axios from 'axios';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            values: [],
            addValueText: ''
        };
        this.getValues = this.getValues.bind(this);
        this.addValue = this.addValue.bind(this);
        this.handleAddValueTextChange = this.handleAddValueTextChange.bind(this);
    }

    componentDidMount() {
        this.getValues()
    }

    getValues() {
        axios.get('/get_values').then(response => {
            this.setState(() => {
                return {
                    values: response.data.values,
                    addValueText: ''
                }
            });
        })
        .catch((error) => {
            console.log(error);
        });
    }

    addValue() {
        let requestData = {value: this.state.addValueText};
        axios.post('/add_value', requestData).then(response => {
            if (response.data.status === 'ok') {
                this.getValues();
            }
        })
        .catch((error) => {
            console.log(error);
        });
    }

    handleAddValueTextChange(e) {
        let text = e.target.value;
        this.setState(() => {
            return {
                addValueText: text
            }
        });
    }

    render() {
        let values = this.state.values.map((value, index) => {
            return (
                <tr key={index}>
                    <td className="App-intro">{value.id}</td>
                    <td className="App-intro">{value.created_at}</td>
                    <td className="App-intro">{value.value}</td>
                </tr>
            );
        });
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">Table of values</h1>
                </header>
                <table align="center" border="1px">
                    <th>
                        id
                    </th>
                    <th>
                        created date
                    </th>
                    <th>
                        value
                    </th>
                    {values}
                </table>
                <br/>
                <input
                    value={this.state.addValueText}
                    type="text"
                    placeholder="Enter value to add"
                    onChange={this.handleAddValueTextChange}
                />
                <button onClick={this.addValue}>Add value</button>
            </div>
        );
    }
}

export default App;
