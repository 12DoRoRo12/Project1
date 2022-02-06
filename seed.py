from faker import Faker
from werkzeug.security import generate_password_hash
from sqlalch import db, PoetsModel, PoemsModel, UserModel
db.create_all()
user_data = [{"user_id": "1", "username": "Nika Tsitskishvili", "email": "n.tsitskishvili@gmail.com", "password": "astalavista"}, {"user_id": "2", "username": "Emilly Berger", "email": "e.berger@gmail.com", "password": "wonderpas"},
             {"user_id": "3", "username": "James Hope", "email": "j.hope@yahoo.com", "password": "amptylife123"},{"user_id": "4", "username": "Ketty Higgins", "email": "k.higgins.1@iliauni.@edu.ge", "password": "studentgreen"},
             {"user_id": "5", "username": "Harry Bing", "email": "h.bing@gmail.com", "password": "kenjimiazava2021"}]

poet_data = [{"poet_id": 1, "poet_name": "მირზა გელოვანი","birth_date": "2 მარტი, 1917","death_date": "ივლისი 1944"},
             {"poet_id": 2,"poet_name": "გალაქტიონ ტაბიძე","birth_date": "17 ნოემბერი, 1891","death_date": "17 მარტი, 1959"},
              {"poet_id": 3, "poet_name": "ლადო ასათიანი", "birth_date": "14 იანვარი, 1917","death_date": "23 ივნისი, 1943"},
             {"poet_id": 4, "poet_name": "ლუკა რაზიკაშვილი", "birth_date": "27 მაისი, 1862","death_date": "27 ივლისი, 1915"},
             {"poet_id": 5, "poet_name": "ტიციან ტაბიძე", "birth_date": "2 აპრილი, 1895","death_date": "16 დეკემბერი, 1937"}]

poem_data = [{"poem_id": 1, "poem_title": "მე და ღამე","youtube_link":"https://www.youtube.com/watch?v=MRMDBQ7BlIg", "creator_id": 2},
             {"poem_id": 2, "poem_title": "შენ","youtube_link":"https://www.youtube.com/watch?v=LYoI18YMUfc", "creator_id": 1},
             {"poem_id": 3,"poem_title": "სალაღობო","youtube_link":"https://www.youtube.com/watch?v=PN9pG1eu_Bk", "creator_id": 3},
             {"poem_id": 4,"poem_title": "ანანურთან","youtube_link":"https://www.youtube.com/watch?v=9bV1j2h0_Go", "creator_id": 5},
             {"poem_id": 5,"poem_title": "სიკვდილი ყველას გვაშინებს","youtube_link": "https://www.youtube.com/watch?v=EAdgfELuA8M", "creator_id": 4}]
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