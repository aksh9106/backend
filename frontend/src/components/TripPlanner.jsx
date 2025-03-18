import React, { useState } from 'react';
import { MapContainer, TileLayer, Polyline, Marker } from 'react-leaflet';
import LogSheet from './LogSheet';
import './TripPlanner.css';

const TripPlanner = () => {
  const [tripDetails, setTripDetails] = useState({
    currentLocation: '',
    pickupLocation: '',
    dropoffLocation: '',
    currentCycleHours: 0
  });

  const [routeData, setRouteData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/trips/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(tripDetails)
      });
      const data = await response.json();
      setRouteData(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="trip-planner">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Current Location:</label>
          <input
            type="text"
            value={tripDetails.currentLocation}
            onChange={(e) => setTripDetails({
              ...tripDetails,
              currentLocation: e.target.value
            })}
          />
        </div>
        {/* Similar input groups for other fields */}
        <button type="submit">Calculate Route</button>
      </form>

      {routeData && (
        <div className="results">
          <div className="map-container">
            <MapContainer center={[39.8283, -98.5795]} zoom={4}>
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; OpenStreetMap contributors'
              />
              {/* Add route polyline and markers */}
            </MapContainer>
          </div>
          <div className="log-sheets">
            {routeData.log_entries.map((log, index) => (
              <LogSheet key={index} logData={log} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default TripPlanner;