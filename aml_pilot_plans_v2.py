import streamlit as st
from datetime import datetime

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

.hero {
    background: linear-gradient(135deg, #0D2B4E 0%, #11375C 60%, #1A4A7A 100%);
    border-radius: 16px; padding: 48px; margin-bottom: 32px; color: white;
}
.hero h1 { font-size: 36px; font-weight: 900; margin: 0 0 10px; }
.hero p { color: rgba(255,255,255,0.7); font-size: 15px; margin: 0; max-width: 650px; }

.pilot-header {
    background: white; border: 1px solid #D1E8F5; border-top: 4px solid;
    border-radius: 12px; padding: 24px 28px; margin-bottom: 24px;
}
.pilot-header h2 { font-size: 22px; font-weight: 800; color: #0D2B4E; margin: 0 0 6px; }
.pilot-header p { font-size: 14px; color: #4A5568; margin: 0; }

.sec-title {
    font-size: 17px; font-weight: 800; color: #0D2B4E;
    border-bottom: 2px solid #29B5E8; padding-bottom: 8px; margin: 32px 0 16px;
}

.card { background: white; border: 1px solid #D1E8F5; border-radius: 12px;
    padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 14px; }

.callout-blue { background: #E8F7FD; border-left: 4px solid #29B5E8;
    border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; font-size: 14px; }
.callout-green { background: #E6FBF3; border-left: 4px solid #00C96F;
    border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; font-size: 14px; }
.callout-orange { background: #FFF8E6; border-left: 4px solid #FF7A00;
    border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; font-size: 14px; }

.kpi { background: linear-gradient(135deg, #0D2B4E, #11375C); color: white;
    border-radius: 12px; padding: 20px; text-align: center; }
.kpi-num { font-size: 28px; font-weight: 900; color: #29B5E8; }
.kpi-label { font-size: 11px; color: rgba(255,255,255,0.7); margin-top: 4px;
    text-transform: uppercase; letter-spacing: 1px; }

.phase-step {
    display: flex; gap: 16px; padding: 16px; background: white;
    border: 1px solid #D1E8F5; border-radius: 10px; margin-bottom: 10px;
}
.phase-num { width: 36px; height: 36px; background: #29B5E8; color: white;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 14px; flex-shrink: 0; }

.live-section {
    background: #FFFBEB; border: 2px solid #F59E0B; border-radius: 12px;
    padding: 24px; margin: 20px 0;
}
.live-badge { display: inline-block; background: #F59E0B; color: white;
    padding: 3px 12px; border-radius: 10px; font-size: 10px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }

.footer { background: #0D2B4E; color: rgba(255,255,255,0.5); text-align: center;
    padding: 20px; border-radius: 12px; margin-top: 40px; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div style="display:inline-block;background:rgba(41,181,232,0.2);border:1px solid rgba(41,181,232,0.4);
    color:#29B5E8;padding:4px 14px;border-radius:20px;font-size:11px;font-weight:700;
    letter-spacing:2px;text-transform:uppercase;margin-bottom:16px">🚀 Pilot Program</div>
    <h1>AML RightSource × Snowflake</h1>
    <p>Three focused pilots to validate Snowflake's impact on advisory speed, data intelligence, and algorithm scale. Each pilot is designed to deliver measurable results in 60 days.</p>
</div>
""", unsafe_allow_html=True)

# ── PILOT TABS ────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "🔍 Pilot 1 — Advisory",
    "📊 Pilot 2 — Data Assets",
    "⚙️ Pilot 3 — Algorithms",
])

# ══════════════════════════════════════════════════════════════════════════════
# PILOT 1 — ADVISORY
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="pilot-header" style="border-top-color:#29B5E8">
    <h2>🔍 Pilot 1 — Advisory Intelligence</h2>
    <p>Validate that Snowflake eliminates advisory engagement data onboarding friction — reducing time-to-data from weeks to hours.</p>
    </div>
    """, unsafe_allow_html=True)

    # Overview
    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip([c1,c2,c3,c4], [
        ("60 Days","Pilot Duration"),("Sabrina Chen","Pilot Owner"),("2–3 Wks → Hrs","Target Improvement"),("85%","Time Reduction Goal"),
    ]):
        with col:
            st.markdown(f'<div class="kpi"><div class="kpi-num">{num}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

    # What We're Solving
    st.markdown('<div class="sec-title">What We\'re Solving</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-orange">
    <strong>Today:</strong> Every advisory engagement starts with a 2–3 week data request cycle — secure FTP, email, normalization — before any analysis begins. Analysts spend 40–60% of their time on data prep instead of advisory work.
    </div>
    <div class="callout-green">
    <strong>With Snowflake:</strong> Bank clients grant a secure, read-only data share. AML RightSource analysts query client data in-place — no data movement, no ETL. Analysis starts the same day.
    </div>
    """, unsafe_allow_html=True)

    # Success Criteria
    st.markdown('<div class="sec-title">How We Measure Success</div>', unsafe_allow_html=True)
    st.markdown("""
| Metric | Current State | Target | How We Measure |
|---|---|---|---|
| Time to first data access | 10–20 days | < 48 hours | Compare pilot share setup vs. last 5 engagements |
| Analyst time on data prep | 40–60% of engagement | < 10% | Time-tracked by Sabrina/David during pilot |
| Data security clearance | 2–3 weeks per client | Upfront platform approval | Snowflake security package review |
| Analyst satisfaction | Baseline TBD | 8/10 or higher | 5-question survey at pilot close |
""")

    # Pilot Plan
    st.markdown('<div class="sec-title">Pilot Plan — 60 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Weeks 1–2: Setup","Snowflake provisions trial account with synthetic AML dataset. Analysts get access and onboarding walkthrough."),
        ("2","Weeks 2–3: Training","Hands-on session on data sharing, Snowsight, and Cortex AI. Sabrina + David run first queries against synthetic data."),
        ("3","Weeks 3–6: Execute","Run 2 simulated advisory engagements using Snowflake data shares. Track time-to-data and analyst productivity vs. current process."),
        ("4","Weeks 7–8: Readout","Compile results vs. success criteria. Present to Abhishek and full leadership team. Recommend path forward."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
        <div class="phase-step">
        <div class="phase-num">{num}</div>
        <div><strong style="color:#0D2B4E">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
        </div>""", unsafe_allow_html=True)

    # What's Needed
    st.markdown('<div class="sec-title">What\'s Needed to Start</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **From Snowflake:**
        - ❄️ Snowflake Business Critical trial account
        - 📊 Synthetic AML dataset (realistic TM + KYC data)
        - 👤 Jordan Ude — SE support & bi-weekly office hours
        """)
    with c2:
        st.markdown("""
        **From AML RightSource:**
        - 👤 Sabrina Chen + David Lutz (4–5 hrs/week)
        - 📋 Baseline metrics: last 5 advisory engagement timelines
        - ✅ Executive sign-off from Abhishek on pilot scope
        """)

    # Live Readout Section
    st.markdown('<div class="sec-title">Pilot Readout & Next Steps</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete at Readout</div>', unsafe_allow_html=True)
    st.text_area("Results Summary", placeholder="Document pilot results here during the readout meeting...", height=100, key="p1_results")
    st.text_area("Did we meet success criteria? (Yes / No / Partial — explain)", placeholder="E.g., 'Yes — time-to-data reduced from 14 days to 3 hours in both simulated engagements...'", height=80, key="p1_criteria")
    st.text_area("Recommended Next Steps", placeholder="E.g., 'Move to production deployment for all FCA advisory engagements...'", height=80, key="p1_next")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions (Pilot 1)", placeholder="Add any questions, comments, or notes here...", height=100, key="p1_notes")

# ══════════════════════════════════════════════════════════════════════════════
# PILOT 2 — DATA ASSETS
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="pilot-header" style="border-top-color:#00C96F">
    <h2>📊 Pilot 2 — Data Assets & Benchmarking</h2>
    <p>Validate that AML RightSource's internal operational data, unified on Snowflake, can power an industry-first cross-client benchmarking intelligence product.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip([c1,c2,c3,c4], [
        ("60 Days","Pilot Duration"),("Jonathan McIsaac","Pilot Owner"),("$0 → Revenue","New Product Goal"),("200+ FIs","Data Asset Scale"),
    ]):
        with col:
            st.markdown(f'<div class="kpi"><div class="kpi-num">{num}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sec-title">What We\'re Solving</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-orange">
    <strong>Today:</strong> AML RightSource has 10+ years of operational data across 200+ bank clients — case resolution rates, false positive rates, analyst productivity — sitting in silos with no unified analytics layer. This data generates $0 in product revenue.
    </div>
    <div class="callout-green">
    <strong>With Snowflake:</strong> Unify the data. Build anonymized cross-client benchmarks. Publish to Snowflake Marketplace as a subscription product — accessible to 10,000+ financial institutions. First-of-its-kind in the industry.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">How We Measure Success</div>', unsafe_allow_html=True)
    st.markdown("""
| Metric | Current State | Target | How We Measure |
|---|---|---|---|
| Data migration completeness | 0% on unified platform | Pilot dataset migrated and queryable | Row counts, data integrity checks |
| Benchmark query performance | No real-time benchmarking exists | Produce benchmark report in < 5 minutes | Time the SQL execution |
| Anonymization compliance | No framework in place | Legal/compliance sign-off on anonymized output | Sample review by AML RS legal |
| Client interest validation | $0 revenue | 3–5 bank clients express interest in subscribing | Share sample report + gather feedback |
""")

    st.markdown('<div class="sec-title">Pilot Plan — 60 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Weeks 1–2: Discovery","Jonathan identifies pilot dataset (2 years of case management data from 1 BU). Audit data sources and volumes."),
        ("2","Weeks 2–4: Migration","AML RS data engineer + Snowflake SE build pipeline. Load pilot data to Snowflake. Validate integrity. Build star schema for benchmarking."),
        ("3","Weeks 4–6: Build","Build 3–5 benchmark queries (FP rate by tier, case resolution by region, analyst productivity). Create Snowsight dashboard. Legal reviews anonymization approach."),
        ("4","Weeks 6–8: Validate & Readout","Share sample benchmark report with 3–5 advisory clients. Gather feedback. Compile results. Present to leadership."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
        <div class="phase-step">
        <div class="phase-num">{num}</div>
        <div><strong style="color:#0D2B4E">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-title">What\'s Needed to Start</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **From Snowflake:**
        - ❄️ Snowflake account with Marketplace capabilities
        - 👤 Jordan Ude — data architecture & migration support
        - 📋 Marketplace listing guidance and timeline
        """)
    with c2:
        st.markdown("""
        **From AML RightSource:**
        - 👤 Jonathan McIsaac (project sponsor, 0.25 FTE)
        - 👩‍💻 1 data engineer (0.5 FTE for pilot duration)
        - ⚖️ Legal review of anonymization approach (Week 3)
        - 📊 Extract of internal case management data (2+ years)
        """)

    st.markdown('<div class="sec-title">Pilot Readout & Next Steps</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete at Readout</div>', unsafe_allow_html=True)
    st.text_area("Results Summary", placeholder="Document pilot results here...", height=100, key="p2_results")
    st.text_area("Did we meet success criteria?", placeholder="E.g., 'Partial — data migration successful, benchmark queries run in 12 seconds, legal approved anonymization. Client validation in progress...'", height=80, key="p2_criteria")
    st.text_area("Recommended Next Steps", placeholder="E.g., 'Proceed with full data migration and Marketplace listing development...'", height=80, key="p2_next")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions (Pilot 2)", placeholder="Add any questions, comments, or notes here...", height=100, key="p2_notes")

# ══════════════════════════════════════════════════════════════════════════════
# PILOT 3 — ALGORITHMS
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="pilot-header" style="border-top-color:#FF7A00">
    <h2>⚙️ Pilot 3 — Algorithm Deployment</h2>
    <p>Validate that Snowflake's Native App Framework enables AML RightSource to package, protect, and deploy scoring algorithms into client environments — at scale.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip([c1,c2,c3,c4], [
        ("60 Days","Pilot Duration"),("Isabel Yeung","Pilot Owner"),("6 Mo → Days","Deployment Speed"),("Full IP","Protection Guarantee"),
    ]):
        with col:
            st.markdown(f'<div class="kpi"><div class="kpi-num">{num}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sec-title">What We\'re Solving</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="callout-orange">
    <strong>Today:</strong> Deploying a scoring algorithm into a client environment takes 3–6 months of custom engineering. Revenue is one-time project fees. IP is exposed. The model doesn't scale to 200+ clients.
    </div>
    <div class="callout-green">
    <strong>With Snowflake:</strong> Package algorithms as Native Apps. Banks install in minutes from Snowflake Marketplace. IP is fully protected. AML RightSource earns recurring subscription revenue per install. One build → unlimited deployments.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">How We Measure Success</div>', unsafe_allow_html=True)
    st.markdown("""
| Metric | Current State | Target | How We Measure |
|---|---|---|---|
| Native App build | Algorithm in isolated Python environment | Successfully packaged as Snowflake Native App | Installs without error in test environment |
| IP protection | Code exposed in every client deployment | Client cannot see or extract algorithm logic | Attempt to view source code from client account |
| Output accuracy | Baseline accuracy (Isabel to confirm) | Native App output matches standalone to > 99% | Run both versions on same test data |
| Deployment time | 3–6 months per client | < 30 minutes per install | Time end-to-end installation on second test environment |
""")

    st.markdown('<div class="sec-title">Pilot Plan — 60 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Weeks 1–2: Discovery","Isabel selects 1 algorithm for pilot (recommendation: AlertIQ priority scorer). Document input/output schema. Jordan provisions Snowflake dev environment + synthetic test data."),
        ("2","Weeks 2–5: Build","Isabel's engineer + Jordan co-build Snowpark Python wrapper. Package as Native App. Test IP protection. Validate accuracy against standalone model."),
        ("3","Weeks 5–7: Client Simulation","Provision second Snowflake account simulating a bank client. Install Native App. Time the process. Run algorithm on synthetic bank data. Capture results."),
        ("4","Weeks 7–8: Readout","Review Marketplace listing requirements. Compile results vs. success criteria. Present to Abhishek and Isabel. Recommend next steps."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
        <div class="phase-step">
        <div class="phase-num">{num}</div>
        <div><strong style="color:#0D2B4E">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-title">What\'s Needed to Start</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **From Snowflake:**
        - ❄️ Snowflake Developer Account with Native App Framework
        - 📊 Synthetic bank data matching algorithm input schema
        - 🧪 Second test environment (simulates client install)
        - 👤 Jordan Ude — Native App build guidance
        """)
    with c2:
        st.markdown("""
        **From AML RightSource:**
        - 👤 Isabel Yeung (pilot sponsor)
        - 👩‍💻 1 engineer (1.0 FTE for build phase, Weeks 2–5)
        - 🐍 Python algorithm source code (1 algorithm ready for Snowpark port)
        - 📋 Algorithm input/output schema documentation
        """)

    st.markdown('<div class="sec-title">Pilot Readout & Next Steps</div>', unsafe_allow_html=True)
    st.markdown('<div class="live-section"><div class="live-badge">🔴 Live — Complete at Readout</div>', unsafe_allow_html=True)
    st.text_area("Results Summary", placeholder="Document pilot results here...", height=100, key="p3_results")
    st.text_area("Did we meet success criteria?", placeholder="E.g., 'Yes — Native App built, IP protected, accuracy 99.7%, install time 4 minutes...'", height=80, key="p3_criteria")
    st.text_area("Recommended Next Steps", placeholder="E.g., 'Begin Marketplace listing process. Identify next 3 algorithms for Native App conversion...'", height=80, key="p3_next")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions (Pilot 3)", placeholder="Add any questions, comments, or notes here...", height=100, key="p3_notes")

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    🚀 AML RightSource × Snowflake — Pilot Plans v2<br>
    Prepared by: Kala Boudreaux · Eric Szenderski · Jordan Ude — Snowflake Enterprise Acquisition<br>
    <span style="font-size:10px">All fields are editable. Add notes and questions during your planning sessions with the Snowflake team.</span>
</div>
""", unsafe_allow_html=True)
