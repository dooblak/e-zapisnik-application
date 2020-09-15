from flask import Flask, request, jsonify, json
from flask.json import JSONEncoder
from flask_cors import CORS
from datetime import datetime
from decimal import Decimal
from .model import User, Post, MatchSchedule, Result, Team, Player, UtakmicaZapisnik, TimZapisnik, IgracZapisnik, Comments, db

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./e-zapisnik-db.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secret'
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    return app

# Home 
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"Message": "Dobrodosli u aplikaciju E-zapisnik"})

#---------------------------------------------------------- USERS ----------------------------------------------------------#

# Get users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users)

# Get single user
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user)

# Create user
@app.route('/user/register', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(fname=data["fname"], 
                    lname=data["lname"],
                    email=data["email"],
                    password=data["password"],
                    is_admin=data["is_admin"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)

# Login user
@app.route('/user/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User(email=data["email"], password=data["password"])
    rez = ""
    upit = User.query.filter_by(email=user.email).first()
    upit2 = User.query.filter_by(password=user.password).first()
    if upit and upit2:
        access_token = create_access_token(identity ={'id': upit.id, 'is_admin': upit.is_admin, 'fname': upit.fname, 'lname': upit.lname, 'email': upit.email, 'password': upit.password})
        rez = access_token
        return rez
    else:
        rez = jsonify({"error":"Neispravana lozinka"})
        return 

# Update user
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()

    user.fname=data["fname"]
    user.lname=data["lname"]
    user.email=data["email"]
    user.password=data["password"]
    user.is_admin=data["is_admin"]

    db.session.add(user)
    db.session.commit()
    return jsonify(user)

# Delete user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify(user)

#---------------------------------------------------------- POSTS ----------------------------------------------------------#

# Get posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify(posts)

# Get single post
@app.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return jsonify(post)

# Create post
@app.route('/post', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = Post(title=data["title"], 
                    content=data["content"],
                    created_at=data["created_at"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post)

# Update post
@app.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = Post.query.filter_by(id=post_id).first()

    post.title = data["title"]
    post.content = data["content"]
    post.created_at = data["created_at"]

    db.session.add(post)
    db.session.commit()
    return jsonify(post)

# Delete post
@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return jsonify(post)

#---------------------------------------------------------- MATCH SCHEDULE ----------------------------------------------------------#

# Get matches
@app.route('/matches', methods=['GET'])
def get_matches():
    matches = MatchSchedule.query.all()
    return jsonify(matches)

# Get single match
@app.route('/match/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = MatchSchedule.query.filter_by(id=match_id).first()
    return jsonify(match)

# Create match
@app.route('/match', methods=['POST'])
def add_match():
    data = request.get_json()
    new_match = MatchSchedule(home=data["home"], 
                            away=data["away"],
                            date=data["date"],
                            hours=data["hours"],
                            arena=data["arena"])
    db.session.add(new_match)
    db.session.commit()
    return jsonify(new_match)

# Update match
@app.route('/match/<int:match_id>', methods=['PUT'])
def update_match(match_id):
    data = request.get_json()
    match = MatchSchedule.query.filter_by(id=match_id).first()

    match.home = data["home"]
    match.away = data["away"]
    match.hours = data["hours"]
    match.date = data["date"]
    match.arena = data["arena"]

    db.session.add(match)
    db.session.commit()
    return jsonify(match)

# Delete post
@app.route('/match/<int:match_id>', methods=['DELETE'])
def delete_match(match_id):
    match = MatchSchedule.query.filter_by(id=match_id).first()
    db.session.delete(match)
    db.session.commit()
    return jsonify(match)

#---------------------------------------------------------- RESULTS ----------------------------------------------------------#

# Get results
@app.route('/results', methods=['GET'])
def get_results():
    results = Result.query.all()
    return jsonify(results)

# Get single result
@app.route('/result/<int:result_id>', methods=['GET'])
def get_result(result_id):
    result = Result.query.filter_by(id=result_id).first()
    return jsonify(result)

# Create result
@app.route('/result', methods=['POST'])
def add_result():
    data = request.get_json()
    new_result = Result(home=data["home"], 
                        away=data["away"],
                        date=data["date"],
                        home_points=data["home_points"],
                        away_points=data["away_points"])
    db.session.add(new_result)
    db.session.commit()
    return jsonify(new_result)

# Update result
@app.route('/result/<int:result_id>', methods=['PUT'])
def update_result(result_id):
    data = request.get_json()
    result = Result.query.filter_by(id=result_id).first()

    result.home = data["home"]
    result.away = data["away"]
    result.date = data["date"]
    result.home_points = data["home_points"]
    result.away_points = data["away_points"]

    db.session.add(result)
    db.session.commit()
    return jsonify(result)

# Delete result
@app.route('/result/<int:result_id>', methods=['DELETE'])
def delete_result(result_id):
    result = Result.query.filter_by(id=result_id).first()
    db.session.delete(result)
    db.session.commit()
    return jsonify(result)

#---------------------------------------------------------- TEAMS ----------------------------------------------------------#

# Get teams
@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify(teams)

# Get single team
@app.route('/team/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    return jsonify(team)

# Create team
@app.route('/team', methods=['POST'])
def add_team():
    data = request.get_json()
    new_team = Team(name=data["name"], 
                    location=data["location"],
                    founded=data["founded"],
                    arena=data["arena"],
                    president=data["president"],
                    head_coach=data["head_coach"])
    db.session.add(new_team)
    db.session.commit()
    return jsonify(new_team)

# Update team
@app.route('/team/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    team = Team.query.filter_by(id=team_id).first()

    team.name = data["name"]
    team.location = data["location"]
    team.founded = data["founded"]
    team.arena = data["arena"]
    team.president = data["president"]
    team.head_coach = data["head_coach"]
    team.wins = data["wins"]
    team.loses = data["loses"]
    team.games_played = data["games_played"]
    team.points = data["points"]

    db.session.add(team)
    db.session.commit()
    return jsonify(team)

# Delete team
@app.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    db.session.delete(team)
    db.session.commit()
    return jsonify(team)

#---------------------------------------------------------- PLAYERS ----------------------------------------------------------#

# Get players
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify(players)

# Get single player
@app.route('/player/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.filter_by(id=player_id).first()
    return jsonify(player)

# Get players of single team
@app.route('/players/<int:team_id>/team', methods=['GET'])
def get_players_of_single_teams(team_id):
    team = Team.query.filter_by(id=team_id).first()
    output = [] if team is None else team.player.all()
    return jsonify(output)

# Create player of single team
@app.route('/player/<int:team_id>/team', methods=['POST'])
def add_player_of_team(team_id):
    data = request.get_json()
    new_player = Player(fname=data["fname"], 
                        lname=data["lname"], 
                        position=data["position"], 
                        born=data["born"], 
                        years=data["years"], 
                        nationality=data["nationality"], 
                        height=data["height"], 
                        place_of_birth=data["place_of_birth"], 
                        number_player=data["number_player"], 
                        id_team=team_id)
    db.session.add(new_player)
    db.session.commit()
    return jsonify(new_player)

# Create player of single team #2
@app.route('/player/team', methods=['POST'])
def add_player_of_team2():
    data = request.get_json()
    new_player = Player(fname=data["fname"], 
                        lname=data["lname"], 
                        position=data["position"], 
                        born=data["born"], 
                        years=data["years"], 
                        nationality=data["nationality"], 
                        height=data["height"], 
                        place_of_birth=data["place_of_birth"],
                        number_player=data["number_player"], 
                        id_team=data["id_team"])
    db.session.add(new_player)
    db.session.commit()
    return jsonify(new_player)

# Update player
@app.route('/player/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    data = request.get_json()
    player = Player.query.filter_by(id=player_id).first()

    player.fname = data["fname"]
    player.lname = data["lname"]
    player.position = data["position"]
    player.born = data["born"]
    player.years = data["years"]
    player.nationality = data["nationality"]
    player.height = data["height"]
    player.place_of_birth = data["place_of_birth"]
    player.number_player=data["number_player"],

    db.session.add(player)
    db.session.commit()
    return jsonify(player)

# Delete player
@app.route('/player/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Player.query.filter_by(id=player_id).first()
    db.session.delete(player)
    db.session.commit()
    return jsonify(player)

#---------------------------------------------------------- utakmica zapisnik ----------------------------------------------------------#

# Get utakmica zapisnik
@app.route('/utakmica/zapisnik', methods=['GET'])
def get_utakmica_zapisnik():
    utakmica_zapisnik = UtakmicaZapisnik.query.all()
    return jsonify(utakmica_zapisnik)

# Get utakmica zapisniks
@app.route('/utakmica/zapisnik/<int:uta_zap_id>', methods=['GET'])
def get_utakmica_zapisniks(uta_zap_id):
    utakmica_zapisniks = UtakmicaZapisnik.query.filter_by(id=uta_zap_id).first()
    return jsonify(utakmica_zapisniks)

# Create utakmica zapisnik
@app.route('/utakmica/zapisnik', methods=['POST'])
def add_utakmica_zapisnik():
    data = request.get_json()
    new_utakmica_zapisnik = UtakmicaZapisnik(id_home=data["id_home"], 
                                            id_away=data["id_away"],
                                            name_home=data["name_home"], 
                                            name_away=data["name_away"],
                                            natjecanje=data["natjecanje"], 
                                            date=data["date"],
                                            mjesto=data["mjesto"], 
                                            prvi_sudac=data["prvi_sudac"],
                                            drugi_sudac=data["drugi_sudac"], 
                                            treci_sudac=data["treci_sudac"],
                                            zapisnicar=data["zapisnicar"])
    db.session.add(new_utakmica_zapisnik)
    db.session.commit()
    return jsonify(new_utakmica_zapisnik)

#---------------------------------------------------------- tim zapisnik ----------------------------------------------------------#

# Get tim zapisnik
@app.route('/tim/zapisnik', methods=['GET'])
def get_tim_zapisnik():
    tim_zapisnik = TimZapisnik.query.all()
    return jsonify(tim_zapisnik)

# Get tim zapisniks
@app.route('/tim/zapisnik/<int:tim_zap_id>', methods=['GET'])
def get_tim_zapisniks(tim_zap_id):
    tim_zapisniks = TimZapisnik.query.filter_by(id=tim_zap_id).first()
    return jsonify(tim_zapisniks)

# Create tim zapisnik
@app.route('/tim/zapisnik', methods=['POST'])
def add_tim_zapisnik():
    data = request.get_json()
    new_tim_zapisnik = TimZapisnik(id_team=data["id_team"], 
                                    id_utakmice=data["id_utakmice"],
                                    name_team=data["name_team"], 
                                    teamouts_1_pol=data["teamouts_1_pol"],
                                    teamouts_2_pol=data["teamouts_2_pol"], 
                                    teamFouls_1_cet=data["teamFouls_1_cet"],
                                    teamFouls_2_cet=data["teamFouls_2_cet"], 
                                    teamFouls_3_cet=data["teamFouls_3_cet"],
                                    teamFouls_4_cet=data["teamFouls_4_cet"])
    db.session.add(new_tim_zapisnik)
    db.session.commit()
    return jsonify(new_tim_zapisnik)


#---------------------------------------------------------- igrac zapisnik ----------------------------------------------------------#

# Get posts
@app.route('/igrac/zapisnik', methods=['GET'])
def get_igrac_zapisnik():
    igrac_zapisnik = IgracZapisnik.query.all()
    return jsonify(igrac_zapisnik)

# Get single post
@app.route('/igrac/zapisnik/<int:igrac_zap_id>', methods=['GET'])
def get_igrac_zapisniks(igrac_zap_id):
    igrac_zapisniks = IgracZapisnik.query.filter_by(id=igrac_zap_id).first()
    return jsonify(igrac_zapisniks)

# Create igrac zapisnik
@app.route('/igrac/zapisnik', methods=['POST'])
def add_igrac_zapisnik():
    data = request.get_json()
    new_igrac_zapisnik = IgracZapisnik(id_team=data["id_team"], 
                                        id_player=data["id_player"],
                                        id_utakmice=data["id_utakmice"], 
                                        name_team=data["name_team"],
                                        name_player=data["name_player"], 
                                        points=data["points"],
                                        oPrekrsaji=data["oPrekrsaji"], 
                                        tPrekrsaji=data["tPrekrsaji"],
                                        skokovi=data["skokovi"],
                                        asist=data["asist"], 
                                        steals=data["steals"],
                                        blocks=data["blocks"], 
                                        number_player=data["number_player"], 
                                        turnovers=data["turnovers"])
    db.session.add(new_igrac_zapisnik)
    db.session.commit()
    return jsonify(new_igrac_zapisnik)

#---------------------------------------------------------- COMMENTS ----------------------------------------------------------#

# Get comments
@app.route('/comments', methods=['GET'])
def get_comments():
    comments = Comments.query.all()
    return jsonify(comments)

# Get single comment
@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comments.query.filter_by(id_post=comment_id).all()
    return jsonify(comment)

# Create comment
@app.route('/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    new_comment = Comments(
                    id_post=data["id_post"], 
                    ime=data["ime"],
                    prezime=data["prezime"],
                    comment=data["comment"])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment)

'''
# Update team
@app.route('/team/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    team = Team.query.filter_by(id=team_id).first()

    team.name = data["name"]
    team.location = data["location"]
    team.founded = data["founded"]
    team.arena = data["arena"]
    team.president = data["president"]
    team.head_coach = data["head_coach"]
    team.wins = data["wins"]
    team.loses = data["loses"]
    team.games_played = data["games_played"]
    team.points = data["points"]

    db.session.add(team)
    db.session.commit()
    return jsonify(team)

# Delete team
@app.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    db.session.delete(team)
    db.session.commit()
    return jsonify(team)
'''

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):

        if hasattr(obj, "serialize"):
          return obj.serialize()

        try:
            if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder


if __name__ =="__main__":
  app.run(debug=True, port=8000)