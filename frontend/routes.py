import flask
import requests

bp = flask.Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    data = {
        "teams": {
            "label": ["PHI", "AZ"],
            "data": [1, 2],
        },
        "college": {
            "label": ["LSU", "STL"],
            "data": [1, 2],
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
    data = {
        "key": key,
        "name": "Philadelphia Eagles",
        "conference": "NFC",
        "division": "East",
        "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
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
        "superbowls": [52],
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
    data = {
        "college_id": college_id,
        "name": "LSU",
        "state": "Lousiana",
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
    data = {
        "edition": edition,
        "date": "2018-02-07",
        "stadium": "El de los Vikings",
        "city": "Mineapolis",
        "home": {
            "key": "PHI",
            "name": "Philadelphia Eagles",
            "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
            "score": 41,
        },
        "away": {
            "key": "NE",
            "name": "New England Patriots",
            "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/NE.svg",
            "score": 33,
        },
        "quarterbacks_home": [
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
        "quarterbacks_away": [
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
    return flask.render_template(
        "superbowl_detail.html", title="Super Bowls", data=data
    )
