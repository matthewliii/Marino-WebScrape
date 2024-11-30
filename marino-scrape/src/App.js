import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Button from '@mui/material/Button';
import Select, { SelectChangeEvent } from '@mui/material/Select';

function LocationSelect() {
  const [age, setAge] = React.useState('');

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Location</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="location"
          value={age}
          label="Location"
          onChange={handleChange}
        >
          <MenuItem value={"SquashBusters - 4th Floor"}>SquashBusters - 4th Floor</MenuItem>
          <MenuItem value={"Marino Center - Studio A"}>Marino Center - Studio A</MenuItem>
          <MenuItem value={"Marino Center - Studio B"}>Marino Center - Studio B</MenuItem>
          <MenuItem value={"Marino Center - 2nd Floor"}>Marino Center - 2nd Floor</MenuItem>
          <MenuItem value={"Marino Center - Gymnasium"}>Marino Center - Gymnasium</MenuItem>
          <MenuItem value={"Marino Center - 3rd Floor Weight Room"}>Marino Center - 3rd Floor Weight Room</MenuItem>
          <MenuItem value={"Marino Center - 3rd Floor Select & Cardio"}>Marino Center - 3rd Floor Select & Cardio</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}

function DaySelect() {
  const [day, setDay] = React.useState('');

  const handleChange = (event) => {
    setDay(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Day</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="day"
          value={day}
          label="Day"
          onChange={handleChange}
        >
          <MenuItem value={"Monday"}>Monday</MenuItem>
          <MenuItem value={"Tuesday"}>Tuesday</MenuItem>
          <MenuItem value={"Wednesday"}>Wednesday</MenuItem>
          <MenuItem value={"Thursday"}>Thursday</MenuItem>
          <MenuItem value={"Friday"}>Friday</MenuItem>
          <MenuItem value={"Saturday"}>Saturday</MenuItem>
          <MenuItem value={"Sunday"}>Sunday</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}

// handles the api call and logic with the data from the two select elements
function View() {

}

function App() {
  return (
    <div className="Container">
      <div className="App">
        <LocationSelect/>
        <DaySelect/>
        <Button variant="contained">View</Button>
      </div>
      <div className="ImageContainer">
        
      </div>
    </div>
  );
}

export default App;
