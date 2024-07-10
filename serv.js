const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'tiger',
    database: 'dbs'
});

db.connect((err) => {
    if (err) {
        console.error('Failed to connect to MySQL:', err);
        return;
    }
    console.log('MySQL Connected');
});

//Author
app.post('/add_author', (req, res) => {
    const { id, name, nationality } = req.body;
    const sql = 'INSERT INTO Author (AuthorID, Name, Nationality) VALUES (?, ?, ?)';
    db.query(sql, [id, name, nationality], (err, result) => {
        
        console.log('Author added successfully');
        res.status(200).send('Author added successfully');
    });
});



app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});


