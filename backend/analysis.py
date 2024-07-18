import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_reports(reports):
    scores = []
    dates = []
    
    for report in reports:
        total_score = report.total_score
        scores.append(total_score)
        dates.append(report.date_posted.strftime('%Y-%m-%d'))  # Format dates for the chart
    
    analysis_result = {
        'current_score': scores[-1] if scores else 0,
        'dates': dates,
        'scores': scores
    }
    return analysis_result

def calculate_total_score(survey):
    total_score = 0
    responses = [
        survey.question1, survey.question2, survey.question3, survey.question4, survey.question5,
        survey.question6, survey.question7, survey.question8, survey.question9
    ]
    
    for response in responses:
        if response == '1':
            total_score += -1
        elif response == '2':
            total_score += 0
        elif response == '3':
            total_score += 1

    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(survey.question10)['compound']
    
    # Adjust the score based on sentiment analysis
    if sentiment_score >= 0.05:
        total_score += 1
    elif sentiment_score <= -0.05:
        total_score += -1


    return total_score
