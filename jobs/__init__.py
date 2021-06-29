import random
from flask import Flask, render_template, g

def create_app():
	app = Flask("jobs")
	app.config.from_mapping(DATABASE="naukri")

	from . import jobs
	app.register_blueprint(jobs.bp)

	from .  import db
	db.init_app(app)

	@app.route("/")
	def index():
		quotes = [["Imagination is more important than knowledge.", "Albert Einstein"],["It does not matter how slowly you go as long as you do not stop", "Confucius"],["All our dreams can come true, if we have the courage to pursue them", "Walt Disney"],["I never dreamed about success, I worked for it", "Estee lauder"],["Difficulties in your life do not come to destroy you but to help you realise your hidden potential and power. Let difficulties know that you too are difficult", "APJ Abdul Kalam"],["My favorite things in life don't cost any money. It's really clear that the most precious resource we all have is time.", "Steve Jobs"],["There is nothing more powerful in the world than the idea that came in time", "Victor Hugo"],["When we close ourselves off, we're not just closing ourselves off to other people, we're closing ourselves off from ourselves and impeding ourselves. When you open up, you allow yourself to be who you are.", "Amy Cuddy"],["We are what we repeatedly do. Excellence, then, is not an act, but a habit", "Aristotle"],["Never bend your head. Always hold it high. Look the world straight in the eye. ", "Helen Keller"],["Begin to be now what you will be hereafter", "William James"],["Nothing is impossible, the word itself says ,' I'm possible", "Audrey Hepburn"],["Setting goals is the first step in turning the invisible into the visible.", "Tony Robbins"],["You cant give up! When you give up, you are like everybody else!", "Chris Evert"],["He can who thinks he can, and he can't who thinks he can't. This is an inexorable, indisputable law.", "Pablo Picasso"]]
		
	return app
