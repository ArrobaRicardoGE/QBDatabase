const queries = require("./queries");

async function QuarterbackID(sql, idQB, callback){
    let pool = new sql.Request()
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

module.exports = {QuarterbackID};