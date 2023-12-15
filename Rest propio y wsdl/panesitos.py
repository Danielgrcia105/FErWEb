#importamos lo que utilizaremos y diremode de domde viene en este caso el from 
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
 
app = Flask(__name__)
api = Api(app)
 
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpanesitos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
# Definición del modelo de datos de los productos
class Panes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
 
# Inicialización del objeto que permite realizar la serialización
ma = Marshmallow(app)
 
# Definición de esquema para la serialización
class PanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Panes
 
# Ruta para obtener todos los productos
class ProductosResource(Resource):
    def get(self):
        productos = Panes.query.all()
        pan_schema = PanSchema(many=True)
        result = pan_schema.dump(productos)
        return jsonify(result)
    #ruta para agregar un producto
    #comando para agregar ejemplo:
    #curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Pan Integral", "precio": 2.0, "cantidad": 15}' http://localhost:5000/productos
    def post(self):
        nuevo_pan_data = request.json
        nuevo_pan = Panes(**nuevo_pan_data)
        db.session.add(nuevo_pan)
        db.session.commit()
        return jsonify({'message': 'Pan agregado correctamente'}), 201
 
# Ruta para obtener información de la tabla "panes" por id
class PanPorIdResource(Resource):
    def get(self, pan_id):
        pan = Panes.query.get(pan_id)
        if pan:
            pan_schema = PanSchema()
            result = pan_schema.dump(pan)
            return jsonify(result)
        else:
            return jsonify({'message': 'Pan no encontrado'}), 404
# Ruta para eliminar pan
def delete(self, pan_id):
        pan = Panes.query.get(pan_id)
        if pan:
            db.session.delete(pan)
            db.session.commit()
            return jsonify({'message': 'Pan eliminado correctamente'})
        else:
            return jsonify({'message': 'Pan no encontrado'}), 404
    #ruta para eliminar pan
    #curl -X DELETE http://localhost:5000/panes/1
 
#ruta para actualizar
def put(self, pan_id):
        pan = Panes.query.get(pan_id)
        if pan:
            nuevo_pan_data = request.json
            pan.nombre = nuevo_pan_data.get('nombre', pan.nombre)
            pan.precio = nuevo_pan_data.get('precio', pan.precio)
            pan.cantidad = nuevo_pan_data.get('cantidad', pan.cantidad)
            db.session.commit()
            return jsonify({'message': 'Pan actualizado correctamente'})
        else:
            return jsonify({'message': 'Pan no encontrado'}), 404
        #comando:
#curl -X PUT -H "Content-Type: application/json" -d '{"nombre": "Pan de Centeno", "precio": 2.5, "cantidad": 20}' http://localhost:5000/panes/1
 
# Agregar recursos a la API
api.add_resource(ProductosResource, '/productos')
api.add_resource(PanPorIdResource, '/panes/<int:pan_id>')
 
if __name__ == '__main__':
    # Crear las tablas en la base de datos antes de ejecutar la aplicación
    with app.app_context():
        db.create_all()
 
    # Iniciar la aplicación
app.run(debug=True)