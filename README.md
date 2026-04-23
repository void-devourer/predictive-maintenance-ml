# Predictive Maintenance System - Industrial Machine Failure Detection

## Overview
A Machine Learning system that predicts industrial machine failures using 
physics-based feature engineering. Built by combining Mechanical Engineering 
domain knowledge with Data Science techniques.

## Live Dashboard
Built with Streamlit - allows maintenance teams to input sensor readings 
and get instant failure predictions with recommended actions.

## Key Results
- 80% failure detection rate
- Only 1 false alarm per 2000 observations
- Physics features contributed 39% of model's predictive power
- 99% reduction in false alarms compared to baseline model

## Physics-Based Features
Three new features derived from Mechanical Engineering principles:

| Feature | Formula | Insight |
|---------|---------|---------|
| Power_Watts | Torque × RPM × π/30 | Overpowered motors fail faster |
| Temp_Difference | Process Temp - Air Temp | Low value = poor heat dissipation |
| Wear_Strain | Tool Wear × Torque | Combined effect of age and stress |

## Model Comparison
| Model | Failures Detected | False Alarms |
|-------|------------------|--------------|
| Logistic Regression (baseline) | 50/61 | 284 |
| Logistic Regression (tuned) | 43/61 | 147 |
| **Random Forest + Physics Features** | **49/61** | **1** |

## Key Finding
Physics-based feature engineering completely changed model selection.
Without physics features, Logistic Regression was best. After adding
physics features, Random Forest achieved similar detection with 284x
fewer false alarms.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

## Dataset
AI4I 2020 Predictive Maintenance Dataset
- 10,000 machine observations
- Features: Temperature, Rotational Speed, Torque, Tool Wear

## Real World Impact
In a factory with 10,000 machines:
- Detects ~800 of every 1000 failing machines
- Near zero false alerts
- Specific recommended actions for each failure type

## Author
Piyush Kumar
B.Tech Mechanical Engineering
IIT Goa



