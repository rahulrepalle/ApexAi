import React from 'react';

function FeatureSelector({ onSelect }) {
  return (
    <div>
      <h2>Select a Feature</h2>
      <button onClick={() => onSelect('email')}>Professional Email Writer</button>
      <button onClick={() => onSelect('blog')}>Blog Post Summarizer</button>
      <button onClick={() => onSelect('content_creator')}>Content Creator (YouTube)</button>
    </div>
  );
}

export default FeatureSelector;
