# ============================================================
# SMS SHIELD AI
# ANALYZE SMS
# PREMIUM THREAT ANALYSIS WORKSPACE
# ============================================================

from pathlib import Path
from datetime import datetime
import math

import joblib
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SMS Shield AI | Analyze",
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


# ============================================================
# MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        return None

    try:
        return joblib.load(MODEL_PATH)

    except Exception:
        return None


model = load_model()


# ============================================================
# SESSION STATE
# ============================================================

if "scan_history" not in st.session_state:
    st.session_state.scan_history = []

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "analysis_message" not in st.session_state:
    st.session_state.analysis_message = ""


# ============================================================
# PAGE DESIGN
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       HERO
       ======================================================== */

    .analyze-hero {

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


    .analyze-hero::after {

        content: "";

        position: absolute;

        width: 390px;
        height: 390px;

        right: -175px;
        top: -205px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(22,135,199,.27),
                rgba(118,86,168,.14),
                transparent 70%
            );
    }


    .analyze-hero-content {

        position: relative;
        z-index: 2;
    }


    .analyze-eyebrow {

        color: #8DD1F2;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;
    }


    .analyze-title {

        margin-top: 8px;

        color: #FFFFFF;

        font-size: 38px;

        line-height: 1.05;

        font-weight: 900;

        letter-spacing: -1.4px;
    }


    .analyze-description {

        max-width: 700px;

        margin-top: 10px;

        color: #D2D6DE;

        font-size: 9px;

        line-height: 1.75;
    }


    .analyze-hero-status {

        display: inline-flex;

        align-items: center;

        gap: 7px;

        margin-top: 16px;

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


    .hero-dot {

        width: 6px;
        height: 6px;

        border-radius: 50%;

        background: #6EB18B;

        box-shadow:
            0 0 0 4px
            rgba(110,177,139,.10);
    }


    /* ========================================================
       SECTION
       ======================================================== */

    .section-head {

        margin-top: 29px;

        margin-bottom: 13px;
    }


    .section-title {

        color: #343746;

        font-size: 17px;

        font-weight: 900;

        letter-spacing: -.3px;
    }


    .section-subtitle {

        margin-top: 3px;

        color: #858B98;

        font-size: 8px;
    }


    /* ========================================================
       ANALYSIS WORKSPACE
       ======================================================== */

    .workspace-card {

        padding: 25px;

        border-radius: 20px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 9px 28px
            rgba(45,52,65,.07);
    }


    .workspace-badge {

        display: inline-flex;

        align-items: center;

        gap: 6px;

        padding: 5px 9px;

        border-radius: 999px;

        background: #EAF5FB;

        border:
            1px solid #D2E8F4;

        color: #155A7A;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .8px;
    }


    .workspace-title {

        margin-top: 11px;

        color: #292D38;

        font-size: 20px;

        font-weight: 900;

        letter-spacing: -.5px;
    }


    .workspace-description {

        margin-top: 5px;

        color: #7D8592;

        font-size: 8px;

        line-height: 1.7;
    }


    /* ========================================================
       EXAMPLES
       ======================================================== */

    .examples-title {

        margin-top: 16px;

        margin-bottom: 8px;

        color: #8A919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .9px;

        text-transform: uppercase;
    }


    /* ========================================================
       ENGINE
       ======================================================== */

    .engine-card {

        padding: 23px;

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
            rgba(45,52,65,.06);
    }


    .engine-header {

        display: flex;

        justify-content: space-between;

        align-items: flex-start;

        gap: 12px;
    }


    .engine-name {

        color: #343746;

        font-size: 15px;

        font-weight: 900;
    }


    .engine-caption {

        margin-top: 4px;

        color: #8A919D;

        font-size: 7px;
    }


    .engine-status {

        padding: 5px 8px;

        border-radius: 999px;

        background: #EAF4EE;

        border:
            1px solid #CDE2D5;

        color: #4F8A68;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .5px;
    }


    .engine-row {

        display: flex;

        justify-content: space-between;

        align-items: center;

        gap: 10px;

        padding: 11px 0;

        border-bottom:
            1px solid #DCE2E8;
    }


    .engine-row:last-child {
        border-bottom: none;
    }


    .engine-label {

        color: #89919D;

        font-size: 7px;
    }


    .engine-value {

        color: #454A57;

        font-size: 7px;

        font-weight: 850;

        text-align: right;
    }


    /* ========================================================
       ANALYSIS RESULT
       ======================================================== */

    .analysis-result {

        margin-top: 20px;

        padding: 24px;

        border-radius: 20px;

        animation:
            resultReveal .38s ease both;
    }


    @keyframes resultReveal {

        from {
            opacity: 0;
            transform:
                translateY(9px)
                scale(.99);
        }

        to {
            opacity: 1;
            transform:
                translateY(0)
                scale(1);
        }
    }


    .spam-result {

        background:
            linear-gradient(
                135deg,
                #FFF4F4,
                #FBEDEE
            );

        border:
            1px solid #EACDD0;
    }


    .ham-result {

        background:
            linear-gradient(
                135deg,
                #F0F7F3,
                #E8F2EC
            );

        border:
            1px solid #CDE2D5;
    }


    .result-status {

        font-size: 7px;

        font-weight: 900;

        letter-spacing: 1px;
    }


    .result-title {

        margin-top: 5px;

        font-size: 29px;

        font-weight: 900;

        letter-spacing: -.8px;
    }


    .spam-result .result-status,
    .spam-result .result-title {

        color: #C95757;
    }


    .ham-result .result-status,
    .ham-result .result-title {

        color: #4F8A68;
    }


    .result-description {

        margin-top: 5px;

        color: #707784;

        font-size: 8px;

        line-height: 1.7;
    }


    /* ========================================================
       RESULT METRICS
       ======================================================== */

    .result-metric {

        min-height: 88px;

        padding: 16px;

        border-radius: 14px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 4px 13px
            rgba(45,52,65,.045);
    }


    .result-metric-label {

        color: #8A919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .8px;

        text-transform: uppercase;
    }


    .result-metric-value {

        margin-top: 7px;

        color: #343746;

        font-size: 19px;

        font-weight: 900;
    }


    /* ========================================================
       MESSAGE PREVIEW
       ======================================================== */

    .message-preview {

        margin-top: 18px;

        padding: 17px;

        border-radius: 14px;

        background:
            rgba(255,255,255,.70);

        border:
            1px solid rgba(221,226,232,.9);
    }


    .message-preview-label {

        color: #8A919D;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .9px;

        text-transform: uppercase;
    }


    .message-preview-text {

        margin-top: 7px;

        color: #505664;

        font-size: 8px;

        line-height: 1.7;

        word-break: break-word;
    }


    /* ========================================================
       INFO NOTE
       ======================================================== */

    .info-note {

        margin-top: 18px;

        padding: 15px 17px;

        border-radius: 13px;

        background: #F0F3F6;

        border:
            1px solid #DCE2E8;

        color: #737B87;

        font-size: 7px;

        line-height: 1.7;
    }


    .info-note strong {
        color: #454A57;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .page-footer {

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

engine_online = model is not None

st.html(
    f"""
    <div class="analyze-hero">

        <div class="analyze-hero-content">

            <div class="analyze-eyebrow">
                THREAT ANALYSIS WORKSPACE
            </div>

            <div class="analyze-title">
                Analyze SMS
            </div>

            <div class="analyze-description">
                Inspect a message using the trained SMS Shield AI
                detection engine and receive an immediate security
                classification.
            </div>

            <div class="analyze-hero-status">

                <span class="hero-dot"></span>

                {
                    "DETECTION ENGINE READY"
                    if engine_online
                    else "MODEL UNAVAILABLE"
                }

            </div>

        </div>

    </div>
    """
)


# ============================================================
# WORKSPACE
# ============================================================

st.html(
    """
    <div class="section-head">

        <div class="section-title">
            Message Security Analysis
        </div>

        <div class="section-subtitle">
            Submit the original SMS for the most meaningful classification
        </div>

    </div>
    """
)


left, right = st.columns(
    [1.42, .78],
    gap="large"
)


# ============================================================
# LEFT — INPUT
# ============================================================

with left:

    st.html(
        """
        <div class="workspace-card">

            <div class="workspace-badge">
                <span>●</span>
                LIVE ANALYSIS
            </div>

            <div class="workspace-title">
                Enter SMS Message
            </div>

            <div class="workspace-description">
                Paste or type the complete message below.
                Keep the original wording, links and numbers
                whenever possible.
            </div>

        </div>
        """
    )


    message = st.text_area(
        "SMS message",
        placeholder=(
            "Paste or type the SMS message here..."
        ),
        height=180,
        label_visibility="collapsed",
        key="analysis_message_input",
    )


    # ========================================================
    # QUICK EXAMPLES
    # ========================================================

    st.html(
        """
        <div class="examples-title">
            Quick test messages
        </div>
        """
    )


    ex1, ex2 = st.columns(
        2,
        gap="small"
    )


    with ex1:

        if st.button(
            "Suspicious Example",
            use_container_width=True,
        ):

            st.session_state.analysis_message = (
                "Congratulations! You have won "
                "a cash prize. Click this link "
                "to claim your reward now."
            )

            st.rerun()


    with ex2:

        if st.button(
            "Normal Example",
            use_container_width=True,
        ):

            st.session_state.analysis_message = (
                "Your appointment is confirmed "
                "for tomorrow at 10 AM."
            )

            st.rerun()


    # ========================================================
    # LOAD EXAMPLE INTO TEXT AREA
    # ========================================================

    if st.session_state.analysis_message:

        st.info(
            "Example selected. Copy it into the message field "
            "above, then run the analysis."
        )


    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    analyze_clicked = st.button(
        "Analyze Message",
        type="primary",
        use_container_width=True,
    )


# ============================================================
# RIGHT — ENGINE
# ============================================================

with right:

    st.html(
        f"""
        <div class="engine-card">

            <div class="engine-header">

                <div>

                    <div class="engine-name">
                        Detection Engine
                    </div>

                    <div class="engine-caption">
                        Active machine-learning pipeline
                    </div>

                </div>

                <div class="engine-status">
                    {"ONLINE" if engine_online else "OFFLINE"}
                </div>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Feature extraction
                </span>

                <span class="engine-value">
                    Character TF-IDF
                </span>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Classifier
                </span>

                <span class="engine-value">
                    Linear SVM
                </span>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Classification
                </span>

                <span class="engine-value">
                    Binary
                </span>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Classes
                </span>

                <span class="engine-value">
                    HAM / SPAM
                </span>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Model status
                </span>

                <span class="engine-value">
                    {"Loaded" if engine_online else "Missing"}
                </span>

            </div>

        </div>
        """
    )


# ============================================================
# RUN ANALYSIS
# ============================================================

if analyze_clicked:

    if not message.strip():

        st.warning(
            "Please enter an SMS message before analyzing."
        )

    elif model is None:

        st.error(
            "The detection model could not be loaded."
        )

    else:

        with st.spinner("Analyzing message..."):

            try:

                clean_message = message.strip()

                # --------------------------------------------
                # PREDICTION
                # --------------------------------------------

                prediction = model.predict(
                    [clean_message]
                )[0]


                prediction_text = (
                    str(prediction)
                    .strip()
                    .lower()
                )


                if prediction_text in {
                    "spam",
                    "1",
                    "true",
                    "yes",
                }:

                    result = "SPAM"

                elif prediction_text in {
                    "ham",
                    "0",
                    "false",
                    "no",
                }:

                    result = "HAM"

                else:

                    result = prediction_text.upper()


                # --------------------------------------------
                # SPAM PROBABILITY / CONFIDENCE
                # --------------------------------------------

                score = None

                try:

                    if hasattr(
                        model,
                        "predict_proba"
                    ):

                        probabilities = (
                            model.predict_proba(
                                [clean_message]
                            )[0]
                        )

                        classes = list(
                            model.classes_
                        )

                        spam_index = None

                        for index, class_name in enumerate(
                            classes
                        ):

                            class_text = (
                                str(class_name)
                                .strip()
                                .lower()
                            )

                            if class_text in {
                                "spam",
                                "1",
                                "true",
                                "yes",
                            }:

                                spam_index = index
                                break

                        if spam_index is not None:

                            score = float(
                                probabilities[
                                    spam_index
                                ]
                            )

                    # Fallback for Linear SVM.
                    if (
                        score is None
                        and hasattr(
                            model,
                            "decision_function"
                        )
                    ):

                        raw_score = (
                            model.decision_function(
                                [clean_message]
                            )
                        )

                        try:
                            decision_score = float(
                                raw_score[0]
                            )

                        except Exception:
                            decision_score = float(
                                raw_score
                            )

                        # Confidence indicator for SVM.
                        # This is not a calibrated probability.
                        score = (
                            1.0 /
                            (
                                1.0 +
                                math.exp(
                                    -abs(
                                        decision_score
                                    )
                                )
                            )
                        )

                except Exception:

                    score = None


                # --------------------------------------------
                # RISK
                # --------------------------------------------

                risk = (
                    "HIGH"
                    if result == "SPAM"
                    else "LOW"
                )


                # --------------------------------------------
                # TIMESTAMP
                # --------------------------------------------

                timestamp = (
                    datetime.now()
                    .strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )


                # --------------------------------------------
                # HISTORY
                # --------------------------------------------

                st.session_state.scan_history.append(
                    {
                        "Message": clean_message,

                        "Prediction": result,

                        "Risk": risk,

                        "Spam Probability": (
                            f"{score:.5f}"
                            if score is not None
                            else "N/A"
                        ),

                        "Timestamp": timestamp,
                    }
                )


                # --------------------------------------------
                # RESULT
                # --------------------------------------------

                st.session_state.analysis_result = {

                    "result": result,

                    "risk": risk,

                    "score": score,

                    "message": clean_message,

                    "timestamp": timestamp,
                }


                st.rerun()


            except Exception as error:

                st.error(
                    f"Analysis failed: {error}"
                )


# ============================================================
# DISPLAY RESULT
# ============================================================

result_data = (
    st.session_state.analysis_result
)


if result_data is not None:

    result = result_data["result"]

    risk = result_data["risk"]

    score = result_data["score"]

    analyzed_message = (
        result_data["message"]
    )


    # ========================================================
    # RESULT CONTENT
    # ========================================================

    if result == "SPAM":

        result_class = "spam-result"

        result_title = "SPAM DETECTED"

        result_description = (
            "The detection engine identified this message "
            "as potentially unwanted, suspicious or fraudulent."
        )

    else:

        result_class = "ham-result"

        result_title = "LEGITIMATE MESSAGE"

        result_description = (
            "The detection engine identified this message "
            "as a legitimate SMS."
        )


    # ========================================================
    # RESULT HEADER
    # ========================================================

    st.html(
        f"""
        <div class="analysis-result {result_class}">

            <div class="result-status">
                ANALYSIS COMPLETE
            </div>

            <div class="result-title">
                {result_title}
            </div>

            <div class="result-description">
                {result_description}
            </div>

        </div>
        """
    )


    # ========================================================
    # RESULT METRICS
    # ========================================================

    c1, c2, c3 = st.columns(
        3,
        gap="medium"
    )


    with c1:

        st.html(
            f"""
            <div class="result-metric">

                <div class="result-metric-label">
                    Risk Level
                </div>

                <div class="result-metric-value">
                    {risk}
                </div>

            </div>
            """
        )


    with c2:

        score_text = (
            f"{score:.5f}"
            if score is not None
            else "N/A"
        )

        st.html(
            f"""
            <div class="result-metric">

                <div class="result-metric-label">
                    Spam Probability
                </div>

                <div class="result-metric-value">
                    {score_text}
                </div>

            </div>
            """
        )


    with c3:

        st.html(
            """
            <div class="result-metric">

                <div class="result-metric-label">
                    Classifier
                </div>

                <div class="result-metric-value">
                    Linear SVM
                </div>

            </div>
            """
        )


    # ========================================================
    # MESSAGE PREVIEW
    # ========================================================

    safe_message = (
        analyzed_message
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#039;")
    )


    st.html(
        f"""
        <div class="message-preview">

            <div class="message-preview-label">
                Analyzed Message
            </div>

            <div class="message-preview-text">
                {safe_message}
            </div>

        </div>
        """
    )


    # ========================================================
    # SUMMARY
    # ========================================================

    st.html(
        f"""
        <div class="info-note">

            <strong>Classification summary:</strong>

            The submitted SMS passed through the
            Character TF-IDF + Linear SVM pipeline
            and was classified as <strong>{result}</strong>.

            This scan has been added to the current
            session history.

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="page-footer">

        SMS SHIELD AI
        &nbsp; • &nbsp;
        THREAT ANALYSIS WORKSPACE
        &nbsp; • &nbsp;
        CHARACTER TF-IDF + LINEAR SVM

    </div>
    """
)
