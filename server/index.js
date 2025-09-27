import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.post('/api/rewriter', async (req, res) => {
  const { email } = req.body;
  try {
    const response = await axios.post('http://localhost:5000/rewrite', { email });
    res.json({ result: response.data.result });
  } catch (error) {
    console.error('Error forwarding to agent:', error.message);
    res.status(500).json({ error: 'Something went wrong' });
  }
});

app.listen(8000, () => console.log('Server running on port 8000'));
