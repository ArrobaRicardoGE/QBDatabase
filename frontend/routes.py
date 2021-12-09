import flask
import requests

bp = flask.Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    r = requests.post("http://localhost:3001/GraficaQBEquipo")
    raw_team_data = r.json()
    r = requests.post("http://localhost:3001/GraficaQBUniversidad")
    raw_college_data = r.json()[:7] + r.json()[9:22]
    data = {
        "teams": {
            "label": [record["nombre"] for record in raw_team_data],
            "data": [record["cantidad"] for record in raw_team_data],
        },
        "college": {
            "label": [record["Nombre"] for record in raw_college_data],
            "data": [record["cantidad"] for record in raw_college_data],
        },
    }
    return flask.render_template("index.html", title="Inicio", data=data)


@bp.route("/quarterbacks", methods=["GET"])
def quarterbacks():
    data = {
        "query": flask.request.args.get("q"),
        "quarterbacks": [
            {
                "qbid": 13,
                "headshot_url": "http://static.nfl.com/static/content/public/static/img/fantasy/transparent/200x200/MCN017517.png",
                "name": "Carson Wentz",
            },
            {
                "qbid": 14,
                "headshot_url": "http://static.nfl.com/static/content/public/static/img/fantasy/transparent/200x200/MCN017517.png",
                "name": "Nick Foles",
            },
        ],
    }
    return flask.render_template("quarterbacks.html", title="Quarterbacks", data=data)


@bp.route("/quarterbacks/<int:qbid>", methods=["GET"])
def quarterback_info(qbid):
    r = requests.post(
        flask.current_app.config["API_URL"] + "/QuarterbackID", data={"ID": qbid}
    )
    raw_data = r.json()
    data = None
    if len(raw_data) > 1:
        data = {
            "qbid": raw_data["id_QB"],
            "name": raw_data["nombre_QB"] + " " + raw_data["apellido"],
            "birth_date": raw_data["fecha_nacimiento"][
                :10
            ],  # TODO: sacar cuenta de la edad
            "height": f'{raw_data["estatura"] * 2.54 :.2f}',
            "weight": f'{raw_data["peso"] / 2.205 :.2f}',
            "headshot_url": raw_data["headshot_url"],
            "college_id": raw_data["id_universidad"],
            "college_name": raw_data["nombre_Universidad"],
            "teams": [
                {
                    "key": team["clave"],
                    "name": team["ciudad"] + " " + team["nombre_equipo"],
                    "year": team["anio"],
                    "logo_url": team["logo_url"],
                }
                for team in raw_data["equipos"]
            ],
        }
    return flask.render_template(
        "quarterback_detail.html", title="Quarterbacks", data=data
    )


@bp.route("/teams", methods=["GET"])
def teams():
    data = [
        {
            "key": "PHI",
            "name": "Philadelphia Eagles",
            "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
        },
        {
            "key": "BUF",
            "name": "Buffalo Bills",
            "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/BUF.svg",
        },
    ]
    return flask.render_template("teams.html", title="Equipos", data=data)


@bp.route("/teams/<string:key>", methods=["GET"])
def team_info(key):
    r = requests.post("http://localhost:3001/EquipoClave", data={"clave": key})
    raw_data = r.json()
    r = requests.post("http://localhost:3001/QuarterbackEquipo", data={"clave": key})
    qb_data = r.json()["jugadores"]
    data = None
    if len(raw_data) > 1:
        data = {
            "key": raw_data["clave"],
            "name": raw_data["ciudad"] + " " + raw_data["nombre"],
            "conference": raw_data["conferencia"],
            "division": raw_data["division"],
            "logo_url": raw_data["logo_url"],
            "quarterbacks": [
                {
                    "qbid": qb["ID"],
                    "name": qb["Nombre"] + " " + qb["Apellido"],
                    "headshot_url": qb["headshot_url"],
                }
                for qb in qb_data
            ],
            "superbowls": [sb["edicion"] for sb in raw_data["SuperBowls"]],
        }
    return flask.render_template("team_detail.html", title="Equipos", data=data)


@bp.route("/colleges", methods=["GET"])
def colleges():
    data = [
        {"id": 123, "name": "LSU"},
        {"id": 123, "name": "Notre Dame"},
    ]
    return flask.render_template("colleges.html", title="Universidades", data=data)


@bp.route("/colleges/<int:college_id>", methods=["GET"])
def college_info(college_id):
    r = requests.post(
        "http://localhost:3001/QuarterbackUniversidad",
        data={"IDUniversidad": college_id},
    )
    raw_data = r.json()
    data = None
    if len(raw_data) > 1:
        data = {
            "college_id": college_id,
            "name": raw_data["nombre"],
            "state": raw_data["estado"],
            "quarterbacks": [
                {
                    "qbid": qb["id"],
                    "headshot_url": qb["headshot_url"],
                    "name": qb["Nombre"] + " " + qb["Apellido"],
                }
                for qb in raw_data["jugadores"]
            ],
        }
    return flask.render_template(
        "college_detail.html", title="Universidades", data=data
    )


@bp.route("/superbowls", methods=["GET"])
def superbowls():
    data = [
        {
            "edition": 51,
            "date": "2017-02-01",
        },
        {
            "edition": 52,
            "date": "2018-02-02",
        },
    ]
    return flask.render_template("superbowls.html", title="Super Bowls", data=data)


@bp.route("/superbowls/<int:edition>", methods=["GET"])
def superbowl_info(edition):
    r = requests.post(
        "http://localhost:3001/SuperBowlEdicion", data={"edicion": edition}
    )
    data = None
    if r.text != "":
        raw_data = r.json()
        data = {
            "edition": raw_data["edicion"],
            "date": raw_data["feca"][:10],
            "stadium": raw_data["estadio_sede"],
            "city": raw_data["ciudad_sede"],
            "home": {
                "key": raw_data["clave_local"],
                "name": raw_data["ciudad_local"] + " " + raw_data["nombre_local"],
                "logo_url": raw_data["logo_local"],
                "score": raw_data["marcador_local"],
            },
            "away": {
                "key": raw_data["clave_visitante"],
                "name": raw_data["ciudad_visitante"]
                + " "
                + raw_data["nombre_visitante"],
                "logo_url": raw_data["logo_visitante"],
                "score": raw_data["marcador_visitante"],
            },
            "quarterbacks_home": [
                {
                    "qbid": qb["ID"],
                    "headshot_url": qb["headshot_url"],
                    "name": qb["Nombre"] + " " + qb["Apellido"],
                }
                for qb in raw_data["qb_locales"]
            ],
            "quarterbacks_away": [
                {
                    "qbid": qb["ID"],
                    "headshot_url": qb["headshot_url"],
                    "name": qb["Nombre"] + " " + qb["Apellido"],
                }
                for qb in raw_data["qb_visitantes"]
            ],
        }
    return flask.render_template(
        "superbowl_detail.html", title="Super Bowls", data=data
    )
