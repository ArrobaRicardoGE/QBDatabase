const queries = require("./queries");

async function QuarterbackID(sql, idQB, callback){
    let pool = new sql.Request();
    let ans = await pool.query(queries.QuarterbackID(idQB));

    pool = new sql.Request();
    let ans2 = await pool.query(queries.QuarterbackIDEquipos(idQB));
    ans = ans.recordsets[0][0];
    ans2 = ans2.recordsets[0];

    resultado = {
        ...ans,
        equipos : ans2
    }

    callback(resultado);
}

async function QuarterbackEquipo(sql, clave, callback){
    let pool = new sql.Request();
    let infoEquipo = await pool.query(queries.QBPorEquipo(clave));

    pool = new sql.Request();
    let arrayPlayers = await pool.query(queries.QBPorEquipoArray(clave));

    infoEquipo = infoEquipo.recordsets[0][0];
    arrayPlayers = arrayPlayers.recordsets[0];

    resultado = {
        ...infoEquipo,
        jugadores : arrayPlayers
    }

    callback(resultado);
}

async function QuarterbackUniversidad(sql, id, callback){
    let pool = new sql.Request();
    let infoUni = await pool.query(queries.QBPorUniversidad(id));

    pool = new sql.Request();
    let arrayPlayers = await pool.query(queries.QBPorUniversidadArray(id));

    infoUni = infoUni.recordsets[0][0];
    arrayPlayers = arrayPlayers.recordsets[0];

    resultado = {
        ...infoUni,
        jugadores : arrayPlayers
    }
    callback(resultado);
}

async function EquipoClave(sql, clave, callback){
    let pool = new sql.Request();
    let infoEquipo = await pool.query(queries.IndivEquipo(clave));
    infoEquipo = infoEquipo.recordsets[0][0];

    pool = new sql.Request();
    let arraySB = await pool.query(queries.IndivEquipoSB(clave));
    arraySB = arraySB.recordsets[0];

    resultado = {
        ...infoEquipo,
        SuperBowls : arraySB
    }
    callback(resultado);

}

async function Equipos(sql, callback){
    let pool = new sql.Request();
    let equipos = await pool.query(queries.Equipos());
    equipos = equipos.recordsets[0];

    callback(equipos);
    
}


module.exports = {QuarterbackID, QuarterbackEquipo, QuarterbackUniversidad, EquipoClave, Equipos};