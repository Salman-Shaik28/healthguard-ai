---
title: HealthGuard-AI
emoji: 🛡️
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# 🛡️ HealthGuard-AI - Intelligent Disease Prediction

An AI-powered health protection system that predicts possible diseases based on symptoms using advanced machine learning.

![Demo](https://img.shields.io/badge/Status-Live-brightgreen)
![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Health](https://img.shields.io/badge/Health-AI%20Assistant-success)

## 🔍 Overview

HealthGuard-AI is your intelligent health protection companion that analyzes symptom patterns to suggest possible medical conditions. Built with a robust Random Forest classifier, it provides instant predictions with confidence scores to help you make informed health decisions.

## 🚀 Features

- **🛡️ AI Health Protection**: Advanced ML model for accurate disease prediction
- **📊 Confidence Metrics**: Transparent probability scores for each prediction
- **🔬 Multi-Condition Analysis**: Identifies top 3 possible diseases
- **⚡ Real-Time Screening**: Instant results with comprehensive analysis
- **🎯 Intuitive Interface**: Simple symptom selection with organized categories

## 🩺 How to Use

1. **Select Symptoms**: Choose from 50+ medical symptoms using checkboxes
2. **AI Analysis**: HealthGuard's ML model processes your symptom patterns
3. **Get Insights**: Receive detailed prediction with confidence levels and alternative possibilities

## 🏗️ Technical Architecture

### Core Model
- **Algorithm**: Ensemble Random Forest Classifier
- **Input Features**: 50+ binary symptom indicators
- **Output**: Multi-class disease prediction with probabilities
- **Performance**: High-accuracy medical screening

### Data Processing
- Advanced feature selection
- Label encoding for disease classification
- Probability calibration for reliable confidence scoring

## 💻 Local Installation

```bash
# Clone and setup
git clone https://github.com/Salman-Shaik28/HealthGuard-AI
cd HealthGuard-AI

# Install dependencies
pip install -r requirements.txt

# Launch application
python app.py
