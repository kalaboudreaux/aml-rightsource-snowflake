import streamlit as st

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

.owner-row {
    display: flex; gap: 24px; padding: 14px 0; border-bottom: 1px solid #E2E8F0;
}
.owner-label { width: 160px; font-size: 12px; font-weight: 700; color: #29B5E8;
    text-transform: uppercase; letter-spacing: 1px; flex-shrink: 0; padding-top: 2px; }
.owner-value { font-size: 14px; font-weight: 600; color: #0D2B4E; }
.owner-sub { font-size: 12px; color: #718096; margin-top: 2px; }

.phase-step {
    display: flex; gap: 16px; padding: 16px; background: white;
    border: 1px solid #D1E8F5; border-radius: 10px; margin-bottom: 10px;
}
.phase-num { width: 36px; height: 36px; background: #29B5E8; color: white;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 14px; flex-shrink: 0; }

.prereq-item {
    display: flex; gap: 12px; padding: 12px 14px; background: #F7FAFC;
    border: 1px solid #E2E8F0; border-radius: 8px; margin-bottom: 8px; align-items: flex-start;
}

.sc-row {
    background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 10px;
    padding: 14px; margin-bottom: 10px;
}

.footer { background: #0D2B4E; color: rgba(255,255,255,0.5); text-align: center;
    padding: 20px; border-radius: 12px; margin-top: 40px; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div style="display:inline-block;background:rgba(41,181,232,0.2);border:1px solid rgba(41,181,232,0.4);
    color:#29B5E8;padding:4px 14px;border-radius:20px;font-size:11px;font-weight:700;
    letter-spacing:2px;text-transform:uppercase;margin-bottom:16px">🚀 30-Day Pilot Program</div>
    <h1>AML RightSource × Snowflake</h1>
    <p>Three focused 30-day pilots — one per use case — designed to deliver measurable proof of value with minimal resource commitment. Each pilot has a clear owner, defined success criteria, and a structured execution plan.</p>
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
    <p>Eliminate advisory engagement data onboarding friction — reducing time-to-data from weeks to hours using Snowflake's zero-copy data sharing.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── OWNERSHIP ─────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Ownership</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="owner-row"><div class="owner-label">Primary Pilot Owner</div><div><div class="owner-value">Sabrina Chen</div><div class="owner-sub">Head of Analytics Practice, Financial Crimes Advisory</div></div></div>
<div class="owner-row"><div class="owner-label">Supporting Owner</div><div><div class="owner-value">David Lutz</div><div class="owner-sub">Associate Director, Financial Crimes Advisory</div></div></div>
<div class="owner-row" style="border-bottom:none"><div class="owner-label">Executive Sponsor</div><div><div class="owner-value">Abhishek Mittal</div><div class="owner-sub">EVP & Chief Product and AI Officer</div></div></div>
""", unsafe_allow_html=True)

    # ── EXEC SUMMARY / POV STATEMENT ─────────────────────────────────────────
    st.markdown('<div class="sec-title">Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>Point of View:</strong> AML RightSource's advisory practice is constrained by a manual, multi-week data onboarding process that prevents analysts from delivering value quickly. We believe Snowflake's zero-copy data sharing model can reduce advisory engagement time-to-data from <strong>10–20 days to under 48 hours</strong>, increase analyst productivity by <strong>50–100%</strong>, and eliminate the security and compliance friction associated with FTP/email-based data transfer — validated through a <strong>30-day pilot</strong> with synthetic client data.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
This pilot validates the foundational infrastructure for AML RightSource's entire advisory transformation. If successful, it proves that Snowflake can serve as the collaboration backbone between AML RightSource and its 200+ bank clients — enabling faster engagements, higher margins, and a differentiated client experience.
""")

    # ── CURRENT BUSINESS PROBLEM ──────────────────────────────────────────────
    st.markdown('<div class="sec-title">Current Business Problem</div>', unsafe_allow_html=True)
    st.markdown("""
Every advisory engagement — model validation, algorithm tuning, AML program assessments — begins with a **data request cycle** that typically takes **10–20 business days:**

1. AML RightSource requests data from client bank's IT/security team
2. Client exports, encrypts, and transfers data via secure FTP, email, or SharePoint
3. AML RightSource normalizes, cleanses, and loads data into an analysis environment
4. **Only then does advisory analysis begin — 2–3 weeks after the engagement was signed**

**The impact:** Analysts spend **40–60% of total engagement time** on data preparation rather than advisory analysis. AML RightSource cannot scale advisory revenue without proportional headcount growth. Client satisfaction suffers from slow start times. Security risk exists with every manual file transfer.
""")

    # ── BUSINESS OBJECTIVE ────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Business Objective</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-green">
<strong>Objective:</strong> Prove that Snowflake's data sharing architecture can reduce advisory engagement time-to-first-data-access from <strong>10–20 days to under 48 hours</strong>, enabling AML RightSource to serve <strong>2× more advisory clients with the same analyst headcount</strong> while improving client satisfaction and eliminating manual data transfer security risks.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
**Specific outcomes this pilot must demonstrate:**
- Advisory analysts can access client data within hours of engagement start (not weeks)
- Data preparation time drops from 40–60% of engagement to less than 10%
- No client data is physically moved or copied — zero security exposure
- The experience is simple enough for any AML RightSource analyst to use without specialized training
""")

    # ── DISCOVERY & CURRENT STATE ─────────────────────────────────────────────
    st.markdown('<div class="sec-title">Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
**Current Data Transfer Method:**
- Secure FTP (primary)
- Encrypted email attachments
- SharePoint document upload
- Per-engagement, manual request-and-delivery cycle
- Each bank delivers data in different formats requiring custom normalization

**Average Time to First Data Access:**
- 10–20 business days (confirmed by Sabrina Chen and David Lutz in April 29 meeting)
""")
    with c2:
        st.markdown("""
**Analyst Time Allocation (per engagement):**
- 40–60% on data preparation and normalization
- 20–30% on actual advisory analysis
- 10–20% on report writing and delivery

**Client Friction Points:**
- Banks are reluctant to share sensitive data via email/FTP
- Each client IT team has different security requirements
- Data format inconsistency adds days per engagement
- Re-requesting data for follow-up analysis restarts the cycle
""")

    st.markdown("""
<div class="callout-orange">
<strong>Pain Level: 8/10</strong> — Data onboarding is the single largest bottleneck to advisory delivery. Multiple stakeholders (Sabrina, David, Abhishek) independently confirmed this as their top priority in the April 29 meeting.
</div>
""", unsafe_allow_html=True)

    # ── POINT OF VIEW ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Point of View — Snowflake\'s Prediction</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>We believe</strong> Snowflake can overcome the <em>manual, insecure, slow data onboarding process for advisory engagements</em><br><br>
<strong>While supporting</strong> AML RightSource's objective of <em>serving 2× more clients with the same headcount and compressing time-to-value</em><br><br>
<strong>By implementing</strong> <em>zero-copy Snowflake Data Sharing between AML RightSource's Snowflake account and participating bank client environments — validated by a 30-day pilot using a synthetic AML dataset that mirrors real advisory engagement data structures.</em>
</div>
""", unsafe_allow_html=True)

    # ── SUCCESS CRITERIA ──────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Success Criteria & Test Cases</div>', unsafe_allow_html=True)

    criteria = [
        ("SC-1: Time-to-First-Data-Access", "10–20 days", "< 48 hours", "Compare pilot data share setup time vs. average of last 5 advisory engagements"),
        ("SC-2: Analyst Data Prep Time", "40–60% of engagement", "< 10% of engagement", "Time-tracked by Sabrina and David during 2 simulated advisory engagements"),
        ("SC-3: Security & Compliance", "2–3 weeks security review per client", "Platform-level approval (no per-engagement review)", "Snowflake Business Critical security package submitted and reviewed by AML RS infosec"),
        ("SC-4: Analyst Satisfaction", "Current NPS baseline TBD", "8/10 or higher", "5-question satisfaction survey at pilot close"),
    ]
    for name, baseline, target, method in criteria:
        st.markdown(f"""
<div class="sc-row">
<div style="font-size:14px;font-weight:700;color:#065F46;margin-bottom:6px">✅ {name}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13px">
<div><strong>Baseline:</strong> {baseline}</div>
<div><strong>Target:</strong> {target}</div>
<div><strong>Measurement:</strong> {method}</div>
</div>
</div>""", unsafe_allow_html=True)

    # ── PREREQUISITES ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**From Snowflake:**")
        prereqs_sf = [
            ("❄️","Snowflake Business Critical trial account","Jordan Ude","Day 1"),
            ("📊","Synthetic AML dataset (realistic TM + KYC data)","Jordan Ude","Day 1–3"),
            ("👤","SE support & weekly office hours","Jordan Ude","Ongoing"),
        ]
        for icon, item, owner, when in prereqs_sf:
            st.markdown(f"""<div class="prereq-item">
<span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div>
</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("**From AML RightSource:**")
        prereqs_aml = [
            ("👤","Sabrina Chen + David Lutz (4–5 hrs/week)","Sabrina Chen","Week 1"),
            ("📋","Baseline metrics: last 5 engagement timelines","David Lutz","Week 1"),
            ("✅","Executive sign-off on pilot scope","Abhishek Mittal","Pre-pilot"),
            ("🔐","Infosec review of Snowflake security package","IT/Security Team","Week 2"),
        ]
        for icon, item, owner, when in prereqs_aml:
            st.markdown(f"""<div class="prereq-item">
<span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div>
</div>""", unsafe_allow_html=True)

    # ── EXECUTION PLAN ────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Execution Plan — 30 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Days 1–5: Environment Setup","Snowflake provisions Business Critical trial account. Jordan loads synthetic AML dataset (TM alerts + KYC records). Sabrina, David, and Abhishek receive access credentials and onboarding materials. Kick-off call to walk through the environment and pilot objectives."),
        ("2","Days 5–10: Training & First Queries","Jordan leads a 90-minute hands-on session: how data sharing works, querying in Snowsight, and Cortex AI capabilities. Sabrina and David run their first advisory queries against the synthetic dataset. Document initial observations and feedback."),
        ("3","Days 10–25: Simulated Advisory Engagements","Run 2 simulated advisory engagements using Snowflake data shares against synthetic data. Track time-to-data and analyst prep time vs. current FTP/email process. Jordan provides weekly office hours for questions. Document all results, friction points, and improvements."),
        ("4","Days 25–30: Analysis & Readout","Compile results against all 4 success criteria. Produce before/after productivity analysis. Quantify business impact. Prepare formal readout. Present to Abhishek and full stakeholder team with recommendation for next steps."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
<div class="phase-step">
<div class="phase-num">{num}</div>
<div><strong style="color:#0D2B4E;font-size:14px">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions — Pilot 1", placeholder="Add any notes, questions, or comments here...", height=100, key="p1_notes")


# ══════════════════════════════════════════════════════════════════════════════
# PILOT 2 — DATA ASSETS
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="pilot-header" style="border-top-color:#00C96F">
    <h2>📊 Pilot 2 — Data Assets & Benchmarking</h2>
    <p>Validate that AML RightSource's internal operational data can power an industry-first cross-client benchmarking intelligence product on Snowflake.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── OWNERSHIP ─────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Ownership</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="owner-row"><div class="owner-label">Primary Pilot Owner</div><div><div class="owner-value">Jonathan McIsaac</div><div class="owner-sub">Global SVP, Head of Client Operations</div></div></div>
<div class="owner-row"><div class="owner-label">Supporting Owner</div><div><div class="owner-value">Abhishek Mittal</div><div class="owner-sub">EVP & Chief Product and AI Officer</div></div></div>
<div class="owner-row" style="border-bottom:none"><div class="owner-label">Executive Sponsor</div><div><div class="owner-value">Abhishek Mittal</div><div class="owner-sub">EVP & Chief Product and AI Officer</div></div></div>
""", unsafe_allow_html=True)

    # ── EXEC SUMMARY / POV STATEMENT ─────────────────────────────────────────
    st.markdown('<div class="sec-title">Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>Point of View:</strong> AML RightSource possesses the most comprehensive dataset of AML/BSA process performance data across 200+ financial institutions in the independent compliance space — currently sitting fragmented and unmonetized across siloed internal systems. We believe Snowflake's unified data platform can consolidate this asset and enable AML RightSource to build the industry's <strong>first real-time cross-client AML benchmarking intelligence product</strong> — creating a new recurring revenue stream while providing superior value to all advisory clients.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
This pilot validates the technical feasibility of migrating internal operational data to Snowflake, producing anonymized cross-client benchmarks, and gauging market appetite from existing bank clients for a subscription benchmarking product.
""")

    # ── CURRENT BUSINESS PROBLEM ──────────────────────────────────────────────
    st.markdown('<div class="sec-title">Current Business Problem</div>', unsafe_allow_html=True)
    st.markdown("""
Jonathan McIsaac's operations team manages **10+ years of AML/BSA process data** across 200+ financial institution clients — including case resolution rates, false positive rates, analyst productivity metrics, SAR filing volumes, and operational benchmarks.

**The problem:** This data sits in **disparate, siloed case management systems** with no unified analytics layer. AML RightSource cannot:
- Produce real-time cross-client benchmarking reports
- Offer clients comparative performance intelligence vs. peers
- Monetize a data asset that no competitor in the market possesses

**The business impact:** A proprietary data asset with estimated **$5–15M ARR potential** is currently generating **$0 in product revenue**. Competitors (Celent, NICE Actimize) already sell inferior benchmark products to the same bank clients. AML RightSource's unique advantage — aggregate visibility across 200+ FIs — remains unleveraged.
""")

    # ── BUSINESS OBJECTIVE ────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Business Objective</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-green">
<strong>Objective:</strong> Prove that AML RightSource's internal operational data can be migrated to Snowflake, anonymized appropriately, and used to generate cross-client benchmark insights — validating both the technical feasibility and market demand for a new data product revenue stream.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
**Specific outcomes this pilot must demonstrate:**
- A representative dataset (2 years, 1 BU) can be successfully migrated and queried on Snowflake
- Anonymized cross-client benchmarking queries produce meaningful, differentiated intelligence
- The anonymization approach passes AML RightSource legal/compliance review
- 3–5 existing advisory clients express interest in a benchmarking subscription product
""")

    # ── DISCOVERY & CURRENT STATE ─────────────────────────────────────────────
    st.markdown('<div class="sec-title">Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
**Internal Data Sources (to be confirmed by Jonathan):**
- Case management platform(s)
- Workflow and ticketing tools
- Reporting databases
- Client engagement records
- Analyst productivity tracking systems

**Estimated Data Volume:**
- 1M–5M cases historically across 200+ clients
- 10–20 years of operational history
- ~500GB–2TB total (estimated)
""")
    with c2:
        st.markdown("""
**Current Analytics Capability:**
- No real-time cross-client benchmarking exists
- Ad hoc reports require manual assembly by senior analysts
- Takes days to weeks to produce a single benchmark comparison
- No productized version — purely internal and reactive

**Data Privacy Constraints:**
- All benchmarking output must be anonymized
- No individual client institution identifiable in aggregate
- Snowflake Data Clean Rooms and aggregation controls will enforce this
- AML RS legal must review and approve before any external sharing
""")

    # ── POINT OF VIEW ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Point of View — Snowflake\'s Prediction</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>We believe</strong> Snowflake can overcome <em>AML RightSource's fragmented internal data infrastructure and zero benchmarking product capability</em><br><br>
<strong>While supporting</strong> the strategic objective of <em>creating a new recurring data product revenue stream from an existing but dormant data asset</em><br><br>
<strong>By implementing</strong> <em>a Snowflake unified data platform for internal operational data, with anonymization controls enabling cross-client benchmarking intelligence — validated in 30 days with a representative dataset and sample client feedback.</em>
</div>
""", unsafe_allow_html=True)

    # ── SUCCESS CRITERIA ──────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Success Criteria & Test Cases</div>', unsafe_allow_html=True)
    criteria2 = [
        ("SC-1: Data Migration", "0% of internal data on a unified platform", "Pilot dataset (2 years, 1 BU) migrated and queryable", "Validate row counts, data integrity checks, query performance"),
        ("SC-2: Benchmark Query Performance", "No real-time cross-client benchmarking", "Produce benchmark report in < 5 minutes", "Run benchmark SQL on migrated dataset; time execution"),
        ("SC-3: Anonymization Compliance", "No anonymization framework exists", "Legal/compliance sign-off on anonymized output", "Legal review of sample benchmark output"),
        ("SC-4: Market Validation", "$0 benchmarking product revenue", "3–5 bank clients express subscription interest", "Share sample benchmark report with 5 current clients; gather feedback"),
    ]
    for name, baseline, target, method in criteria2:
        st.markdown(f"""
<div class="sc-row">
<div style="font-size:14px;font-weight:700;color:#065F46;margin-bottom:6px">✅ {name}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13px">
<div><strong>Baseline:</strong> {baseline}</div>
<div><strong>Target:</strong> {target}</div>
<div><strong>Measurement:</strong> {method}</div>
</div>
</div>""", unsafe_allow_html=True)

    # ── PREREQUISITES ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**From Snowflake:**")
        for icon, item, owner, when in [
            ("❄️","Snowflake account with Marketplace capabilities","Jordan Ude","Day 1"),
            ("👤","Jordan Ude — data architecture & migration support","Jordan Ude","Ongoing"),
            ("📋","Marketplace listing guidance and timeline","Snowflake Partner Team","Week 3"),
        ]:
            st.markdown(f"""<div class="prereq-item"><span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("**From AML RightSource:**")
        for icon, item, owner, when in [
            ("👤","Jonathan McIsaac — pilot sponsor (0.25 FTE)","Jonathan McIsaac","Ongoing"),
            ("👩‍💻","1 data engineer (0.5 FTE for migration)","AML RS Engineering","Weeks 1–3"),
            ("📊","Extract of internal case management data (2+ years)","Jonathan / Data Team","Week 1"),
            ("⚖️","Legal review of anonymization approach","AML RS Legal","Week 3"),
            ("📋","List of 3–5 clients willing to preview benchmark product","Sabrina Chen","Week 3"),
        ]:
            st.markdown(f"""<div class="prereq-item"><span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div></div>""", unsafe_allow_html=True)

    # ── EXECUTION PLAN ────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Execution Plan — 30 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Days 1–5: Discovery & Data Audit","Jonathan discovery call: identify pilot dataset (2 years of case management data from 1 BU). Catalog internal data sources and confirm volumes. Set baseline: what benchmark questions can AML RS answer today vs. what the target state looks like."),
        ("2","Days 5–15: Data Migration & Modeling","AML RS data engineer + Jordan co-build Snowflake data pipeline. Load pilot dataset; validate integrity. Build star schema optimized for benchmarking analytics. Implement anonymization layer (aggregate-level controls, k-anonymity)."),
        ("3","Days 15–22: Benchmark Product Build","Build 3–5 benchmark queries: false positive rate by institution tier, case resolution time by region, analyst productivity comparisons. Create Snowsight dashboard for visualization. Legal reviews anonymized sample output."),
        ("4","Days 22–30: Client Validation & Readout","Share sample benchmark report with 3–5 willing advisory clients. Gather qualitative feedback on value and willingness to pay. Compile results vs. success criteria. Formal readout with Abhishek and Jonathan."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
<div class="phase-step">
<div class="phase-num">{num}</div>
<div><strong style="color:#0D2B4E;font-size:14px">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions — Pilot 2", placeholder="Add any notes, questions, or comments here...", height=100, key="p2_notes")


# ══════════════════════════════════════════════════════════════════════════════
# PILOT 3 — ALGORITHMS
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="pilot-header" style="border-top-color:#FF7A00">
    <h2>⚙️ Pilot 3 — Algorithm Deployment</h2>
    <p>Validate that Snowflake's Native App Framework enables AML RightSource to package, protect, and deploy scoring algorithms into client environments in minutes — not months.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── OWNERSHIP ─────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Ownership</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="owner-row"><div class="owner-label">Primary Pilot Owner</div><div><div class="owner-value">Isabel Yeung</div><div class="owner-sub">VP Tech Operations — Product Development & Engineering</div></div></div>
<div class="owner-row"><div class="owner-label">Supporting Owner</div><div><div class="owner-value">Abhishek Mittal</div><div class="owner-sub">EVP & Chief Product and AI Officer</div></div></div>
<div class="owner-row" style="border-bottom:none"><div class="owner-label">Executive Sponsor</div><div><div class="owner-value">Abhishek Mittal</div><div class="owner-sub">EVP & Chief Product and AI Officer</div></div></div>
""", unsafe_allow_html=True)

    # ── EXEC SUMMARY / POV STATEMENT ─────────────────────────────────────────
    st.markdown('<div class="sec-title">Executive Summary / POV Statement</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>Point of View:</strong> AML RightSource's engineering team has built proprietary AML scoring algorithms that represent years of domain expertise and IP investment. Today, deploying these algorithms into client environments requires <strong>3–6 months of bespoke engineering per client</strong> — making the business model fundamentally unscalable. We believe Snowflake's Native App Framework can package this IP into <strong>self-serve, installable applications</strong> that bank clients deploy in minutes from the Snowflake Marketplace — protecting IP, creating recurring SaaS revenue, and unlocking deployment at scale across all 200+ bank clients.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
This pilot validates that one existing AML RightSource algorithm can be successfully packaged as a Snowflake Native App with full IP protection, accurate output, and dramatically faster deployment — proving the viability of a scalable product distribution model.
""")

    # ── CURRENT BUSINESS PROBLEM ──────────────────────────────────────────────
    st.markdown('<div class="sec-title">Current Business Problem</div>', unsafe_allow_html=True)
    st.markdown("""
Isabel Yeung's engineering team builds proprietary AML scoring algorithms, case prioritization models, and QA automation logic in Python environments. Deploying these into a client's environment currently requires:

1. **Understanding the client's data infrastructure** (weeks of discovery)
2. **Custom API/connector build** per client (months of engineering)
3. **Security and compliance review** at each client institution (additional weeks)
4. **Ongoing per-client maintenance** (indefinite)

**The math doesn't work:** 200+ clients × 3–6 months = an engineering backlog that cannot be cleared. Revenue model is project-based (one-time fees), not recurring. IP is exposed in each custom deployment.

**The result:** AML RightSource has algorithms that work — but no scalable way to get them into the hands of all 200+ bank clients. Revenue from data products is capped by engineering capacity, not market demand.
""")

    # ── BUSINESS OBJECTIVE ────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Business Objective</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-green">
<strong>Objective:</strong> Prove that 1 existing AML RightSource algorithm can be successfully packaged as a Snowflake Native App — with full IP protection, output accuracy matching the standalone version, and deployment time reduced from months to minutes — validating a scalable SaaS distribution model for the entire algorithm portfolio.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
**Specific outcomes this pilot must demonstrate:**
- An existing Python algorithm runs correctly inside the Snowflake Native App framework
- IP is fully protected — clients cannot see or extract algorithm logic
- Output accuracy matches the standalone algorithm to > 99%
- A bank client can install and run the Native App in under 30 minutes (vs. 3–6 months today)
""")

    # ── DISCOVERY & CURRENT STATE ─────────────────────────────────────────────
    st.markdown('<div class="sec-title">Discovery & Current State Assessment</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
**Algorithm Inventory (Isabel to confirm):**
- AlertIQ — alert prioritization (XGBoost-based)
- KYC Refresh — customer risk re-scoring (Random Forest)
- SAR Quality Scorer — narrative quality analysis
- Network Risk Graph — beneficial ownership risk detection

**Current Technology Stack (to confirm):**
- Python (version TBD)
- ML libraries: XGBoost, scikit-learn, Pandas
- Current cloud: AWS and/or Azure (TBD)
- Current model serving: custom API per client
""")
    with c2:
        st.markdown("""
**Current Deployment Process:**
- 3–6 months per client, per algorithm
- Custom integration required at every client
- IP exposed in delivery
- Revenue: one-time project fee (~$50K–$150K/engagement)
- No recurring subscription model

**Key Deployment Friction Points (to confirm with Isabel):**
- Each client has different infrastructure
- Security review required at each client bank
- No standard deployment framework or packaging
- Ongoing maintenance burden per deployment
""")

    # ── POINT OF VIEW ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Point of View — Snowflake\'s Prediction</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="callout-blue">
<strong>We believe</strong> Snowflake can overcome <em>AML RightSource's inability to scale algorithm deployment across 200+ bank clients</em><br><br>
<strong>While supporting</strong> <em>Isabel's product roadmap and AML RightSource's objective of creating recurring SaaS algorithm revenue</em><br><br>
<strong>By implementing</strong> <em>Snowflake's Native App Framework — packaging 1 AML RightSource scoring algorithm as a Native App with Snowpark Python, demonstrating IP-protected one-click installation on synthetic bank data in a 30-day pilot.</em>
</div>
""", unsafe_allow_html=True)

    # ── SUCCESS CRITERIA ──────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Success Criteria & Test Cases</div>', unsafe_allow_html=True)
    criteria3 = [
        ("SC-1: Native App Build", "Algorithm runs in isolated Python environment", "Successfully packaged as Snowflake Native App; installs without error", "Jordan + Isabel build and test install in pilot environment"),
        ("SC-2: IP Protection", "Algorithm code exposed in every client deployment", "Client cannot see or extract algorithm logic", "Attempt to view source code from simulated client account — confirm access denied"),
        ("SC-3: Output Accuracy", "Standalone algorithm accuracy (Isabel to confirm)", "Native App output matches standalone to > 99%", "Run both versions on same synthetic test dataset; compare results"),
        ("SC-4: Deployment Speed", "3–6 months per client deployment", "< 30 minutes end-to-end install", "Time full installation on second test environment simulating a bank client"),
    ]
    for name, baseline, target, method in criteria3:
        st.markdown(f"""
<div class="sc-row">
<div style="font-size:14px;font-weight:700;color:#065F46;margin-bottom:6px">✅ {name}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13px">
<div><strong>Baseline:</strong> {baseline}</div>
<div><strong>Target:</strong> {target}</div>
<div><strong>Measurement:</strong> {method}</div>
</div>
</div>""", unsafe_allow_html=True)

    # ── PREREQUISITES ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Prerequisites & Resources</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**From Snowflake:**")
        for icon, item, owner, when in [
            ("❄️","Snowflake Developer Account with Native App Framework","Jordan Ude","Day 1"),
            ("📊","Synthetic bank data matching algorithm input schema","Jordan Ude","Days 1–3"),
            ("🧪","Second test environment (simulates client install)","Jordan Ude","Week 3"),
            ("👤","Jordan Ude — Native App build guidance","Jordan Ude","Ongoing"),
        ]:
            st.markdown(f"""<div class="prereq-item"><span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("**From AML RightSource:**")
        for icon, item, owner, when in [
            ("👤","Isabel Yeung — pilot sponsor","Isabel Yeung","Ongoing"),
            ("👩‍💻","1 engineer (1.0 FTE for build phase)","Isabel's Team","Weeks 1–3"),
            ("🐍","Python algorithm source code (1 algorithm ready for Snowpark port)","Isabel's Team","Week 1"),
            ("📋","Algorithm input/output schema documentation","Isabel's Team","Week 1"),
            ("🔐","IP protection review (legal sign-off on Native App structure)","AML RS Legal","Week 3"),
        ]:
            st.markdown(f"""<div class="prereq-item"><span style="font-size:18px">{icon}</span>
<div><div style="font-size:13px;font-weight:600;color:#0D2B4E">{item}</div>
<div style="font-size:11px;color:#718096">Owner: {owner} · {when}</div></div></div>""", unsafe_allow_html=True)

    # ── EXECUTION PLAN ────────────────────────────────────────────────────────
    st.markdown('<div class="sec-title">Pilot Execution Plan — 30 Days</div>', unsafe_allow_html=True)
    phases = [
        ("1","Days 1–5: Discovery & Scoping","Isabel technical discovery call with Jordan — current stack, algorithm architecture, Snowpark compatibility assessment. Select 1 algorithm for pilot (recommendation: AlertIQ priority scorer). Document input/output schema. Jordan provisions dev environment + synthetic test data."),
        ("2","Days 5–20: Native App Development","Isabel's engineer + Jordan co-build Snowpark Python wrapper for selected algorithm. Package as Native App with consumer privileges defined. IP protection testing: verify client cannot view source. Accuracy testing: compare Native App output vs. standalone model."),
        ("3","Days 20–25: Client Simulation","Jordan provisions second Snowflake account simulating a bank client environment. Install Native App from AML RS account to client test account — time the process. Run algorithm on synthetic bank data in 'client' environment. Capture deployment time, setup requirements, and any dependencies."),
        ("4","Days 25–30: Marketplace Readiness & Readout","Review Snowflake Marketplace listing requirements. Draft listing description and pricing model. Compile results vs. all success criteria. Readout meeting with Abhishek and Isabel — recommend next steps for full algorithm portfolio."),
    ]
    for num, title, desc in phases:
        st.markdown(f"""
<div class="phase-step">
<div class="phase-num">{num}</div>
<div><strong style="color:#0D2B4E;font-size:14px">{title}</strong><br><span style="font-size:13px;color:#4A5568">{desc}</span></div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.text_area("💬 Notes & Questions — Pilot 3", placeholder="Add any notes, questions, or comments here...", height=100, key="p3_notes")


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    🚀 AML RightSource × Snowflake — 30-Day Pilot Plans<br>
    Prepared by: Kala Boudreaux · Eric Szenderski · Jordan Ude — Snowflake Enterprise Acquisition<br>
    <span style="font-size:10px">All fields are editable. Add notes and questions during planning sessions with the Snowflake team.</span>
</div>
""", unsafe_allow_html=True)
