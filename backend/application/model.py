from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Class User
class User(db.Model):
    _tablename_ = "user"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin
    }

# Class Post
class Post(db.Model):
    _tablename_ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
    }

# Class Match schedule
class MatchSchedule(db.Model):
    _tablename_ = "matchSchedule"

    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(50), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    hours = db.Column(db.String(12), nullable=False)
    arena = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'home': self.home,
            'away': self.away,
            'date': self.date,
            'hours': self.hours,
            'arena': self.arena
    }

# Class Result
class Result(db.Model):
    _tablename_ = "result"

    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(25), nullable=False)
    away = db.Column(db.String(25), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    home_points = db.Column(db.Integer, nullable=False)
    away_points = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'home': self.home,
            'away': self.away,
            'date': self.date,
            'home_points': self.home_points,
            'away_points': self.away_points
    }

# Class Team
class Team(db.Model):
    _tablename_ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.String(20), nullable=False)
    arena = db.Column(db.String(100), nullable=False)
    president = db.Column(db.String(100), nullable=False)
    head_coach = db.Column(db.String(100), nullable=False)
    wins = db.Column(db.Integer, nullable=True)
    loses = db.Column(db.Integer, nullable=True)
    games_played = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)

    player = db.relationship('Player', back_populates='team', lazy="dynamic")

    def __init__(self, **kwargs):
        super(Team, self).__init__(**kwargs)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'founded': self.founded,
            'arena': self.arena,
            'president': self.president,
            'head_coach': self.head_coach,
            'wins': self.wins,
            'loses': self.loses,
            'games_played': self.games_played,
            'points': self.points
    }

# Class Player
class Player(db.Model):
    _tablename_ = "player"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    born = db.Column(db.String(70), nullable=False)
    years = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    place_of_birth = db.Column(db.String(40), nullable=False)
    number_player = db.Column(db.Integer, nullable=False)

    id_team = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    team = db.relationship('Team', back_populates='player', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'position': self.position,
            'born': self.born,
            'years': self.years,
            'nationality': self.nationality,
            'height': self.height,
            'place_of_birth': self.place_of_birth,
            'number_player': self.number_player
    }

# Class utakmica zapisnik
class UtakmicaZapisnik(db.Model):
    _tablename_ = "utakmica_zapisnik"

    id = db.Column(db.Integer, primary_key=True)
    id_home = db.Column(db.Integer, nullable=False)
    id_away = db.Column(db.Integer, nullable=False)
    name_home = db.Column(db.String(35), nullable=False)
    name_away = db.Column(db.String(35), nullable=False)
    natjecanje = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    mjesto = db.Column(db.String(20), nullable=False)
    prvi_sudac = db.Column(db.String(35), nullable=False)
    drugi_sudac = db.Column(db.String(35), nullable=False)
    treci_sudac = db.Column(db.String(35), nullable=False)
    zapisnicar = db.Column(db.String(35), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'id_home': self.id_home,
            'id_away': self.id_away,
            'name_home': self.name_home,
            'name_away': self.name_away,
            'natjecanje': self.natjecanje,
            'date': self.date,
            'mjesto': self.mjesto,
            'prvi_sudac': self.prvi_sudac,
            'drugi_sudac': self.drugi_sudac,
            'treci_sudac': self.treci_sudac,
            'zapisnicar': self.zapisnicar
    }

# Class tim zapisnik
class TimZapisnik(db.Model):
    _tablename_ = "tim_zapisnik"

    id = db.Column(db.Integer, primary_key=True)
    id_team = db.Column(db.Integer, nullable=False)
    id_utakmice = db.Column(db.Integer, nullable=False)
    name_team = db.Column(db.String(35), nullable=False)
    teamouts_1_pol = db.Column(db.Integer, nullable=False)
    teamouts_2_pol = db.Column(db.Integer, nullable=False)
    teamFouls_1_cet = db.Column(db.Integer, nullable=False)
    teamFouls_2_cet = db.Column(db.Integer, nullable=False)
    teamFouls_3_cet = db.Column(db.Integer, nullable=False)
    teamFouls_4_cet = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'id_team': self.id_team,
            'id_utakmice': self.id_utakmice,
            'name_team': self.name_team,
            'teamouts_1_pol': self.teamouts_1_pol,
            'teamouts_2_pol': self.teamouts_2_pol,
            'teamFouls_1_cet': self.teamFouls_1_cet,
            'teamFouls_2_cet': self.teamFouls_2_cet,
            'teamFouls_3_cet': self.teamFouls_3_cet,
            'teamFouls_4_cet': self.teamFouls_4_cet
    }

# Class igrac zapisnik
class IgracZapisnik(db.Model):
    _tablename_ = "igrac_zapisnik"

    id = db.Column(db.Integer, primary_key=True)
    id_team = db.Column(db.Integer, nullable=False)
    id_player = db.Column(db.Integer, nullable=False)
    id_utakmice = db.Column(db.Integer, nullable=False)
    name_team = db.Column(db.String(35), nullable=False)
    name_player = db.Column(db.String(35), nullable=False)
    number_player = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    oPrekrsaji = db.Column(db.Integer, nullable=False)
    tPrekrsaji = db.Column(db.Integer, nullable=False)
    skokovi = db.Column(db.Integer, nullable=False)
    asist = db.Column(db.Integer, nullable=False)
    steals = db.Column(db.Integer, nullable=False)
    blocks = db.Column(db.Integer, nullable=False)
    turnovers = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'id_team': self.id_team,
            'id_player': self.id_player,
            'id_utakmice': self.id_utakmice,
            'name_team': self.name_team,
            'name_player': self.name_player,
            'points': self.points,
            'oPrekrsaji': self.oPrekrsaji,
            'tPrekrsaji': self.tPrekrsaji,
            'skokovi': self.skokovi,
            'asist': self.asist,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'number_player': self.number_player
    }

# Class Comments
class Comments(db.Model):
    _tablename_ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, nullable=False)
    ime = db.Column(db.String(50), nullable=False)
    prezime = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(100000), nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'id_post': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'comment': self.comment
    }