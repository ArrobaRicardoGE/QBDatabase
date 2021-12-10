# QBDatabase
Proyecto final de Bases de Datos I

## Para ejecutar

### API
- Instalar [Node.js](https://nodejs.org/)
- Cambiar al directorio API
- `npm install`
- Crear el archivo `dbconfig.js` con lo siguiente:
  ```js
  const config = {
      user: "[Usuario de base de datos]",
      password: "[Contraseña del usuario]",
      server: "127.0.0.1",
      database: "QuarterbackDB",
      port: 1433,
      options: {
          trustedconnection: true,
          enableArithAbort: true,
          instancename: "SQLEXPRESS",
          trustServerCertificate: true,
      },
  };

  module.exports = { config };
  ```
- `node server.js`

### Frontend
- Instalar [Python 3.8+](https://www.python.org/)
- Cambiar el directorio a frontend
- (Recomendado) Crear un entorno virutal: `python3 -m venv venv`.
- [Activar](https://docs.python.org/es/3/library/venv.html#:~:text=Comando%20para%20activar%20el%20entorno%20virtual) el entorno virtual.
- `python3 -m pip install -r requirements.txt`
- Configurar la variable de entorno
  - En bash: `export FLASK_APP=hello` 
  - En Windows CMD: `set FLASK_APP=hello` 
  - En Windows Powershell: `$env:FLASK_APP = "hello"`
- Cambiar al directorio raíz del proyecto
- `flask run`

La aplicación debería de correr en `localhost:5000`
