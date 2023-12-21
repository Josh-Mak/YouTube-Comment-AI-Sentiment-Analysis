# YouTube-Comment-AI-Sentiment-Analysis
A simple data analysis project that uses AI to analyze the positivity of YouTube comments.

**Intro**: I made this project because I wanted to play around with Googles new LLM (gemini-pro), and I wanted to explore different API's and learn how to use them to collect data (in this case, YouTube API). 

**Technical Overview**: This project has 3 main sections.
  1. Data Collection: Using YouTube's API, the program first generates a list of all videos from a certain channel, and then grabs a list of every comment for each video on that channel.
  2. LLM Setup: The large language model (Gemini-Pro) is setup, with a specific base prompt that uses few shot prompting to ensure it produces only a single numerical value as response.
  3. Data Analysis: Each comment is run through the LLM and given a score based on how "positive" the comment is.

**Future Improvements**: Most of the improvement in this project will come in the analysis part. I did not focus on very detailed analysis, but rather set the project up so that it allows for easy editing of the data collection, and/or prompting to allow for analysis on any metric(s) that the YouTube API provides.
