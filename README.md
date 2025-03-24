# AI-Football-Match-Stats
This project automates the generation of football match reports using real-time match data and AI-based text generation. It fetches match details from the Football Data API, extracts key statistics, and uses Google Gemini AI to generate a natural-language summary of the match.

How It Works:

1️⃣ fetch_match_data.py (Fetching Match Data):
Calls the Football Data API to get match details.
Extracts teams, score, goal scorers, possession, shots, fouls, and yellow cards.
Returns this structured data for further processing.

2️⃣ report_generator.py (AI-Generated Report)
Uses Google Gemini AI to create a match summary.
Takes the match stats and converts them into a readable report.

3️⃣ main.py (Runs Everything)
Calls the match data fetcher.
Sends data to AI for report generation.
Displays the final match report.
