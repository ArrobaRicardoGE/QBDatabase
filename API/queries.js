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

function QBPorEquipo(Clave){
    let query = `SELECT Nombre, Ciudad, logo_url FROM Equipo
    WHERE clave = '${Clave}';`
    return query;
}

function QBPorEquipoArray(Clave){
    let query = `SELECT qb.ID, qb.Nombre, qb.Apellido, qb.headshot_url
    FROM Quarterback_Equipo tab
    JOIN Quarterback qb on tab.id_quaterback = qb.id
    WHERE tab.clave_equipo = '${Clave}';`
    return query;
}

function QBPorUniversidad(ID){
    let query = `SELECT nombre, estado FROM Universidad
    WHERE id = ${ID};`
    return query;
}

function QBPorUniversidadArray(ID){
    let query = `SELECT id, headshot_url, Nombre, Apellido
    FROM Quarterback
    WHERE id_universidad = ${ID};`
    return query;
}

function IndivEquipo(Clave){
    let query = `SELECT clave, nombre, ciudad, division, conferencia, logo_url
    FROM Equipo
    WHERE clave = '${Clave}';`
    return query;
}

function IndivEquipoSB(Clave){
    let query = `SELECT edicion FROM SuperBowl
    WHERE clave_local = '${Clave}' OR clave_visitante= '${Clave}';`
    return query;
}

function Equipos(){
    let query = `SELECT Clave, Nombre, Ciudad, logo_url
    FROM Equipo;`;
    return query;
}


module.exports = {QuarterbackID, QuarterbackIDEquipos, QBPorEquipo, QBPorEquipoArray,
QBPorUniversidad, QBPorUniversidadArray, IndivEquipo, IndivEquipoSB, Equipos};