import os
from flask import Flask, jsonify, send_file
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.database import db
from app.serializer import ma
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import app_config


def create_app():

	app = Flask(__name__)
	api = Api(app)
	config_name = os.getenv("APP_SETTINGS")
	app.config['CORS_HEADERS'] = 'Content-Type'

	
	cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
	app.config.from_object(app_config[config_name])

	jwt = JWTManager(app)

	

	@jwt.user_claims_loader
	def add_claims_to_jwt(identity):

		#TODO: change condition to check if user is admin
		if identity == 1 : #instead of hard-coding, read from a config or database
			return { 'is_admin': True }
		return { 'is_admin': False }


	@jwt.token_in_blacklist_loader
	def check_if_token_in_blacklist(decrypted_token):
		from app.security import TokenBlacklist

		return decrypted_token['jti'] in TokenBlacklist.get_all()

	@jwt.expired_token_loader
	def expired_token_callback():

		return jsonify({
		'description': 'The token has expired',
		'error': 'token_expired'
		}), 401

	@jwt.invalid_token_loader
	def invalid_token_callback(error):
		return jsonify({
		'description': 'Signature verification failed.',
		'error': 'invalid_token'
		}), 401

	@jwt.unauthorized_loader
	def missing_token_callback(error):
		return jsonify({
		'description': 'Request does not contain an access token.',
		'error': 'authorization_required'
		}), 401

	@jwt.needs_fresh_token_loader
	def token_not_fresh_callback():
		return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    	}), 401


	@jwt.revoked_token_loader
	def revoked_token_callback():
		return jsonify({
        'description': 'The token has been revoked.',
        'error': 'token_revoked'
    	}), 401
	
	@app.route("/plot/<string:filename>")
	def getPlot(filename):

		return send_file("static/plots/{}.png".format(filename))
	
	@app.route("/placeholder")
	def placeholder():
		return send_file("static/plots/placeholder.png")
		

	## import area für resource
	from app.api.qrk.resources import QrkApi, QrkListApi, MesswertApi, MesswertListApi
	api.add_resource(QrkListApi, "/api/v1/qrk")
	api.add_resource(QrkApi, "/api/v1/qrk/<string:qrk_id>")
	api.add_resource(MesswertListApi, "/api/v1/qrk/<string:qrk_id>/messwert")
	api.add_resource(MesswertApi, "/api/v1/qrk/<string:qrk_id>/messwert/<string:messwert_id>" )
	
	

	db.init_app(app)
	migrate = Migrate(app, db)
	ma.init_app(app)

	return app
