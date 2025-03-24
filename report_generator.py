import google.generativeai as genai

#API Key
API_KEY = "XXXXXXXXXXXXXXXXXXXXX"  #Replace with actual API key
genai.configure(api_key=API_KEY)

def generate_match_report_gemini(match_data):
    """Generate match report using Gemini AI"""
    model = genai.GenerativeModel("gemini-pro")

    #Simple structured prompt
    prompt = f"""
    Generate a short football match report with the following details:
    - Teams: {match_data['teams'][0]} vs {match_data['teams'][1]}
    - Final Score: {match_data['score'][0]}-{match_data['score'][1]}
    - Goal Scorers: {', '.join(match_data['scorers']) if match_data['scorers'] else 'No goalscorers recorded'}
    - Possession: {match_data['possession'][0]}% - {match_data['possession'][1]}%
    - Shots on Target: {match_data['shots_on_target'][0]} - {match_data['shots_on_target'][1]}
    - Fouls Committed: {match_data['fouls'][0]} - {match_data['fouls'][1]}
    - Yellow Cards: {match_data['yellow_cards'][0]} - {match_data['yellow_cards'][1]}

    Provide a brief summary of the match dynamics in 3-4 sentences.
    """

    response = model.generate_content(prompt)
    return response.text
