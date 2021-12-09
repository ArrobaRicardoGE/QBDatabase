function QuarterbackID(IDQuarterBack){
    let query = `SELECT qb.id id_QB, qb.nombre nombre_QB, qb.apellido, qb.fecha_nacimiento, qb.estatura, qb.peso, qb.headshot_url, U.ID id_universidad, U.nombre nombre_Universidad
    FROM Quarterback qb
    JOIN Universidad U on qb.id_universidad = U.id
    WHERE qb.id = ${IDQuarterBack};`
    return query;
}

function QuarterbackIDEquipos(ID){
    let query = `SELECT e.clave, e.nombre nombre_equipo, e.ciudad, e.logo_url, tab.anio
    FROM Quarterback_Equipo tab
    JOIN Equipo e on tab.clave_equipo = E.clave
    WHERE tab.id_quaterback = ${ID};`
    return query;
}

QuarterbackID

module.exports = {QuarterbackID, QuarterbackIDEquipos};