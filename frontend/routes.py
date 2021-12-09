import flask

bp = flask.Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html", title="Inicio")


@bp.route("/quarterbacks", methods=["GET"])
def quarterbacks():
    return flask.render_template("quarterbacks.html", title="Quarterbacks")


@bp.route("/teams", methods=["GET"])
def teams():
    return flask.render_template("teams.html", title="Teams")


@bp.route("/colleges", methods=["GET"])
def colleges():
    return flask.render_template("colleges.html", title="Universidades")


@bp.route("/superbowls", methods=["GET"])
def superbowls():
    return flask.render_template("superbowls.html", title="Super Bowls")
