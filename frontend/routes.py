import flask

bp = flask.Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html", title="Inicio")


@bp.route("/quarterbacks", methods=["GET"])
def quarterbacks():
    return flask.render_template("quarterbacks.html", title="Quarterbacks")


@bp.route("/quarterbacks/<int:qbid>", methods=["GET"])
def quarterback_info(qbid):
    data = {
        "qbid": qbid,
        "name": "Randall" + " " + "Cunningham",
        "birth_date": "1970-01-01",
        "height": 192,
        "weight": 110,
        "headshot_url": "http://static.nfl.com/static/content/public/static/img/fantasy/transparent/200x200/MCN017517.png",
        "college_id": 45,
        "college_name": "Princeton",
        "teams": [
            {
                "key": "PHI",
                "name": "Philadelphia Eagles",
                "year": 1999,
                "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
            },
            {
                "key": "PHI",
                "name": "Philadelphia Eagles",
                "year": 2000,
                "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
            },
            {
                "key": "PHI",
                "name": "Philadelphia Eagles",
                "year": 2000,
                "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
            },
            {
                "key": "PHI",
                "name": "Philadelphia Eagles",
                "year": 2000,
                "logo_url": "https://static.www.nfl.com/league/api/clubs/logos/PHI.svg",
            },
        ],
    }
    return flask.render_template("qb_detail.html", title="Quarterbacks", data=data)


@bp.route("/teams", methods=["GET"])
def teams():
    return flask.render_template("teams.html", title="Equipos")


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
    return flask.render_template("colleges.html", title="Universidades")


@bp.route("/superbowls", methods=["GET"])
def superbowls():
    return flask.render_template("superbowls.html", title="Super Bowls")
