from flask_sqlalchemy import SQLAlchemy

con = app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Zivish2019#@localhost/usernamedb?charset=utf8mb4&use_unicode=0"
db = SQLAlchemy(con)
class user_table(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(120), nullable=False)
    Login = db.Column(db.String(120), nullable=False)
    Email = db.Column(db.String(120), nullable=False)
    Name = db.Column(db.Boolean, nullable=False)

    def __init__(self, code, agent_name, phone, idno, email,county, added_by,  create_date, active):
        self.code = code
        self.agent_name = agent_name
        self.phone = phone
        self.idno = idno
        self.email = email 
        self.county = county 
        self.added_by = added_by 
        self.create_date = create_date 
        self.active = active 