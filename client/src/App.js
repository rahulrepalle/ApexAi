import React, { useState } from 'react';
import './App.css';
import FeatureSelector from './components/FeatureSelector';
import AgentForm from './components/AgentForm';

function App() {
  const [selectedFeature, setSelectedFeature] = useState(null);

  return (
    <div className="App">
      <h1>AI Assistant</h1>
      <FeatureSelector onSelect={setSelectedFeature} />
      {selectedFeature && <AgentForm feature={selectedFeature} />}
    </div>
  );
}

export default App;
