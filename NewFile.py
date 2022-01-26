#LAST HOMEWORK PY
# from flask import Flask
# from flask_restful import Resource, Api
# import sqlite3
# conn = sqlite3.connect(':memory:', check_same_thread=False) #კოდის დასრულებამდე დროებით მონაცემთა ბაზას ვქმნი
# c = conn.cursor()
# c.execute("""CREATE TABLE students (
#             id int,
#             name text,
#             course text,
#             age int,
#             university text
# )""")
# c.execute("INSERT INTO students VALUES (:id,:name,:course,:age,:university)",
#                   {"id": 1, "name": "George", "course": "second",
#                    "age": 20,"university": "Tbilisi State University"})
# c.execute("INSERT INTO students VALUES (:id,:name,:course,:age,:university)",
#                   {"id": 2, "name": "Natka", "course": "second",
#                    "age": 19,"university": "Free University"})
# c.execute("INSERT INTO students VALUES (:id,:name,:course,:age,:university)",
#                   {"id": 3, "name": "Ella", "course": "First",
#                    "age": 18,"university": "Ilia State University"})
# c.execute("INSERT INTO students VALUES (:id,:name,:course,:age,:university)",
#                   {"id": 4, "name": "Vaso", "course": "First",
#                    "age": 21,"university": "Sulkhan Kvernadze University"})
# c.execute("INSERT INTO students VALUES (:id,:name,:course,:age,:university)",
#                   {"id": 5, "name": "Gela", "course": "Third",
#                    "age": 34,"university": "Georgian Technical University"})
# conn.commit()
# app = Flask(__name__)
# api = Api(app)
# class HelloWorld(Resource):
#     def get(self):
#         return {"Table": "With five students' data"}
#     def post(self,student_id):
#         with conn:
#             student_id = int(student_id)
#             c.execute("SELECT * FROM students WHERE id=:id", {"id": student_id})
#         return c.fetchall()
#
#     def delete(self,student_id):
#         with conn:
#             c.execute("DELETE from students WHERE id = :id ", {"id": student_id})
#         return {"You have deleted student with id number": student_id}
# api.add_resource(HelloWorld, '/get',endpoint="get")
# api.add_resource(HelloWorld, '/<string:student_id>',endpoint="post")
# api.add_resource(HelloWorld, '/delete/<string:name>',endpoint="delete")
# if __name__ == "__main__":
#     app.run(debug=True)
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

