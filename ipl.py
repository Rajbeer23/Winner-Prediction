from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Dummy player statistics data (replace with actual data)
player_stats_data = {
    'Player': ['Player 1', 'Player 2'],
    'Runs': [1200, 800],
    'Wickets': [50, 30],
    'Batting_Avg': [40.5, 35.2],
    'Bowling_Avg': [25.3, 28.7],
    'Strike_Rate': [120, 110]
}

# Dummy player performance data for radar chart (replace with actual data)
player_performance_data = {
    'Player': ['Player 1', 'Player 2'],
    'Condition_A': [80, 70],
    'Condition_B': [90, 85],
    'Condition_C': [75, 80],
    # Add more conditions as needed
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_player = request.form['player_select']

        # Filter player statistics data for the selected player
        player_stats = pd.DataFrame(player_stats_data)
        selected_player_stats = player_stats[player_stats['Player'] == selected_player]

        # Create radar chart for player performance
        player_performance = pd.DataFrame(player_performance_data)
        selected_player_performance = player_performance[player_performance['Player'] == selected_player]
        fig = px.line_polar(selected_player_performance, r=selected_player_performance.iloc[:, 1:].values.flatten(), theta=selected_player_performance.columns[1:], line_close=True)
        fig.update_traces(fill='toself')

        return render_template('index.html', selected_player=selected_player, player_stats=selected_player_stats.to_dict('records'), radar_chart=fig.to_html(include_plotlyjs=False, full_html=False))

    # If no player is selected, render the template with empty data
    return render_template('index.html', selected_player=None, player_stats=None, radar_chart=None)

if __name__ == '__main__':
    app.run(debug=True)
