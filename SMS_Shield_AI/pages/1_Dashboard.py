# ============================================================
# SMS SHIELD AI
# PREMIUM SECURITY COMMAND CENTER
# DASHBOARD
# ============================================================

from pathlib import Path
from datetime import datetime

import html
import joblib
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SMS Shield AI | Dashboard",
    page_icon="🛡️",
    layout="wide",
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "spam_detection_final_pipeline.joblib"


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

if "dashboard_result" not in st.session_state:
    st.session_state.dashboard_result = None


# ============================================================
# DASHBOARD MICRO CSS
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       PREMIUM HERO
       ======================================================== */

    .premium-hero {
        position: relative;
        overflow: hidden;

        padding: 38px 42px;

        border-radius: 24px;

        background:
            linear-gradient(
                125deg,
                #494D5F 0%,
                #414555 55%,
                #343746 100%
            );

        border:
            1px solid #5B6071;

        box-shadow:
            0 20px 50px
            rgba(45,52,65,.18);
    }


    .premium-hero::before {

        content: "";

        position: absolute;

        width: 430px;
        height: 430px;

        right: -170px;
        top: -230px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(22,135,199,.28),
                rgba(118,86,168,.13),
                transparent 70%
            );
    }


    .premium-hero::after {

        content: "";

        position: absolute;

        width: 180px;
        height: 180px;

        right: 210px;
        bottom: -130px;

        border-radius: 50%;

        background:
            rgba(118,86,168,.10);
    }


    .hero-content {

        position: relative;
        z-index: 2;
    }


    .hero-top {

        display: flex;
        justify-content: space-between;
        align-items: flex-start;

        gap: 30px;
    }


    .hero-eyebrow {

        color: #8DD1F2;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2.2px;

        text-transform: uppercase;
    }


    .hero-title {

        margin-top: 9px;

        color: #FFFFFF;

        font-size: 40px;

        line-height: 1.05;

        font-weight: 900;

        letter-spacing: -1.5px;
    }


    .hero-description {

        max-width: 680px;

        margin-top: 12px;

        color: #D7DAE1;

        font-size: 10px;

        line-height: 1.75;
    }


    .hero-status {

        display: inline-flex;

        align-items: center;

        gap: 8px;

        margin-top: 19px;

        padding: 7px 11px;

        border-radius: 999px;

        background: rgba(79,138,104,.20);

        border: 1px solid rgba(110,177,139,.35);

        color: #B8E0C8;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .8px;
    }


    .hero-status-dot {

        width: 6px;
        height: 6px;

        border-radius: 50%;

        background: #6EB18B;

        box-shadow:
            0 0 0 4px
            rgba(110,177,139,.12);

        animation:
            livePulse 2s infinite;
    }


    @keyframes livePulse {

        0%,100% {
            opacity: 1;
            transform: scale(1);
        }

        50% {
            opacity: .55;
            transform: scale(.72);
        }
    }


    .hero-side {

        min-width: 185px;

        padding: 17px;

        border-radius: 15px;

        background:
            rgba(255,255,255,.065);

        border:
            1px solid
            rgba(255,255,255,.10);

        backdrop-filter:
            blur(12px);
    }


    .hero-side-label {

        color: #AEB4C0;

        font-size: 6px;

        font-weight: 850;

        letter-spacing: 1px;

        text-transform: uppercase;
    }


    .hero-side-value {

        margin-top: 7px;

        color: #FFFFFF;

        font-size: 17px;

        font-weight: 900;
    }


    .hero-side-detail {

        margin-top: 3px;

        color: #AAB0BB;

        font-size: 7px;
    }


    /* ========================================================
       SECTION HEADER
       ======================================================== */

    .section-head {

        margin-top: 30px;
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
       METRICS
       ======================================================== */

    .metric-card {

        position: relative;

        overflow: hidden;

        min-height: 118px;

        padding: 19px;

        border-radius: 17px;

        background: #FFFFFF;

        border: 1px solid #DDE2E8;

        box-shadow:
            0 5px 18px
            rgba(45,52,65,.06);

        transition:
            transform .22s ease,
            box-shadow .22s ease,
            border-color .22s ease;
    }


    .metric-card:hover {

        transform:
            translateY(-4px);

        border-color:
            #C6D7E2;

        box-shadow:
            0 14px 32px
            rgba(45,52,65,.11);
    }


    .metric-card::after {

        content: "";

        position: absolute;

        width: 70px;
        height: 70px;

        right: -27px;
        bottom: -28px;

        border-radius: 50%;

        background:
            rgba(22,135,199,.055);
    }


    .metric-top {

        display: flex;

        justify-content: space-between;

        align-items: center;
    }


    .metric-label {

        color: #8A919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: 1px;

        text-transform: uppercase;
    }


    .metric-icon {

        width: 24px;
        height: 24px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 8px;

        background: #EAF5FB;

        border: 1px solid #D2E8F4;

        color: #1687C7;

        font-size: 9px;

        font-weight: 900;
    }


    .metric-value {

        margin-top: 8px;

        color: #292D38;

        font-size: 27px;

        font-weight: 900;

        letter-spacing: -.9px;
    }


    .metric-note {

        margin-top: 3px;

        color: #9AA1AB;

        font-size: 7px;
    }


    /* ========================================================
       COMMAND CENTER
       ======================================================== */

    .command-card {

        padding: 25px;

        border-radius: 20px;

        background: #FFFFFF;

        border: 1px solid #DDE2E8;

        box-shadow:
            0 9px 28px
            rgba(45,52,65,.07);
    }


    .command-badge {

        display: inline-flex;

        align-items: center;

        gap: 6px;

        padding: 5px 9px;

        border-radius: 999px;

        background: #EAF5FB;

        border: 1px solid #D2E8F4;

        color: #155A7A;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .7px;

        text-transform: uppercase;
    }


    .command-title {

        margin-top: 11px;

        color: #292D38;

        font-size: 21px;

        font-weight: 900;

        letter-spacing: -.5px;
    }


    .command-description {

        margin-top: 5px;
        margin-bottom: 16px;

        color: #7D8592;

        font-size: 8px;

        line-height: 1.65;
    }


    /* ========================================================
       ENGINE PANEL
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

        border: 1px solid #D7DEE5;

        box-shadow:
            0 7px 23px
            rgba(45,52,65,.055);
    }


    .engine-header {

        display: flex;

        justify-content: space-between;

        align-items: flex-start;

        gap: 12px;
    }


    .engine-title {

        color: #343746;

        font-size: 15px;

        font-weight: 900;
    }


    .engine-subtitle {

        margin-top: 4px;

        color: #8A919D;

        font-size: 7px;
    }


    .engine-online {

        padding: 5px 8px;

        border-radius: 999px;

        background: #EAF4EE;

        border: 1px solid #CDE2D5;

        color: #4F8A68;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .5px;
    }


    .engine-row {

        display: flex;

        justify-content: space-between;

        align-items: center;

        gap: 8px;

        padding: 11px 0;

        border-bottom:
            1px solid #DCE2E8;
    }


    .engine-row:last-child {
        border-bottom: none;
    }


    .engine-label {

        color: #8A919D;

        font-size: 7px;
    }


    .engine-value {

        color: #454A57;

        font-size: 7px;

        font-weight: 850;

        text-align: right;
    }


    /* ========================================================
       RESULT
       ======================================================== */

    .result-card {

        margin-top: 17px;

        padding: 20px;

        border-radius: 17px;

        animation:
            resultIn .35s ease both;
    }


    @keyframes resultIn {

        from {
            opacity: 0;
            transform: translateY(8px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }


    .result-spam {

        background:
            linear-gradient(
                135deg,
                #FFF4F4,
                #FBEDEE
            );

        border: 1px solid #EACDD0;
    }


    .result-ham {

        background:
            linear-gradient(
                135deg,
                #F0F7F3,
                #E8F2EC
            );

        border: 1px solid #CDE2D5;
    }


    .result-label {

        font-size: 7px;

        font-weight: 900;

        letter-spacing: 1px;
    }


    .result-title {

        margin-top: 4px;

        font-size: 24px;

        font-weight: 900;

        letter-spacing: -.6px;
    }


    .result-spam .result-label,
    .result-spam .result-title {
        color: #C95757;
    }


    .result-ham .result-label,
    .result-ham .result-title {
        color: #4F8A68;
    }


    .result-text {

        margin-top: 5px;

        color: #707784;

        font-size: 8px;

        line-height: 1.65;
    }


    /* ========================================================
       SECURITY FLOW
       ======================================================== */

    .flow-card {

        min-height: 155px;

        padding: 21px;

        border-radius: 17px;

        background: #FFFFFF;

        border: 1px solid #DDE2E8;

        box-shadow:
            0 5px 18px
            rgba(45,52,65,.055);

        transition:
            transform .22s ease,
            box-shadow .22s ease;
    }


    .flow-card:hover {

        transform:
            translateY(-4px);

        box-shadow:
            0 13px 28px
            rgba(45,52,65,.09);
    }


    .flow-number {

        width: 34px;
        height: 34px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 10px;

        background: #F0EBF8;

        border: 1px solid #DCCFF0;

        color: #7656A8;

        font-size: 10px;

        font-weight: 900;
    }


    .flow-title {

        margin-top: 12px;

        color: #454A57;

        font-size: 10px;

        font-weight: 900;
    }


    .flow-text {

        margin-top: 5px;

        color: #8A929D;

        font-size: 7px;

        line-height: 1.7;
    }


    /* ========================================================
       DASHBOARD FOOTER
       ======================================================== */

    .dashboard-footer {

        margin-top: 38px;

        padding-top: 16px;

        border-top:
            1px solid #DDE2E8;

        text-align: center;

        color: #9AA1AB;

        font-size: 7px;

        letter-spacing: .5px;
    }


    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 850px) {

        .hero-top {
            flex-direction: column;
        }

        .hero-side {
            width: 100%;
        }

        .hero-title {
            font-size: 32px;
        }
    }

    </style>
    """
)


# ============================================================
# HELPER
# ============================================================

def safe_text(value):

    return html.escape(str(value))


# ============================================================
# MODEL STATUS
# ============================================================

model_online = model is not None

status_text = (
    "DETECTION ENGINE OPERATIONAL"
    if model_online
    else "DETECTION ENGINE UNAVAILABLE"
)


# ============================================================
# HERO
# ============================================================

st.html(
    f"""
    <div class="premium-hero">

        <div class="hero-content">

            <div class="hero-top">

                <div>

                    <div class="hero-eyebrow">
                        AI SECURITY COMMAND CENTER
                    </div>

                    <div class="hero-title">
                        SMS Shield AI
                    </div>

                    <div class="hero-description">
                        Intelligent SMS threat detection powered by
                        character-level text intelligence and a trained
                        Linear SVM classification engine.
                    </div>

                    <div class="hero-status">

                        <span class="hero-status-dot"></span>

                        {status_text}

                    </div>

                </div>


                <div class="hero-side">

                    <div class="hero-side-label">
                        Detection Engine
                    </div>

                    <div class="hero-side-value">
                        {"Online" if model_online else "Offline"}
                    </div>

                    <div class="hero-side-detail">
                        Character TF-IDF + Linear SVM
                    </div>

                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# PERFORMANCE SECTION
# ============================================================

st.html(
    """
    <div class="section-head">

        <div class="section-title">
            Model Performance
        </div>

        <div class="section-subtitle">
            Final evaluation results from the trained detection system
        </div>

    </div>
    """
)


# ============================================================
# METRICS
# ============================================================

metrics = [
    ("Accuracy", "99.13%", "Overall classification", "A"),
    ("Precision", "99.17%", "Positive prediction quality", "P"),
    ("F1 Score", "96.39%", "Precision / recall balance", "F"),
    ("ROC-AUC", "99.87%", "Model discrimination", "R"),
]


metric_columns = st.columns(4, gap="medium")


for column, metric in zip(metric_columns, metrics):

    with column:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-top">

                    <div class="metric-label">
                        {metric[0]}
                    </div>

                    <div class="metric-icon">
                        {metric[3]}
                    </div>

                </div>

                <div class="metric-value">
                    {metric[1]}
                </div>

                <div class="metric-note">
                    {metric[2]}
                </div>

            </div>
            """
        )


# ============================================================
# COMMAND CENTER HEADER
# ============================================================

st.html(
    """
    <div class="section-head">

        <div class="section-title">
            Security Command Center
        </div>

        <div class="section-subtitle">
            Run a live classification directly from the dashboard
        </div>

    </div>
    """
)


# ============================================================
# MAIN WORKSPACE
# ============================================================

left_column, right_column = st.columns(
    [1.42, .78],
    gap="large"
)


# ============================================================
# SMS ANALYZER
# ============================================================

with left_column:

    st.html(
        """
        <div class="command-card">

            <div class="command-badge">
                <span>●</span>
                LIVE ANALYSIS
            </div>

            <div class="command-title">
                Analyze an SMS
            </div>

            <div class="command-description">
                Enter a message below and let the trained detection
                engine determine whether it is legitimate or potentially
                unwanted.
            </div>

        </div>
        """
    )


    sms = st.text_area(
        "SMS Message",
        placeholder=(
            "Paste or type the SMS message you want to analyze..."
        ),
        height=150,
        label_visibility="collapsed",
        key="dashboard_sms_input",
    )


    analyze_clicked = st.button(
        "Analyze Message",
        type="primary",
        use_container_width=True,
    )


    # ========================================================
    # ANALYSIS
    # ========================================================

    if analyze_clicked:

        if not sms.strip():

            st.warning(
                "Please enter an SMS message first."
            )

        elif model is None:

            st.error(
                "The detection model could not be loaded."
            )

        else:

            with st.spinner("Analyzing message..."):

                try:

                    message = sms.strip()

                    prediction = model.predict(
                        [message]
                    )[0]


                    # ----------------------------------------
                    # NORMALIZE PREDICTION
                    # ----------------------------------------

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


                    # ----------------------------------------
                    # OPTIONAL DECISION SCORE
                    # ----------------------------------------

                    decision_score = None

                    try:

                        if hasattr(
                            model,
                            "decision_function"
                        ):

                            raw_score = model.decision_function(
                                [message]
                            )

                            if hasattr(
                                raw_score,
                                "__len__"
                            ):

                                decision_score = float(
                                    raw_score[0]
                                )

                            else:

                                decision_score = float(
                                    raw_score
                                )

                    except Exception:

                        decision_score = None


                    # ----------------------------------------
                    # TIMESTAMP
                    # ----------------------------------------

                    timestamp = (
                        datetime.now()
                        .strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    )


                    # ----------------------------------------
                    # HISTORY
                    # ----------------------------------------

                    st.session_state.scan_history.append(
                        {
                            "Message": message,

                            "Prediction": result,

                            "Risk": (
                                "HIGH"
                                if result == "SPAM"
                                else "LOW"
                            ),

                            "Decision Score": (
                                f"{decision_score:.5f}"
                                if decision_score is not None
                                else "N/A"
                            ),

                            "Timestamp": timestamp,
                        }
                    )


                    # ----------------------------------------
                    # DASHBOARD RESULT
                    # ----------------------------------------

                    st.session_state.dashboard_result = {

                        "result": result,

                        "message": message,

                        "decision_score": (
                            decision_score
                        ),

                        "timestamp": timestamp,
                    }


                    st.rerun()


                except Exception as error:

                    st.error(
                        f"Analysis failed: {error}"
                    )


    # ========================================================
    # RESULT
    # ========================================================

    result_data = (
        st.session_state.dashboard_result
    )


    if result_data is not None:

        result = result_data["result"]


        if result == "SPAM":

            result_class = "result-spam"

            title = "SPAM DETECTED"

            description = (
                "The detection engine classified this "
                "message as potentially unwanted or fraudulent."
            )

        else:

            result_class = "result-ham"

            title = "LEGITIMATE MESSAGE"

            description = (
                "The detection engine classified this "
                "message as a legitimate SMS."
            )


        score = result_data.get(
            "decision_score"
        )


        score_text = (
            f"Decision score: {score:.5f}"
            if score is not None
            else "Decision score unavailable"
        )


        st.html(
            f"""
            <div class="result-card {result_class}">

                <div class="result-label">
                    ANALYSIS COMPLETE
                </div>

                <div class="result-title">
                    {title}
                </div>

                <div class="result-text">
                    {description}
                    &nbsp; {score_text}
                </div>

            </div>
            """
        )


# ============================================================
# DETECTION ENGINE PANEL
# ============================================================

with right_column:

    st.html(
        f"""
        <div class="engine-card">

            <div class="engine-header">

                <div>

                    <div class="engine-title">
                        Detection Engine
                    </div>

                    <div class="engine-subtitle">
                        Active machine-learning configuration
                    </div>

                </div>

                <div class="engine-online">
                    {"ONLINE" if model_online else "OFFLINE"}
                </div>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Features
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
                    Classes
                </span>

                <span class="engine-value">
                    HAM / SPAM
                </span>

            </div>


            <div class="engine-row">

                <span class="engine-label">
                    Model File
                </span>

                <span class="engine-value">
                    {"Loaded" if model_online else "Missing"}
                </span>

            </div>

        </div>
        """
    )


# ============================================================
# QUICK ACTIVITY
# ============================================================

history_count = len(
    st.session_state.scan_history
)

spam_count = sum(
    1
    for item in st.session_state.scan_history
    if str(
        item.get("Prediction", "")
    ).upper() == "SPAM"
)

ham_count = sum(
    1
    for item in st.session_state.scan_history
    if str(
        item.get("Prediction", "")
    ).upper() == "HAM"
)


st.html(
    """
    <div class="section-head">

        <div class="section-title">
            Security Activity
        </div>

        <div class="section-subtitle">
            Current analysis activity in this session
        </div>

    </div>
    """
)


activity_columns = st.columns(
    3,
    gap="medium"
)


activity_data = [
    (
        "TOTAL SCANS",
        str(history_count),
        "Messages analyzed",
        "T",
    ),
    (
        "THREATS FOUND",
        str(spam_count),
        "Potential spam detections",
        "S",
    ),
    (
        "LEGITIMATE",
        str(ham_count),
        "HAM classifications",
        "H",
    ),
]


for column, item in zip(
    activity_columns,
    activity_data
):

    with column:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-top">

                    <div class="metric-label">
                        {item[0]}
                    </div>

                    <div class="metric-icon">
                        {item[3]}
                    </div>

                </div>

                <div class="metric-value">
                    {item[1]}
                </div>

                <div class="metric-note">
                    {item[2]}
                </div>

            </div>
            """
        )


# ============================================================
# HOW THE SYSTEM WORKS
# ============================================================

st.html(
    """
    <div class="section-head">

        <div class="section-title">
            How SMS Shield AI Works
        </div>

        <div class="section-subtitle">
            Three stages from incoming text to security decision
        </div>

    </div>
    """
)


flow_columns = st.columns(
    3,
    gap="medium"
)


flow_steps = [

    (
        "01",
        "Message Input",
        "The user enters or pastes the SMS that needs to be inspected."
    ),

    (
        "02",
        "Text Intelligence",
        "Character-level TF-IDF transforms the message into machine-learning features."
    ),

    (
        "03",
        "Security Decision",
        "The trained Linear SVM evaluates the extracted features and returns the final class."
    ),
]


for column, step in zip(
    flow_columns,
    flow_steps
):

    with column:

        st.html(
            f"""
            <div class="flow-card">

                <div class="flow-number">
                    {step[0]}
                </div>

                <div class="flow-title">
                    {step[1]}
                </div>

                <div class="flow-text">
                    {step[2]}
                </div>

            </div>
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="dashboard-footer">

        SMS SHIELD AI
        &nbsp; • &nbsp;
        AI SMS THREAT INTELLIGENCE
        &nbsp; • &nbsp;
        CHARACTER TF-IDF + LINEAR SVM

    </div>
    """
)