from flask import Blueprint, g
from . import db

bp = Blueprint("jobs", "jobs", url_prefix="/jobs")

@bp.route("/")
def alljobs():
	conn = db.get_db()
	cursor = conn.cursor()
	cursor.execute("SELECT title, company_name, jd_text FROM openings") # Query
	jobs = cursor.fetchall() # Get data
	return render_template("jobs/jobslist.html", jobs=jobs) # Render
