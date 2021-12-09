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
    let query = `SELECT DISTINCT qb.ID, qb.Nombre, qb.Apellido, qb.headshot_url
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
    FROM Equipo
    ORDER BY Clave;`;
    return query;
}

function Universidades(){
    let query = `SELECT ID, Nombre, Estado
    FROM Universidad
    ORDER BY ID;`;
    return query;
}

function IndivSB(edicion){
    let query = `SELECT sb.edicion edicion, sb.fecha feca, sb.estadio_sede estadio_sede, sb.ciudad_sede ciudad_sede, sb.marcador_local marcador_local, sb.marcador_visitante marcador_visitante,
    lc.clave clave_local, vis.clave clave_visitante, lc.nombre nombre_local, lc.ciudad ciudad_local, lc.logo_url logo_local,
    vis.nombre nombre_visitante, vis.ciudad ciudad_visitante, vis.logo_url logo_visitante
    FROM SuperBowl sb
    JOIN Equipo lc on lc.clave = sb.clave_local
    JOIN Equipo vis on vis.clave = sb.clave_visitante
    WHERE edicion = ${edicion};`;
    return query;
}

function IndivSBQB(anio, clave){
    let query = `SELECT qb.ID ID, qb.headshot_url headshot_url, qb.nombre Nombre, qb.apellido Apellido
    FROM Quarterback_Equipo tab
    JOIN Quarterback qb on qb.id = tab.id_quaterback
    WHERE anio = ${anio} and clave_equipo = '${clave}';`;
    return query;
}

function SuperBowl(){
    let query = `SELECT Edicion, Fecha FROM SuperBowl
    ORDER BY Edicion;`;
    return query;
}

function QBPorNombre(str){
    let query = `SELECT TOP 20 ID, headshot_url, Nombre, Apellido FROM Quarterback
    WHERE nombre + ' ' + apellido LIKE ('%${str}%');`;
    return query;
}



module.exports = {QuarterbackID, QuarterbackIDEquipos, QBPorEquipo, QBPorEquipoArray,
QBPorUniversidad, QBPorUniversidadArray, IndivEquipo, IndivEquipoSB, Equipos, Universidades,
IndivSB, IndivSBQB, SuperBowl, QBPorNombre};