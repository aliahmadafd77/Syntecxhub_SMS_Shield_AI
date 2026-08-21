# ============================================================
# SMS SHIELD AI
# APPLICATION ENTRY POINT
# ============================================================

from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SMS Shield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

CSS_PATH = BASE_DIR / "assets" / "style.css"

MODEL_PATH = (
    BASE_DIR
    / "spam_detection_final_pipeline.joblib"
)

THRESHOLD_PATH = (
    BASE_DIR
    / "decision_threshold.json"
)


# ============================================================
# LOAD GLOBAL CSS
# ============================================================

def load_global_css():

    if not CSS_PATH.exists():
        return

    try:

        css = CSS_PATH.read_text(
            encoding="utf-8"
        )

        st.html(
            f"""
            <style>
            {css}
            </style>
            """
        )

    except Exception:
        pass


load_global_css()


# ============================================================
# SYSTEM STATUS
# ============================================================

model_ready = MODEL_PATH.exists()

threshold_ready = THRESHOLD_PATH.exists()


if model_ready:

    engine_text = "ONLINE"
    engine_class = "sidebar-status-online"

else:

    engine_text = "OFFLINE"
    engine_class = "sidebar-status-offline"


threshold_text = (
    "Configured"
    if threshold_ready
    else "Unavailable"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # ========================================================
    # BRAND
    # ========================================================

    st.html(
        """
        <div class="sidebar-brand">

            <div class="sidebar-brand-icon">
                🛡️
            </div>

            <div class="sidebar-brand-content">

                <div class="sidebar-brand-name">
                    SMS Shield AI
                </div>

                <div class="sidebar-brand-subtitle">
                    INTELLIGENT SMS SECURITY
                </div>

            </div>

        </div>
        """
    )


    # ========================================================
    # WORKSPACE LABEL
    # ========================================================

    st.html(
        """
        <div class="sidebar-label">
            WORKSPACE
        </div>
        """
    )


    # ========================================================
    # DETECTION ENGINE
    # ========================================================

    st.html(
        f"""
        <div class="sidebar-engine-card">

            <div class="sidebar-engine-top">

                <div>

                    <div class="sidebar-engine-title">
                        Detection Engine
                    </div>

                    <div class="sidebar-engine-model">
                        Character TF-IDF + Linear SVM
                    </div>

                </div>


                <div class="{engine_class}">

                    <span class="sidebar-status-dot"></span>

                    {engine_text}

                </div>

            </div>


            <div class="sidebar-engine-divider"></div>


            <div class="sidebar-engine-meta">

                <span>
                    Model
                </span>

                <strong>
                    {
                        "Loaded"
                        if model_ready
                        else "Unavailable"
                    }
                </strong>

            </div>


            <div class="sidebar-engine-meta">

                <span>
                    Threshold
                </span>

                <strong>
                    {threshold_text}
                </strong>

            </div>

        </div>
        """
    )


    # ========================================================
    # SYSTEM LABEL
    # ========================================================

    st.html(
        """
        <div class="sidebar-label sidebar-label-system">
            SYSTEM
        </div>
        """
    )


    # ========================================================
    # SYSTEM SUMMARY
    # ========================================================

    st.html(
        """
        <div class="sidebar-system-card">

            <div class="sidebar-system-row">

                <span>
                    Classifier
                </span>

                <strong>
                    Linear SVM
                </strong>

            </div>


            <div class="sidebar-system-row">

                <span>
                    Features
                </span>

                <strong>
                    Character TF-IDF
                </strong>

            </div>


            <div class="sidebar-system-row">

                <span>
                    Classes
                </span>

                <strong>
                    HAM / SPAM
                </strong>

            </div>

        </div>
        """
    )


    # ========================================================
    # PLATFORM NOTE
    # ========================================================

    st.html(
        """
        <div class="sidebar-platform-note">

            <div class="sidebar-platform-kicker">
                SMS SECURITY PLATFORM
            </div>

            <div class="sidebar-platform-text">
                Analyze messages, review scan activity,
                and inspect the machine learning engine.
            </div>

        </div>
        """
    )


    # ========================================================
    # SIDEBAR FOOTER
    # ========================================================

    st.html(
        """
        <div class="sidebar-footer">

            <div class="sidebar-footer-title">
                SMS SHIELD AI
            </div>

            <div>
                Machine Learning Security Platform
            </div>

            <span>
                v1.0 • Detection Engine
            </span>

        </div>
        """
    )


# ============================================================
# APPLICATION PAGES
# ============================================================

dashboard_page = st.Page(
    "pages/1_Dashboard.py",
    title="Dashboard",
    icon=":material/home:",
    default=True,
)


analyze_page = st.Page(
    "pages/2_Analyze_SMS.py",
    title="Analyze SMS",
    icon=":material/search:",
)


history_page = st.Page(
    "pages/3_Scan_History.py",
    title="Scan History",
    icon=":material/history:",
)


insights_page = st.Page(
    "pages/4_Model_Insights.py",
    title="Model Insights",
    icon=":material/psychology:",
)


# ============================================================
# NAVIGATION
# ============================================================

navigation = st.navigation(
    [
        dashboard_page,
        analyze_page,
        history_page,
        insights_page,
    ],
    position="sidebar",
)


# ============================================================
# RUN APPLICATION
# ============================================================

navigation.run()