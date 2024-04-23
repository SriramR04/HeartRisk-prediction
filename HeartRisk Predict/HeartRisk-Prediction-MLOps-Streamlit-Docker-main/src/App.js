import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    age: '',
    height: '',
    weight: '',
    gender: '',
    duration: '',
    heartRate: '',
    bodyTemp: '',
    prediction: null,
    error: null,
  };

  handleChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const { age, height, weight, gender, duration, heartRate, bodyTemp } = this.state;
  
    axios.post("http://127.0.0.1:8000", {
        age,
        height,
        weight,
        gender,
        duration,
        heartRate,
        bodyTemp
      })
      .then((response) => {
        this.setState({ prediction: response.data.prediction, error: null });
      })
      .catch((error) => {
        console.error('Error:', error);
        this.setState({ error: 'An error occurred while processing your request.' });
      });
  };
  
  render() {
    const { age, height, weight, gender, duration, heartRate, bodyTemp, prediction, error } = this.state;

    return (
      <div>
        <h1>Calories Prediction</h1>
        <form onSubmit={this.handleSubmit}>
          <div>
            <label>Age:</label>
            <input type="number" name="age" value={age} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Height:</label>
            <input type="number" name="height" value={height} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Weight:</label>
            <input type="number" name="weight" value={weight} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Gender:</label>
            <input type="text" name="gender" value={gender} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Duration:</label>
            <input type="number" name="duration" value={duration} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Heart Rate:</label>
            <input type="number" name="heartRate" value={heartRate} onChange={this.handleChange} required />
          </div>
          <div>
            <label>Body Temperature:</label>
            <input type="number" name="bodyTemp" value={bodyTemp} onChange={this.handleChange} required />
          </div>
          <button type="submit">Predict</button>
        </form>
        {prediction !== null && (
          <div>
            <h2>Prediction:</h2>
            <p>{prediction}</p>
          </div>
        )}
        {error && <div>Error: {error}</div>}
      </div>
    );
  }
}

export default App;
