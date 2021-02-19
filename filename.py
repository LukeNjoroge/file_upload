from flask_sqlalchemy import SQLAlchemy
from users import user_table
import csv

def file_upload(file):
    con = app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Zivish2019#@localhost/usernamedb?charset=utf8mb4&use_unicode=0"
    db = SQLAlchemy(con)
    reader = csv.DictReader(open(file))
    for row in reader:
        Name = row['Name']
        Login = row['Login']
        Email = row['Email']
        Active = row['Active']
        new_user = user_table(
            Name,
            Login,
            Email,
            Active,
        )
        db.session.add(new_user)
        db.session.commit()
    return file