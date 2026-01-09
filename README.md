# Knowledge Decay Predictor

## Overview
The Knowledge Decay Predictor is a machine learning-based system that models how human memory weakens over time when topics are not revised. The project predicts a learner’s memory strength for different topics and provides personalized revision recommendations.

Unlike traditional academic prediction systems that focus only on grades, this project focuses on understanding the *forgetting process itself* and optimizing revision schedules for long-term retention.

## Problem Statement
Human memory naturally decays over time. If a topic is not revised at the right moment, it is likely to be forgotten. This project aims to:
- Predict how strongly a learner remembers a topic
- Identify topics that are at risk of being forgotten
- Recommend the best time to revise each topic

## How It Works
1. A synthetic dataset is created with realistic learning patterns
2. Feature engineering is applied to model memory decay behavior
3. Regression models are trained to predict memory strength
4. Multiple models are evaluated and compared
5. A recommendation layer converts predictions into actions:
   - Revise Now
   - Revise Soon
   - Safe

## Features
- Memory strength prediction using regression models
- Feature engineering for time-based decay modeling
- Model evaluation and comparison
- Personalized revision recommendations
- Visual analysis of forgetting patterns

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Why This Project Is Unique
Most ML projects focus only on classification or score prediction. This project models **human memory behavior**, making it more realistic, insightful, and practically useful.

It can be extended to:
- Smart study planners
- Personalized learning platforms
- Spaced repetition systems



