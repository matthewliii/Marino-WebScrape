// import logo from './logo.svg';
// import './App.css';
// import * as React from 'react';
// import Box from '@mui/material/Box';
// import InputLabel from '@mui/material/InputLabel';
// import MenuItem from '@mui/material/MenuItem';
// import FormControl from '@mui/material/FormControl';
// import Button from '@mui/material/Button';
// import Select, { SelectChangeEvent } from '@mui/material/Select';

// function LocationSelect() {
//   const [age, setAge] = React.useState('');

//   const handleChange = (event) => {
//     setAge(event.target.value);
//   };

//   return (
//     <Box sx={{ minWidth: 120 }}>
//       <FormControl fullWidth>
//         <InputLabel id="demo-simple-select-label">Location</InputLabel>
//         <Select
//           labelId="demo-simple-select-label"
//           id="location"
//           value={age}
//           label="Location"
//           onChange={handleChange}
//         >
//           <MenuItem value={"SquashBusters - 4th Floor"}>SquashBusters - 4th Floor</MenuItem>
//           <MenuItem value={"Marino Center - Studio A"}>Marino Center - Studio A</MenuItem>
//           <MenuItem value={"Marino Center - Studio B"}>Marino Center - Studio B</MenuItem>
//           <MenuItem value={"Marino Center - 2nd Floor"}>Marino Center - 2nd Floor</MenuItem>
//           <MenuItem value={"Marino Center - Gymnasium"}>Marino Center - Gymnasium</MenuItem>
//           <MenuItem value={"Marino Center - 3rd Floor Weight Room"}>Marino Center - 3rd Floor Weight Room</MenuItem>
//           <MenuItem value={"Marino Center - 3rd Floor Select & Cardio"}>Marino Center - 3rd Floor Select & Cardio</MenuItem>
//         </Select>
//       </FormControl>
//     </Box>
//   );
// }

// function DaySelect() {
//   const [day, setDay] = React.useState('');

//   const handleChange = (event) => {
//     setDay(event.target.value);
//   };

//   return (
//     <Box sx={{ minWidth: 120 }}>
//       <FormControl fullWidth>
//         <InputLabel id="demo-simple-select-label">Day</InputLabel>
//         <Select
//           labelId="demo-simple-select-label"
//           id="day"
//           value={day}
//           label="Day"
//           onChange={handleChange}
//         >
//           <MenuItem value={"Monday"}>Monday</MenuItem>
//           <MenuItem value={"Tuesday"}>Tuesday</MenuItem>
//           <MenuItem value={"Wednesday"}>Wednesday</MenuItem>
//           <MenuItem value={"Thursday"}>Thursday</MenuItem>
//           <MenuItem value={"Friday"}>Friday</MenuItem>
//           <MenuItem value={"Saturday"}>Saturday</MenuItem>
//           <MenuItem value={"Sunday"}>Sunday</MenuItem>
//         </Select>
//       </FormControl>
//     </Box>
//   );
// }

// // handles the api call and logic with the data from the two select elements
// function View() {

// }

// function App() {
//   return (
//     <div className="Container">
//       <div className="App">
//         <LocationSelect/>
//         <DaySelect/>
//         <Button variant="contained">View</Button>
//       </div>
//       <div className="ImageContainer">
        
//       </div>
//     </div>
//   );
// }

// export default App;


import React, { useState } from "react";
import { Box, Button, FormControl, InputLabel, MenuItem, Select, Typography } from "@mui/material";

const App = () => {
  const [location, setLocation] = useState("");
  const [day, setDay] = useState("");
  const [graphImage, setGraphImage] = useState(null);

  const locations = ["SquashBusters - 4th Floor", "Marino Center - Studio A", "Marino Center - Studio B", "Marino Center - 2nd Floor", "Marino Center - Gymnasium", "Marino Center - 3rd Floor Weight Room", "Marino Center - 3rd Floor Select & Cardio"];
  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  const handleLocationChange = (event) => setLocation(event.target.value);
  const handleDayChange = (event) => setDay(event.target.value);

  const generateGraph = async () => {
    if (!location || !day) {
      alert("Please select both Location and Day!");
      return;
    }

    try {
      const response = await fetch(
        `http://192.168.104.104:3000/generate-graph?location=${location}&day=${day}`
      );
      const data = await response.json();

      if (response.ok) {
        setGraphImage(`data:image/png;base64,${data.graph}`);
      } else {
        alert(data.error);
      }
    } catch (error) {
      console.error("Error fetching graph:", error);
    }
  };

  return (
    <Box sx={{ p: 4, maxWidth: 600, mx: "auto" }}>
      <Typography variant="h4" gutterBottom>
        Graph Generator
      </Typography>

      {/* Location Dropdown */}
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="location-select-label">Location</InputLabel>
        <Select
          labelId="location-select-label"
          value={location}
          onChange={handleLocationChange}
          label="Location"
        >
          {locations.map((loc) => (
            <MenuItem key={loc} value={loc}>
              {loc}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      {/* Day Dropdown */}
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="day-select-label">Day</InputLabel>
        <Select labelId="day-select-label" value={day} onChange={handleDayChange} label="Day">
          {days.map((d) => (
            <MenuItem key={d} value={d}>
              {d}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      {/* Generate Button */}
      <Button
        variant="contained"
        color="primary"
        fullWidth
        onClick={generateGraph}
        sx={{ mb: 4 }}
      >
        Generate Graph
      </Button>

      {/* Display Graph */}
      {graphImage && (
        <Box sx={{ mt: 4, textAlign: "center" }}>
          <img src={graphImage} alt="Generated Graph" style={{ maxWidth: "100%" }} />
        </Box>
      )}
    </Box>
  );
};

export default App;
