# ============================================================
# SMS SHIELD AI
# SCAN HISTORY
# PREMIUM SECURITY ACTIVITY CENTER
# ============================================================

import html
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SMS Shield AI | Scan History",
    page_icon="🛡️",
    layout="wide",
)


# ============================================================
# SESSION STATE
# ============================================================

if "scan_history" not in st.session_state:
    st.session_state.scan_history = []


history = st.session_state.scan_history


# ============================================================
# PAGE DESIGN
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       HERO
       ======================================================== */

    .history-hero-premium {

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


    .history-hero-premium::after {

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


    .history-hero-content {

        position: relative;
        z-index: 2;
    }


    .history-eyebrow-premium {

        color: #8DD1F2;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;
    }


    .history-title-premium {

        margin-top: 8px;

        color: #FFFFFF;

        font-size: 38px;

        line-height: 1.05;

        font-weight: 900;

        letter-spacing: -1.4px;
    }


    .history-description-premium {

        max-width: 720px;

        margin-top: 10px;

        color: #D2D6DE;

        font-size: 9px;

        line-height: 1.75;
    }


    /* ========================================================
       SECTION
       ======================================================== */

    .history-section {

        margin-top: 30px;

        margin-bottom: 13px;
    }


    .history-section-title {

        color: #343746;

        font-size: 17px;

        font-weight: 900;

        letter-spacing: -.3px;
    }


    .history-section-subtitle {

        margin-top: 3px;

        color: #858B98;

        font-size: 8px;
    }


    /* ========================================================
       STAT CARDS
       ======================================================== */

    .history-stat {

        min-height: 112px;

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


    .history-stat:hover {

        transform:
            translateY(-4px);

        border-color:
            #C6D7E2;

        box-shadow:
            0 14px 32px
            rgba(45,52,65,.10);
    }


    .history-stat-label {

        color: #89919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: 1px;

        text-transform: uppercase;
    }


    .history-stat-value {

        margin-top: 7px;

        color: #343746;

        font-size: 27px;

        font-weight: 900;

        letter-spacing: -.8px;
    }


    .history-stat-note {

        margin-top: 3px;

        color: #9AA1AB;

        font-size: 7px;
    }


    /* ========================================================
       ACTIVITY TOOLBAR
       ======================================================== */

    .toolbar-card {

        padding: 21px;

        border-radius: 18px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 6px 19px
            rgba(45,52,65,.055);
    }


    .toolbar-label {

        color: #454A57;

        font-size: 8px;

        font-weight: 900;

        letter-spacing: .7px;

        margin-bottom: 7px;
    }


    /* ========================================================
       EMPTY STATE
       ======================================================== */

    .history-empty {

        margin-top: 17px;

        padding: 55px 30px;

        text-align: center;

        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                #F8FAFB,
                #F0F3F6
            );

        border:
            1px dashed #CCD5DD;
    }


    .history-empty-icon {

        width: 52px;
        height: 52px;

        margin: 0 auto;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 15px;

        background: #F0EBF8;

        border:
            1px solid #DCCFF0;

        color: #7656A8;

        font-size: 20px;
    }


    .history-empty-title {

        margin-top: 14px;

        color: #454A57;

        font-size: 15px;

        font-weight: 900;
    }


    .history-empty-text {

        max-width: 470px;

        margin: 6px auto 0;

        color: #89919D;

        font-size: 8px;

        line-height: 1.7;
    }


    /* ========================================================
       SCAN CARD
       ======================================================== */

    .scan-card-premium {

        margin-top: 10px;

        padding: 19px;

        border-radius: 17px;

        background: #FFFFFF;

        border:
            1px solid #DDE2E8;

        box-shadow:
            0 5px 17px
            rgba(45,52,65,.055);

        transition:
            transform .20s ease,
            box-shadow .20s ease,
            border-color .20s ease;

        animation:
            scanReveal .30s ease both;
    }


    @keyframes scanReveal {

        from {

            opacity: 0;

            transform:
                translateY(7px);
        }

        to {

            opacity: 1;

            transform:
                translateY(0);
        }
    }


    .scan-card-premium:hover {

        transform:
            translateY(-3px);

        border-color:
            #C7D7E2;

        box-shadow:
            0 12px 27px
            rgba(45,52,65,.095);
    }


    .scan-header {

        display: flex;

        justify-content: space-between;

        align-items: center;

        gap: 12px;
    }


    .scan-number {

        color: #89919D;

        font-size: 7px;

        font-weight: 900;

        letter-spacing: .8px;
    }


    .scan-time {

        color: #9AA1AB;

        font-size: 7px;
    }


    .scan-message {

        margin-top: 10px;

        color: #454A57;

        font-size: 9px;

        line-height: 1.7;

        word-break: break-word;
    }


    .scan-footer {

        display: flex;

        align-items: center;

        gap: 7px;

        margin-top: 13px;
    }


    .scan-badge {

        padding: 5px 9px;

        border-radius: 999px;

        font-size: 6px;

        font-weight: 900;

        letter-spacing: .6px;
    }


    .badge-spam {

        color: #C95757;

        background: #FBEDED;

        border:
            1px solid #EACDD0;
    }


    .badge-ham {

        color: #4F8A68;

        background: #EAF4EE;

        border:
            1px solid #CDE2D5;
    }


    .badge-high {

        color: #B04D4D;

        background: #FFF3F3;

        border:
            1px solid #EACFD0;
    }


    .badge-low {

        color: #4F8068;

        background: #F0F7F3;

        border:
            1px solid #D2E5D9;
    }


    /* ========================================================
       RESULT SCORE
       ======================================================== */

    .score-badge {

        margin-left: auto;

        color: #7656A8;

        background: #F0EBF8;

        border:
            1px solid #DCCFF0;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .history-footer {

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
    """
    <div class="history-hero-premium">

        <div class="history-hero-content">

            <div class="history-eyebrow-premium">
                SECURITY ACTIVITY CENTER
            </div>

            <div class="history-title-premium">
                Scan History
            </div>

            <div class="history-description-premium">
                Review analyzed messages, identify previous threats,
                and monitor classification activity from the current
                application session.
            </div>

        </div>

    </div>
    """
)


# ============================================================
# STATISTICS
# ============================================================

total_scans = len(history)

spam_count = sum(
    1
    for item in history
    if str(
        item.get("Prediction", "")
    ).upper() == "SPAM"
)

ham_count = sum(
    1
    for item in history
    if str(
        item.get("Prediction", "")
    ).upper() == "HAM"
)


st.html(
    """
    <div class="history-section">

        <div class="history-section-title">
            Activity Overview
        </div>

        <div class="history-section-subtitle">
            Current session security statistics
        </div>

    </div>
    """
)


stat_columns = st.columns(
    3,
    gap="medium"
)


stats = [
    (
        "TOTAL SCANS",
        total_scans,
        "Messages analyzed",
    ),
    (
        "THREATS FOUND",
        spam_count,
        "Potential spam detections",
    ),
    (
        "LEGITIMATE",
        ham_count,
        "Safe classifications",
    ),
]


for column, stat in zip(
    stat_columns,
    stats
):

    with column:

        st.html(
            f"""
            <div class="history-stat">

                <div class="history-stat-label">
                    {stat[0]}
                </div>

                <div class="history-stat-value">
                    {stat[1]}
                </div>

                <div class="history-stat-note">
                    {stat[2]}
                </div>

            </div>
            """
        )


# ============================================================
# ACTIVITY LOG
# ============================================================

st.html(
    """
    <div class="history-section">

        <div class="history-section-title">
            Activity Log
        </div>

        <div class="history-section-subtitle">
            Search and filter previously analyzed messages
        </div>

    </div>
    """
)


st.html(
    """
    <div class="toolbar-card">

        <div class="toolbar-label">
            FILTER ACTIVITY
        </div>

    </div>
    """
)


filter_column, search_column = st.columns(
    [1, 2],
    gap="medium"
)


with filter_column:

    filter_type = st.selectbox(
        "Filter",
        [
            "All Results",
            "Spam Only",
            "Legitimate Only",
        ],
        label_visibility="collapsed",
    )


with search_column:

    search_text = st.text_input(
        "Search",
        placeholder="Search analyzed messages...",
        label_visibility="collapsed",
    )


# ============================================================
# FILTER DATA
# ============================================================

filtered_history = history.copy()


if filter_type == "Spam Only":

    filtered_history = [
        item
        for item in filtered_history
        if str(
            item.get("Prediction", "")
        ).upper() == "SPAM"
    ]


elif filter_type == "Legitimate Only":

    filtered_history = [
        item
        for item in filtered_history
        if str(
            item.get("Prediction", "")
        ).upper() == "HAM"
    ]


if search_text.strip():

    query = search_text.strip().lower()

    filtered_history = [
        item
        for item in filtered_history
        if query in str(
            item.get("Message", "")
        ).lower()
    ]


# ============================================================
# ACTIONS
# ============================================================

action_1, action_2, action_3 = st.columns(
    [1, 1, 1],
    gap="medium"
)


with action_1:

    if st.button(
        "Refresh Activity",
        use_container_width=True,
    ):

        st.rerun()


with action_2:

    if st.button(
        "Clear History",
        use_container_width=True,
    ):

        st.session_state.scan_history = []

        if "dashboard_result" in st.session_state:
            st.session_state.dashboard_result = None

        if "analysis_result" in st.session_state:
            st.session_state.analysis_result = None

        st.rerun()


with action_3:

    st.caption(
        f"{len(filtered_history)} result"
        f"{'' if len(filtered_history) == 1 else 's'}"
    )


# ============================================================
# EMPTY STATE
# ============================================================

if not filtered_history:

    st.html(
        """
        <div class="history-empty">

            <div class="history-empty-icon">
                ◷
            </div>

            <div class="history-empty-title">
                No scan activity found
            </div>

            <div class="history-empty-text">
                Messages analyzed from Dashboard or Analyze SMS
                will automatically appear here. Run an analysis
                to start building your security activity history.
            </div>

        </div>
        """
    )


# ============================================================
# DISPLAY HISTORY
# ============================================================

else:

    display_history = list(
        reversed(filtered_history)
    )


    for index, item in enumerate(
        display_history,
        start=1,
    ):

        prediction = str(
            item.get(
                "Prediction",
                "UNKNOWN",
            )
        ).upper()


        risk = str(
            item.get(
                "Risk",
                "N/A",
            )
        ).upper()


        message = str(
            item.get(
                "Message",
                "",
            )
        )


        timestamp = str(
            item.get(
                "Timestamp",
                "Unknown time",
            )
        )


        score = str(
            item.get(
                "Decision Score",
                "N/A",
            )
        )


        # ----------------------------------------------------
        # ESCAPE USER DATA
        # ----------------------------------------------------

        safe_message = html.escape(
            message
        )

        safe_timestamp = html.escape(
            timestamp
        )

        safe_score = html.escape(
            score
        )


        # ----------------------------------------------------
        # PREVIEW
        # ----------------------------------------------------

        if len(safe_message) > 260:

            safe_message = (
                safe_message[:260]
                + "..."
            )


        # ----------------------------------------------------
        # BADGES
        # ----------------------------------------------------

        prediction_class = (
            "badge-spam"
            if prediction == "SPAM"
            else "badge-ham"
        )


        risk_class = (
            "badge-high"
            if risk == "HIGH"
            else "badge-low"
        )


        st.html(
            f"""
            <div class="scan-card-premium">

                <div class="scan-header">

                    <span class="scan-number">
                        SCAN #{index:02d}
                    </span>

                    <span class="scan-time">
                        {safe_timestamp}
                    </span>

                </div>


                <div class="scan-message">
                    {safe_message}
                </div>


                <div class="scan-footer">

                    <span class="scan-badge {prediction_class}">
                        {prediction}
                    </span>

                    <span class="scan-badge {risk_class}">
                        {risk} RISK
                    </span>

                    <span class="scan-badge score-badge">
                        SCORE {safe_score}
                    </span>

                </div>

            </div>
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="history-footer">

        SMS SHIELD AI
        &nbsp; • &nbsp;
        SECURITY ACTIVITY CENTER
        &nbsp; • &nbsp;
        SESSION ANALYTICS

    </div>
    """
)