from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #ar gvinda modifikaciebis trrackingi
app.config["JWT_SECRET_KEY"] = "our-secret-key" #must be changed

db = SQLAlchemy(app)
jwt = JWTManager(app)

resource_user = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "password": fields.String
}

resource_poets = {            #stringad rom gadaiqces rata postmenma waikitxos user getshi
    "poet_id": fields.Integer,
    "poet_name": fields.String,
    "birth_date": fields.String,
    "death_date": fields.String
}
resource_poems = {
    "poem_id": fields.Integer,
    "poem_title": fields.String,
    "youtube_link": fields.String,
    "creator_id": fields.Integer
}

resource_register = {
    "username": fields.String,
    "email": fields.String,
    "password": fields.String
}

registerparser = reqparse.RequestParser()
registerparser.add_argument("username", type=str, help='user_name must be string')
registerparser.add_argument("email", type=str, required=True, help='Email must be string')
registerparser.add_argument("password", type=str, required=True, help='Email must be string')

userparser = reqparse.RequestParser()
userparser.add_argument("username", type=str, help='user_name must be string')
userparser.add_argument("email", type=str, help='Email must be string')
userparser.add_argument("password", type=str, help='Email must be string')

poetparser = reqparse.RequestParser()
poetparser.add_argument("poet_id", type=int, help='Id must be integer')
poetparser.add_argument("poet_name", type=str, help='Poet_name must be string')
poetparser.add_argument("birth_date", type=str, help='Birth date must be string')
poetparser.add_argument("death_date", type=str, help='Death date must be string')

poemparser = reqparse.RequestParser()
poemparser.add_argument("poem_id", type=int, help='Id must be integer')
poemparser.add_argument("poem_title", type=str, help='Title must be string')
poemparser.add_argument("youtube_link", type=str, help='Body must be string')
poemparser.add_argument("creator_id", type=int, help='User_id must be integer')

class User(Resource):
    @marshal_with(resource_user)
    # @jwt_required()
    def get(self, user_id):
        if user_id == 999:
            return UserModel.query.all()
        args = userparser.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        return user

    @marshal_with(resource_user)
    @jwt_required()
    def post(self, user_id):
        args = userparser.parse_args()
        password = generate_password_hash(args["password"])
        user = UserModel(username=args["username"],email=args["email"], password=password)
        db.session.add(user)
        db.session.commit()
        return "inserted"

    @marshal_with(resource_user)
    # @jwt_required()
    def put(self, user_id):
        args = userparser.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        password = generate_password_hash(args["password"])
        if user == None:
            user = UserModel(username=args["username"], email=args["email"], password=password)
        else:
            user.username = args["username"]
            user.email = args["email"]
            user.password = password
        db.session.add(user)
        db.session.commit()
        return "updated"

    # @marshal_with(resource_user)
    # @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return f"User with id {user_id} has been deleted"

class Poet(Resource):
    @marshal_with(resource_poets)
    def get(self, poet_id):
        if poet_id == 999:
            return PoetsModel.query.all()
        # args = poetparser.parse_args()
        poet = PoetsModel.query.filter_by(poet_id=poet_id).first()
        return poet

    @marshal_with(resource_poets)
    @jwt_required()
    def post(self, poet_id):
        args = poetparser.parse_args()
        poet = PoetsModel(poet_name=args["poet_name"], birth_date=args["birth_date"],death_date=args["death_date"])
        db.session.add(poet)
        db.session.commit()
        return "inserted"

    @marshal_with(resource_poets)
    @jwt_required()
    def put(self, poet_id):
        args = poetparser.parse_args()
        poet = PoetsModel.query.filter_by(poet_id=poet_id).first()
        if poet == None:
            poet = PoetsModel(poet_name=args["poet_name"], birth_date=args["birth_date"],death_date=args["death_date"])
        else:
            poet.poet_name = args["poet_name"]
            poet.birth_date = args["birth_date"]
            poet.death_date = args["death_date"]
        db.session.add(poet)
        db.session.commit()
        return "updated"

    # @marshal_with(resource_poets)
    @jwt_required()
    def delete(self, poet_id):
        poet = PoetsModel.query.filter_by(poet_id=poet_id).first()
        db.session.delete(poet)
        db.session.commit()
        return f"Poet with id {poet_id} has been deleted"


class Poem(Resource):
    @marshal_with(resource_poems)
    def get(self, poem_id):
        if poem_id == 000:
            return PoemsModel.query.all()
        args = poemparser.parse_args()
        poem = PoemsModel.query.filter_by(poem_id=poem_id).first()
        return poem

    @marshal_with(resource_poems)
    @jwt_required()
    def post(self, poem_id):
        args = poemparser.parse_args()
        if PoetsModel.query.filter_by(poet_id=args["creator_id"]).first():
            poem = PoemsModel(poem_title=args["poem_title"], youtube_link=args["youtube_link"],creator_id=args["creator_id"])
            db.session.add(poem)
            db.session.commit()
            return "Item has been inserted!"
        else:
            return "Given creator_id doesn't exist"

    @marshal_with(resource_poems)
    @jwt_required()
    def put(self, poem_id):
        args = poemparser.parse_args()
        poem = PoemsModel.query.filter_by(poem_id=poem_id).first()
        if poem == None:
            poem = PoemsModel(poem_title=args["poem_title"], youtube_link=args["youtube_link"],creator_id=args["creator_id"])
        else:
            poem.poem_title = args["poem_title"]
            poem.youtube_link = args["youtube_link"]
            poem.creator_id = args["creator_id"]
        db.session.add(poem)
        db.session.commit()
        return "updated"

    # @marshal_with(resource_poems)
    @jwt_required()
    def delete(self, poem_id):
        poem = PoemsModel.query.filter_by(poem_id=poem_id).first()
        db.session.delete(poem)
        db.session.commit()
        return f"Poem with id {poem_id} has been deleted"



class Register(Resource):
    @marshal_with(resource_register)
    def post(self):
        args = registerparser.parse_args()
        user = UserModel(username=args["username"], email=args["email"], password=generate_password_hash(args["password"]))
        db.session.add(user)
        db.session.commit()
        return {"msg": "Created"}, 201

class Auth(Resource):
    # @marshal_with(resource_user)
    def post(self):
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        user = UserModel.query.filter_by(email=email).first_or_404()
        if user == None:
            return {"msg": "Email was not found"}
        if email != user.email or check_password_hash(user.password,password) == False:
            return jsonify({"msg": "Bad email or password"}), 401
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"User {self.username}"

class PoetsModel(db.Model):
    __tablename__ = "poets"
    poet_id = db.Column(db.Integer, primary_key=True)
    poet_name = db.Column(db.String(20), unique=True, nullable=False)
    birth_date = db.Column(db.String(20), nullable=False)
    death_date = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Poet {self.poet_name}"

class PoemsModel(db.Model):
    __tablename__ = 'poems'
    poem_id = db.Column(db.Integer, primary_key=True)
    poem_title = db.Column(db.String(20), nullable=False)
    youtube_link = db.Column(db.String(80), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('poets.poet_id'), nullable=False)

    def __repr__(self):
        return f"Poem {self.poem_title}"

# @app.before_first_request
# def before_first_request():
#     import seed
# db.create_all()
# quit()

api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Poet, '/poet/<int:poet_id>')
api.add_resource(Poem, '/poem/<int:poem_id>')
api.add_resource(Auth, '/login')
api.add_resource(Register, '/register')



if __name__ == "__main__":
    app.run(debug=True)

