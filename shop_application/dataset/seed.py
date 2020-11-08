import csv
import os
from shop_application.models import db, Category, Meal, User

curdir = os.path.dirname(os.path.abspath(__file__))


def seed_categories():
    with open(os.path.join(curdir, "delivery_categories.csv"),
              encoding="utf-8") as fp:
        reader = csv.reader(fp, delimiter=",")
        for row in reader:
            if row[1] == "title":
                continue
            db.session.add(Category(title=row[1]))
        db.session.commit()


def seed_items():
    with open(os.path.join(curdir, "delivery_items.csv"),
              encoding="utf-8") as fp:
        reader = csv.reader(fp, delimiter=",")
        for row in reader:
            if row[1] == "title":
                continue
            db.session.add(
                Meal(title=row[1],
                     price=float(row[2]),
                     description=row[3],
                     picture=row[4],
                     category_id=int(row[5])
                     ))
        db.session.commit()

def seed_test_user():
    db.session.add(User(mail="tester", password="tester"))
    db.session.commit()
