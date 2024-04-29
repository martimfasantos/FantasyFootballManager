from flask import Blueprint, jsonify, redirect, render_template, request, flash, url_for
from flask_login import login_required
import json
from ..services.auth_service import AuthService
from ..services.team_service import TeamService
from ..utils.constants import Sports


views = Blueprint("views", __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        team_name = request.form.get("team_name")

        if len(team_name) < 1:
            flash("Team name must be greater than 1 character!", category="error")
        try:
            TeamService.create_team(team_name, AuthService.get_current_user().id, Sports.FOOTBALL.value)
            flash('New Team created!', category='success')
            # return redirect(url_for('views.create_team', user_username=AuthService.get_current_user().username, team_name=team_name))
        except Exception as e:
            flash(str(e), category='error')

    return render_template("home.html", user=AuthService.get_current_user())

@views.route('/delete-team', methods=["DELETE"])
def delete_team():
    try:
        team = json.loads(request.data)
        team_id = team['id']
        TeamService.delete_team(team_id)
        flash('Team deleted!', category='success')
    except Exception as e:
        flash(str(e), category='error')
    
    return jsonify({})

@views.route('/team/<user_username>/<team_name>', methods=["GET", "POST"])
@login_required
def add_players():
    pass