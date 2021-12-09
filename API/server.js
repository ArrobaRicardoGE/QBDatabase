/*jshint esversion: 6 */ 

// ---------------MSSQL ------------------------------
const configFileDB = require('./dbconfig');
const sql = require('mssql');

    async function getPool(){
        try{
            let pool = await sql.connect(configFileDB.config);
            //let ans = await pool.request().query("SELECT * FROM SuperBowl");
            //console.log(ans.recordsets[0][1]);
            console.log("Connectado a base de datos :)");
            return pool;
        }catch (error){
            console.log(error);
        }
    }

const dbConnection = getPool();


// -----------------------Express-----------------------
const express = require('express');
const path = require('path');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
    res.send("App running");
});


// Server setup
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});