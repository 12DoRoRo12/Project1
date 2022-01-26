from faker import Faker
from sqlalch import db, UserModel, PostModel
from random import random
fake = Faker()
for i in range(1,200):
    user = UserModel(username=fake.name(), email=fake.email())
    db.session.add(user)
    db.session.commit()

for i in range(1,200):
    post = PostModel(title=fake.paragraph(nb_sentences=1), body=fake.text(), user_id=abs(i-200))
    db.session.add(post)
    db.session.commit()