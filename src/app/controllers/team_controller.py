# controllers/team_controller.py

from flask import Blueprint, request, jsonify
from ..services.team_service import TeamService

team = Blueprint('team', __name__)

@team.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    team_name = data.get('team_name')
    user_id = data.get('user_id')
    sport = data.get('sport')

    if not team_name or not user_id or not sport:
        return jsonify({'message': 'Team name, user ID, and sport are required!'}), 400

    team = TeamService.create_team(team_name, user_id, sport)
    return jsonify({'message': 'Team created successfully!', 'team_id': team.team_id})
