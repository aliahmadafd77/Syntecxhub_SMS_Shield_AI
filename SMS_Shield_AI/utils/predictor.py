# ============================================================
# SMS SHIELD AI
# PREDICTION ENGINE
# ============================================================

from pathlib import Path
import json

import joblib


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_ROOT /
    "spam_detection_final_pipeline.joblib"
)

THRESHOLD_PATH = (
    PROJECT_ROOT /
    "decision_threshold.json"
)


# ============================================================
# LOAD MODEL
# ============================================================

def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"Model file not found:\n{MODEL_PATH}"
        )

    return joblib.load(
        MODEL_PATH
    )


# ============================================================
# LOAD OPTIMIZED THRESHOLD
# ============================================================

def load_threshold():

    if not THRESHOLD_PATH.exists():

        raise FileNotFoundError(
            f"Threshold file not found:\n{THRESHOLD_PATH}"
        )

    with open(
        THRESHOLD_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    if "optimized_threshold" in data:

        return float(
            data["optimized_threshold"]
        )

    if "threshold" in data:

        return float(
            data["threshold"]
        )

    for value in data.values():

        if isinstance(
            value,
            (int, float)
        ):

            return float(value)

    raise ValueError(
        "No numeric decision threshold found "
        "in decision_threshold.json"
    )


# ============================================================
# TEXT PREPARATION
# ============================================================

def prepare_message(message):

    if message is None:

        raise ValueError(
            "Message cannot be empty."
        )

    message = str(
        message
    ).strip()

    if not message:

        raise ValueError(
            "Message cannot be empty."
        )

    return message


# ============================================================
# IDENTIFY SPAM CLASS
# ============================================================

def get_spam_class_index(model):

    classifier = (
        model.named_steps["classifier"]
    )

    classes = classifier.classes_

    for index, value in enumerate(classes):

        text = str(
            value
        ).strip().lower()

        if text in {
            "spam",
            "1",
            "true",
            "yes"
        }:

            return index

    if set(classes) == {0, 1}:

        return list(classes).index(1)

    raise ValueError(
        f"Unable to identify SPAM class. "
        f"Model classes: {classes}"
    )


# ============================================================
# SINGLE SMS PREDICTION
# ============================================================

def predict_message(
    message,
    model,
    threshold
):

    message = prepare_message(
        message
    )

    # --------------------------------------------------------
    # GET CLASS PROBABILITIES
    # --------------------------------------------------------

    probabilities = (
        model.predict_proba(
            [message]
        )[0]
    )

    spam_index = (
        get_spam_class_index(
            model
        )
    )

    spam_probability = float(
        probabilities[
            spam_index
        ]
    )

    ham_probability = float(
        1.0 -
        spam_probability
    )


    # --------------------------------------------------------
    # OPTIMIZED THRESHOLD DECISION
    # --------------------------------------------------------

    prediction = int(
        spam_probability >= threshold
    )


    # --------------------------------------------------------
    # FINAL LABEL
    # --------------------------------------------------------

    if prediction == 1:

        label = "SPAM"

    else:

        label = "HAM"


    # --------------------------------------------------------
    # DECISION MARGIN
    # --------------------------------------------------------

    margin = abs(
        spam_probability -
        threshold
    )


    # --------------------------------------------------------
    # CONFIDENCE INDICATOR
    #
    # This is a decision confidence indicator,
    # NOT a calibrated probability.
    # --------------------------------------------------------

    confidence_indicator = min(
        99.9,
        50.0 +
        (
            margin * 100.0
        )
    )


    # --------------------------------------------------------
    # RISK CLASSIFICATION
    # --------------------------------------------------------

    if prediction == 1:

        if spam_probability >= 0.90:

            risk_level = "Very High"

        elif spam_probability >= 0.75:

            risk_level = "High"

        elif spam_probability >= threshold:

            risk_level = "Moderate"

        else:

            risk_level = "Low"

    else:

        if spam_probability <= 0.10:

            risk_level = "Very Low"

        elif spam_probability <= 0.25:

            risk_level = "Low"

        elif spam_probability < threshold:

            risk_level = "Moderate"

        else:

            risk_level = "High"


    # --------------------------------------------------------
    # RETURN COMPLETE ANALYSIS
    # --------------------------------------------------------

    return {

        "label":
            label,

        "prediction":
            prediction,

        "decision_score":
            spam_probability,

        "spam_probability":
            spam_probability,

        "ham_probability":
            ham_probability,

        "threshold":
            threshold,

        "margin":
            margin,

        "confidence":
            confidence_indicator,

        "risk_level":
            risk_level,

        "message":
            message
    }


# ============================================================
# HIGH-LEVEL SMS ANALYSIS
# ============================================================

def analyze_sms(
    message,
    model=None,
    threshold=None
):

    if model is None:

        model = load_model()


    if threshold is None:

        threshold = load_threshold()


    return predict_message(
        message=message,
        model=model,
        threshold=threshold
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

def get_model_information():

    model_available = (
        MODEL_PATH.exists()
    )

    threshold_available = (
        THRESHOLD_PATH.exists()
    )

    return {

        "model_name":
            "SMS Spam Detection",

        "feature_extraction":
            "Character-level TF-IDF",

        "classifier":
            "Logistic Regression",

        "task":
            "Binary Text Classification",

        "classes":
            [
                "HAM",
                "SPAM"
            ],

        "model_file":
            MODEL_PATH.name,

        "threshold_file":
            THRESHOLD_PATH.name,

        "model_available":
            model_available,

        "threshold_available":
            threshold_available
    }


# ============================================================
# MODEL STATUS
# ============================================================

def is_model_ready():

    return (
        MODEL_PATH.exists()
        and
        THRESHOLD_PATH.exists()
    )


# ============================================================
# QUICK MODEL VALIDATION
# ============================================================

def validate_model():

    if not MODEL_PATH.exists():

        return {
            "ready": False,
            "message": "Model file not found."
        }


    if not THRESHOLD_PATH.exists():

        return {
            "ready": False,
            "message": "Decision threshold file not found."
        }


    try:

        model = load_model()

        threshold = load_threshold()

        classifier = (
            model.named_steps["classifier"]
        )

        classifier_name = type(
            classifier
        ).__name__


        if classifier_name != "LogisticRegression":

            return {

                "ready": False,

                "message":
                    (
                        "Unexpected classifier: "
                        f"{classifier_name}"
                    )
            }


        return {

            "ready": True,

            "message":
                "Logistic Regression model loaded successfully.",

            "classifier":
                classifier_name,

            "threshold":
                threshold,

            "model_file":
                MODEL_PATH.name,

            "threshold_file":
                THRESHOLD_PATH.name
        }


    except Exception as error:

        return {

            "ready": False,

            "message":
                str(error)
        }