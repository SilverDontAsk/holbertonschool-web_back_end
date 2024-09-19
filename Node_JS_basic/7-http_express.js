const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  const dbpath = process.argv[2];
  if (!dbpath) {
    res.send('Cannot load the database');
    return;
  }
  try {
    let o = 'This is the list of our students\n';
    const studentsData = await countStudents(dbpath);
    o += studentsData;
    res.send(o);
  } catch (error) {
    res.send('Cannot load the database');
  }
});

app.listen(1245, () => {
  console.log('Express server is listening on port 1245');
});

module.exports = app;
