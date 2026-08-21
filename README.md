# SMS Shield AI

## Intelligent SMS Spam Detection System

SMS Shield AI is a machine learning-based web application designed to detect whether an SMS message is **HAM (Legitimate)** or **SPAM (Suspicious/Unwanted)**.

The system uses **Character-level TF-IDF feature extraction** with a **Linear SVM classifier** to analyze SMS messages and provide a security classification.

---

## Project Overview

SMS Shield AI provides a simple security workspace where users can:

- Analyze individual SMS messages
- Detect SPAM and HAM messages
- View risk levels
- Review scan history
- Explore model information and performance
- View the active detection pipeline

The application is developed using Python and Streamlit.

---

## Machine Learning Pipeline

The detection system follows this pipeline:

```text
SMS Message
     ↓
Character-level TF-IDF
     ↓
Linear SVM Classifier
     ↓
Decision Score
     ↓
Optimized Threshold
     ↓
HAM / SPAM Classification
