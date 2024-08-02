# Cricket Data Fetcher

## Overview

  - Cricket Data Fetcher is a Python-based application that leverages the Crickbuzz API to provide real-time updates on cricket matches, news, and ICC rankings. This command-line interface (CLI) tool is designed to deliver a comprehensive and interactive user experience by retrieving and displaying various cricket-related information. The application utilizes the Requests library for API interactions and PrettyPrinter for organized output formatting.

## Features

  ### HomeFeed
  
   **Latest News**: Fetches and displays the most recent cricket news articles with detailed information such as headlines, context, introductions, and news IDs.
   **ScoreBoard**: Provides detailed information on ongoing and completed matches, including match descriptions, formats, IDs, types, series names, current statuses, and final statuses. Additionally, it displays teams, venues, and scorecards with runs, wickets, and overs.
  
  ### MatchesFeed
  **Live Matches**: Retrieves and displays information about live cricket matches, including match types, series names, match descriptions, formats, IDs, statuses, teams, venues, and scorecards.
  **Upcoming Matches**: Displays upcoming matches categorized into International, League, Domestic, and Women’s cricket. Provides match descriptions, formats, IDs, series names, statuses, teams, and venues.
  
  ### News
  - Fetches and displays recent cricket news articles, including context, summaries, headlines, news IDs, and sources.
  
  ### ICC Rankings
  **1:Batsman:** Shows rankings for batsmen, including rank, name, country, average, rating, and trend.
  **2:Bowler:** Shows rankings for bowlers, including rank, name, country, average, rating, and trend.
  **3:All-Rounder:** Shows rankings for all-rounders, including rank, name, country, average, rating, and trend.
  **4:Teams:** Displays team rankings, including rank, name, matches, points, and rating.
  
  ## Usage
  ### Requirements
  - Python 3.x
  - Requests library (pip install requests)
  - PrettyPrinter library (part of the Python standard library)

  ### How to Run
  - Clone the repository or download the source code.
  - Install the required libraries using pip:

        pip install requests

        python cricket_data_fetcher.py
  
  ### Navigation
  
  - The application presents a main menu with options to view Home, Matches, News, and ICC Rankings.
  - Users can select options by entering the corresponding index number.
  - For quitting the application, users can enter 'q' at any time.

### Code Overview
  #### HomeFeed()
  - Fetches data from the Crickbuzz home API endpoint.
  - Displays latest news or scoreboard based on user selection.
  - Iterates through the fetched data and prints detailed information.
  #### matchesfeed()
  - Fetches live or upcoming matches from the Crickbuzz API.
  - Displays match details based on user selection.
  - Provides options to filter upcoming matches by category (International, League, Domestic, Women).
  #### news()
  - Fetches and displays recent news articles from the Crickbuzz API.
  - Iterates through the fetched data and prints detailed information.
  #### iccrank()
  - Fetches ICC rankings for batsmen, bowlers, all-rounders, or teams from the Crickbuzz API.
  - Displays rankings based on user-selected category and format (Test, ODI, T20).
  #### main()
  - Main function that presents the menu and handles user input.
  - Calls appropriate functions based on user selection.
  #### API Integration
  - Utilizes the Crickbuzz API to fetch cricket data.
  - Uses an API key for authentication, set in the headers.

### Conclusion
Cricket Data Fetcher is an interactive CLI tool designed for cricket enthusiasts who want real-time updates and detailed information about matches, news, and rankings. The application demonstrates the effective use of APIs and Python programming to deliver a comprehensive user experience.
