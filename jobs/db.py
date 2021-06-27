import psycopg2

from flask import current_app, g


def get_db():

	if 'db' not in g:
		dbname = current_app.config['DATABASE']
		g.db = psycopg2.connect(f"dbname = {dbname}")
	return g.db
