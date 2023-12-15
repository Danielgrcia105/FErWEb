
import pymysql
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from pymysql.cursors import DictCursor
 
app = Flask(__name__)
api = Api(app)
 
# Configura la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdleans'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
# Define la tabla "Categoria"
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))
 
    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp
 
# Crea las tablas en la base de datos
with app.app_context():
    db.create_all()
 
# Define el esquema para la clase "Categoria"
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id', 'cat_nom', 'cat_desp')
        categoria_schema = (id)
 
categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)
 
# Endpoint para obtener todas las categorías
@app.route('/categoria', methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

#get por id ###############################
@app.route('/categoria/<id>', methods=['GET'])
def get_categoria_x_id(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)

#post"##########################
@app.route('/categoria', methods=['POST'])
def insert_categoria():
    data = request. get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']
    
    nuevocategoria=Categoria(cat_nom,cat_desp)
    
    db.session.add(nuevocategoria)
    db.session.commit()
    return categoria_schema.jsonify(nuevocategoria)

#put#############################
@app.route('/categoria', methods=['PUT'])
def update_categoria(id):
    actualizarcategoria = Categoria.query.get(id)
    
    cat_nom = request.json['cat_nom']
    cat_desp = request.json['cat_desp']
    
    actualizarcategoria.cat_nom = cat_nom
    actualizarcategoria.cat_desp = cat_desp
    
    db.session.commit()
    return categoria_schema.jsonify(actualizarcategoria)  
#deleteeeeeeeeeeeeeeeeeeeee
@app.route('/categoria', methods=['DELETE'])
def delete_categoria(id):
    eliminacategtoria = Categoria.query.get(id)
    db.session.delete(eliminacategtoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminacategtoria)
    
  
# Mensaje de bienvenida
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje': 'Bienvenido a este tutorial de API REST'})
 
class Data(Resource):
    def get(self):
        return {"message": "data", "database": "bdleans"}
 
class Student(Resource):
    def get(self):
        # Implementa la lógica para obtener datos de estudiantes aquí
        pass
 
class Course(Resource):
    def get(self):
        # Implementa la lógica para obtener datos de cursos aquí
        pass
 
api.add_resource(Data, '/data')
api.add_resource(Course, '/courses')
 
if __name__ == '__main__':
    app.run(debug=True)