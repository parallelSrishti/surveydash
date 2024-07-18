import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime

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

    # Assume +1 for any response to the 10th question
    total_score += 1 if survey.question10 else 0

    return total_score
