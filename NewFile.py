#LAST HOMEWORK PY
from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self,name):
        return {"name": name}
    def put(self):
        return {"hello": "world"}
    def delete(self,name):
        return {"name": name}
api.add_resource(HelloWorld, '/get/',endpoint="get")
api.add_resource(HelloWorld, '/post/<string:name>',endpoint="post")
api.add_resource(HelloWorld, '/put/<string:name>',endpoint="put")
api.add_resource(HelloWorld, '/delete/<string:name>',endpoint="delete")
if __name__ == "__main__":
    app.run(debug=True)
# @app.route("/")
# def hello_world():
#     return "<h1>Hello World!</h1>"
# @app.route("/home", methods=['POST','GET'])
# def home_page():
#     return "<h1>It is our home page!</h1>"
# @app.route("/store")
# def store():
#     return "<h1>It is our Store!</h1>"
# if __name__ == "__main__":
#     app.run(debug=True)
# git bash here + git init დირექტორიაში შესაძლებელს ხდის გითის დაკვირვებას
# git config --global user.name"FIRST_NAME LAST_NAME" ... git config --global user.email"s.something@gmail.com"დაქომითებისთვის სახელის და ელფოსტის ჩაწერაა საჭირო, როდესაც ვწერთ გლობალს ერთჯერადად იწერება და ინახება კომპში
# git status გვიჩვენებს რა დირექტორიები და ფაილებია მოცემულ დირექტორიაში (სამუშაო ადგილას)
# git add გადააქვს სასურველი ფაილი უბრალოდ სამუშაო ადგილიდან გითის თვალთვალის ქვეშ
# git commit -m "comment" სქრინშოთის გადაღება და კომენტირება,
# git push origin master ვებგვერდზე ატვირთვა
# git log ანახებს დაქომითებულ ფაილებს
#pip freeze რა ბიბლიოთეკები გვიყენია (ტერმინა) დასაყენებლად pip install -r requaired.txt

