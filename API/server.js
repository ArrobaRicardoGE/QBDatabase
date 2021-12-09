/*jshint esversion: 6 */ 

// ---------------MSSQL ------------------------------
const configFileDB = require('./dbconfig');
var sql = require('mssql');

    async function getPool(){
        try{
            let pool = await sql.connect(configFileDB.config);
            let ans = await pool.request().query("SELECT * FROM SuperBowl");
            //console.log(ans.recordsets[0][1]);
            console.log("Connectado a base de datos :)");
            return pool;
        }catch (error){
            console.log(error);
        }
    }

const pool = getPool();

// ------ misModulos ----
const peticiones = require('./peticiones.js');


// -----------------------Express-----------------------
const express = require('express');
var bodyParser = require('body-parser');
const path = require('path');
const app = express();
const port = 3001;
app.use(express.json());
app.use(express.urlencoded({ extended: false }));


app.get('/', (req, res) => {
    res.send("App running");
});


objetoPrueba = {
    nombre : " Juan",
    apellido: " Marroquin"
}

// Individual por QB
app.post('/QuarterbackID', (req, res) => {
    console.log(req.body.ID);
    peticiones.QuarterbackID(sql, req.body.ID, (result) => {
        res.json(result);
    }); 
});

// QB por equipo
app.post('/QuarterbackEquipo', (req, res) => {
    console.log(req.body.clave);
    peticiones.QuarterbackEquipo(sql, req.body.clave, (result) => {
        res.json(result);
    })
});

// QB por uni
app.post('/QuarterbackUniversidad', (req, res) => {
    console.log(req.body.IDUniversidad);
    peticiones.QuarterbackUniversidad(sql, req.body.IDUniversidad, (result) => {
        res.json(result);
    })
});


// Individual equipo
app.post('/EquipoClave', (req, res) => {
    console.log(req.body.clave);
    peticiones.EquipoClave(sql, req.body.clave, (result) => {
        res.json(result);
    });
});

// Equipos
app.post('/Equipos', (req, res) => {
    peticiones.Equipos(sql, (result) => {
        res.json(result);
    });
});

// Universidades
app.post('/Universidades', (req, res) => {
    peticiones.Universidades(sql, (result) => {
        res.json(result);
    });
});

// Individual SuperBowl
app.post('/SuperBowlEdicion', (req, res) => {
    console.log(req.body.edicion);
    peticiones.SuperBowlEdicion(sql, req.body.edicion, (result) => {
        res.json(result);
    })
});

// SuperBowl
app.post('/SuperBowl', (req, res) => {
    peticiones.SuperBowl(sql, (result) => {
        res.json(result);
    });
});

// QBs por nombre
app.post('/QuarterbackNombre', (req, res) => {
    console.log(req.body.nombreQuery);
    peticiones.QuarterbackNombre(sql, req.body.nombreQuery, (result) => {
        res.json(result);
    });
});

// Graifca de QBs por equipo
app.post('/GraficaQBEquipo', (req, res) => {
    res.json(objetoPrueba);
});

// Graifca de QBs por universidad
app.post('/GraficaQBUniversidad', (req, res) => {
    res.json(objetoPrueba);
});


// Server setup
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});