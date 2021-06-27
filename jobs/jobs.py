from flask import Blueprint, g


bp = Blueprint("jobs", "jobs", url_prefix="/jobs")

@bp.route("/jobs")
def alljobs():
	cursor = g.db.cursor()\
	cursor.execute("SELECT title, company_name, jd_text FROM openings") # Query
	jobs = cursor.fetchall() # Get data
	return render_template("joblist.html", jobs=jobs) # Render
