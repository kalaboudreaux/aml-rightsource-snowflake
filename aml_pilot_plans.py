import streamlit as st
import json
from datetime import datetime, date
import uuid

st.set_page_config(
    page_title="AML RightSource × Snowflake — Pilot Plans",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.pilot-hero {
    background: linear-gradient(135deg, #0D2B4E 0%, #11375C 60%, #1A4A7A 100%);
    border-radius: 16px; padding: 40px 48px; margin-bottom: 28px; color: white;
}
.pilot-badge {
    display: inline-block; background: rgba(41,181,232,0.2);
    border: 1px solid rgba(41,181,232,0.4); color: #29B5E8;
    padding: 4px 12px; border-radius: 20px; font-size: 11px;
    font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px;
}
.pilot-hero h1 { font-size: 34px; font-weight: 900; margin: 0 0 8px; }
.pilot-hero p { color: rgba(255,255,255,0.7); font-size: 15px; margin: 0; }

.pilot-tab-header {
    background: white; border: 1px solid #D1E8F5; border-top: 4px solid;
    border-radius: 12px; padding: 20px 24px; margin-bottom: 20px;
}

.section-h {
    font-size: 17px; font-weight: 800; color: #0D2B4E;
    border-bottom: 2px solid #E2E8F0; padding-bottom: 8px; margin: 28px 0 16px;
    display: flex; align-items: center; gap: 10px;
}
.section-num {
    width: 28px; height: 28px; background: #29B5E8; color: white;
    border-radius: 6px; display: flex; align-items: center; justify-content: center;
    font-size: 12px; font-weight: 800; flex-shrink: 0;
}

.editable-label { font-size: 13px; font-weight: 600; color: #0D2B4E; margin-bottom: 4px; }
.read-only-field {
    background: #F7FBFE; border: 1px solid #D1E8F5; border-radius: 8px;
    padding: 12px 14px; font-size: 13px; color: #4A5568; margin-bottom: 12px;
}

.comment-card {
    background: white; border: 1px solid #D1E8F5; border-left: 3px solid #29B5E8;
    border-radius: 0 8px 8px 0; padding: 12px 14px; margin: 8px 0;
}
.comment-header { font-size: 11px; color: #718096; margin-bottom: 6px; }
.comment-text { font-size: 13px; color: #2D3748; }

.success-criterion {
    background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 10px;
    padding: 14px; margin-bottom: 10px;
}
.sc-metric { font-size: 14px; font-weight: 700; color: #065F46; }
.sc-detail { font-size: 12px; color: #047857; margin-top: 4px; }

.prereq-item {
    display: flex; align-items: flex-start; gap: 12px; padding: 12px;
    background: #F7FAFC; border-radius: 8px; margin-bottom: 8px; border: 1px solid #E2E8F0;
}

.phase-card {
    background: white; border: 1px solid #D1E8F5; border-radius: 10px;
    padding: 16px; margin-bottom: 10px;
}
.phase-header { font-size: 14px; font-weight: 700; color: #0D2B4E; margin-bottom: 8px;
    display: flex; align-items: center; gap: 8px; }
.phase-badge {
    font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px;
    background: #DBEFFE; color: #1E6FA8;
}

.results-row {
    display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 8px;
    padding: 10px; border-bottom: 1px solid #E2E8F0; font-size: 13px;
    align-items: center;
}
.results-header { background: #0D2B4E; color: white; border-radius: 8px; padding: 10px; }

.live-section {
    background: linear-gradient(135deg, #FFF8E6, #FEF3C7);
    border: 2px solid #F59E0B; border-radius: 12px; padding: 20px; margin: 16px 0;
}
.live-badge {
    display: inline-block; background: #F59E0B; color: white;
    padding: 3px 10px; border-radius: 10px; font-size: 10px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;
}

.callout-blue { background: #E8F7FD; border-left: 3px solid #29B5E8; border-radius: 0 8px 8px 0; padding: 12px 16px; margin: 8px 0; font-size: 13px; }
.callout-green { background: #E6FBF3; border-left: 3px solid #00C96F; border-radius: 0 8px 8px 0; padding: 12px 16px; margin: 8px 0; font-size: 13px; }
.callout-orange { background: #FFF8E6; border-left: 3px solid #FF7A00; border-radius: 0 8px 8px 0; padding: 12px 16px; margin: 8px 0; font-size: 13px; }

.footer-bar {
    background: #0D2B4E; color: rgba(255,255,255,0.5); text-align: center;
    padding: 20px; border-radius: 12px; margin-top: 40px; font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE FOR LIVE COMMENTS/NOTES ────────────────────────────────────
if "comments" not in st.session_state:
    st.session_state.comments = {"advisory": [], "data_assets": [], "algorithms": []}
if "live_notes" not in st.session_state:
    st.session_state.live_notes = {"advisory": {}, "data_assets": {}, "algorithms": {}}
if "owner_names" not in st.session_state:
    st.session_state.owner_names = {
        "advisory": "Sabrina Chen",
        "data_assets": "Jonathan McIsaac",
        "algorithms": "Isabel Yeung"
    }

def add_comment(track, author, text):
    if text.strip():
        ts = datetime.now().strftime("%b %d, %Y %I:%M %p")
        st.session_state.comments[track].append({"author": author, "text": text, "ts": ts, "id": str(uuid.uuid4())[:8]})

def render_comments(track):
    comments = st.session_state.comments[track]
    if comments:
        st.markdown(f"**💬 {len(comments)} Comment(s):**")
        for c in reversed(comments[-10:]):
            st.markdown(f"""
            <div class="comment-card">
            <div class="comment-header">👤 <strong>{c['author']}</strong> · {c['ts']}</div>
            <div class="comment-text">{c['text']}</div>
            </div>
            """, unsafe_allow_html=True)

def comment_box(track, label_text="💬 Add Comment or Question"):
    with st.expander(label_text, expanded=False):
        c1, c2 = st.columns([3, 1])
        with c1:
            author = st.text_input("Your Name", key=f"author_{track}_{label_text[:20]}", placeholder="Enter your name")
            comment_text = st.text_area("Comment / Question / Note", key=f"comment_{track}_{label_text[:20]}", placeholder="Type your comment, question, or note here...")
        with c2:
            st.markdown("<br><br>", unsafe_allow_html=True)
            if st.button("Post Comment", key=f"btn_{track}_{label_text[:20]}"):
                if author and comment_text:
                    add_comment(track, author, comment_text)
                    st.success("Comment added!")
                    st.rerun()
                else:
                    st.warning("Please enter your name and comment.")

def editable_field(label, default_val, key, height=None, track=None):
    st.markdown(f'<div class="editable-label">✏️ {label}</div>', unsafe_allow_html=True)
    if key not in st.session_state.live_notes.get(track or "advisory", {}):
        if track:
            st.session_state.live_notes[track][key] = default_val
    val = st.session_state.live_notes.get(track or "advisory", {}).get(key, default_val)
    if height:
        new_val = st.text_area("", value=val, key=f"field_{track}_{key}", height=height, label_visibility="collapsed")
    else:
        new_val = st.text_input("", value=val, key=f"field_{track}_{key}", label_visibility="collapsed")
    if track:
        st.session_state.live_notes[track][key] = new_val
    return new_val

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="pilot-hero">
    <div class="pilot-badge">🚀 Snowflake Pilot Plans</div>
    <h1>AML RightSource × Snowflake</h1>
    <p>Three structured pilot plans — one per use case. Fully editable. Add notes, questions, and comments in real time during your planning sessions with the Snowflake team.</p>
    <div style="margin-top:20px; display:flex; gap:16px; flex-wrap:wrap">
        <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 16px; font-size:13px">🔍 <strong>Pilot 1:</strong> Advisory Intelligence</div>
        <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 16px; font-size:13px">📊 <strong>Pilot 2:</strong> Data Assets & Benchmarking</div>
        <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:10px 16px; font-size:13px">⚙️ <strong>Pilot 3:</strong> Algorithm Deployment</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PILOT SELECTOR ────────────────────────────────────────────────────────────
pilot_tab1, pilot_tab2, pilot_tab3 = st.tabs([
    "🔍 Pilot 1 — Advisory",
    "📊 Pilot 2 — Data Assets",
    "⚙️ Pilot 3 — Algorithms",
])

# ══════════════════════════════════════════════════════════════════════════════
# PILOT 1 — ADVISORY
# ══════════════════════════════════════════════════════════════════════════════
with pilot_tab1:
    TRACK = "advisory"

    st.markdown("""
    <div class="pilot-tab-header" style="border-top-color:#29B5E8">
    <h3 style="margin:0; color:#0D2B4E">🔍 Pilot 1 — Advisory Intelligence: ETL-Free Client Data Collaboration</h3>
    <p style="color:#718096; font-size:13px; margin:6px 0 0">Validate that Snowflake's zero-copy data sharing model eliminates advisory engagement data onboarding friction — compressing time-to-data from 10–20 days to hours.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 1: OWNER ─────────────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">1</div> Pilot Owner from AML RightSource</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        editable_field("Primary Pilot Owner", "Sabrina Chen — Head of Analytics, FCA", "owner_primary", track=TRACK)
    with c2:
        editable_field("Supporting Owner", "David Lutz — Associate Director, FCA", "owner_secondary", track=TRACK)
    editable_field("Executive Sponsor", "Abhishek Mittal — EVP & Chief Product and AI Officer", "exec_sponsor", track=TRACK)
    comment_box(TRACK, "💬 Section 1: Questions about pilot ownership")

    # ── SECTION 2: EXECUTIVE SUMMARY ─────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">2</div> Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    editable_field("POV Statement (editable)", 
        "AML RightSource's advisory practice is constrained by a manual, multi-week data onboarding process that prevents analysts from delivering value quickly. We believe Snowflake's zero-copy data sharing model can reduce advisory engagement time-to-data from 10–20 days to under 48 hours, increase analyst productivity by 50–100%, and eliminate the security and compliance friction associated with FTP/email-based data transfer — validated through a 60-day pilot with synthetic (or agreed real) client data.",
        "pov_statement", height=150, track=TRACK)
    st.markdown("""
    <div class="callout-blue">
    <strong>Why this matters:</strong> Advisory is AML RightSource's highest-margin line. Every day shaved off engagement start = direct margin improvement and competitive advantage. This pilot validates the foundational data infrastructure for the entire Snowflake partnership.
    </div>
    """, unsafe_allow_html=True)
    comment_box(TRACK, "💬 Section 2: Questions about the POV")

    # ── SECTION 3: BUSINESS DRIVERS ──────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">3</div> Business Drivers & Objectives</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Current Business Problem:**")
        editable_field("Describe the current problem", 
            "Each advisory engagement requires AML RightSource to manually request, receive, and normalize client data (TM alerts, KYC records, lookback transaction data) via secure FTP, email, or SharePoint. This takes 10–20 business days and consumes 40–60% of analyst time per engagement — before any advisory analysis begins. The process also introduces security and compliance risk every time client data is transmitted.",
            "biz_problem", height=150, track=TRACK)
    with col2:
        st.markdown("**Business Objective:**")
        editable_field("What does success look like for the business?",
            "Reduce advisory engagement time-to-first-data-access from 10–20 days to <48 hours. Reduce analyst data prep time from 40–60% to <10% of engagement. Enable AML RightSource to serve 50–100% more advisory clients with the same analyst headcount. Create a differentiated, secure, client-friendly advisory experience that wins new mandates.",
            "biz_objective", height=150, track=TRACK)
    comment_box(TRACK, "💬 Section 3: Add your business context")

    # ── SECTION 4: DISCOVERY & CURRENT STATE ─────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">4</div> Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        editable_field("Current Data Transfer Method",
            "Secure FTP, encrypted email, SharePoint document upload. Per-engagement, manual request and delivery cycle.", "current_method", height=100, track=TRACK)
    with c2:
        editable_field("Average Time to First Data Access (confirm or update)",
            "10–20 business days (estimated — Sabrina/David to confirm actual average)", "ttd_current", height=100, track=TRACK)
    with c3:
        editable_field("% Analyst Time Spent on Data Prep (confirm or update)",
            "40–60% estimated. To be confirmed with time-tracking data during pilot.", "analyst_time", height=100, track=TRACK)
    editable_field("Current Pain Level (1–10) and Description",
        "8/10 — Data prep is the single largest bottleneck to advisory delivery. Multiple stakeholders (Sabrina, David, Abhishek) independently confirmed this in the April 29 meeting.", "pain_level", track=TRACK)
    editable_field("What has been tried before?",
        "Secure file transfer portals (SharePoint, Box). Custom API connections for specific large bank clients. None have scaled — each requires per-client configuration and ongoing maintenance.", "tried_before", track=TRACK)
    comment_box(TRACK, "💬 Section 4: Update with actual current state numbers")

    # ── SECTION 5: POINT OF VIEW ──────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">5</div> Point of View (Snowflake\'s Prediction)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-blue">
    <strong>Snowflake's POV:</strong> We believe Snowflake can overcome the <strong>manual, insecure, slow data onboarding process for advisory engagements</strong> while supporting <strong>AML RightSource's objective of serving 2× more clients with the same headcount</strong> by implementing <strong>zero-copy Snowflake Data Sharing between AML RightSource's Snowflake account and participating bank clients' Snowflake environments — validated by a 60-day pilot using a synthetic AML dataset that mirrors real advisory engagement data.</strong>
    </div>
    """, unsafe_allow_html=True)
    editable_field("Add any modifications or additions to the POV",
        "", "pov_addl", height=80, track=TRACK)
    comment_box(TRACK, "💬 Section 5: Questions about the POV")

    # ── SECTION 6: SUCCESS CRITERIA ──────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">6</div> Success Criteria & Test Cases</div>', unsafe_allow_html=True)

    criteria = [
        ("SC-1", "Time-to-First-Data-Access", "Baseline: 10–20 days", "Target: <48 hours", "How: Compare pilot data share setup time vs. last 5 advisory engagements"),
        ("SC-2", "Analyst Data Prep Time per Engagement", "Baseline: 40–60% of engagement", "Target: <10% of engagement", "How: Time-tracked by Sabrina/David during 2 pilot advisory engagements"),
        ("SC-3", "Data Security & Compliance Clearance", "Baseline: 2–3 weeks security review per client", "Target: Pass Snowflake Business Critical security review upfront — no per-engagement review", "How: Snowflake security package submitted to AML RS infosec for sign-off"),
        ("SC-4", "Analyst Satisfaction Score", "Baseline: Current NPS/satisfaction TBD", "Target: 8/10 or higher analyst satisfaction with Snowflake advisory workflow", "How: 5-question satisfaction survey at pilot close"),
    ]

    for sc_id, metric, baseline, target, method in criteria:
        st.markdown(f"""
        <div class="success-criterion">
        <div class="sc-metric">✅ {sc_id}: {metric}</div>
        <div class="sc-detail">📊 {baseline} &nbsp;→&nbsp; 🎯 {target}</div>
        <div class="sc-detail">📋 {method}</div>
        </div>
        """, unsafe_allow_html=True)

    editable_field("Add or modify success criteria (AML RightSource team input)",
        "", "sc_addl", height=80, track=TRACK)
    comment_box(TRACK, "💬 Section 6: Agree on success criteria — most important section")

    # ── SECTION 7: PREREQUISITES ─────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">7</div> Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)

    prereqs = [
        ("❄️", "Snowflake Trial Account (Business Critical)", "Snowflake", "Day 1", "Jordan Ude provisions this within 24 hours of pilot kick-off"),
        ("📊", "Synthetic AML Dataset (realistic TM + KYC data)", "Snowflake (Jordan)", "Day 1–3", "Jordan creates synthetic dataset mirroring a mid-tier bank's TM alert and KYC structure"),
        ("👤", "Named Pilot Users from AML RS (2–4 analysts)", "AML RightSource", "Week 1", "Sabrina/David identify 2–4 advisory analysts to participate in pilot"),
        ("🔐", "NDA for Pilot Data Governance", "Both parties", "Pre-pilot", "✅ NDA already signed — confirm scope covers pilot data"),
        ("📅", "Timeline Commitment (60 days, 4–5 hrs/week per analyst)", "AML RightSource", "Week 1", "Need confirmed bandwidth from Sabrina/David before pilot launches"),
        ("🏦", "(Optional) Real Client Bank Data Share", "AML RightSource + Client Bank", "Week 2–3", "If agreed: identify 1 bank client willing to share data via Snowflake for pilot"),
        ("📋", "Baseline Metrics Documentation", "AML RightSource", "Week 1", "Sabrina/David document current engagement time-to-data for last 5 advisory engagements"),
        ("🔒", "Infosec/CISO Review of Snowflake Business Critical", "AML RightSource IT", "Week 2", "Snowflake provides full security package; AML RS infosec reviews and signs off"),
    ]

    for icon, item, owner, timeline, notes in prereqs:
        st.markdown(f"""
        <div class="prereq-item">
        <div style="font-size:22px; flex-shrink:0">{icon}</div>
        <div style="flex:1">
        <div style="font-size:14px; font-weight:700; color:#0D2B4E">{item}</div>
        <div style="font-size:12px; color:#718096; margin-top:2px">Owner: <strong>{owner}</strong> &nbsp;|&nbsp; Target: <strong>{timeline}</strong></div>
        <div style="font-size:12px; color:#4A5568; margin-top:4px">{notes}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    editable_field("Additional prerequisites or blockers (add here)",
        "", "prereq_addl", height=80, track=TRACK)
    comment_box(TRACK, "💬 Section 7: Flag any missing prerequisites")

    # ── SECTION 8: EXECUTION PLAN ─────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">8</div> Pilot Execution Plan</div>', unsafe_allow_html=True)

    phases = [
        ("Week 1–2", "Introduction & Scoping", "#29B5E8",
         ["Pilot kick-off call with Sabrina, David, Jordan, Kala",
          "Provision Snowflake Business Critical trial account",
          "Load synthetic AML dataset (TM alerts + KYC records)",
          "Provide access credentials and onboarding documentation",
          "Set baseline metrics (document last 5 advisory engagement timelines)"]),
        ("Week 2–3", "Environment Setup & Training", "#0D2B4E",
         ["Snowflake product walkthrough — Data Sharing, Snowsight, Cortex AI",
          "Jordan-led hands-on session: how to set up a data share",
          "Sabrina + David run first advisory query against synthetic data",
          "Optional: set up live data share with willing bank client",
          "Document initial observations and friction points"]),
        ("Week 3–6", "Pilot Execution", "#00C96F",
         ["Run 2 simulated advisory engagements using Snowflake data shares",
          "Compare time-to-data vs. current FTP/email process",
          "Track analyst time on data prep vs. advisory analysis",
          "Snowflake SE office hours twice per week",
          "Document all results, issues, and improvements"]),
        ("Week 7–8", "Analysis & Readout", "#FF7A00",
         ["Compile pilot results vs. success criteria",
          "Produce before/after productivity analysis",
          "Quantify business impact (time saved, engagements enabled)",
          "Prepare formal readout deck",
          "Readout meeting with Abhishek + all stakeholders"]),
    ]

    for period, phase_name, color, activities in phases:
        st.markdown(f"""
        <div class="phase-card">
        <div class="phase-header">
        <div style="width:10px;height:10px;border-radius:50%;background:{color};flex-shrink:0"></div>
        <span class="phase-badge">{period}</span>
        <strong>{phase_name}</strong>
        </div>
        <ul style="margin:0 0 0 20px; padding:0">
        {''.join(f'<li style="font-size:13px; color:#4A5568; margin-bottom:4px">{a}</li>' for a in activities)}
        </ul>
        </div>
        """, unsafe_allow_html=True)

    comment_box(TRACK, "💬 Section 8: Add notes on timeline or activities")

    # ── SECTION 9: RESULTS ────────────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">9</div> Pilot Results & Readout</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="live-section">
    <div class="live-badge">🔴 Live — Complete During Pilot</div>
    <p style="font-size:13px; color:#92400E; margin-bottom:16px">This section is filled in during and after the pilot. Document actual results against each success criterion below.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        editable_field("SC-1: Actual Time-to-First-Data-Access (days)",
            "[TO BE COMPLETED DURING PILOT]", "result_sc1", track=TRACK)
        editable_field("SC-2: Actual Analyst Data Prep % per Engagement",
            "[TO BE COMPLETED DURING PILOT]", "result_sc2", track=TRACK)
    with col2:
        editable_field("SC-3: Security Review Outcome",
            "[TO BE COMPLETED DURING PILOT]", "result_sc3", track=TRACK)
        editable_field("SC-4: Analyst Satisfaction Score (1–10)",
            "[TO BE COMPLETED DURING PILOT]", "result_sc4", track=TRACK)
    editable_field("Overall Business Value Quantification",
        "[TO BE COMPLETED AT PILOT READOUT — e.g., 'This pilot demonstrated $X in annual productivity savings if deployed across all advisory engagements']",
        "biz_value", height=80, track=TRACK)

    st.markdown("</div>", unsafe_allow_html=True)
    comment_box(TRACK, "💬 Section 9: Update results here during the pilot")

    # ── SECTION 10: NEXT STEPS ────────────────────────────────────────────────
    st.markdown('<div class="section-h"><div class="section-num">10</div> Pilot Readout & Path Forward</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="live-section">
    <div class="live-badge">🔴 Live — Complete at Readout Meeting</div>
    """, unsafe_allow_html=True)

    editable_field("Did results validate the POV? (Yes / No / Partially — explain)",
        "[TO BE COMPLETED AT READOUT — 'Yes, Snowflake reduced time-to-data by X% which validates our POV that...' or 'Partial — we achieved X but need more work on Y before recommending full deployment...']",
        "pov_validated", height=100, track=TRACK)
    editable_field("Confirmed Outcomes vs. Success Criteria",
        "[SC-1: X achieved vs. Y target — PASS/FAIL]\n[SC-2: X achieved vs. Y target — PASS/FAIL]\n[SC-3: X achieved vs. Y target — PASS/FAIL]\n[SC-4: X achieved vs. Y target — PASS/FAIL]",
        "outcomes_confirmed", height=120, track=TRACK)
    editable_field("Path Forward — Recommended Next Step",
        "[Example: 'Based on pilot results, we recommend moving to a production Snowflake deployment covering all FCA advisory engagements. Proposed timeline: contract signature by [DATE], Phase 1 production go-live by [DATE]. Estimated Year 1 investment: $[X]K.']",
        "path_forward", height=100, track=TRACK)
    editable_field("Outstanding Questions / Issues Before Contracting",
        "[List any unresolved questions, concerns, or issues that must be addressed before AML RightSource can move forward with a Snowflake contract.]",
        "outstanding_qs", height=80, track=TRACK)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("#### 💬 Overall Comments & Questions — Pilot 1")
    render_comments(TRACK)
    comment_box(TRACK, "💬 Add overall comment, question, or note for Pilot 1")


# ══════════════════════════════════════════════════════════════════════════════
# PILOT 2 — DATA ASSETS
# ══════════════════════════════════════════════════════════════════════════════
with pilot_tab2:
    TRACK2 = "data_assets"

    st.markdown("""
    <div class="pilot-tab-header" style="border-top-color:#00C96F">
    <h3 style="margin:0; color:#0D2B4E">📊 Pilot 2 — Data Assets: Cross-Client Benchmarking Intelligence Platform</h3>
    <p style="color:#718096; font-size:13px; margin:6px 0 0">Validate that AML RightSource's internal operational data, unified on Snowflake, can power an industry-first cross-client AML benchmarking intelligence product — generating new recurring SaaS revenue.</p>
    </div>
    """, unsafe_allow_html=True)

    # SECTION 1
    st.markdown('<div class="section-h"><div class="section-num">1</div> Pilot Owner from AML RightSource</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        editable_field("Primary Pilot Owner", "Jonathan McIsaac — Global SVP, Head Client Operations", "owner_primary", track=TRACK2)
    with c2:
        editable_field("Supporting Owner", "Abhishek Mittal — EVP & Chief Product and AI Officer", "owner_secondary", track=TRACK2)
    comment_box(TRACK2, "💬 Section 1: Questions about pilot ownership")

    # SECTION 2
    st.markdown('<div class="section-h"><div class="section-num">2</div> Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    editable_field("POV Statement",
        "AML RightSource possesses the most comprehensive dataset of AML/BSA process performance data across 200+ financial institutions in the independent compliance space — currently sitting fragmented and unmonetized across siloed internal systems. We believe Snowflake's unified data platform can consolidate this asset, and its Marketplace and Data Clean Room capabilities can enable AML RightSource to build and distribute the industry's first real-time cross-client AML benchmarking intelligence product — creating $2–5M in new ARR by Year 2 while providing superior advisory value to all clients.",
        "pov_statement", height=150, track=TRACK2)
    st.markdown("""
    <div class="callout-green">
    <strong>Strategic significance:</strong> This use case is the difference between AML RightSource being a services firm (8–10× EBITDA multiple) and a data/SaaS firm (15–25× ARR multiple). This pilot validates the data product strategy that the PE board needs to see.
    </div>
    """, unsafe_allow_html=True)
    comment_box(TRACK2, "💬 Section 2: Questions about the POV")

    # SECTION 3
    st.markdown('<div class="section-h"><div class="section-num">3</div> Business Drivers & Objectives</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        editable_field("Current Business Problem",
            "AML RightSource manages 200+ financial institution clients but has no unified platform to aggregate, analyze, or productize the operational intelligence generated across those engagements. Jonathan's operational data — case resolution rates, false positive rates, analyst productivity, SAR filing volumes — lives in disparate case management systems with no cross-client analytics layer. The company cannot generate benchmark reports, peer comparisons, or industry intelligence at scale.",
            "biz_problem", height=150, track=TRACK2)
    with col2:
        editable_field("Business Objective",
            "1) Migrate AML RightSource's internal operational data to Snowflake as a unified single source of truth. 2) Build an anonymized cross-client analytics layer enabling peer benchmarking. 3) Validate the technical feasibility of a Snowflake Marketplace benchmarking product. 4) Quantify the revenue potential of a benchmarking intelligence subscription offering.",
            "biz_objective", height=150, track=TRACK2)
    comment_box(TRACK2, "💬 Section 3: Jonathan — what internal data do you want to explore?")

    # SECTION 4
    st.markdown('<div class="section-h"><div class="section-num">4</div> Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    editable_field("Internal Data Sources (list all case management and operational systems)",
        "[Jonathan to complete: list all internal systems where AML/BSA process data lives — case management platform(s), workflow tools, reporting databases, etc. This is required before pilot scope can be finalized.]",
        "data_sources", height=100, track=TRACK2)
    editable_field("Estimated Data Volume & History",
        "[Jonathan to confirm: approximate number of cases processed, years of history, volume of data in internal systems. This drives Snowflake sizing and migration planning.]",
        "data_volume", height=80, track=TRACK2)
    editable_field("Current Analytics Capabilities",
        "[Currently, what analytical reports or benchmarking can AML RightSource produce? What can you NOT produce but wish you could?]",
        "current_analytics", height=80, track=TRACK2)
    editable_field("Client Data Privacy Constraints",
        "All benchmarking analytics must be anonymized — no individual client institution identifiable in aggregate output. Snowflake Data Clean Rooms and aggregation controls ensure this. AML RS legal review of anonymization approach required before going live.", 
        "privacy_constraints", height=80, track=TRACK2)
    comment_box(TRACK2, "💬 Section 4: Jonathan — fill in your current state details")

    # SECTION 5
    st.markdown('<div class="section-h"><div class="section-num">5</div> Point of View (Snowflake\'s Prediction)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-blue">
    <strong>Snowflake's POV:</strong> We believe Snowflake can overcome <strong>AML RightSource's fragmented internal data infrastructure and zero benchmarking product capability</strong> while supporting <strong>the strategic objective of creating a new $5M+ ARR data product revenue stream</strong> by implementing <strong>a Snowflake unified data platform for internal operational data, with a Data Clean Room anonymization layer enabling cross-client benchmarking, and a Snowflake Marketplace listing for distribution to 10,000+ FSI customers.</strong>
    </div>
    """, unsafe_allow_html=True)
    editable_field("Modifications or additions to the POV", "", "pov_addl", height=80, track=TRACK2)
    comment_box(TRACK2, "💬 Section 5: Questions about the benchmarking POV")

    # SECTION 6
    st.markdown('<div class="section-h"><div class="section-num">6</div> Success Criteria & Test Cases</div>', unsafe_allow_html=True)

    criteria2 = [
        ("SC-1", "Data Migration Completeness", "Baseline: 0% of internal data on a unified platform", "Target: Pilot data set (1–2 years of case data from 1 BU) successfully migrated to Snowflake and queryable", "How: Validate row counts, data integrity checks, query performance"),
        ("SC-2", "Cross-Client Benchmark Query Performance", "Baseline: No real-time cross-client benchmarking exists", "Target: Produce a benchmark report (false positive rate by institution type) in <5 minutes on Snowflake", "How: Run benchmark SQL on migrated dataset; time the query execution"),
        ("SC-3", "Anonymization Compliance", "Baseline: No anonymization framework in place", "Target: Anonymized output reviewed and approved by AML RS legal/compliance — no individual institution identifiable", "How: Legal review of sample benchmark output"),
        ("SC-4", "Product Revenue Hypothesis Validation", "Baseline: $0 benchmarking product revenue", "Target: 3–5 bank clients express interest in subscribing to benchmark product at $X/month", "How: Share sample benchmark report with 5 current advisory clients and gather feedback/LOIs"),
    ]

    for sc_id, metric, baseline, target, method in criteria2:
        st.markdown(f"""
        <div class="success-criterion">
        <div class="sc-metric">✅ {sc_id}: {metric}</div>
        <div class="sc-detail">📊 {baseline}</div>
        <div class="sc-detail">🎯 {target}</div>
        <div class="sc-detail">📋 {method}</div>
        </div>
        """, unsafe_allow_html=True)

    editable_field("Additional success criteria", "", "sc_addl", height=80, track=TRACK2)
    comment_box(TRACK2, "💬 Section 6: Agree on benchmarking success metrics")

    # SECTION 7
    st.markdown('<div class="section-h"><div class="section-num">7</div> Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)
    prereqs2 = [
        ("❄️", "Snowflake Account with Data Engineering & Marketplace features", "Snowflake", "Day 1", "Standard Business Critical account; Marketplace listing capability included"),
        ("📁", "Extract of internal case management data (2+ years, 1 BU)", "Jonathan McIsaac / AML RS Data Team", "Week 1–2", "Critical blocker — pilot cannot start without this. Jonathan to identify data engineer to pull extract."),
        ("👩‍💻", "AML RS Data Engineer (0.5 FTE for pilot duration)", "AML RightSource", "Week 1", "Required to participate in migration and analytics build. Isabel's team likely source."),
        ("⚖️", "Legal review of anonymization approach", "AML RS Legal", "Week 3", "Required before any benchmark output is shared externally"),
        ("📊", "List of 3–5 current advisory clients willing to preview benchmark product", "AML RS Advisory Team (Sabrina)", "Week 6", "For SC-4 validation — Sabrina to identify candidates"),
        ("🔐", "Data classification and governance policy for internal data", "AML RS Compliance", "Week 2", "Determines what internal data can be migrated and how it must be tagged"),
    ]
    for icon, item, owner, timeline, notes in prereqs2:
        st.markdown(f"""
        <div class="prereq-item">
        <div style="font-size:22px; flex-shrink:0">{icon}</div>
        <div style="flex:1">
        <div style="font-size:14px; font-weight:700; color:#0D2B4E">{item}</div>
        <div style="font-size:12px; color:#718096; margin-top:2px">Owner: <strong>{owner}</strong> &nbsp;|&nbsp; Target: <strong>{timeline}</strong></div>
        <div style="font-size:12px; color:#4A5568; margin-top:4px">{notes}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    editable_field("Additional prerequisites or blockers", "", "prereq_addl", height=60, track=TRACK2)
    comment_box(TRACK2, "💬 Section 7: Jonathan — what data can you pull for the pilot?")

    # SECTION 8
    st.markdown('<div class="section-h"><div class="section-num">8</div> Pilot Execution Plan</div>', unsafe_allow_html=True)
    phases2 = [
        ("Week 1–2", "Discovery & Data Audit", "#00C96F",
         ["Jonathan discovery call: current systems, data volumes, analytics wish list",
          "Data audit: catalog all internal AML process data sources",
          "Identify pilot dataset (recommend: 2 years of case management data from 1 BU)",
          "Set baseline: what benchmark questions can AML RS answer today vs. target"]),
        ("Week 2–4", "Data Migration & Modeling", "#0D2B4E",
         ["AML RS data engineer + Jordan co-build Snowflake data pipeline",
          "Load pilot dataset to Snowflake; validate integrity",
          "Build Snowflake data model (star schema for benchmarking analytics)",
          "Implement anonymization layer (aggregate-level controls, k-anonymity)"]),
        ("Week 4–6", "Benchmark Product Build", "#29B5E8",
         ["Build 3–5 benchmark queries: FP rate by tier, case resolution by region, analyst productivity",
          "Snowsight dashboard for benchmarking intelligence visualization",
          "Jordan technical review of Marketplace listing feasibility",
          "Legal review of anonymized sample output"]),
        ("Week 6–8", "Client Validation & Readout", "#FF7A00",
         ["Share sample benchmark report with 3–5 willing advisory clients",
          "Gather qualitative feedback on value and willingness to pay",
          "Compile pilot results vs. success criteria",
          "Formal readout with Abhishek, Jonathan, and full stakeholder team"]),
    ]
    for period, phase_name, color, activities in phases2:
        st.markdown(f"""
        <div class="phase-card">
        <div class="phase-header"><div style="width:10px;height:10px;border-radius:50%;background:{color};flex-shrink:0"></div><span class="phase-badge">{period}</span><strong>{phase_name}</strong></div>
        <ul style="margin:0 0 0 20px; padding:0">{''.join(f'<li style="font-size:13px; color:#4A5568; margin-bottom:4px">{a}</li>' for a in activities)}</ul>
        </div>
        """, unsafe_allow_html=True)
    comment_box(TRACK2, "💬 Section 8: Timeline notes and adjustments")

    # SECTION 9
    st.markdown('<div class="section-h"><div class="section-num">9</div> Pilot Results & Readout</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete During Pilot</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        editable_field("SC-1: Migration Success (data volume, integrity)", "[COMPLETE DURING PILOT]", "result_sc1", track=TRACK2)
        editable_field("SC-2: Benchmark Query Performance (seconds)", "[COMPLETE DURING PILOT]", "result_sc2", track=TRACK2)
    with c2:
        editable_field("SC-3: Anonymization Legal Approval (Yes/No)", "[COMPLETE DURING PILOT]", "result_sc3", track=TRACK2)
        editable_field("SC-4: Client Interest in Benchmark Product (# of interested clients)", "[COMPLETE DURING PILOT]", "result_sc4", track=TRACK2)
    editable_field("Estimated ARR from benchmark product based on pilot feedback", "[COMPLETE AT READOUT]", "biz_value", height=80, track=TRACK2)
    st.markdown("</div>", unsafe_allow_html=True)
    comment_box(TRACK2, "💬 Section 9: Add results as they come in")

    # SECTION 10
    st.markdown('<div class="section-h"><div class="section-num">10</div> Pilot Readout & Path Forward</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete at Readout</div>', unsafe_allow_html=True)
    editable_field("Did results validate the POV?", "[COMPLETE AT READOUT]", "pov_validated", height=80, track=TRACK2)
    editable_field("Path Forward", "[COMPLETE AT READOUT — Recommended next steps for full data migration, Marketplace listing, and go-to-market for benchmarking product]", "path_forward", height=100, track=TRACK2)
    editable_field("Outstanding Questions Before Contracting", "[COMPLETE AT READOUT]", "outstanding_qs", height=80, track=TRACK2)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("#### 💬 Overall Comments & Questions — Pilot 2")
    render_comments(TRACK2)
    comment_box(TRACK2, "💬 Add overall comment, question, or note for Pilot 2")


# ══════════════════════════════════════════════════════════════════════════════
# PILOT 3 — ALGORITHMS
# ══════════════════════════════════════════════════════════════════════════════
with pilot_tab3:
    TRACK3 = "algorithms"

    st.markdown("""
    <div class="pilot-tab-header" style="border-top-color:#FF7A00">
    <h3 style="margin:0; color:#0D2B4E">⚙️ Pilot 3 — Algorithm Deployment: Native App-Powered Scoring Engine</h3>
    <p style="color:#718096; font-size:13px; margin:6px 0 0">Validate that Snowflake's Native App Framework enables AML RightSource to package, protect, and deploy their proprietary AML scoring algorithms into client environments — transforming a 3–6 month bespoke project into a one-click Marketplace install.</p>
    </div>
    """, unsafe_allow_html=True)

    # SECTION 1
    st.markdown('<div class="section-h"><div class="section-num">1</div> Pilot Owner from AML RightSource</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        editable_field("Primary Pilot Owner", "Isabel Yeung — VP Tech Operations (BloomBrella / Product Engineering)", "owner_primary", track=TRACK3)
    with c2:
        editable_field("Supporting Owner", "Abhishek Mittal — EVP & Chief Product and AI Officer", "owner_secondary", track=TRACK3)
    comment_box(TRACK3, "💬 Section 1: Questions about pilot ownership")

    # SECTION 2
    st.markdown('<div class="section-h"><div class="section-num">2</div> Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    editable_field("POV Statement",
        "AML RightSource's engineering team (led by Isabel Yeung) has built proprietary AML scoring algorithms, case prioritization models, and QA automation logic that represent years of domain expertise and IP investment. Today, deploying these algorithms into client environments requires 3–6 months of bespoke engineering per client — making the business model fundamentally unscalable. We believe Snowflake's Native App Framework can package this IP into self-serve, installable applications that bank clients deploy in minutes from the Snowflake Marketplace, protecting AML RightSource's IP while creating a recurring SaaS revenue model scalable to all 200+ bank clients.",
        "pov_statement", height=150, track=TRACK3)
    st.markdown("""
    <div class="callout-orange">
    <strong>Why this is transformational:</strong> Isabel's team is building AML RightSource's future as a technology company. Without a scalable distribution mechanism, these algorithms remain professional services deliverables. Native Apps turn them into products. This changes the P&L, the exit story, and the competitive moat permanently.
    </div>
    """, unsafe_allow_html=True)
    comment_box(TRACK3, "💬 Section 2: Questions about the algorithm deployment POV")

    # SECTION 3
    st.markdown('<div class="section-h"><div class="section-num">3</div> Business Drivers & Objectives</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        editable_field("Current Business Problem",
            "Isabel's engineering team builds AML scoring algorithms in Python environments. Deploying these into a client's environment currently requires: (1) understanding client's data infrastructure, (2) custom API/connector build, (3) security and compliance review at each client, (4) ongoing maintenance per client. This is 3–6 months × 200 clients = an engineering backlog that cannot be cleared. Revenue model is project-based, not recurring. IP is exposed in each custom deployment.",
            "biz_problem", height=150, track=TRACK3)
    with col2:
        editable_field("Business Objective",
            "1) Build and package 1 existing AML scoring algorithm as a Snowflake Native App. 2) Validate that the Native App runs correctly on a bank client's Snowflake data (using synthetic data in pilot). 3) Confirm IP is protected — client cannot see algorithm logic. 4) Estimate deployment time reduction vs. current process. 5) Validate subscription revenue model vs. project-based model.",
            "biz_objective", height=150, track=TRACK3)
    comment_box(TRACK3, "💬 Section 3: Isabel — what algorithms are most ready for productization?")

    # SECTION 4
    st.markdown('<div class="section-h"><div class="section-num">4</div> Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    editable_field("Current Algorithm / Product Inventory (Isabel to complete)",
        "[Isabel to complete: list the algorithms and data products currently built or in roadmap. For each: name, purpose, current language/framework (Python/SQL?), current deployment method, number of clients using it today, and monthly revenue generated.]\n\nExample format:\n• AlertIQ — alert prioritization — Python (XGBoost) — Manual integration per client — 3 clients — $15K/engagement\n• KYC Refresh — Python (RF) — in development — 0 clients",
        "algo_inventory", height=150, track=TRACK3)
    editable_field("Current Technology Stack (Isabel to confirm)",
        "[Python version, ML libraries used (XGBoost, sklearn, Pandas, etc.), current cloud platform (AWS/Azure?), current model serving approach (Docker containers? API? Manual?)]\nThis determines Snowpark compatibility and migration complexity.",
        "tech_stack", height=100, track=TRACK3)
    editable_field("Current Deployment Friction Points",
        "[Isabel to describe the top 3 frustrations with current algorithm deployment process — specific blockers, integration challenges, client IT friction, IP concerns, etc.]",
        "deploy_friction", height=80, track=TRACK3)
    comment_box(TRACK3, "💬 Section 4: Isabel — your current state details are critical for pilot design")

    # SECTION 5
    st.markdown('<div class="section-h"><div class="section-num">5</div> Point of View (Snowflake\'s Prediction)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-blue">
    <strong>Snowflake's POV:</strong> We believe Snowflake can overcome <strong>AML RightSource's inability to scale algorithm deployment across 200+ bank clients</strong> while supporting <strong>Isabel's product roadmap and AML RightSource's objective of recurring SaaS algorithm revenue</strong> by implementing <strong>Snowflake's Native App Framework — packaging AML RightSource's first scoring algorithm as a Native App with Snowpark Python, publishing it to Snowflake Marketplace, and demonstrating one-click installation on synthetic bank data in a 60-day pilot.</strong>
    </div>
    """, unsafe_allow_html=True)
    editable_field("Modifications or additions to POV", "", "pov_addl", height=80, track=TRACK3)
    comment_box(TRACK3, "💬 Section 5: Questions about Native App POV")

    # SECTION 6
    st.markdown('<div class="section-h"><div class="section-num">6</div> Success Criteria & Test Cases</div>', unsafe_allow_html=True)
    criteria3 = [
        ("SC-1", "Native App Build Success", "Baseline: Algorithm runs in isolated Python environment", "Target: Algorithm successfully packaged as Snowflake Native App and installs in test environment without error", "How: Jordan + Isabel build Native App in pilot environment; test install on synthetic bank Snowflake account"),
        ("SC-2", "IP Protection Validation", "Baseline: Algorithm code exposed in every client deployment", "Target: Client Snowflake account can execute the Native App but cannot see or extract the underlying algorithm code", "How: Attempt to view algorithm source code from client account — confirm access denied"),
        ("SC-3", "Algorithm Output Accuracy", "Baseline: Algorithm accuracy in production (Isabel to confirm)", "Target: Native App output matches standalone algorithm output to >99% accuracy on synthetic test dataset", "How: Run both versions on same synthetic dataset; compare results"),
        ("SC-4", "Deployment Time Reduction", "Baseline: 3–6 months per client deployment", "Target: Native App install in <30 minutes on a new client Snowflake account", "How: Time the end-to-end installation on second test environment"),
    ]
    for sc_id, metric, baseline, target, method in criteria3:
        st.markdown(f"""
        <div class="success-criterion">
        <div class="sc-metric">✅ {sc_id}: {metric}</div>
        <div class="sc-detail">📊 {baseline}</div>
        <div class="sc-detail">🎯 {target}</div>
        <div class="sc-detail">📋 {method}</div>
        </div>
        """, unsafe_allow_html=True)
    editable_field("Additional success criteria (Isabel's input)", "", "sc_addl", height=80, track=TRACK3)
    comment_box(TRACK3, "💬 Section 6: Isabel — are these the right technical success criteria?")

    # SECTION 7
    st.markdown('<div class="section-h"><div class="section-num">7</div> Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)
    prereqs3 = [
        ("❄️", "Snowflake Developer Account with Native App Framework access", "Snowflake", "Day 1", "Jordan provisions this. Snowflake Business Critical recommended for IP protection testing."),
        ("🐍", "Python Algorithm Source Code (1 algorithm ready for Snowpark port)", "Isabel Yeung / Engineering Team", "Week 1", "Critical: Isabel identifies which algorithm is most ready. Code must be compatible with Snowpark Python (standard libraries supported)."),
        ("👩‍💻", "AML RS Engineer (1.0 FTE for Native App build)", "Isabel's Engineering Team", "Week 1–6", "This is a significant engineering commitment. Isabel needs to allocate an engineer for the 6-week build phase."),
        ("📊", "Synthetic Bank Data (matching algorithm input schema)", "Snowflake (Jordan)", "Week 1–2", "Jordan creates synthetic TM alert dataset that matches the algorithm's required input format"),
        ("🧪", "Second Test Environment (simulate client install)", "Snowflake", "Week 4", "Jordan provisions a second Snowflake trial account to simulate the client installation experience"),
        ("📋", "Algorithm input/output schema documentation", "Isabel's Team", "Week 1", "Required to build correct Snowpark wrapper and test data. Isabel's team to provide before pilot starts."),
        ("🔐", "IP protection review (confirm what client can/cannot see in Native App)", "AML RS Legal + Jordan", "Week 3", "Legal must confirm Native App structure meets IP protection requirements before any client-facing deployment"),
    ]
    for icon, item, owner, timeline, notes in prereqs3:
        st.markdown(f"""
        <div class="prereq-item">
        <div style="font-size:22px; flex-shrink:0">{icon}</div>
        <div style="flex:1">
        <div style="font-size:14px; font-weight:700; color:#0D2B4E">{item}</div>
        <div style="font-size:12px; color:#718096; margin-top:2px">Owner: <strong>{owner}</strong> &nbsp;|&nbsp; Target: <strong>{timeline}</strong></div>
        <div style="font-size:12px; color:#4A5568; margin-top:4px">{notes}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    editable_field("Additional prerequisites or blockers", "", "prereq_addl", height=60, track=TRACK3)
    comment_box(TRACK3, "💬 Section 7: Isabel — flag any tech prerequisites we're missing")

    # SECTION 8
    st.markdown('<div class="section-h"><div class="section-num">8</div> Pilot Execution Plan</div>', unsafe_allow_html=True)
    phases3 = [
        ("Week 1–2", "Algorithm Discovery & Scoping", "#FF7A00",
         ["Isabel technical discovery call with Jordan — current stack, algorithm architecture, Snowpark compatibility assessment",
          "Select 1 algorithm for Native App pilot (recommendation: AlertIQ priority scorer — highest client impact)",
          "Document algorithm input/output schema",
          "Jordan provisions Snowflake dev environment + synthetic test dataset"]),
        ("Week 2–5", "Native App Development", "#0D2B4E",
         ["Isabel's engineer + Jordan co-build Snowpark Python wrapper for selected algorithm",
          "Package algorithm as Native App with consumer privileges defined",
          "Week 3: First functional Native App install test in dev environment",
          "IP protection testing: verify client cannot view algorithm source",
          "Accuracy testing: compare Native App output vs. standalone model"]),
        ("Week 5–7", "Client Simulation & Performance", "#29B5E8",
         ["Jordan provisions second Snowflake account (simulates client environment)",
          "Install Native App from AML RS account to client test account — time the process",
          "Run algorithm on synthetic bank data in 'client' environment",
          "Capture deployment time, setup requirements, any client IT dependencies"]),
        ("Week 7–8", "Marketplace Readiness & Readout", "#00C96F",
         ["Review Snowflake Marketplace listing requirements with Jordan",
          "Draft Marketplace listing description, pricing model, and documentation",
          "Compile pilot results vs. all success criteria",
          "Readout meeting — Abhishek, Isabel, full stakeholder team"]),
    ]
    for period, phase_name, color, activities in phases3:
        st.markdown(f"""
        <div class="phase-card">
        <div class="phase-header"><div style="width:10px;height:10px;border-radius:50%;background:{color};flex-shrink:0"></div><span class="phase-badge">{period}</span><strong>{phase_name}</strong></div>
        <ul style="margin:0 0 0 20px; padding:0">{''.join(f'<li style="font-size:13px; color:#4A5568; margin-bottom:4px">{a}</li>' for a in activities)}</ul>
        </div>
        """, unsafe_allow_html=True)
    comment_box(TRACK3, "💬 Section 8: Isabel — adjust timeline for engineering capacity")

    # SECTION 9
    st.markdown('<div class="section-h"><div class="section-num">9</div> Pilot Results & Readout</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete During Pilot</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        editable_field("SC-1: Native App Build — Success / Blockers", "[COMPLETE DURING PILOT]", "result_sc1", track=TRACK3)
        editable_field("SC-2: IP Protection Test Result", "[COMPLETE DURING PILOT]", "result_sc2", track=TRACK3)
    with c2:
        editable_field("SC-3: Algorithm Accuracy (Native App vs. Standalone)", "[COMPLETE DURING PILOT]", "result_sc3", track=TRACK3)
        editable_field("SC-4: Deployment Time (minutes)", "[COMPLETE DURING PILOT]", "result_sc4", track=TRACK3)
    editable_field("Business Value Summary — Revenue Model Comparison",
        "[COMPLETE AT READOUT — Compare: Old model (project-based deployment revenue per client) vs. New model (Native App subscription ARR at scale). Estimate 3-year revenue impact if all 200 clients adopt 1 algorithm as Native App subscription.]",
        "biz_value", height=100, track=TRACK3)
    st.markdown("</div>", unsafe_allow_html=True)
    comment_box(TRACK3, "💬 Section 9: Add engineering results as pilot progresses")

    # SECTION 10
    st.markdown('<div class="section-h"><div class="section-num">10</div> Pilot Readout & Path Forward</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete at Readout</div>', unsafe_allow_html=True)
    editable_field("Did results validate the POV? (Yes / Partial / No — explain)", "[COMPLETE AT READOUT]", "pov_validated", height=80, track=TRACK3)
    editable_field("Confirmed Outcomes vs. Success Criteria", "[SC-1: ]\n[SC-2: ]\n[SC-3: ]\n[SC-4: ]", "outcomes_confirmed", height=100, track=TRACK3)
    editable_field("Path Forward — Recommended Next Steps",
        "[Example: 'Pilot validates Native App viability. Recommended: full algorithm portfolio Native App buildout — 4 algorithms over 12 months. Target Marketplace launch date: [DATE]. Estimated Year 1 algorithm ARR: $[X]M at $[price]/mo × [N] installs.']",
        "path_forward", height=100, track=TRACK3)
    editable_field("Roadmap for Remaining Algorithm Portfolio",
        "[Which algorithms should be productized next? What is the priority order? What engineering resources are needed?]",
        "algo_roadmap", height=80, track=TRACK3)
    editable_field("Outstanding Questions Before Contracting", "[COMPLETE AT READOUT]", "outstanding_qs", height=80, track=TRACK3)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("#### 💬 Overall Comments & Questions — Pilot 3")
    render_comments(TRACK3)
    comment_box(TRACK3, "💬 Add overall comment, question, or note for Pilot 3")

# ── GLOBAL COMMENT VIEW ───────────────────────────────────────────────────────
st.markdown("---")
with st.expander("📬 View All Comments Across All Pilots"):
    for track_name, track_key in [("Pilot 1 — Advisory", "advisory"), ("Pilot 2 — Data Assets", "data_assets"), ("Pilot 3 — Algorithms", "algorithms")]:
        comments = st.session_state.comments[track_key]
        if comments:
            st.markdown(f"#### {track_name} ({len(comments)} comments)")
            render_comments(track_key)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
    🚀 AML RightSource × Snowflake — Pilot Planning Suite<br>
    Prepared by: Kala Boudreaux · Eric Szenderski · Jordan Ude — Snowflake Enterprise Acquisition<br>
    <span style="font-size:10px">All fields are editable. Your inputs are saved for this session. For persistent storage, contact your Snowflake account team.</span>
</div>
""", unsafe_allow_html=True)
