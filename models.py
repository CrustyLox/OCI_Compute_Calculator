from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oci_shapes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ShapePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shape_name = db.Column(db.String, unique=True, nullable=False)
    cpu_part_number = db.Column(db.String, nullable=True)
    ram_part_number = db.Column(db.String, nullable=True)
    storage_part_number = db.Column(db.String, nullable=True)

with app.app_context():
    db.create_all()
