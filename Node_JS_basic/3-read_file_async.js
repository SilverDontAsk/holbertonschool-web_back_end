const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      lines.shift();
      const students = {};
      let totalStudents = 0;
      let red = '';

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!firstname || !field) {
          return;
        }

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        totalStudents += 1;
      });

      red += `Number of students: ${totalStudents}\n`;
      for (const field in students) {
        if (Object.prototype.hasOwnProperty.call(students, field)) {
          const studentList = students[field];
          red += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
        }
      }
      resolve(red);
    });
  });
}

module.exports = countStudents;
