import React, { useState } from 'react';

function AgentForm({ feature }) {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const featureLabels = {
    email: { title: 'Email Content Input', placeholder: 'Enter email details (purpose, audience, tone)...' },
    blog: { title: 'Blog Topic Input', placeholder: 'Enter blog topic or URL to summarize...' },
    content_creator: { title: 'YouTube Video Topic', placeholder: 'Enter YouTube video topic (e.g. "10-minute beginner yoga routine")...' }
  };

  const current = featureLabels[feature] || { title: 'Input', placeholder: 'Enter input...' };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult('');
    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: feature,   // backend should handle "content_creator" type
          input
        }),
      });

      if (!response.ok) {
        const text = await response.text();
        throw new Error(`Server error: ${response.status} ${text}`);
      }

      const data = await response.json();
      // assume backend returns { result: "..." }
      setResult(data.result || JSON.stringify(data, null, 2));
    } catch (err) {
      setResult(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>{current.title}</h3>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="5"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={current.placeholder}
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </form>
      {result && (
        <div>
          <h4>Generated Output</h4>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default AgentForm;
