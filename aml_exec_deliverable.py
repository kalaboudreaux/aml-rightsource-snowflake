import streamlit as st

st.set_page_config(
    page_title="AML RightSource × Snowflake",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.hero {
    background: linear-gradient(135deg, #0D2B4E 0%, #11375C 50%, #1A4A7A 100%);
    border-radius: 16px; padding: 56px 48px; margin-bottom: 32px;
    position: relative; overflow: hidden;
}
.hero::before {
    content: ''; position: absolute; top: -50px; right: -50px;
    width: 300px; height: 300px; border-radius: 50%;
    background: radial-gradient(circle, rgba(41,181,232,0.15) 0%, transparent 70%);
}
.hero-badge {
    display: inline-block; background: rgba(41,181,232,0.15);
    border: 1px solid rgba(41,181,232,0.35); color: #29B5E8;
    padding: 5px 14px; border-radius: 20px; font-size: 11px;
    font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 20px;
}
.hero h1 { color: white; font-size: 42px; font-weight: 800; line-height: 1.1; margin: 0 0 12px; }
.hero h1 span { color: #29B5E8; }
.hero p { color: rgba(255,255,255,0.7); font-size: 17px; margin: 0; max-width: 600px; }

.kpi-card {
    background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 12px; padding: 20px; text-align: center;
}
.kpi-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px;
    color: rgba(255,255,255,0.55); margin-bottom: 8px; }
.kpi-value { font-size: 26px; font-weight: 800; color: white; }
.kpi-sub { font-size: 11px; color: rgba(255,255,255,0.5); margin-top: 4px; }

.section-title {
    font-size: 26px; font-weight: 800; color: #0D2B4E;
    border-bottom: 3px solid #29B5E8; padding-bottom: 10px; margin-bottom: 24px;
}

.card {
    background: white; border: 1px solid #D1E8F5; border-radius: 12px;
    padding: 22px; box-shadow: 0 2px 10px rgba(0,0,0,0.04); height: 100%;
}
.card-icon { font-size: 28px; margin-bottom: 10px; }
.card-title { font-size: 15px; font-weight: 700; color: #0D2B4E; margin-bottom: 8px; }
.card p { font-size: 13px; color: #4A5568; margin: 0; line-height: 1.6; }

.callout-blue {
    background: #E8F7FD; border-left: 4px solid #29B5E8;
    border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 8px 0;
}
.callout-green {
    background: #E6FBF3; border-left: 4px solid #00C96F;
    border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 8px 0;
}
.callout-orange {
    background: #FFF8E6; border-left: 4px solid #FF7A00;
    border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 8px 0;
}

.problem-card {
    background: #FEF3F2; border: 1px solid #FECACA; border-radius: 10px;
    padding: 16px; margin-bottom: 12px;
}
.problem-title { font-size: 14px; font-weight: 700; color: #991B1B; margin-bottom: 6px; }
.problem-body { font-size: 13px; color: #7F1D1D; }

.solution-card {
    background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 10px;
    padding: 16px; margin-bottom: 12px;
}
.solution-title { font-size: 14px; font-weight: 700; color: #065F46; margin-bottom: 6px; }
.solution-body { font-size: 13px; color: #064E3B; }

.impact-card {
    background: linear-gradient(135deg, #0D2B4E, #11375C); color: white;
    border-radius: 12px; padding: 20px; text-align: center;
}
.impact-num { font-size: 36px; font-weight: 900; color: #29B5E8; }
.impact-label { font-size: 12px; color: rgba(255,255,255,0.7); margin-top: 4px; }

.uc-card {
    background: white; border: 1px solid #D1E8F5; border-top: 4px solid;
    border-radius: 12px; padding: 24px; margin-bottom: 16px;
}

.why-snf {
    background: linear-gradient(135deg, #29B5E8 0%, #0D2B4E 100%);
    border-radius: 16px; padding: 40px; color: white; margin: 24px 0;
}
.why-snf h3 { color: white; font-size: 22px; font-weight: 800; margin-bottom: 20px; }
.snf-point { display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }
.snf-check { font-size: 20px; flex-shrink: 0; padding-top: 2px; }
.snf-text strong { color: white; font-size: 14px; }
.snf-text p { color: rgba(255,255,255,0.75); font-size: 13px; margin: 2px 0 0; }

.ref-card {
    background: white; border: 1px solid #D1E8F5; border-radius: 10px;
    padding: 16px; margin-bottom: 10px;
}
.ref-company { font-size: 15px; font-weight: 700; color: #0D2B4E; }
.ref-industry { font-size: 11px; color: #29B5E8; font-weight: 600; text-transform: uppercase;
    letter-spacing: 1px; margin: 2px 0 8px; }
.ref-summary { font-size: 13px; color: #4A5568; }
.ref-link { font-size: 12px; color: #29B5E8; margin-top: 8px; text-decoration: none; }

.nav-pill {
    display: inline-block; padding: 8px 18px; border-radius: 20px;
    font-size: 13px; font-weight: 600; cursor: pointer; margin: 4px;
    border: 2px solid #29B5E8; color: #29B5E8; background: transparent;
    transition: all 0.2s;
}

stTabGroup [data-baseweb="tab"] {
    font-weight: 600 !important;
}

.footer {
    background: #0D2B4E; color: rgba(255,255,255,0.5); text-align: center;
    padding: 20px; border-radius: 12px; margin-top: 40px; font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">❄️ Powered by Snowflake</div>
    <h1>AML RightSource &<br><span>The Snowflake Data Cloud</span></h1>
    <p>A strategic partnership to transform financial crimes compliance from a manual, fragmented process into an AI-powered intelligence platform — delivering faster advisory outcomes, scalable data products, and a defensible competitive moat.</p>
    <div style="display:grid; grid-template-columns: repeat(4,1fr); gap:16px; margin-top:32px">
        <div class="kpi-card"><div class="kpi-label">Bank Clients Served</div><div class="kpi-value">200+</div><div class="kpi-sub">Financial Institutions Globally</div></div>
        <div class="kpi-card"><div class="kpi-label">Snowflake FSI Network</div><div class="kpi-value">10 of 12</div><div class="kpi-sub">Largest US Banks on Snowflake</div></div>
        <div class="kpi-card"><div class="kpi-label">Advisory Time Reduction</div><div class="kpi-value">~85%</div><div class="kpi-sub">Days → Hours (Data Access)</div></div>
        <div class="kpi-card"><div class="kpi-label">New Revenue Potential</div><div class="kpi-value">$10M+</div><div class="kpi-sub">Data Product ARR (Year 3)</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAV TABS ──────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📋 Executive Summary",
    "⚡ Current State & Challenges",
    "🚀 How Snowflake Solves It",
    "🎯 Use Cases",
    "📊 Business Impact",
    "❄️ Why Snowflake",
    "🏆 Customer References",
])

# ────────────────────────────────────────────────────────────────────────────
# TAB 1 — EXECUTIVE SUMMARY
# ────────────────────────────────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="callout-blue">
    <strong>Strategic Opportunity:</strong> AML RightSource is at a defining inflection point — transitioning from a labor-intensive managed services model to an AI-powered financial crimes intelligence platform. Snowflake is the platform that makes this transformation possible, with capabilities uniquely matched to every dimension of AML RightSource's strategic priorities.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
        <div class="card-title">🏢 About AML RightSource</div>
        <p>AML RightSource is the leading managed services and advisory firm in financial crimes compliance — serving 200+ financial institutions across AML/BSA monitoring, KYC, SAR filing, and regulatory advisory. With the acquisition of BloomBrella and the appointment of Abhishek Mittal as Chief Product and AI Officer, the company has launched a strategic transformation to become a technology-native intelligence platform.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div class="card-title">🎯 The Strategic Mandate</div>
        <p>Three strategic imperatives drive every major technology decision at AML RightSource today: (1) Compress advisory engagement timelines to compete on speed and cost, (2) Monetize the company's unique aggregate data asset across 200+ FI clients, and (3) Scale algorithm and data product deployment to create defensible, recurring revenue ahead of a PE exit. Snowflake directly enables all three.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Three Use Case Tracks")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card" style="border-top:4px solid #29B5E8">
        <div class="card-icon">🔍</div>
        <div class="card-title">Track 1 — Advisory Intelligence</div>
        <p><strong>Fastest Time to Value.</strong> ETL-free, secure data collaboration for advisory engagements — reducing engagement time-to-data from weeks to hours and allowing analysts to focus on insights, not data prep.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card" style="border-top:4px solid #00C96F">
        <div class="card-icon">📊</div>
        <div class="card-title">Track 2 — Data Assets</div>
        <p><strong>New Revenue Category.</strong> Unify AML RightSource's massive internal operational data asset to build the first-ever cross-client benchmarking intelligence product — a SaaS offering no competitor can replicate.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card" style="border-top:4px solid #FF7A00">
        <div class="card-icon">⚙️</div>
        <div class="card-title">Track 3 — Algorithms</div>
        <p><strong>Product-Led Scale.</strong> Package and deploy AML scoring algorithms as Native Apps via Snowflake Marketplace — transforming algorithm delivery from 3–6 month bespoke projects to self-serve installs.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Focus Priorities — Why These Use Cases")
    st.markdown("""
    <div class="callout-green">
    <strong>Why Advisory First:</strong> The advisory use case is the fastest, lowest-risk path to measurable ROI. Advisory engagements are project-based — meaning value is visible within a single engagement cycle. Sabrina Chen and David Lutz have clear, quantifiable pain (days of data prep per engagement) and Snowflake's zero-copy data sharing solves it directly. Starting here builds internal confidence and creates a proof point for Tracks 2 and 3.
    </div>
    <div class="callout-blue" style="margin-top:8px">
    <strong>Why Data Assets &amp; Algorithms:</strong> These use cases unlock AML RightSource's long-term transformation narrative. Data products and algorithm distribution via Snowflake Marketplace create recurring SaaS revenue — fundamentally different from project-based advisory fees. For a PE-backed company approaching an exit horizon, this shift in revenue quality is a valuation multiplier.
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────
# TAB 2 — CURRENT STATE & CHALLENGES
# ────────────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">Current State & Challenges</div>', unsafe_allow_html=True)

    st.markdown("### Current State")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **AML RightSource today operates at the intersection of three business models:**
        - **Managed Services** (core): High-volume, labor-intensive AML/BSA operations for 200+ FI clients
        - **Advisory (FCA)**: Project-based engagements for model validation, program assessments, and regulatory remediation
        - **Blue Umbrella**: Third-party risk management and due diligence (BloomBrella acquisition)
        
        Each business unit generates significant value — but each is constrained by the same root problem: **manual, fragmented data workflows** that create friction, cost, and scale limitations.
        """)
    with col2:
        st.markdown("""
        **The Current Technology Environment:**
        - Client data arrives via secure FTP, email, or SharePoint — manually, per engagement
        - Each bank delivers data in different formats, requiring custom normalization every time
        - Internal operational data across 200+ clients lives in siloed systems with no unified analytics layer
        - Algorithm deployment requires 3–6 months of custom engineering per client
        - No ability to produce real-time cross-client benchmarking
        - Regulatory reference data is manually downloaded and maintained
        """)

    st.markdown("### Current Challenges")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="problem-card">
        <div class="problem-title">🔴 Advisory Data Onboarding Takes Weeks</div>
        <div class="problem-body">For every advisory engagement, AML RightSource must request, receive, and normalize client data via manual channels. This process typically takes 10–20 days per engagement — before any actual analysis work begins. Analysts spend 40–60% of engagement time on data preparation rather than advisory analysis.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="problem-card">
        <div class="problem-title">🔴 Algorithm Deployment Is Not Scalable</div>
        <div class="problem-body">Isabel Yeung's team builds AML scoring algorithms, case prioritization models, and QA automation tools. Deploying these into a client's environment today requires 3–6 months of bespoke engineering per client. With 200+ clients, this approach fundamentally cannot scale — each algorithm delivery is a custom professional services project with no recurring revenue model.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="problem-card">
        <div class="problem-title">🔴 A $10M+ Data Asset Is Generating $0 Revenue</div>
        <div class="problem-body">Jonathan McIsaac's operations team holds 10+ years of AML/BSA process data across 200+ financial institutions — the largest proprietary dataset of its kind in the independent compliance space. But this data sits in siloed systems with no unified analytics layer. The company cannot produce peer benchmarking products, and a massive competitive differentiator sits dormant.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="problem-card">
        <div class="problem-title">🔴 Data Security Concerns Slow Every Engagement</div>
        <div class="problem-body">Banks are rightly cautious about sharing sensitive transaction, KYC, and alert data with third parties. The current model — moving data via FTP or email — creates real security risk and consumes significant client IT bandwidth for each engagement. This compounds the time problem and introduces compliance risk for both AML RightSource and its clients.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Implications of Current Challenges")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="callout-orange">
        <strong>Growth Ceiling:</strong> Advisory cannot scale beyond current headcount without proportional hiring. Each new client adds linear cost. The firm's growth trajectory is artificially constrained by a solvable data infrastructure problem.
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="callout-orange">
        <strong>Competitive Exposure:</strong> RegTech competitors (NICE Actimize, Quantifind, SAS) are building cloud-native data platforms. If AML RightSource does not modernize, it will lose competitive position in advisory and data product markets.
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="callout-orange">
        <strong>PE Exit Risk:</strong> A services-only firm exits at 8–10x EBITDA. A data/SaaS firm exits at 15–25x ARR. Without Snowflake-enabled data products, AML RightSource may leave $50–100M+ of enterprise value on the table at exit.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### The Need Payoff")
    st.markdown("""
    <div class="callout-green">
    <strong>If AML RightSource solves these challenges:</strong><br>
    ✅ Advisory engagements start in <strong>hours, not weeks</strong> — more clients served, higher margins, higher NPS<br>
    ✅ Jonathan's data asset becomes a <strong>$5–10M ARR benchmarking product</strong> no competitor can replicate<br>
    ✅ Isabel's algorithms reach <strong>all 200+ bank clients through self-serve installs</strong> — recurring SaaS revenue at minimal incremental cost<br>
    ✅ AML RightSource transforms from a services company to a <strong>data intelligence platform</strong> — fundamentally changing its valuation story
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────
# TAB 3 — HOW SNOWFLAKE SOLVES IT
# ────────────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">How Snowflake Solves It</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="callout-blue">
    Snowflake is not just a data warehouse. It's a unified data platform with three capabilities that directly address AML RightSource's three strategic use cases — built for exactly the FSI regulatory environment you operate in.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="solution-card">
        <div class="solution-title">✅ Zero-Copy Data Sharing → Solves Advisory Onboarding</div>
        <div class="solution-body">Snowflake's data sharing architecture allows bank clients to grant AML RightSource read-only access to their transaction and KYC data — without the data ever leaving the bank's environment. No FTP, no email, no manual normalization. AML RightSource's advisory analysts query client data in-place, in real time. Result: engagement time-to-data drops from 10–20 days to hours.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="solution-card">
        <div class="solution-title">✅ Snowflake Marketplace → Monetizes Data Assets</div>
        <div class="solution-body">Once Jonathan's operational data is unified on Snowflake, AML RightSource can build anonymized benchmarking intelligence products and publish them on the Snowflake Marketplace — accessible to 10,000+ financial services customers globally. Banks can subscribe to benchmark comparisons directly from the Marketplace. New recurring SaaS revenue stream, zero data movement.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="solution-card">
        <div class="solution-title">✅ Native App Framework → Scales Algorithm Deployment</div>
        <div class="solution-body">Isabel's team packages AML scoring algorithms as Snowflake Native Apps — protected IP that clients can install in one click from the Marketplace into their own Snowflake environment. The algorithm runs on their data, in their compute. AML RightSource charges a subscription. One development cycle enables unlimited deployments across 200+ clients — no bespoke integration required.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Key Snowflake Capabilities for AML RightSource")

        caps = [
            ("❄️", "Unified Cloud Data Platform", "All data types — structured, semi-structured, unstructured. All clouds — AWS, Azure, GCP. One platform for analytics, AI/ML, and data products."),
            ("🔐", "Business Critical Security", "FedRAMP High, SOC 2 Type II, HIPAA, PCI DSS. Purpose-built for regulated industries. Passes bank infosec review."),
            ("🤝", "Data Sharing & Clean Rooms", "Zero-copy secure sharing between Snowflake accounts. Data Clean Rooms for double-blind collaboration. No data movement, no compliance risk."),
            ("🛒", "Snowflake Marketplace", "10,000+ customers including 10 of 12 largest US banks. List data products, algorithms, and apps. Built-in distribution for FSI."),
            ("📱", "Native App Framework", "Package algorithms as installable apps with IP protection. Self-serve deployment into client Snowflake environments. Recurring SaaS revenue model."),
            ("🤖", "Cortex AI (Native)", "LLM-powered analytics, document intelligence, SAR narrative generation, alert investigation summarization — no additional AI platform required."),
        ]
        for icon, title, desc in caps:
            st.markdown(f"""
            <div style="background:white; border:1px solid #D1E8F5; border-radius:10px; padding:14px; margin-bottom:10px; display:flex; gap:12px; align-items:flex-start">
            <span style="font-size:22px; flex-shrink:0">{icon}</span>
            <div><strong style="color:#0D2B4E; font-size:14px">{title}</strong><br><span style="color:#4A5568; font-size:13px">{desc}</span></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### Needs That Snowflake Directly Addresses")
    needs = [
        ("Eliminate manual FTP/email data exchange with clients", "Data Sharing — zero-copy, read-only, real-time"),
        ("Normalize disparate client data structures without custom ETL per client", "Semantic layer + Snowpark data transformation within the shared data"),
        ("Enable real-time analytics on client transaction data", "Live data sharing — no replication lag, no batch ETL"),
        ("Deploy algorithms into client environments securely", "Native App Framework — IP-protected, one-click client install"),
        ("Monetize aggregate benchmarking intelligence", "Snowflake Marketplace — 10,000+ FSI customers as potential buyers"),
        ("Build AI-native advisory tools (SAR drafting, alert triage)", "Cortex AI — native LLMs, Document AI, Cortex Search"),
        ("Meet bank security/compliance requirements for data collaboration", "FedRAMP High, SOC2, Business Critical edition with customer-managed keys"),
    ]
    for need, solution in needs:
        st.markdown(f"""
        <div style="display:flex; gap:16px; align-items:flex-start; padding:10px; background:#FAFCFE; border-radius:8px; margin-bottom:8px">
        <div style="flex:1; font-size:13px; color:#4A5568">🔴 <strong>Need:</strong> {need}</div>
        <div style="width:4px; background:#29B5E8; border-radius:2px; flex-shrink:0; min-height:20px"></div>
        <div style="flex:1; font-size:13px; color:#065F46">✅ <strong>Snowflake:</strong> {solution}</div>
        </div>
        """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────
# TAB 4 — USE CASES
# ────────────────────────────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Use Cases We\'re Focused On</div>', unsafe_allow_html=True)

    uc_sel = st.radio("Select Use Case", ["🔍 UC-1: Advisory Intelligence", "📊 UC-2: Data Assets & Benchmarking", "⚙️ UC-3: Algorithm Deployment"], horizontal=True)

    if "Advisory" in uc_sel:
        st.markdown("""
        <div class="uc-card" style="border-top-color:#29B5E8">
        <h3 style="color:#0D2B4E; margin-top:0">UC-1: Advisory Intelligence — ETL-Free Client Data Collaboration</h3>
        <p style="color:#4A5568"><strong>SMEs:</strong> Sabrina Chen · David Lutz · FCA Advisory Team</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### Why This Use Case Matters
            Advisory engagements — model validation, algorithm tuning, AML program assessments — are AML RightSource's highest-margin offering and fastest growth engine. Every dollar saved in data preparation time flows directly to margin or client capacity. More critically, faster advisory delivery is a direct competitive advantage: clients choose advisors who can start work today, not in three weeks.
            
            #### The Specific Problem
            Today, every advisory engagement starts with a data request cycle:
            1. Request data from client IT/security team
            2. Client exports, encrypts, and transfers data (email/FTP)
            3. AML RS normalizes, cleanses, and loads into analysis environment
            4. **Only then does actual advisory analysis begin — 2–3 weeks later**
            
            This cycle repeats for every client, every engagement, every data refresh.
            """)
        with c2:
            st.markdown("""
            #### Snowflake's Solution
            **Zero-Copy Data Sharing:** Bank clients grant AML RightSource a read-only Snowflake data share of their relevant transaction, alert, and KYC data. No data moves. AML RS analysts query in-place — analysis starts the same day the share is granted.
            
            **Cortex AI:** AI-native investigation summarization, narrative generation, and model validation accelerators reduce analyst time further.
            
            #### How We Measure Success
            | Metric | Before | Target |
            |--------|--------|--------|
            | Time to first data access | 10–20 days | <48 hours |
            | Analyst time on data prep | 40–60% | <10% |
            | Engagements/analyst/quarter | Baseline | +50–100% |
            | Client time-to-report | 4–8 weeks | 1–2 weeks |
            """)

    elif "Data Assets" in uc_sel:
        st.markdown("""
        <div class="uc-card" style="border-top-color:#00C96F">
        <h3 style="color:#0D2B4E; margin-top:0">UC-2: Data Assets & Cross-Client Benchmarking Intelligence</h3>
        <p style="color:#4A5568"><strong>SME:</strong> Jonathan McIsaac · Global SVP, Client Operations</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### Why This Use Case Matters
            AML RightSource has a data asset that no competitor in the world possesses: 10+ years of AML/BSA process data across 200+ financial institutions — case resolution rates, false positive rates, analyst productivity metrics, SAR volumes, and more. 
            
            Banks pay millions of dollars annually for benchmarking intelligence from sources like Celent, Gartner, and The Financial Crimes Enforcement Network. AML RightSource is sitting on a category-defining proprietary version of this — currently generating zero revenue.
            
            **This is not a technology problem. It's an infrastructure problem. Snowflake is the infrastructure.**
            """)
        with c2:
            st.markdown("""
            #### Snowflake's Solution
            1. **Migrate** Jonathan's operational data to Snowflake (unified single platform)
            2. **Build** an anonymized analytics layer — cross-client benchmarking without exposing client PII
            3. **Leverage** Snowflake Data Clean Rooms for double-blind data collaboration
            4. **Publish** benchmarking intelligence product to Snowflake Marketplace — 10,000+ FSI subscribers
            
            #### How We Measure Success
            | Metric | Before | Target |
            |--------|--------|--------|
            | Benchmark product ARR | $0 | $2–5M (Year 2) |
            | Time to produce benchmarking report | Days (manual) | Minutes (automated) |
            | Internal data unified on platform | ~0% | 80%+ |
            | New Marketplace subscribers | 0 | 50–200 banks (Year 2) |
            """)

    else:
        st.markdown("""
        <div class="uc-card" style="border-top-color:#FF7A00">
        <h3 style="color:#0D2B4E; margin-top:0">UC-3: Algorithms — Native App-Powered Algorithm Deployment</h3>
        <p style="color:#4A5568"><strong>SME:</strong> Isabel Yeung · VP Tech Operations</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            #### Why This Use Case Matters
            Isabel's engineering team has built (and continues to build) proprietary AML scoring algorithms, case prioritization models, and quality assurance automation. These represent years of IP investment.
            
            The problem: getting these algorithms into client environments today is a 3–6 month bespoke engineering project per client. The IP delivery mechanism doesn't scale. At 200 clients, this means:
            - 200 × 6 months = **100 years of engineering time** to fully deploy
            - Revenue per algorithm deployment: one-time project fee, not recurring
            - IP exposure risk with each custom deployment
            
            **The business model doesn't scale. Snowflake's Native App framework changes everything.**
            """)
        with c2:
            st.markdown("""
            #### Snowflake's Solution
            **Native App Framework:** Isabel's team packages each algorithm as a Snowflake Native App. Banks install it directly from the Marketplace in minutes. The algorithm runs on their data, in their compute, with AML RS's IP fully protected (clients cannot see or extract the logic).
            
            - One development cycle → unlimited deployments
            - AML RS charges subscription fee per install (recurring SaaS)
            - 10 of 12 largest US banks already on Snowflake = immediate distribution
            
            #### How We Measure Success
            | Metric | Before | Target |
            |--------|--------|--------|
            | Deployment time per client | 3–6 months | <1 week |
            | Algorithm installs across client base | 0 | 20–50 (Year 2) |
            | Algorithm ARR (SaaS model) | $0 | $1–3M (Year 2) |
            | Engineering time per deployment | 500+ hours | <10 hours |
            """)

# ────────────────────────────────────────────────────────────────────────────
# TAB 5 — BUSINESS IMPACT
# ────────────────────────────────────────────────────────────────────────────
with tab5:
    st.markdown('<div class="section-title">Business Impact & Outcomes</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="impact-card">
        <div class="impact-num">85%</div>
        <div class="impact-label">Reduction in advisory engagement time-to-data (20 days → 2 hrs)</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="impact-card">
        <div class="impact-num">2–3×</div>
        <div class="impact-label">Analyst productivity improvement per advisory engagement</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="impact-card">
        <div class="impact-num">$10M+</div>
        <div class="impact-label">New data product ARR potential (Year 3) from Marketplace</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="impact-card">
        <div class="impact-num">10×</div>
        <div class="impact-label">Algorithm deployment capacity improvement per engineer</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 3-Year Value Creation Summary")
    st.markdown("""
    <div style="overflow-x:auto; margin:16px 0">
    <table style="width:100%; border-collapse:collapse; font-size:13px">
    <thead style="background:#0D2B4E; color:white">
    <tr>
    <th style="padding:12px 14px; text-align:left">Value Driver</th>
    <th style="padding:12px 14px; text-align:right">Year 1</th>
    <th style="padding:12px 14px; text-align:right">Year 2</th>
    <th style="padding:12px 14px; text-align:right">Year 3</th>
    </tr>
    </thead>
    <tbody>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px"><strong>Advisory Productivity Gain</strong></td><td style="padding:10px 14px; text-align:right">$500K–$1M</td><td style="padding:10px 14px; text-align:right">$1.5M–$3M</td><td style="padding:10px 14px; text-align:right">$3M–$5M</td></tr>
    <tr><td style="padding:10px 14px"><strong>Benchmarking Product Revenue (New)</strong></td><td style="padding:10px 14px; text-align:right">$0</td><td style="padding:10px 14px; text-align:right">$1M–$3M</td><td style="padding:10px 14px; text-align:right">$3M–$8M</td></tr>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px"><strong>Algorithm SaaS Revenue (New)</strong></td><td style="padding:10px 14px; text-align:right">$0</td><td style="padding:10px 14px; text-align:right">$500K–$1.5M</td><td style="padding:10px 14px; text-align:right">$2M–$5M</td></tr>
    <tr><td style="padding:10px 14px"><strong>COGS Reduction (ETL/data ops)</strong></td><td style="padding:10px 14px; text-align:right">$200K–$500K</td><td style="padding:10px 14px; text-align:right">$400K–$800K</td><td style="padding:10px 14px; text-align:right">$600K–$1.2M</td></tr>
    <tr style="background:#E8F7FD; font-weight:700"><td style="padding:10px 14px">Total Business Value</td><td style="padding:10px 14px; text-align:right; color:#065F46">$700K–$1.5M</td><td style="padding:10px 14px; text-align:right; color:#065F46">$3.4M–$8.3M</td><td style="padding:10px 14px; text-align:right; color:#065F46">$8.6M–$19.2M</td></tr>
    </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="callout-green">
    <strong>PE Exit Value Creation:</strong> A managed services company exits at ~8–10× EBITDA. A data products / SaaS company exits at 15–25× ARR. By building new recurring data product revenue on Snowflake, <strong>AML RightSource can fundamentally shift its revenue quality and exit multiple — creating significant incremental enterprise value for shareholders.</strong>
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────
# TAB 6 — WHY SNOWFLAKE
# ────────────────────────────────────────────────────────────────────────────
with tab6:
    st.markdown('<div class="section-title">Why Snowflake</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="why-snf">
    <h3>❄️ Snowflake is the only platform purpose-built for what AML RightSource is trying to do.</h3>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>10 of 12 Largest US Banks Are Already on Snowflake</strong><p>When you deploy your advisory workflow on Snowflake, you're deploying on the same platform your bank clients already use. Zero new vendor onboarding for your clients — the path to data sharing is already paved.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>Only Platform with Zero-Copy Data Sharing Across All Three Clouds</strong><p>Databricks requires data movement. MS Fabric requires Azure. Snowflake's data sharing works across AWS, Azure, and GCP — with no data movement, no latency, and no additional security perimeter to manage.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>Native App Framework — No Equivalent Exists in the Market</strong><p>The ability to package your algorithms as installable apps with full IP protection, deployed via a built-in marketplace with 10,000+ FSI customers, is unique to Snowflake. No other platform offers this for financial services data products.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>FedRAMP High + SOC 2 Type II — Passes Every Bank's Security Review</strong><p>Snowflake holds more compliance certifications than any other data platform — specifically designed for regulated industries. Every bank security questionnaire Snowflake has faced in FSI, it has passed.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>Consumption-Based Pricing Aligns with Your Project-Based Revenue Model</strong><p>AML RightSource earns revenue on a project-by-project basis. Snowflake's consumption model means you only pay when you're using it — no idle infrastructure cost between engagements. Cost of goods sold for advisory engagements is tightly controlled.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>Cortex AI — Native AI Out of the Box, Day One</strong><p>Every Snowflake customer has access to LLM-powered analytics, document AI, vector search, and ML model registry from day one — no additional AI platform or API key required. SAR narrative generation, alert investigation summarization, and model validation acceleration are available immediately.</p></div></div>
    <div class="snf-point"><div class="snf-check">✅</div><div class="snf-text"><strong>The Team You See Is the Team You Get</strong><p>Snowflake's Ohio Valley team (Kala, Eric, Jordan) has direct relationships with the Snowflake FSI account teams covering your top bank clients. We are your channel into that network — helping accelerate the client-side engagement needed for Track 1 to succeed.</p></div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Snowflake vs. Alternatives")
    st.markdown("""
    <div style="overflow-x:auto">
    <table style="width:100%; border-collapse:collapse; font-size:13px">
    <thead style="background:#0D2B4E; color:white">
    <tr><th style="padding:12px 14px; text-align:left">Capability</th><th style="padding:12px 14px; text-align:center">Snowflake</th><th style="padding:12px 14px; text-align:center">Databricks</th><th style="padding:12px 14px; text-align:center">MS Fabric</th><th style="padding:12px 14px; text-align:center">AWS Native</th></tr>
    </thead>
    <tbody>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px">Zero-copy data sharing (cross-cloud)</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Native, all clouds</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌ Requires data movement</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌ Azure-only</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️ AWS-only</td></tr>
    <tr><td style="padding:10px 14px">Native App / Algorithm Marketplace</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Purpose-built for FSI</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌ No equivalent</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌ No equivalent</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌ No equivalent</td></tr>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px">Data Clean Rooms</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Industry standard</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️ Limited</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️ Limited</td><td style="padding:10px 14px; text-align:center; color:#991B1B">❌</td></tr>
    <tr><td style="padding:10px 14px">FedRAMP High / SOC2 Type II</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️ In progress</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td></tr>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px">Native AI (no separate AI platform)</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Cortex AI built-in</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Strong ML</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅ Copilot</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️ SageMaker separate</td></tr>
    <tr><td style="padding:10px 14px">Consumption-based (no idle cost)</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">⚠️</td><td style="padding:10px 14px; text-align:center; color:#065F46">✅</td></tr>
    <tr style="background:#F7FBFE"><td style="padding:10px 14px">FSI bank customer base (distribution)</td><td style="padding:10px 14px; text-align:center; color:#065F46"><strong>10 of 12 largest US banks</strong></td><td style="padding:10px 14px; text-align:center; color:#FF7A00">Growing</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">Mixed</td><td style="padding:10px 14px; text-align:center; color:#FF7A00">Moderate</td></tr>
    </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────
# TAB 7 — CUSTOMER REFERENCES
# ────────────────────────────────────────────────────────────────────────────
with tab7:
    st.markdown('<div class="section-title">Customer References</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="callout-blue">
    The following Snowflake customers represent real-world proof that the platform delivers for financial services, compliance, and data product companies with use cases highly similar to AML RightSource's strategic priorities.
    </div>
    """, unsafe_allow_html=True)

    refs = [
        {
            "company": "Fiserv",
            "industry": "Core Banking Platform / FinTech",
            "summary": "Fiserv leverages Snowflake to power their Data as a Service (DaaS) offering — enabling financial institutions to strengthen customer relationships through real-time data sharing and analytics. Fiserv's DaaS model is built on the same zero-copy data sharing architecture AML RightSource needs for its advisory engagements: bank clients get instant, secure access to their own data insights without data movement or complex ETL pipelines.",
            "outcome": "Fiserv DaaS enables financial institutions to move from static reporting to real-time, relationship-strengthening data intelligence",
            "link": "https://www.carat.fiserv.com/en-us/resources/daas-strengthen-customer-relationships/",
            "tag": "🔍 Directly Relevant to UC-1"
        },
        {
            "company": "FIS",
            "industry": "Global Financial Technology Leader",
            "summary": "FIS, one of the world's largest fintech companies serving banks, capital markets, and institutions globally, chose Snowflake as their core data platform. FIS uses Snowflake to unify data across its vast portfolio of banking products — enabling real-time analytics, regulatory reporting, and client intelligence at massive scale. Their story validates that the world's most critical financial infrastructure runs on Snowflake.",
            "outcome": "Unified data platform across global banking product portfolio; real-time analytics and regulatory intelligence at scale",
            "link": "https://www.snowflake.com/en/customers/all-customers/case-study/fis/",
            "tag": "🏦 FSI Platform Validation"
        },
        {
            "company": "Coinbase",
            "industry": "Crypto Exchange / Financial Services",
            "summary": "Coinbase, the largest US crypto exchange and a highly regulated financial services firm, built their entire data and analytics infrastructure on Snowflake. Coinbase uses Snowflake for transaction analytics, compliance monitoring, fraud detection, and customer intelligence — demonstrating that even the most security-sensitive, regulatory-scrutinized financial platforms trust Snowflake with their most critical data workloads.",
            "outcome": "Enterprise-scale transaction analytics and compliance monitoring for millions of customers on a single Snowflake platform",
            "link": "https://www.snowflake.com/en/customers/all-customers/video/coinbase/",
            "tag": "🔐 Regulated FinServ Proof Point"
        },
        {
            "company": "TransUnion",
            "industry": "Credit & Identity Data / Information Services",
            "summary": "TransUnion shares how they use Snowflake to modernize their data infrastructure and deliver real-time credit, identity, and risk intelligence to financial institutions. TransUnion's use of Snowflake's data sharing and Marketplace capabilities mirrors exactly the architecture AML RightSource can leverage to distribute benchmarking intelligence and data products to bank clients at scale — without data movement or per-client integration overhead.",
            "outcome": "Real-time financial risk intelligence delivered to FSI clients via Snowflake data sharing; accelerated data product distribution",
            "link": "https://www.youtube.com/watch?v=NUjIFvwNdCw",
            "tag": "📊 Directly Relevant to UC-2"
        },
        {
            "company": "ADP",
            "industry": "HR / Payroll / Workforce Intelligence",
            "summary": "ADP built a dynamic benchmarking platform on Snowflake that delivers real-time HCM (Human Capital Management) metrics benchmarking to their clients — allowing organizations to compare their workforce metrics against anonymized industry peers. This is precisely the architecture AML RightSource needs for its cross-client AML benchmarking intelligence product: ADP's story proves that aggregate, anonymized benchmarking across thousands of clients is not only possible on Snowflake, but a proven SaaS revenue model.",
            "outcome": "Industry-first dynamic benchmarking product delivering real-time peer comparisons across thousands of employer clients",
            "link": "https://www.snowflake.com/en/blog/adp-enables-dynamic-benchmarking-hcm-metrics/",
            "tag": "📊 Most Relevant to UC-2 Benchmarking"
        },
        {
            "company": "Block (Square)",
            "industry": "Payments / Financial Technology",
            "summary": "Block (formerly Square) shares how they use Snowflake to power data-driven financial services for millions of merchants and consumers. Block leverages Snowflake for real-time payments analytics, fraud detection, risk scoring, and merchant intelligence — demonstrating how a modern fintech company operationalizes Snowflake across compliance, risk, and customer analytics simultaneously. A strong proof point for AML RightSource's algorithm and analytics use cases.",
            "outcome": "Unified real-time analytics across payments, fraud, and risk workloads; accelerated product development on a single platform",
            "link": "https://www.youtube.com/watch?v=AmzxyTjbUK0&t=27s",
            "tag": "⚙️ FinTech Analytics & Risk Proof Point"
        },
        {
            "company": "Purpose Financial",
            "industry": "Consumer Lending / Alternative Financial Services",
            "summary": "Purpose Financial, a consumer lending company serving underbanked communities, shares how Snowflake transformed their data operations. Purpose Financial uses Snowflake to unify loan performance data, compliance reporting, and customer analytics — enabling faster regulatory reporting and better risk management. As a regulated lender operating across complex compliance requirements, Purpose Financial's story directly reflects the regulatory data challenges AML RightSource's bank clients face.",
            "outcome": "Unified compliance and analytics platform; faster regulatory reporting and risk intelligence for a regulated lending business",
            "link": "https://www.snowflake.com/en/customers/all-customers/video/purpose-financial/",
            "tag": "🔍 Regulated Compliance Data Proof Point"
        },
    ]

    for ref in refs:
        with st.expander(f"**{ref['company']}** — {ref['industry']} — {ref['tag']}"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown(f"""
                <div class="ref-card">
                <div class="ref-company">{ref['company']}</div>
                <div class="ref-industry">{ref['industry']}</div>
                <div class="ref-summary">{ref['summary']}</div>
                </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="callout-green" style="height:100%">
                <strong>Key Outcome:</strong><br>{ref['outcome']}
                <br><br>
                <strong>Relevance:</strong><br>{ref['tag']}
                </div>
                """, unsafe_allow_html=True)
            st.markdown(f"[View on Snowflake Customer Hub →]({ref['link']})")

    st.markdown("""
    ---
    ### Want to Talk to a Peer?
    The Snowflake team can arrange a reference call with customers in similar roles at comparable firms in the financial crimes compliance and RegTech space. Ask your Snowflake account team to set this up as part of the evaluation process.
    """)

# FOOTER
st.markdown("""
<div class="footer">
    ❄️ Prepared by the Snowflake Enterprise Acquisition Team for AML RightSource<br>
    Kala Boudreaux · Eric Szenderski · Jordan Ude<br>
    <span style="font-size:10px">For questions, contact your Snowflake account team. All metrics are estimates unless otherwise stated.</span>
</div>
""", unsafe_allow_html=True)
