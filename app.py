
from flask import Flask
from flask_restful import Resource, Api
import socket
from datetime import date
from datetime import datetime


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):    
        return {'hello': 'world'}

class Hostname(Resource):
    def get(self):    
        #return {'host': socket.gethostname()}
        return socket.gethostname()
        
class Dateandtime(Resource):
    def get(self):    
        now = datetime.utcnow() 
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")        
        #return {'current date and time UTC': dt_string }
        return dt_string
                
api.add_resource(HelloWorld, '/hello')
api.add_resource(Hostname, '/host')
api.add_resource(Dateandtime, '/date')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')