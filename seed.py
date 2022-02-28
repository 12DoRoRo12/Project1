from faker import Faker
from werkzeug.security import generate_password_hash
from sqlalch import db, PoetsModel, PoemsModel, UserModel



user_data = [{"id": "1", "username": "Nika Tsitskishvili", "email": "n.tsitskishvili@gmail.com", "password": "astalavista"}, {"user_id": "2", "username": "Emilly Berger", "email": "e.berger@gmail.com", "password": "wonderpas"},
             {"id": "3", "username": "James Hope", "email": "j.hope@yahoo.com", "password": "amptylife123"},{"user_id": "4", "username": "Ketty Higgins", "email": "k.higgins.1@iliauni.@edu.ge", "password": "studentgreen"},
             {"id": "5", "username": "Harry Bing", "email": "h.bing@gmail.com", "password": "kenjimiazava2021"}]

poet_data = [{"poet_id": 1, "poet_name": "Mirza Gelovani","birth_date": "2 March, 1917","death_date": "July 1944"},
             {"poet_id": 2,"poet_name": "Galaktion Tabidze","birth_date": "17 November, 1891","death_date": "17 March, 1959"},
              {"poet_id": 3, "poet_name": "Lado Asatiani", "birth_date": "14 January, 1917","death_date": "23 June, 1943"},
             {"poet_id": 4, "poet_name": "Vazha Pshavela", "birth_date": "27 May, 1862","death_date": "27 July, 1915"},
             {"poet_id": 5, "poet_name": "Titsian Tabidze", "birth_date": "2 April, 1895","death_date": "16 December, 1937"}]

poem_data = [{"poem_id": 1, "poem_title": "Me and Night","youtube_link":"https://www.youtube.com/watch?v=MRMDBQ7BlIg", "creator_id": 2},
             {"poem_id": 2, "poem_title": "Undertaker","youtube_link":"https://www.youtube.com/watch?v=G7oRDw5eAgY", "creator_id": 2},
             {"poem_id": 3, "poem_title": "Moon of the Saint Mountain","youtube_link":"https://www.youtube.com/watch?v=vhTIeuWRnk4", "creator_id": 2},
             {"poem_id": 4, "poem_title": "Without Love","youtube_link":"https://www.youtube.com/watch?v=S3LZhuDd-C4", "creator_id": 2},
             {"poem_id": 5, "poem_title": "You","youtube_link":"https://www.youtube.com/watch?v=LYoI18YMUfc", "creator_id": 1},
             {"poem_id": 6, "poem_title": "To Mother","youtube_link":"https://www.youtube.com/watch?v=QQzQxKTd-tQ", "creator_id": 1},
             {"poem_id": 7, "poem_title": "Smile","youtube_link":"https://www.youtube.com/watch?v=CutwiS420ys", "creator_id": 1},
             {"poem_id": 8,"poem_title": "Salagobo","youtube_link":"https://www.youtube.com/watch?v=PN9pG1eu_Bk", "creator_id": 3},
             {"poem_id": 9,"poem_title": "Bardnala","youtube_link":"https://www.youtube.com/watch?v=prbR_OZ9K8c", "creator_id": 3},
             {"poem_id": 10,"poem_title": "Georgian Language","youtube_link":"https://www.youtube.com/watch?v=tjsdV4PMCKc", "creator_id": 3},
             {"poem_id": 11,"poem_title": "At Ananuri","youtube_link":"https://www.youtube.com/watch?v=9bV1j2h0_Go", "creator_id": 5},
             {"poem_id": 12,"poem_title": "All are Frightened by Death","youtube_link": "https://www.youtube.com/watch?v=EAdgfELuA8M", "creator_id": 4},
             {"poem_id": 13,"poem_title": "Lonliness","youtube_link": "https://www.youtube.com/watch?v=DkUHZGcVZaI", "creator_id": 4},
             {"poem_id": 14,"poem_title": "Bakhtrioni","youtube_link": "https://www.youtube.com/watch?v=vibvlUXhi7c", "creator_id": 4}]
def create_database():
    for i in user_data:
        user = UserModel(username=i["username"], email=i["email"], password=generate_password_hash(i["password"]))
        db.session.add(user)
        db.session.commit()
    for i in poet_data:
        poet = PoetsModel(poet_name=i["poet_name"], birth_date=i["birth_date"], death_date=i["death_date"])
        db.session.add(poet)
        db.session.commit()
    for i in poem_data:
        poet = PoemsModel(poem_title=i["poem_title"], youtube_link=i["youtube_link"], creator_id=i["creator_id"])
        db.session.add(poet)
        db.session.commit()
# db.create_all()
# create_database()
#
# if __name__ == "__main__":
#     create_database()

# fake = Faker()
# for i in range(1,50):
#     user = UserModel(username=fake.name(), email=fake.email(),password=fake.name())
#     db.session.add(poet)
#     db.session.commit()
# fake = Faker()
# for i in range(1,200):
#     poet = PoetsModel(poet_name=fake.name(), birth_date=fake.date(),death_date=fake.date())
#     db.session.add(poet)
#     db.session.commit()
#
# for i in range(1,200):
#     poem = PoemsModel(poem_title=fake.paragraph(nb_sentences=1), youtube_link=fake.paragraph(nb_sentences=1), creator_id=abs(i-200))
#     db.session.add(poem)
#     db.session.commit()