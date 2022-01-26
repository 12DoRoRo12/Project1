#LAST HOMEWORK PY
from flask import Flask
from flask_restful import Resource, Api
import sqlite3
# conn = sqlite3.connect(':memory:', check_same_thread=False)
# c = conn.cursor()
# c.execute("""CREATE TABLE poets (
#             p_id int,
#             name text,
#             birth text,
#             death text,
#             poem text,
#             youtubelink text
# )""")
# c.execute("INSERT INTO poets VALUES (:p_id,:name,:birth,:death,:poem,:youtubelink)",
#                   {"p_id": 1, "name": "გალაქტიონ ტაბიძე","birth": "17 ნოემბერი, 1891",
#                    "death": "17 მარტი, 1959","poem": "მე და ღამე","youtubelink":"https://www.youtube.com/watch?v=MRMDBQ7BlIg"})
# c.execute("INSERT INTO poets VALUES (:p_id,:name,:birth,:death,:poem,:youtubelink)",
#                   {"p_id": 2, "name": "მირზა გელოვანი","birth": "2 მარტი, 1917",
#                    "death": "ივლისი 1944","poem": "შენ","youtubelink":"https://www.youtube.com/watch?v=LYoI18YMUfc"})
# c.execute("INSERT INTO poets VALUES (:p_id,:name,:birth,:death,:poem,:youtubelink)",
#                   {"p_id": 3, "name": "ლადო ასათიანი","birth": "14 იანვარი, 1917",
#                    "death": "23 ივნისი, 1943","poem": "სალაღობო","youtubelink":"https://www.youtube.com/watch?v=PN9pG1eu_Bk"})
# c.execute("INSERT INTO poets VALUES (:p_id,:name,:birth,:death,:poem,:youtubelink)",
#                   {"p_id": 4, "name": "ტიციან ტაბიძე","birth": "2 აპრილი, 1895",
#                    "death": "16 დეკემბერი, 1937","poem": "ანანურთან","youtubelink":"https://www.youtube.com/watch?v=9bV1j2h0_Go"})
# c.execute("INSERT INTO poets VALUES (:p_id,:name,:birth,:death,:poem,:youtubelink)",
#                   {"p_id": 5, "name": "ლუკა რაზიკაშვილი","birth": "27 მაისი, 1862",
#                    "death": "27 ივლისი, 1915","poem": "სიკვდილი ყველას გვაშინებს","youtubelink": "https://www.youtube.com/watch?v=EAdgfELuA8M"})
#
# conn.commit()
# app = Flask(__name__)
# api = Api(app)
# class HelloWorld(Resource):
#     def get(self):
#         return {"ქართველი პოეტები": "აირჩიე ხუთიდან ერთი!"}
#     def post(self,id):
#         c.execute("SELECT name, poem, youtubelink FROM poets WHERE p_id=:p_id", {"p_id": id})
#         return c.fetchall()
#     def delete(self,id):
#         with conn:
#             c.execute("DELETE from poets WHERE p_id = :p_id ", {"p_id": id})
#         return {"You have deleted poet with id number": id}
# api.add_resource(HelloWorld, '/get',endpoint="get")
# api.add_resource(HelloWorld, '/<string:id>',endpoint="post")
# api.add_resource(HelloWorld, '/delete/<string:id>',endpoint="delete")
# if __name__ == "__main__":
#     app.run(debug=True)


