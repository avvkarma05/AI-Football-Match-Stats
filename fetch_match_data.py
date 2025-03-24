import requests

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXX"  # Replace with actual API key
HEADERS = {"X-Auth-Token": API_KEY}

def get_match_data(match_id):
    """Fetch match details dynamically from Football-Data API"""
    url = f"https://api.football-data.org/v4/matches/{match_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()

        # Extract match stats
        match_data = {
            "teams": [data["match"]["homeTeam"]["name"], data["match"]["awayTeam"]["name"]],
            "score": [data["match"]["score"]["fullTime"]["home"], data["match"]["score"]["fullTime"]["away"]],
            "scorers": [event["player"]["name"] for event in data["match"]["goals"]],
            "possession": [data["match"]["homeTeam"]["statistics"]["possession"],
                           data["match"]["awayTeam"]["statistics"]["possession"]],
            "shots_on_target": [data["match"]["homeTeam"]["statistics"]["shotsOnTarget"],
                                data["match"]["awayTeam"]["statistics"]["shotsOnTarget"]],
            "fouls": [data["match"]["homeTeam"]["statistics"]["fouls"],
                      data["match"]["awayTeam"]["statistics"]["fouls"]],
            "yellow_cards": [data["match"]["homeTeam"]["statistics"]["yellowCards"],
                             data["match"]["awayTeam"]["statistics"]["yellowCards"]]
        }
        
        return match_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

