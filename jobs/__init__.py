from flask import Flask, g

def create_app():
	app = Flask("jobs")
	app.config.from_mapping(DATABASE="naukri")


	@app.route('/')
	def index():
		return "Hello World"

	return app
