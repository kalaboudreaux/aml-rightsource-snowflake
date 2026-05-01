import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import json
from datetime import datetime, timedelta

st.set_page_config(
    page_title="AML RightSource × Snowflake — Live Demo",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.demo-hero {
    background: linear-gradient(135deg, #0D2B4E 0%, #1A3A6B 60%, #29B5E8 150%);
    border-radius: 16px; padding: 40px 48px; margin-bottom: 28px; color: white;
    position: relative; overflow: hidden;
}
.demo-hero::after {
    content: ''; position: absolute; right: -30px; bottom: -30px;
    width: 200px; height: 200px; border-radius: 50%;
    background: rgba(41,181,232,0.1); border: 40px solid rgba(41,181,232,0.08);
}
.demo-badge {
    display: inline-block; background: rgba(41,181,232,0.2);
    border: 1px solid rgba(41,181,232,0.4); color: #29B5E8;
    padding: 4px 12px; border-radius: 20px; font-size: 11px;
    font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px;
}
.demo-hero h1 { font-size: 36px; font-weight: 900; margin: 0 0 8px; }
.demo-hero p { color: rgba(255,255,255,0.7); font-size: 15px; margin: 0; }

.metric-big {
    background: white; border: 1px solid #D1E8F5; border-radius: 12px;
    padding: 20px; text-align: center;
    box-shadow: 0 2px 12px rgba(41,181,232,0.08);
}
.metric-big-num { font-size: 32px; font-weight: 900; color: #29B5E8; }
.metric-big-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px;
    color: #718096; margin-top: 4px; }
.metric-big-delta { font-size: 13px; font-weight: 600; color: #00C96F; margin-top: 2px; }

.alert-card {
    border-radius: 10px; padding: 14px 16px; margin-bottom: 8px;
    border: 1px solid; transition: all 0.3s;
}
.alert-high { background: #FEF2F2; border-color: #FECACA; }
.alert-med { background: #FFFBEB; border-color: #FDE68A; }
.alert-low { background: #F0FDF4; border-color: #BBF7D0; }

.ai-bubble {
    background: linear-gradient(135deg, #E8F7FD, #F0F9FF);
    border: 1px solid #29B5E8; border-radius: 12px 12px 12px 0;
    padding: 16px 20px; margin: 12px 0; position: relative;
}
.ai-bubble::before {
    content: '🤖 Cortex AI';
    font-size: 11px; font-weight: 700; color: #29B5E8;
    text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px;
}

.share-box {
    background: linear-gradient(135deg, #F0FDF4, #E8F7FD);
    border: 2px dashed #29B5E8; border-radius: 12px; padding: 24px; text-align: center;
}

.typing-cursor::after { content: '|'; animation: blink 1s infinite; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

.flow-step {
    display: flex; align-items: center; gap: 12px; padding: 12px 16px;
    border-radius: 8px; margin-bottom: 8px;
}
.flow-step.active { background: #E8F7FD; border: 1px solid #29B5E8; }
.flow-step.done { background: #E6FBF3; border: 1px solid #BBF7D0; }
.flow-step.pending { background: #F7FAFC; border: 1px solid #E2E8F0; }

.tab-content { padding: 8px 0; }

.benchmark-bar {
    background: #E2E8F0; border-radius: 4px; height: 20px;
    overflow: hidden; position: relative;
}
.benchmark-fill {
    height: 100%; border-radius: 4px;
    display: flex; align-items: center; padding-left: 8px;
    font-size: 11px; font-weight: 700; color: white;
}

.clean-room-card {
    background: linear-gradient(135deg, #1A1A2E, #0D2B4E);
    color: white; border-radius: 14px; padding: 24px; margin: 12px 0;
}

.marketplace-card {
    background: white; border: 1px solid #D1E8F5; border-radius: 12px;
    padding: 16px; display: flex; gap: 14px; align-items: flex-start;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 10px;
}

.native-app-card {
    background: linear-gradient(135deg, #29B5E8, #0D2B4E);
    color: white; border-radius: 12px; padding: 20px; text-align: center;
}

.status-chip {
    display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;
}
.status-active { background: #D1FAE5; color: #065F46; }
.status-pending { background: #FEF3C7; color: #92400E; }
.status-new { background: #DBEFFE; color: #1E6FA8; }
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="demo-hero">
    <div class="demo-badge">🎯 Interactive Live Demo</div>
    <h1>AML RightSource × Snowflake</h1>
    <p>Experience the power of Snowflake's AI Data Cloud — built for financial crimes compliance.<br>This is what your platform could look like, live and in production.</p>
</div>
""", unsafe_allow_html=True)

# Real-time clock
now = datetime.now()
st.markdown(f"<div style='text-align:right; color:#718096; font-size:12px; margin-top:-20px; margin-bottom:16px'>🟢 Live Demo Environment — {now.strftime('%B %d, %Y %I:%M %p')}</div>", unsafe_allow_html=True)

# ── TOP METRICS ───────────────────────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
mets = [
    ("🏦", "Active Client Shares", "47", "+3 today"),
    ("🚨", "Live Alerts (TM)", "2,847", "↓ 18% (AI filter)"),
    ("⚡", "Avg Data Access Time", "1.4 hrs", "Was 14 days"),
    ("🤖", "AI Investigations", "312", "Today"),
    ("💰", "Data Product Revenue", "$142K", "This Month"),
]
for col, (icon, label, val, delta) in zip([c1,c2,c3,c4,c5], mets):
    with col:
        st.markdown(f"""
        <div class="metric-big">
        <div style="font-size:22px">{icon}</div>
        <div class="metric-big-num">{val}</div>
        <div class="metric-big-label">{label}</div>
        <div class="metric-big-delta">{delta}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── MAIN DEMO TABS ────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔗 Live Data Sharing",
    "🤖 Cortex AI — Alert Intelligence",
    "📊 Benchmarking Platform",
    "🛡️ Data Clean Room",
    "📱 Native App Marketplace",
    "🔮 Predictive Analytics",
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — LIVE DATA SHARING DEMO
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.markdown("### 🔗 Zero-Copy Data Sharing — Live Client Onboarding")
    st.markdown("""
    **Watch:** A bank client grants AML RightSource secure, read-only access to their transaction monitoring data — no file transfer, no ETL, no email. Click to simulate the end-to-end flow.
    """)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("#### Onboarding Simulation")

        bank_name = st.selectbox("Select Client Bank", [
            "First National Bank (Mid-West)",
            "Community Trust Bank",
            "Heritage Financial Group",
            "Regional Savings & Loan",
            "Valley Business Bank"
        ])

        share_type = st.radio("Data Share Type", [
            "TM Alert Data + Case History",
            "KYC/CDD Customer Records",
            "Full Advisory Package (TM + KYC + SAR)"
        ], horizontal=True)

        if st.button("⚡ Initiate Secure Data Share", type="primary"):
            steps = [
                ("🔐", "Establishing encrypted Snowflake-to-Snowflake connection..."),
                ("📋", f"Client {bank_name} granting read-only share permissions..."),
                ("✅", "Security and access controls validated (zero-copy)..."),
                ("📊", "Materializing shared data view in AML RightSource account..."),
                ("🤖", "Running Cortex AI schema detection and normalization..."),
                ("🚀", "Data ready for advisory analysis!"),
            ]

            progress = st.progress(0)
            status_ph = st.empty()
            for i, (icon, msg) in enumerate(steps):
                time.sleep(0.5)
                progress.progress((i + 1) / len(steps))
                status_ph.markdown(f"""
                <div style="background:#E8F7FD; border-left:3px solid #29B5E8; border-radius:0 8px 8px 0; padding:10px 14px; font-size:13px; color:#0D2B4E">
                {icon} {msg}
                </div>
                """, unsafe_allow_html=True)

            st.success(f"✅ **{bank_name}** data share established in **8 seconds**. Previously this took **14 days** via FTP/email.")

            st.markdown("""
            <div style="background:#E6FBF3; border:1px solid #BBF7D0; border-radius:10px; padding:16px; margin-top:8px">
            <strong>🟢 Active Share Details:</strong><br>
            📁 Tables shared: <strong>ALERTS_LIVE, CUSTOMER_RISK, CASE_HISTORY, TM_RULES</strong><br>
            🔐 Access: <strong>Read-Only · Zero-Copy · No Data Movement</strong><br>
            ⏱️ Latency: <strong>Real-time (sub-second)</strong><br>
            🌐 Residency: <strong>Data never leaves client's Snowflake environment</strong>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Active Client Shares")

        np.random.seed(42)
        shares_data = pd.DataFrame({
            "Bank Client": ["First National", "Heritage Financial", "Community Trust", "Valley Business", "Regional S&L", "Pacific Coast Bank", "Midwest Cooperative"],
            "Status": ["🟢 Active", "🟢 Active", "🟢 Active", "🟡 Pending", "🟢 Active", "🔵 New", "🟢 Active"],
            "Tables Shared": [12, 8, 15, 0, 9, 6, 11],
            "Last Update": ["2 min ago", "14 min ago", "1 hr ago", "Awaiting", "5 min ago", "Today", "3 hr ago"],
            "Records (M)": [4.2, 1.8, 7.1, 0, 2.9, 1.2, 5.4],
        })
        st.dataframe(shares_data, use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="share-box">
        <div style="font-size:32px">⏱️</div>
        <div style="font-size:28px; font-weight:900; color:#0D2B4E">14 days → 8 seconds</div>
        <div style="font-size:14px; color:#718096; margin-top:4px">Average client data onboarding time</div>
        <div style="font-size:12px; color:#00C96F; font-weight:600; margin-top:4px">98% time reduction</div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — CORTEX AI ALERT INTELLIGENCE
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown("### 🤖 Cortex AI — Intelligent Alert Investigation")
    st.markdown("**Experience:** AI-powered alert triage, investigation summarization, and SAR narrative generation — all native in Snowflake with no additional AI platform.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### Alert Queue (Live Simulation)")

        alerts = [
            {"id": "ALT-8847", "customer": "Jorge Martinez", "amount": "$147,500", "type": "Structuring", "risk": "HIGH", "score": 94, "pattern": "15 cash deposits <$10K over 18 days"},
            {"id": "ALT-8851", "customer": "Sunrise Holdings LLC", "amount": "$2.4M", "type": "Wire Transfer", "risk": "HIGH", "score": 89, "pattern": "Multiple wires to sanctioned jurisdiction proximity"},
            {"id": "ALT-8863", "customer": "Amanda Chen", "amount": "$8,200", "type": "Unusual Activity", "risk": "MEDIUM", "score": 62, "pattern": "Out-of-pattern activity vs. 6-month baseline"},
            {"id": "ALT-8879", "customer": "TechFlow Payments", "amount": "$45,000", "type": "Rapid Movement", "risk": "MEDIUM", "score": 57, "pattern": "Funds in/out <24hr, 3rd party payees"},
            {"id": "ALT-8891", "customer": "Green Valley Farm", "amount": "$3,100", "type": "Low Risk Flag", "risk": "LOW", "score": 28, "pattern": "Seasonal revenue pattern — likely false positive"},
        ]

        selected = st.selectbox("Select Alert to Investigate",
            [f"{a['id']} | {a['risk']} | {a['customer']} | {a['amount']}" for a in alerts])

        alert_idx = [a['id'] for a in alerts].index(selected.split(" | ")[0])
        alert = alerts[alert_idx]

        risk_color = {"HIGH": "#alert-high", "MEDIUM": "#alert-med", "LOW": "#alert-low"}
        risk_bg = {"HIGH": "#FEF2F2", "MEDIUM": "#FFFBEB", "LOW": "#F0FDF4"}
        risk_border = {"HIGH": "#FECACA", "MEDIUM": "#FDE68A", "LOW": "#BBF7D0"}

        st.markdown(f"""
        <div style="background:{risk_bg[alert['risk']]}; border:1px solid {risk_border[alert['risk']]}; border-radius:10px; padding:16px">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px">
        <div><strong style="font-size:16px">{alert['id']}</strong> — {alert['customer']}</div>
        <div style="font-weight:700; color:{'#991B1B' if alert['risk']=='HIGH' else '#92400E' if alert['risk']=='MEDIUM' else '#065F46'}">{alert['risk']} RISK</div>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:13px">
        <div>💰 <strong>Amount:</strong> {alert['amount']}</div>
        <div>🎯 <strong>Type:</strong> {alert['type']}</div>
        <div>📊 <strong>Risk Score:</strong> {alert['score']}/100</div>
        <div>🔍 <strong>Pattern:</strong> {alert['pattern']}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Risk Score Progression:**")
        score_prog = [random.randint(20, 40)] * 3 + list(range(40, alert['score'], 8)) + [alert['score']]
        score_df = pd.DataFrame({"Day": range(len(score_prog)), "Risk Score": score_prog})
        st.line_chart(score_df.set_index("Day"), color="#29B5E8", height=120)

    with col2:
        st.markdown("#### Cortex AI Investigation")

        if st.button("🤖 Run Cortex AI Investigation", type="primary"):
            with st.spinner("Cortex AI analyzing transaction patterns..."):
                time.sleep(1.5)

            ai_summaries = {
                "ALT-8847": """**Investigation Summary — ALT-8847 (Jorge Martinez)**

The subject has engaged in a classic structuring pattern across 15 transactions totaling $147,500 over an 18-day period. All deposits are cash, ranging from $8,200 to $9,800 — consistently below the $10,000 Currency Transaction Report threshold. Transaction timestamps are distributed across 6 branch locations to avoid detection at any single branch.

**Key Risk Indicators:**
• Smurfing pattern with >95% confidence (ML model score: 94/100)
• Zero prior structuring alerts in 4-year account history — sudden behavioral shift
• Geographic dispersion across branches inconsistent with customer's stated address
• No corresponding wire or deposit source that explains cash volume

**AI Recommendation: File SAR — Priority 1**
Estimated SAR filing time with AI assist: 12 minutes (vs. 45 min manual)""",

                "ALT-8851": """**Investigation Summary — ALT-8851 (Sunrise Holdings LLC)**

Entity has executed 7 international wire transfers totaling $2.4M over 21 days. Destination jurisdictions include UAE (3 wires), Turkey (2 wires), and Lebanon (2 wires) — all FATF grey list or high-risk jurisdictions as of Q1 2026.

**Key Risk Indicators:**
• Beneficial ownership structure is opaque — single managing member, no known business purpose
• Wire amounts calibrated just below SWIFT reporting threshold on 5 of 7 transactions
• No corresponding revenue deposits or documented business operations
• Entity registered 4 months prior to first suspicious wire

**AI Recommendation: Escalate to BSA Officer — Possible SAR + OFAC review**""",

                "ALT-8863": """**Investigation Summary — ALT-8863 (Amanda Chen)**

Customer shows out-of-pattern activity vs. 6-month behavioral baseline. ML anomaly score: 62/100. Pattern is unusual but not immediately indicative of financial crime.

**Key Risk Indicators:**
• 3 transactions totaling $8,200 to new payees not in historical network
• Timing coincides with stated job change (captured in CDD refresh)
• Payees are registered US businesses with clean profiles

**AI Recommendation: No SAR Required — Monitor 30 days**
High probability of false positive (78% confidence). Document analysis and close alert.""",

                "ALT-8879": """**Investigation Summary — ALT-8879 (TechFlow Payments)**

Entity demonstrating rapid movement pattern — funds move in and out within 24 hours to third-party payees. Risk score 57/100.

**Key Risk Indicators:**
• 6 pass-through transactions in 14 days
• Payee analysis: 4 of 6 payees are high-risk freelance platforms
• However, entity is a documented payments processor — this may be core business activity

**AI Recommendation: Clarifying documentation request before SAR decision**""",

                "ALT-8891": """**Investigation Summary — ALT-8891 (Green Valley Farm)**

Low-risk flag generated by rule engine. Pattern analysis indicates seasonal agricultural revenue cycle — consistent with 3-year account history.

**AI Recommendation: False Positive — Close Alert**
This alert matches the seasonal harvesting revenue pattern seen in 2023 and 2024 for this customer. Risk score: 28/100. No investigative action required. Closing alert saves analyst 25 minutes.""",
            }

            st.markdown(f"""
            <div class="ai-bubble">
            {ai_summaries.get(alert['id'], "Analysis complete.")}
            </div>
            """, unsafe_allow_html=True)

            if alert['risk'] == "HIGH":
                st.markdown("#### 📝 AI-Generated SAR Narrative Draft")
                if st.button("Generate SAR Narrative with Cortex AI"):
                    with st.spinner("Generating SAR narrative..."):
                        time.sleep(1)
                    st.markdown("""
                    <div class="ai-bubble">
                    <strong>DRAFT SAR Narrative — [AML RightSource Advisory]</strong><br><br>
                    The reporting financial institution is filing this Suspicious Activity Report (SAR) regarding the account activity of [Customer Name], account number [XXXX], for the period [Date Range].<br><br>
                    The subject engaged in a structured cash deposit pattern across multiple branch locations, totaling $147,500 in 15 separate transactions. All transactions were conducted in cash and ranged from $8,200 to $9,800, consistently below the Currency Transaction Report (CTR) threshold of $10,000. The geographic dispersion of transactions across 6 branch locations, combined with the absence of legitimate business income sufficient to explain the cash volume, is consistent with structuring as defined under 31 U.S.C. § 5324.<br><br>
                    <em>[AI Draft — requires analyst review before submission. Estimated review time: 8 minutes]</em>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("#### AI Performance Metrics")
        ai_metrics = pd.DataFrame({
            "Metric": ["False Positive Rate", "SAR Filing Time", "Alert Triage Time", "Analyst Accuracy"],
            "Before Cortex AI": ["35%", "45 min", "22 min", "Baseline"],
            "With Cortex AI": ["14%", "12 min", "4 min", "+23%"],
            "Improvement": ["60%↓", "73%↓", "82%↓", "+23%"],
        })
        st.dataframe(ai_metrics, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — BENCHMARKING PLATFORM
# ─────────────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown("### 📊 AML Intelligence Benchmarking Platform")
    st.markdown("**Powered by:** AML RightSource's aggregate data asset across 200+ FI clients, unified on Snowflake")

    st.markdown("""
    <div style="background:#FFF8E6; border-left:3px solid #FF7A00; border-radius:0 8px 8px 0; padding:12px 16px; font-size:13px; margin-bottom:16px">
    <strong>⭐ This is the crown jewel.</strong> No other advisory firm in financial crimes compliance has visibility across 200+ FIs simultaneously. This benchmarking capability is only possible because AML RightSource's operational data is unified on Snowflake.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.2])

    with c1:
        st.markdown("#### Configure Your Benchmark")
        bank_tier = st.selectbox("Institution Tier", ["Community Bank (<$1B)", "Mid-Tier ($1B–$10B)", "Regional ($10B–$50B)", "Large ($50B+)"])
        region = st.selectbox("Geography", ["National", "Midwest", "Northeast", "Southeast", "West Coast"])
        metric = st.selectbox("Benchmark Metric", [
            "False Positive Rate (TM Alerts)",
            "SAR Filing Rate",
            "Case Resolution Time",
            "Analyst Productivity (Cases/Day)",
            "KYC Refresh Cycle Time",
        ])

        if st.button("📊 Generate Benchmark Report", type="primary"):
            with st.spinner("Querying cross-client intelligence..."):
                time.sleep(1)

            st.markdown(f"#### {metric} — {bank_tier} Benchmark")

            np.random.seed(123)
            n_banks = 47
            baseline = {"False Positive Rate (TM Alerts)": 32, "SAR Filing Rate": 0.8, "Case Resolution Time": 18, "Analyst Productivity (Cases/Day)": 12, "KYC Refresh Cycle Time": 45}
            base = baseline.get(metric, 25)
            unit = {"False Positive Rate (TM Alerts)": "%", "SAR Filing Rate": "%", "Case Resolution Time": " days", "Analyst Productivity (Cases/Day)": " cases/day", "KYC Refresh Cycle Time": " days"}
            u = unit.get(metric, "")

            data = np.random.normal(base, base * 0.25, n_banks)
            data = np.clip(data, base * 0.4, base * 1.8)
            your_val = base * 1.15

            df_bench = pd.DataFrame({"Bank": [f"Bank {i+1:02d}" for i in range(n_banks)], "Value": data})
            df_bench = df_bench.sort_values("Value")

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Your Institution", f"{your_val:.1f}{u}", f"{((your_val/base)-1)*100:+.0f}% vs. peer median")
            with col_b:
                st.metric("Peer Median", f"{base:.1f}{u}", f"{n_banks} peers in cohort")
            with col_c:
                st.metric("Top Quartile", f"{np.percentile(data, 25):.1f}{u}", "25th percentile benchmark")

            st.bar_chart(df_bench.set_index("Bank").head(20), height=200, color="#29B5E8")

            st.markdown(f"""
            <div style="background:#E8F7FD; border:1px solid #29B5E8; border-radius:10px; padding:14px; font-size:13px">
            <strong>🤖 AI Insight:</strong> Your institution's {metric.lower()} of <strong>{your_val:.1f}{u}</strong> places you in the <strong>62nd percentile</strong> among {bank_tier} institutions in {region}. The top-performing quartile achieves <strong>{np.percentile(data, 25):.1f}{u}</strong>. 
            Implementing AML RightSource's recommended TM rule tuning methodology could improve your score by an estimated <strong>18–22%</strong> — moving you to the top quartile within 90 days.
            </div>
            """, unsafe_allow_html=True)

    with c2:
        st.markdown("#### Industry Trend Analysis")
        months = pd.date_range(start='2024-01-01', periods=16, freq='ME')
        np.random.seed(42)
        trend_df = pd.DataFrame({
            "Month": months,
            "Industry Avg FP Rate": 35 - np.cumsum(np.random.uniform(0.2, 0.8, 16)),
            "AML RS Client Avg": 30 - np.cumsum(np.random.uniform(0.4, 1.1, 16)),
        }).set_index("Month")
        st.line_chart(trend_df, height=220)
        st.caption("16-month trend: AML RightSource clients consistently outperform industry average by 12–18%")

        st.markdown("#### Cross-Client Intelligence (Live)")
        intel = pd.DataFrame({
            "Emerging Pattern": [
                "Crypto→Fiat structuring via DEX",
                "Business email compromise → wire",
                "Romance scam payroll deposits",
                "BNPL platform layering",
                "NFT wash trading",
            ],
            "Detected Across": ["34 FIs", "67 FIs", "28 FIs", "19 FIs", "12 FIs"],
            "Alert Issued": ["✅", "✅", "✅", "⚠️ New", "⚠️ New"],
        })
        st.dataframe(intel, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 4 — DATA CLEAN ROOM
# ─────────────────────────────────────────────────────────────────────────────
with tab4:
    st.markdown("### 🛡️ Snowflake Data Clean Room — Secure Intelligence Sharing")
    st.markdown("**The most powerful AML tool you've never had:** Discover shared patterns across client institutions without either party seeing the other's raw data.")

    st.markdown("""
    <div class="clean-room-card">
    <h4 style="color:#29B5E8; margin-top:0">🔐 What is a Data Clean Room?</h4>
    <p style="color:rgba(255,255,255,0.8); font-size:14px">
    A Snowflake Data Clean Room allows two parties to compute on a combined dataset — seeing only the result of the computation, never the underlying data. In AML/BSA, this means AML RightSource can help two bank clients identify shared money mule networks, common structuring actors, or cross-institution fraud patterns <strong>without either bank ever seeing the other bank's customer data.</strong>
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:16px">
    <div style="background:rgba(255,255,255,0.08); border-radius:8px; padding:12px; text-align:center"><div style="font-size:22px">🏦</div><div style="font-size:12px; color:rgba(255,255,255,0.7)">Bank A shares data<br>(never visible to Bank B)</div></div>
    <div style="background:rgba(41,181,232,0.2); border:1px solid rgba(41,181,232,0.5); border-radius:8px; padding:12px; text-align:center"><div style="font-size:22px">🔬</div><div style="font-size:12px; color:white"><strong>Clean Room</strong><br>AML RightSource runs matching logic here</div></div>
    <div style="background:rgba(255,255,255,0.08); border-radius:8px; padding:12px; text-align:center"><div style="font-size:22px">🏦</div><div style="font-size:12px; color:rgba(255,255,255,0.7)">Bank B shares data<br>(never visible to Bank A)</div></div>
    </div>
    <p style="color:rgba(255,255,255,0.6); font-size:12px; margin-top:12px; text-align:center">Only the match result is shared — "these 5 accounts appear in both institutions' high-risk alert queues"</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Clean Room Use Case Simulator")
        cr_use_case = st.selectbox("Select Analysis Type", [
            "Money Mule Network Detection",
            "Shared Structuring Actors",
            "Cross-Institution Fraud Ring",
            "OFAC Match Confirmation",
            "Beneficial Ownership Overlap"
        ])

        bank_a = st.selectbox("Institution A", ["First National Bank", "Heritage Financial", "Community Trust"])
        bank_b = st.selectbox("Institution B", ["Valley Business Bank", "Pacific Coast Bank", "Regional S&L"])

        if st.button("🔬 Run Clean Room Analysis", type="primary"):
            with st.spinner("Executing secure multi-party computation..."):
                time.sleep(1.5)

            matches = random.randint(3, 12)
            st.success(f"✅ Clean Room analysis complete — **{matches} matches found** between {bank_a} and {bank_b}")

            match_df = pd.DataFrame({
                "Match ID": [f"MULE-{random.randint(1000,9999)}" for _ in range(matches)],
                "Risk Category": random.choices(["💰 Money Mule", "🔄 Structurer", "🌐 Wire Fraud", "👤 ID Theft"], k=matches),
                "Confidence": [f"{random.randint(78, 99)}%" for _ in range(matches)],
                "Bank A Activity": [f"{random.randint(2,8)} alerts" for _ in range(matches)],
                "Bank B Activity": [f"{random.randint(1,6)} alerts" for _ in range(matches)],
            })
            st.dataframe(match_df, use_container_width=True, hide_index=True)

            st.markdown(f"""
            <div class="ai-bubble">
            <strong>Cortex AI Clean Room Summary:</strong><br>
            {matches} shared risk actors identified between {bank_a} and {bank_b} with high confidence. The most significant match cluster (confidence: 96%) appears to represent a coordinated structuring operation operating simultaneously across both institutions. Neither bank's raw customer data was shared — both institutions should independently review their respective matches and consider joint SAR filing under FinCEN's guidance on coordinated reporting.
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Clean Room Impact")

        impacts = [
            ("🎯", "Cross-Bank Mule Networks Discovered", "127", "This year"),
            ("⚡", "Joint SAR Filings Enabled", "43", "Cross-institution"),
            ("💡", "New Detection Rules Triggered", "18", "Shared intelligence"),
            ("🔐", "Zero Data Exposure Events", "0", "Fully protected"),
        ]

        for icon, label, val, sub in impacts:
            st.markdown(f"""
            <div style="background:white; border:1px solid #D1E8F5; border-radius:10px; padding:14px; display:flex; gap:14px; align-items:center; margin-bottom:8px">
            <div style="font-size:24px">{icon}</div>
            <div style="flex:1"><div style="font-size:11px; color:#718096; text-transform:uppercase; letter-spacing:1px">{label}</div><div style="font-size:22px; font-weight:800; color:#0D2B4E">{val}</div><div style="font-size:11px; color:#29B5E8">{sub}</div></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:14px; margin-top:8px; font-size:13px; color:#065F46">
        <strong>🏆 Regulatory Recognition:</strong> FinCEN has explicitly encouraged financial institutions to use privacy-preserving technologies for collaborative AML intelligence sharing. Snowflake Data Clean Rooms are specifically cited as a compliant approach in multiple federal guidance documents.
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 5 — NATIVE APP MARKETPLACE
# ─────────────────────────────────────────────────────────────────────────────
with tab5:
    st.markdown("### 📱 AML RightSource Native App Marketplace")
    st.markdown("**Your algorithms. Your IP. Delivered to 200+ bank clients in one click.**")

    st.markdown("""
    <div style="background:linear-gradient(135deg,#0D2B4E,#29B5E8); color:white; border-radius:14px; padding:24px; margin-bottom:24px">
    <h4 style="color:white; margin-top:0">🎯 The Native App Model</h4>
    <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:12px; text-align:center">
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:14px"><div style="font-size:20px">👩‍💻</div><div style="font-size:12px; margin-top:6px; color:rgba(255,255,255,0.8)">Isabel's team builds algorithm in Snowpark Python</div></div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:14px"><div style="font-size:20px">📦</div><div style="font-size:12px; margin-top:6px; color:rgba(255,255,255,0.8)">Package as Native App with IP protection</div></div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:14px"><div style="font-size:20px">🛒</div><div style="font-size:12px; margin-top:6px; color:rgba(255,255,255,0.8)">List on Snowflake Marketplace (10,000+ FSI customers)</div></div>
    <div style="background:rgba(255,255,255,0.1); border-radius:8px; padding:14px"><div style="font-size:20px">💰</div><div style="font-size:12px; margin-top:6px; color:rgba(255,255,255,0.8)">Bank installs → AML RS earns subscription fee</div></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("#### AML RightSource App Catalog")

        apps = [
            {
                "name": "AlertIQ — Priority Scoring Engine",
                "version": "v2.4",
                "desc": "ML-powered alert prioritization that reduces false positive rates by 60%+. Runs directly in client's Snowflake account.",
                "installs": 34,
                "rating": 4.8,
                "price": "$2,500/mo",
                "status": "active",
            },
            {
                "name": "KYC Refresh Accelerator",
                "version": "v1.1",
                "desc": "Automated customer due diligence refresh with Experian and public records enrichment via Marketplace.",
                "installs": 21,
                "rating": 4.6,
                "price": "$1,800/mo",
                "status": "active",
            },
            {
                "name": "SAR Quality Scorer",
                "version": "v3.0",
                "desc": "Cortex AI-powered SAR narrative quality analysis. Scores completeness, accuracy, and regulatory compliance before filing.",
                "installs": 18,
                "rating": 4.9,
                "price": "$1,200/mo",
                "status": "active",
            },
            {
                "name": "Network Risk Graph Analyzer",
                "version": "v1.0 BETA",
                "desc": "Graph analytics for beneficial ownership and transaction network risk — identifies complex multi-hop money laundering patterns.",
                "installs": 7,
                "rating": 4.7,
                "price": "$3,500/mo",
                "status": "new",
            },
        ]

        for app in apps:
            status_badge = '<span style="background:#DBEFFE;color:#1E6FA8;padding:2px 8px;border-radius:8px;font-size:10px;font-weight:700">NEW</span>' if app['status'] == 'new' else '<span style="background:#D1FAE5;color:#065F46;padding:2px 8px;border-radius:8px;font-size:10px;font-weight:700">ACTIVE</span>'
            stars = "⭐" * round(app['rating']) + f" {app['rating']}"
            with st.expander(f"**{app['name']}** {app['version']} — {app['price']}"):
                c_a, c_b = st.columns([2, 1])
                with c_a:
                    st.markdown(f"""
                    <div style="font-size:13px; color:#4A5568; margin-bottom:10px">{app['desc']}</div>
                    <div style="font-size:12px">{stars} &nbsp;|&nbsp; {app['installs']} installs &nbsp;|&nbsp; {status_badge}</div>
                    """, unsafe_allow_html=True)
                with c_b:
                    if st.button(f"⬇️ Install", key=f"install_{app['name']}"):
                        with st.spinner("Installing Native App..."):
                            time.sleep(1)
                        st.success(f"✅ {app['name']} installed! Algorithm is now running on your data.")

    with col2:
        st.markdown("#### Revenue Dashboard")

        rev_months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
        rev_data = [28000, 34000, 41000, 52000, 68000, 89000, 142000]
        rev_df = pd.DataFrame({"Month": rev_months, "MRR ($)": rev_data}).set_index("Month")
        st.line_chart(rev_df, height=180, color="#00C96F")
        st.caption("Native App MRR growing 400%+ YoY as new apps launch")

        st.markdown("""
        <div style="background:#E6FBF3; border:1px solid #BBF7D0; border-radius:10px; padding:14px">
        <div style="font-size:11px; text-transform:uppercase; letter-spacing:1px; color:#065F46; margin-bottom:8px">Revenue Model Comparison</div>
        <div style="font-size:13px; margin-bottom:6px">🔴 <strong>Old model:</strong> One-time project fee ($50K–$150K per algorithm deployment) — 3–6 months to deliver</div>
        <div style="font-size:13px">🟢 <strong>New model:</strong> $2,500/mo subscription × 34 installs = <strong>$85K MRR</strong> — recurring, scalable, margin-rich</div>
        <div style="font-size:12px; color:#065F46; margin-top:8px; font-weight:600">Lifetime value improvement: 12× per algorithm</div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 6 — PREDICTIVE ANALYTICS
# ─────────────────────────────────────────────────────────────────────────────
with tab6:
    st.markdown("### 🔮 Predictive Analytics & ML Models")
    st.markdown("**Snowpark ML + Cortex:** Train, deploy, and serve ML models without leaving Snowflake.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Live Model Performance Dashboard")

        np.random.seed(42)
        dates = pd.date_range(start='2025-11-01', periods=180, freq='D')
        model_df = pd.DataFrame({
            "Date": dates,
            "AlertIQ Accuracy": np.clip(0.78 + np.cumsum(np.random.normal(0.001, 0.003, 180)), 0.78, 0.96),
            "SAR Predictor Accuracy": np.clip(0.82 + np.cumsum(np.random.normal(0.0015, 0.002, 180)), 0.82, 0.97),
        }).set_index("Date")

        st.line_chart(model_df, height=180)
        st.caption("Model accuracy continuously improves as more data is processed")

        st.markdown("#### ML Model Registry")
        model_reg = pd.DataFrame({
            "Model": ["AlertIQ v2.4", "SAR Predictor v1.2", "KYC Refresh ML v1.1", "Network Risk Graph v1.0"],
            "Algorithm": ["XGBoost + SHAP", "BERT Fine-tuned", "Random Forest", "GraphNN"],
            "Accuracy": ["94.2%", "96.7%", "91.3%", "88.9%"],
            "Version": ["Production", "Production", "Staging", "Beta"],
            "Records/Day": ["4.2M", "12K", "890K", "2.1M"],
        })
        st.dataframe(model_reg, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("#### Predict: Transaction Risk Score")
        st.markdown("*Enter transaction parameters to get an instant AI risk score*")

        txn_amount = st.slider("Transaction Amount ($)", 1000, 500000, 45000, step=1000)
        txn_type = st.selectbox("Transaction Type", ["ACH", "Wire Transfer", "Cash Deposit", "Check", "ATM Withdrawal"])
        customer_tenure = st.slider("Customer Account Age (months)", 1, 120, 24)
        prior_alerts = st.slider("Prior SAR/Alert History (count)", 0, 20, 0)
        cross_border = st.checkbox("Cross-Border Transaction")

        if st.button("🤖 Score This Transaction", type="primary"):
            base_score = min(95, max(5,
                (txn_amount / 500000 * 40) +
                ({"Cash Deposit": 25, "Wire Transfer": 20, "ACH": 5, "Check": 3, "ATM Withdrawal": 10}.get(txn_type, 10)) +
                (max(0, 20 - customer_tenure * 0.3)) +
                (prior_alerts * 4) +
                (20 if cross_border else 0)
            ))

            color = "#E63946" if base_score > 70 else "#FF7A00" if base_score > 40 else "#00C96F"
            level = "HIGH RISK" if base_score > 70 else "MEDIUM RISK" if base_score > 40 else "LOW RISK"

            st.markdown(f"""
            <div style="background:white; border:2px solid {color}; border-radius:14px; padding:24px; text-align:center; margin:12px 0">
            <div style="font-size:48px; font-weight:900; color:{color}">{base_score:.0f}</div>
            <div style="font-size:16px; font-weight:700; color:{color}">{level}</div>
            <div style="font-size:12px; color:#718096; margin-top:8px">AI Risk Score / 100 — Powered by AlertIQ v2.4</div>
            </div>
            """, unsafe_allow_html=True)

            contrib = {
                "Transaction Amount": txn_amount / 500000 * 40,
                "Transaction Type": {"Cash Deposit": 25, "Wire Transfer": 20, "ACH": 5, "Check": 3, "ATM Withdrawal": 10}.get(txn_type, 10),
                "Account Tenure": max(0, 20 - customer_tenure * 0.3),
                "Prior Alert History": prior_alerts * 4,
                "Cross-Border": 20 if cross_border else 0,
            }

            st.markdown("**Risk Factor Contributions (SHAP):**")
            contrib_df = pd.DataFrame(list(contrib.items()), columns=["Factor", "Contribution"]).set_index("Factor")
            st.bar_chart(contrib_df, color="#29B5E8", height=180)

            if base_score > 70:
                st.markdown("""
                <div class="ai-bubble">
                <strong>Recommended Action:</strong> Flag for immediate analyst review. Transaction characteristics (amount, type, cross-border) exceed threshold for standard auto-clear. 
                Estimated analyst review time: <strong>4 minutes</strong> with Cortex AI pre-analysis.
                </div>
                """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div style="background:#0D2B4E; color:rgba(255,255,255,0.5); text-align:center; padding:20px; border-radius:12px; font-size:12px">
    🎯 AML RightSource × Snowflake Interactive Demo Environment<br>
    <span style="font-size:10px">All data shown is synthetic and for demonstration purposes only. Prepared by the Snowflake Enterprise Acquisition Team.</span><br>
    Kala Boudreaux · Eric Szenderski · Jordan Ude
</div>
""", unsafe_allow_html=True)
