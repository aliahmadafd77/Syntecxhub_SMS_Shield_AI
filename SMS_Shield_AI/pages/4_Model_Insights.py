# ============================================================
# SMS SHIELD AI
# MODEL INSIGHTS
# PREMIUM ML INTELLIGENCE CENTER
# ============================================================

from pathlib import Path
import json

import joblib
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SMS Shield AI | Model Insights",
    page_icon="🛡️",
    layout="wide",
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "spam_detection_final_pipeline.joblib"
)

THRESHOLD_PATH = (
    BASE_DIR /
    "decision_threshold.json"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        return None

    try:
        return joblib.load(MODEL_PATH)

    except Exception:
        return None


# ============================================================
# LOAD THRESHOLD
# ============================================================

@st.cache_data
def load_threshold():

    if not THRESHOLD_PATH.exists():
        return None

    try:

        with open(
            THRESHOLD_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


        if isinstance(
            data,
            (int, float)
        ):

            return float(data)


        if isinstance(data, dict):

            possible_keys = [
                "threshold",
                "decision_threshold",
                "optimized_threshold",
                "best_threshold",
                "optimal_threshold",
            ]


            for key in possible_keys:

                if key in data:

                    try:
                        return float(data[key])

                    except (
                        TypeError,
                        ValueError
                    ):
                        pass


            for value in data.values():

                if isinstance(
                    value,
                    (int, float)
                ):

                    return float(value)

    except Exception:
        pass


    return None


model = load_model()

threshold = load_threshold()


# ============================================================
# PREMIUM PAGE CSS
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       HERO
       ======================================================== */

    .insights-hero-premium {

        position: relative;
        overflow: hidden;

        padding: 36px 40px;

        border-radius: 24px;

        background:
            linear-gradient(
                125deg,
                #494D5F 0%,
                #414555 55%,
                #343746 100%
            );

        border:
            1px solid #5A5F70;

        box-shadow:
            0 18px 45px
            rgba(45,52,65,.17);
    }


    .insights-hero-premium::after {

        content: "";

        position: absolute;

        width: 400px;
        height: 400px;

        right: -180px;
        top: -210px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(22,135,199,.27),
                rgba(118,86,168,.14),
                transparent 70%
            );
    }


    .insights-hero-content {

        position: relative;
        z-index: 2;
    }


    .insights-eyebrow-premium {

        color: #8DD1F2;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;
    }


    .insights-title-premium {

        margin-top: 8px;

        color: #FFFFFF;

        font-size: 38px;

        line-height: 1.05;

        font-weight: 900;

        letter-spacing: -1.4px;
    }


    .insights-description-premium {

        max-width: 720px;

        margin-top: 10px;

        color: #D2D6DE;

        font-size: 9px;

        line-height: 1.75;
    }


    .hero-engine-state {

        display: inline-flex;

        align-items: center;

        gap: 7px;

        margin-top: 17px;

        padding: 7px 10px;

        border-radius: 999px;

        background:
            rgba(79,138,104,.20);

        border:
            1px solid
            rgba(110,177,139,.32);

        color:
            #B8E0C8;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .8px;
    }


    .hero-engine-dot {

        width: 6px;
        height: 6px;

        border-radius: 50%;

        background: #6EB18B;

        box-shadow:
            0 0 0 4px
            rgba(110,177,139,.10);

        animation:
            enginePulse 2s ease-in-out infinite;
    }


    @keyframes enginePulse {

        0%, 100% {
            opacity: 1;
        }

        50% {
            opacity: .45;
        }
    }


    /* ========================================================
       SECTION
       ======================================================== */

    .insights-section {

        margin-top: 30px;

        margin-bottom: 13px;
    }


    .insights-section-title {

        color: #343746;

        font-size: 17px;

        font-weight: 900;

        letter-spacing: -.3px;
    }


    .insights-section-subtitle {

        margin-top: 3px;

        color: #858B98;

        font-size: 8px;
    }


    /* ========================================================
       MODEL STATUS
       ======================================================== */

    .model-status-card {

        display: flex;

        align-items: center;

        gap: 12px;

        margin-top: 19px;

        padding: 15px 18px;

        border-radius: 15px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 5px 17px
            rgba(45,52,65,.055);

        animation:
            statusIn .35s ease both;
    }


    @keyframes statusIn {

        from {
            opacity: 0;
            transform: translateY(6px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    .status-dot {

        width: 8px;
        height: 8px;

        flex-shrink: 0;

        border-radius: 50%;

        background: #4F8A68;

        box-shadow:
            0 0 0 5px
            rgba(79,138,104,.10);

        animation:
            statusPulse 2s infinite;
    }


    @keyframes statusPulse {

        0%, 100% {
            opacity: 1;
        }

        50% {
            opacity: .5;
        }
    }


    .status-title {

        color: #454A57;

        font-size: 8px;

        font-weight: 900;
    }


    .status-text {

        margin-top: 2px;

        color: #8A919D;

        font-size: 7px;
    }


    /* ========================================================
       PERFORMANCE CARDS
       ======================================================== */

    .insight-metric {

        min-height: 116px;

        padding: 19px;

        border-radius: 17px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 5px 18px
            rgba(45,52,65,.06);

        transition:
            transform .22s ease,
            box-shadow .22s ease,
            border-color .22s ease;
    }


    .insight-metric:hover {

        transform:
            translateY(-4px);

        border-color:
            #C6D7E2;

        box-shadow:
            0 14px 32px
            rgba(45,52,65,.10);
    }


    .insight-metric-label {

        color: #89919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: 1px;

        text-transform: uppercase;
    }


    .insight-metric-value {

        margin-top: 7px;

        color: #343746;

        font-size: 27px;

        font-weight: 900;

        letter-spacing: -.8px;
    }


    .insight-metric-note {

        margin-top: 3px;

        color: #9AA1AB;

        font-size: 7px;
    }


    /* ========================================================
       PIPELINE
       ======================================================== */

    .pipeline-card {

        padding: 24px;

        border-radius: 20px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 8px 25px
            rgba(45,52,65,.065);
    }


    .pipeline-title {

        color: #343746;

        font-size: 16px;

        font-weight: 900;
    }


    .pipeline-subtitle {

        margin-top: 4px;

        margin-bottom: 16px;

        color: #89919D;

        font-size: 8px;

        line-height: 1.7;
    }


    .pipeline-step {

        display: flex;

        gap: 12px;

        padding: 13px 0;

        border-bottom:
            1px solid #E9EDF1;
    }


    .pipeline-step:last-child {
        border-bottom: none;
    }


    .pipeline-number {

        width: 30px;
        height: 30px;

        flex-shrink: 0;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 9px;

        background: #F0EBF8;

        border:
            1px solid #DCCFF0;

        color: #7656A8;

        font-size: 7px;

        font-weight: 900;
    }


    .pipeline-name {

        color: #454A57;

        font-size: 8px;

        font-weight: 900;
    }


    .pipeline-description {

        margin-top: 3px;

        color: #89919D;

        font-size: 7px;

        line-height: 1.65;
    }


    /* ========================================================
       CONFIGURATION
       ======================================================== */

    .config-card {

        padding: 24px;

        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                #F8FAFB,
                #EEF2F5
            );

        border:
            1px solid #D7DEE5;

        box-shadow:
            0 7px 23px
            rgba(45,52,65,.055);
    }


    .config-title {

        color: #343746;

        font-size: 16px;

        font-weight: 900;
    }


    .config-subtitle {

        margin-top: 4px;

        margin-bottom: 13px;

        color: #89919D;

        font-size: 8px;

        line-height: 1.7;
    }


    .config-row {

        display: flex;

        justify-content: space-between;

        gap: 12px;

        padding: 11px 0;

        border-bottom:
            1px solid #DCE2E8;
    }


    .config-row:last-child {
        border-bottom: none;
    }


    .config-label {

        color: #7D8793;

        font-size: 7px;
    }


    .config-value {

        color: #454A57;

        font-size: 7px;

        font-weight: 900;

        text-align: right;
    }


    .config-ready {
        color: #4F8A68;
    }


    /* ========================================================
       THRESHOLD
       ======================================================== */

    .threshold-card {

        padding: 23px;

        border-radius: 19px;

        background:
            linear-gradient(
                135deg,
                #EEF6FB,
                #F3F0F8
            );

        border:
            1px solid #D9E2EC;

        box-shadow:
            0 7px 23px
            rgba(45,52,65,.055);
    }


    .threshold-label {

        color: #7D8793;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .9px;

        text-transform: uppercase;
    }


    .threshold-value {

        margin-top: 6px;

        color: #1687C7;

        font-size: 30px;

        font-weight: 900;

        letter-spacing: -.8px;
    }


    .threshold-description {

        margin-top: 5px;

        color: #77818D;

        font-size: 7px;

        line-height: 1.7;
    }


    /* ========================================================
       RUNTIME CARD
       ======================================================== */

    .runtime-card {

        padding: 20px;

        border-radius: 17px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 5px 18px
            rgba(45,52,65,.055);
    }


    .runtime-row {

        display: flex;

        justify-content: space-between;

        gap: 12px;

        padding: 10px 0;

        border-bottom:
            1px solid #E9EDF1;
    }


    .runtime-row:last-child {
        border-bottom: none;
    }


    .runtime-label {

        color: #89919D;

        font-size: 7px;
    }


    .runtime-value {

        max-width: 62%;

        color: #454A57;

        font-size: 7px;

        font-weight: 900;

        text-align: right;

        word-break: break-word;
    }


    /* ========================================================
       INFORMATION NOTE
       ======================================================== */

    .insight-note {

        margin-top: 16px;

        padding: 15px 17px;

        border-radius: 14px;

        background: #F4F6F8;

        border:
            1px solid #DDE3E8;

        color: #707984;

        font-size: 7px;

        line-height: 1.75;
    }


    .insight-note strong {
        color: #454A57;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .insights-footer {

        margin-top: 38px;

        padding-top: 15px;

        border-top:
            1px solid #DDE2E8;

        text-align: center;

        color: #9AA1AB;

        font-size: 7px;

        letter-spacing: .5px;
    }

    </style>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    f"""
    <div class="insights-hero-premium">

        <div class="insights-hero-content">

            <div class="insights-eyebrow-premium">
                MACHINE LEARNING INTELLIGENCE
            </div>

            <div class="insights-title-premium">
                Model Insights
            </div>

            <div class="insights-description-premium">
                Explore the machine-learning architecture,
                evaluation performance and active configuration
                powering SMS Shield AI.
            </div>

            <div class="hero-engine-state">

                <span class="hero-engine-dot"></span>

                {
                    "MODEL ENGINE READY"
                    if model is not None
                    else "MODEL ENGINE UNAVAILABLE"
                }

            </div>

        </div>

    </div>
    """
)


# ============================================================
# MODEL STATUS
# ============================================================

if model is not None:

    st.html(
        """
        <div class="model-status-card">

            <div class="status-dot"></div>

            <div>

                <div class="status-title">
                    Detection model loaded successfully
                </div>

                <div class="status-text">
                    The application is connected to the saved
                    machine-learning pipeline.
                </div>

            </div>

        </div>
        """
    )

else:

    st.error(
        "Detection model could not be loaded."
    )


# ============================================================
# PERFORMANCE
# ============================================================

st.html(
    """
    <div class="insights-section">

        <div class="insights-section-title">
            Evaluation Performance
        </div>

        <div class="insights-section-subtitle">
            Reported evaluation results of the trained model
        </div>

    </div>
    """
)


metrics = [
    (
        "Accuracy",
        "99.13%",
        "Overall classification",
    ),
    (
        "Precision",
        "99.17%",
        "Positive prediction quality",
    ),
    (
        "F1 Score",
        "96.39%",
        "Precision / recall balance",
    ),
    (
        "ROC-AUC",
        "99.87%",
        "Model discrimination",
    ),
]


metric_columns = st.columns(
    4,
    gap="medium",
)


for column, metric in zip(
    metric_columns,
    metrics,
):

    with column:

        st.html(
            f"""
            <div class="insight-metric">

                <div class="insight-metric-label">
                    {metric[0]}
                </div>

                <div class="insight-metric-value">
                    {metric[1]}
                </div>

                <div class="insight-metric-note">
                    {metric[2]}
                </div>

            </div>
            """
        )


# ============================================================
# DETECTION PIPELINE
# ============================================================

st.html(
    """
    <div class="insights-section">

        <div class="insights-section-title">
            Detection Pipeline
        </div>

        <div class="insights-section-subtitle">
            From raw SMS text to the final security decision
        </div>

    </div>
    """
)


pipeline_column, config_column = st.columns(
    [1.25, .85],
    gap="large",
)


# ============================================================
# PIPELINE
# ============================================================

with pipeline_column:

    st.html(
        """
        <div class="pipeline-card">

            <div class="pipeline-title">
                How the Model Works
            </div>

            <div class="pipeline-subtitle">
                SMS Shield AI transforms incoming text into
                numerical features and evaluates them using
                a trained classification model.
            </div>


            <div class="pipeline-step">

                <div class="pipeline-number">
                    01
                </div>

                <div>

                    <div class="pipeline-name">
                        SMS Input
                    </div>

                    <div class="pipeline-description">
                        The original message enters the
                        security analysis pipeline.
                    </div>

                </div>

            </div>


            <div class="pipeline-step">

                <div class="pipeline-number">
                    02
                </div>

                <div>

                    <div class="pipeline-name">
                        Character TF-IDF
                    </div>

                    <div class="pipeline-description">
                        Character-level text patterns are
                        transformed into numerical features.
                    </div>

                </div>

            </div>


            <div class="pipeline-step">

                <div class="pipeline-number">
                    03
                </div>

                <div>

                    <div class="pipeline-name">
                        Linear SVM
                    </div>

                    <div class="pipeline-description">
                        The trained classifier evaluates the
                        extracted feature representation.
                    </div>

                </div>

            </div>


            <div class="pipeline-step">

                <div class="pipeline-number">
                    04
                </div>

                <div>

                    <div class="pipeline-name">
                        Security Classification
                    </div>

                    <div class="pipeline-description">
                        The final prediction is returned as
                        HAM or SPAM.
                    </div>

                </div>

            </div>

        </div>
        """
    )


# ============================================================
# CONFIGURATION
# ============================================================

with config_column:

    st.html(
        f"""
        <div class="config-card">

            <div class="config-title">
                Model Configuration
            </div>

            <div class="config-subtitle">
                Active configuration detected by the application.
            </div>


            <div class="config-row">

                <span class="config-label">
                    Classifier
                </span>

                <strong class="config-value">
                    Linear SVM
                </strong>

            </div>


            <div class="config-row">

                <span class="config-label">
                    Features
                </span>

                <strong class="config-value">
                    Character TF-IDF
                </strong>

            </div>


            <div class="config-row">

                <span class="config-label">
                    Task
                </span>

                <strong class="config-value">
                    Binary Classification
                </strong>

            </div>


            <div class="config-row">

                <span class="config-label">
                    Classes
                </span>

                <strong class="config-value">
                    HAM / SPAM
                </strong>

            </div>


            <div class="config-row">

                <span class="config-label">
                    Model
                </span>

                <strong class="config-value config-ready">
                    {
                        "Loaded"
                        if model is not None
                        else "Unavailable"
                    }
                </strong>

            </div>


            <div class="config-row">

                <span class="config-label">
                    Threshold
                </span>

                <strong class="config-value config-ready">
                    {
                        "Available"
                        if threshold is not None
                        else "Unavailable"
                    }
                </strong>

            </div>

        </div>
        """
    )


# ============================================================
# DECISION CONFIGURATION
# ============================================================

st.html(
    """
    <div class="insights-section">

        <div class="insights-section-title">
            Decision Configuration
        </div>

        <div class="insights-section-subtitle">
            Saved threshold and decision-boundary information
        </div>

    </div>
    """
)


threshold_column, boundary_column = st.columns(
    [.65, 1.35],
    gap="large",
)


# ============================================================
# THRESHOLD
# ============================================================

with threshold_column:

    threshold_display = (
        f"{threshold:.5f}"
        if threshold is not None
        else "Unavailable"
    )


    st.html(
        f"""
        <div class="threshold-card">

            <div class="threshold-label">
                Optimized Threshold
            </div>

            <div class="threshold-value">
                {threshold_display}
            </div>

            <div class="threshold-description">
                Saved threshold configuration detected
                by the application.
            </div>

        </div>
        """
    )


# ============================================================
# DECISION BOUNDARY
# ============================================================

with boundary_column:

    st.html(
        """
        <div class="pipeline-card">

            <div class="pipeline-title">
                Decision Boundary
            </div>

            <div class="pipeline-subtitle">
                The classifier produces a decision score for
                the submitted SMS. The configured threshold
                represents the saved decision configuration.
            </div>

            <div class="insight-note">

                <strong>Why this matters:</strong>

                The threshold provides an additional layer of
                transparency when explaining how the trained
                classification system makes its final decision.

            </div>

        </div>
        """
    )


# ============================================================
# RUNTIME INFORMATION
# ============================================================

if model is not None:

    st.html(
        """
        <div class="insights-section">

            <div class="insights-section-title">
                Runtime Information
            </div>

            <div class="insights-section-subtitle">
                Information detected from the loaded model object
            </div>

        </div>
        """
    )


    runtime_1, runtime_2 = st.columns(
        2,
        gap="medium",
    )


    with runtime_1:

        st.html(
            f"""
            <div class="runtime-card">

                <div class="runtime-row">

                    <span class="runtime-label">
                        Object Type
                    </span>

                    <strong class="runtime-value">
                        {type(model).__name__}
                    </strong>

                </div>


                <div class="runtime-row">

                    <span class="runtime-label">
                        Python Module
                    </span>

                    <strong class="runtime-value">
                        {type(model).__module__}
                    </strong>

                </div>

            </div>
            """
        )


    with runtime_2:

        st.html(
            """
            <div class="runtime-card">

                <div class="runtime-row">

                    <span class="runtime-label">
                        Saved Model
                    </span>

                    <strong class="runtime-value">
                        spam_detection_final_pipeline.joblib
                    </strong>

                </div>


                <div class="runtime-row">

                    <span class="runtime-label">
                        Runtime Status
                    </span>

                    <strong class="runtime-value">
                        Ready
                    </strong>

                </div>

            </div>
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="insights-footer">

        SMS SHIELD AI
        &nbsp; • &nbsp;
        MACHINE LEARNING INTELLIGENCE
        &nbsp; • &nbsp;
        CHARACTER TF-IDF + LINEAR SVM

    </div>
    """
)