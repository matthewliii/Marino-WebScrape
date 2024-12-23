import React, { useState } from "react";
import { Box, Button, FormControl, InputLabel, MenuItem, Select, Typography } from "@mui/material";

const App = () => {
  const [location, setLocation] = useState("");
  const [day, setDay] = useState("");
  const [graphImage, setGraphImage] = useState(null);

  const locations = [
    "SquashBusters - 4th Floor",
    "Marino Center - Studio A",
    "Marino Center - Studio B",
    "Marino Center - 2nd Floor",
    "Marino Center - Gymnasium",
    "Marino Center - 3rd Floor Weight Room",
    "Marino Center - 3rd Floor Select & Cardio",
  ];

  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  const handleLocationChange = (event) => setLocation(event.target.value);
  const handleDayChange = (event) => setDay(event.target.value);

  const generateGraph = async () => {
    if (!location || !day) {
      alert("Please select both a location and a day.");
      return;
    }

    try {
      const response = await fetch(
        `https://marino-scrape-inio5.ondigitalocean.app/generate-graph?location=${encodeURIComponent(location)}&day=${encodeURIComponent(day)}`
      );

      const data = await response.json();

      if (response.ok) {
        setGraphImage(`data:image/png;base64,${data.graph}`);
      } else {
        alert(data.error);
      }
    } catch (error) {
      console.error("Error fetching graph:", error);
      alert("An error occurred while generating the graph. Please try again.");
    }
  };

  return (
    <Box sx={{ p: 4, maxWidth: 800, mx: "auto" }}>
      <Typography variant="h4" gutterBottom>
        Northeastern Campus Recreation Traffic Visualization
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
        <Select
          labelId="day-select-label"
          value={day}
          onChange={handleDayChange}
          label="Day"
        >
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
        size="large"
        onClick={generateGraph}
        sx={{ mb: 4, py: 2 }}
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
