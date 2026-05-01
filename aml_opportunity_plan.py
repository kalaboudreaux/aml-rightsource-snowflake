import streamlit as st
from datetime import datetime
import uuid

st.set_page_config(
    page_title="AML RightSource — Opportunity Plan",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "section_notes" not in st.session_state:
    st.session_state.section_notes = {}
if "comments" not in st.session_state:
    st.session_state.comments = {}

def get_note(key, default=""):
    return st.session_state.section_notes.get(key, default)

def save_note(key, val):
    st.session_state.section_notes[key] = val

def add_comment(section_key, author, text):
    if section_key not in st.session_state.comments:
        st.session_state.comments[section_key] = []
    if author.strip() and text.strip():
        st.session_state.comments[section_key].append({
            "id": str(uuid.uuid4())[:6],
            "author": author,
            "text": text,
            "ts": datetime.now().strftime("%b %d, %Y %I:%M %p"),
        })

def show_comments(section_key):
    comments = st.session_state.comments.get(section_key, [])
    if comments:
        st.markdown(f"**💬 {len(comments)} Comment(s):**")
        for c in reversed(comments[-8:]):
            st.markdown(f"""
<div style="background:white;border:1px solid #D1E8F5;border-left:3px solid #29B5E8;
border-radius:0 8px 8px 0;padding:10px 14px;margin:6px 0">
<span style="font-size:11px;color:#718096">👤 <strong>{c['author']}</strong> · {c['ts']}</span><br>
<span style="font-size:13px;color:#2D3748">{c['text']}</span>
</div>""", unsafe_allow_html=True)

def notes_comments_block(section_key, note_label="📝 Account Team Notes", note_default=""):
    with st.expander("✏️ Notes & Comments — Click to expand", expanded=False):
        st.markdown(f'<span style="font-size:12px;font-weight:700;color:#29B5E8;text-transform:uppercase;letter-spacing:1px">{note_label}</span>', unsafe_allow_html=True)
        note_val = st.text_area("", value=get_note(section_key, note_default), height=100,
                                 key=f"note_{section_key}", label_visibility="collapsed",
                                 placeholder="Add account team notes, strategy thoughts, or follow-up items here...")
        save_note(section_key, note_val)
        st.markdown("---")
        c1, c2 = st.columns([2, 1])
        with c1:
            author = st.text_input("Your Name", key=f"auth_{section_key}", placeholder="Enter your name")
            comment = st.text_area("Comment / Question", key=f"comm_{section_key}", height=70,
                                    label_visibility="visible", placeholder="Add a question or comment...")
        with c2:
            st.markdown("<br><br>", unsafe_allow_html=True)
            if st.button("Post", key=f"btn_{section_key}", type="primary"):
                if author.strip() and comment.strip():
                    add_comment(section_key, author, comment)
                    st.rerun()
                else:
                    st.warning("Please enter your name and comment.")
        show_comments(section_key)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.section-hero {
    background: linear-gradient(135deg,#0D2B4E,#11375C);
    color:white; border-radius:14px; padding:32px 36px; margin-bottom:24px;
}
.section-hero h1 { font-size:28px; font-weight:900; margin:0 0 6px; }
.section-hero p { color:rgba(255,255,255,0.7); font-size:14px; margin:0; }
.sec-num { background:#29B5E8; color:white; border-radius:8px; padding:4px 10px;
    font-size:12px; font-weight:800; margin-right:10px; }
.section-title { font-size:22px; font-weight:800; color:#0D2B4E;
    border-bottom:3px solid #29B5E8; padding-bottom:10px; margin-bottom:20px;
    display:flex; align-items:center; gap:8px; }
.card { background:white; border:1px solid #D1E8F5; border-radius:12px;
    padding:18px 20px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.04); }
.card-title { font-size:14px; font-weight:700; color:#0D2B4E; margin-bottom:6px; }
.callout-blue { background:#E8F7FD; border-left:4px solid #29B5E8;
    border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; font-size:13px; }
.callout-green { background:#E6FBF3; border-left:4px solid #00C96F;
    border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; font-size:13px; }
.callout-orange { background:#FFF8E6; border-left:4px solid #FF7A00;
    border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; font-size:13px; }
.callout-red { background:#FEF2F2; border-left:4px solid #E63946;
    border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; font-size:13px; }
.tag { display:inline-block; padding:2px 10px; border-radius:10px; font-size:11px; font-weight:700; margin:2px; }
.tag-blue { background:#DBEFFE; color:#1E6FA8; }
.tag-green { background:#D1FAE5; color:#065F46; }
.tag-orange { background:#FEF3C7; color:#92400E; }
.tag-red { background:#FEE2E2; color:#991B1B; }
.tag-purple { background:#EDE9FE; color:#5B21B6; }
.medd-card { background:white; border:1px solid #D1E8F5; border-radius:10px;
    padding:16px; margin-bottom:12px; }
.medd-letter { font-size:28px; font-weight:900; color:#29B5E8; line-height:1; }
.medd-word { font-size:13px; font-weight:700; color:#0D2B4E; margin-bottom:8px; }
.step-item { display:flex; gap:14px; padding:14px; background:white;
    border:1px solid #D1E8F5; border-radius:10px; margin-bottom:10px; }
.step-num { width:32px; height:32px; background:#0D2B4E; color:white; border-radius:8px;
    display:flex; align-items:center; justify-content:center; font-weight:800;
    font-size:13px; flex-shrink:0; }
.sidebar-nav-item { padding:8px 12px; border-radius:8px; font-size:13px;
    cursor:pointer; margin-bottom:2px; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR NAVIGATION ────────────────────────────────────────────────────────
SECTIONS = [
    "01 · Executive Summary",
    "02 · Opportunity Summary",
    "03 · Stakeholders Engaged",
    "04 · Company Priorities",
    "05 · Company Profile & Financials",
    "06 · Business Units",
    "07 · Market Headwinds & Tailwinds",
    "08 · Leadership & Power Center",
    "09 · Stakeholder Map",
    "10 · IT & Data Spending",
    "11 · Data Sources",
    "12 · Estimated Data Volumes",
    "13 · Current Challenges by Source",
    "14 · Use Cases by Data Source",
    "15 · Focused Use Cases",
    "16 · MEDDPICC Analysis",
    "17 · Why These Use Cases Matter",
    "18 · How Snowflake Solves Them",
    "19 · Business Impact Measurement",
    "20 · Capacity Planning",
    "21 · Investment & ROI",
    "22 · Migration & Architecture",
    "23 · Strategic Execution Analysis",
    "24 · Next Actions & Pursuit Strategy",
    "25 · Step-by-Step Win Plan",
    "26 · Path to Contracting",
    "27 · Making Contracting Easy",
    "28 · Open Questions",
    "29 · Accelerating to Signature",
    "📊 All Notes Summary",
]

with st.sidebar:
    st.markdown("""
<div style="background:linear-gradient(135deg,#0D2B4E,#11375C);border-radius:12px;
padding:20px;margin-bottom:16px;color:white;text-align:center">
<div style="font-size:24px">❄️</div>
<div style="font-size:14px;font-weight:800;margin-top:6px">AML RightSource</div>
<div style="font-size:11px;color:rgba(255,255,255,0.6);margin-top:2px">Opportunity Plan</div>
<div style="background:rgba(41,181,232,0.2);border-radius:6px;padding:4px 8px;
margin-top:10px;font-size:10px;color:#29B5E8;font-weight:700">🔒 INTERNAL — SNOWFLAKE ONLY</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("**Navigate Sections**")
    selected = st.selectbox("", SECTIONS, label_visibility="collapsed")

    total_notes = sum(1 for v in st.session_state.section_notes.values() if v.strip())
    total_comments = sum(len(v) for v in st.session_state.comments.values())
    st.markdown(f"""
<div style="background:#E8F7FD;border-radius:8px;padding:12px;margin-top:16px;font-size:12px">
📝 <strong>{total_notes}</strong> sections with notes<br>
💬 <strong>{total_comments}</strong> total comments
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style="font-size:11px;color:#718096">
<strong>Account Team</strong><br>
Kala Boudreaux · AE<br>
Eric Szenderski · DM<br>
Jordan Ude · SE
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION RENDERER
# ══════════════════════════════════════════════════════════════════════════════

# ── SECTION 01 ────────────────────────────────────────────────────────────────
if selected == SECTIONS[0]:
    st.markdown("""<div class="section-hero">
<h1>01 — Executive Summary</h1>
<p>Bottom line up front: AML RightSource is a PE-backed, market-leading financial crimes managed services provider at a pivotal transformation inflection point.</p>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-green">
<strong>Bottom Line:</strong> AML RightSource is pivoting from a services business to an AI-powered intelligence platform. Snowflake is uniquely positioned as the data infrastructure backbone for all three of their growth vectors. Champion identified: Abhishek Mittal (CPAIO). NDA signed. Pilot planning in motion.
</div>""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (label, val, sub) in zip([c1,c2,c3,c4],[
        ("Deal Stage","Discovery → Pilot","Pilot planning in motion, NDA signed"),
        ("Champion","Abhishek Mittal","EVP & Chief Product and AI Officer"),
        ("Active Use Cases","3","Advisory · Data Assets · Algorithms"),
        ("Est. Year 1 ACV","$500K–$1.5M","3-yr potential: $3–8M"),
    ]):
        with col:
            st.markdown(f"""<div class="card" style="text-align:center">
<div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#29B5E8;margin-bottom:6px">{label}</div>
<div style="font-size:20px;font-weight:900;color:#0D2B4E">{val}</div>
<div style="font-size:11px;color:#718096;margin-top:4px">{sub}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""
AML RightSource was founded as a specialized anti-money laundering and financial crimes compliance managed services firm. Through the acquisition of BloomBrella and appointment of Abhishek Mittal as Chief Product and AI Officer, the company has embarked on a strategic transformation — evolving from labor-intensive services to a technology and AI-driven intelligence platform that amplifies analyst productivity, accelerates client time-to-value, and creates defensible, scalable data products monetizable across their 200+ financial institution client base.

**Three use case tracks identified:**
- **Track 1 — Advisory (Sabrina Chen + David Lutz):** ETL-free, secure client data collaboration for advisory engagements. Fastest time to value.
- **Track 2 — Data Assets (Jonathan McIsaac):** Monetize the massive internal operational data asset for cross-client benchmarking intelligence.
- **Track 3 — Algorithms (Isabel Yeung):** Deploy scoring algorithms as Native Apps via Snowflake Marketplace — scalable SaaS model.
""")
    notes_comments_block("s01", "Account Team Notes — Executive Summary")

# ── SECTION 02 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[1]:
    st.markdown("""<div class="section-hero"><h1>02 — Opportunity Summary</h1><p>Deal profile, revenue opportunity, and strategic context.</p></div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Deal Profile")
        data = [("Company","AML RightSource, LLC"),("HQ","Overland Park, KS"),("Industry","Financial Crimes Compliance / RegTech"),("Ownership","PE-backed — Gridiron Capital + Clarion Capital"),("Employees","~1,200–1,500 (post-BloomBrella)"),("Clients","200+ financial institutions globally"),("Current Snowflake","None — net new acquisition"),("NDA","✅ Signed"),("Deal Type","Platform + ISV/Marketplace Partnership"),("Pilot Target","Q2/Q3 2026"),("Close Target","Q3/Q4 2026"),]
        for k, v in data:
            st.markdown(f"""<div style="display:flex;gap:12px;padding:8px;border-bottom:1px solid #E2E8F0;font-size:13px">
<div style="width:160px;color:#718096;flex-shrink:0">{k}</div><div style="font-weight:600;color:#0D2B4E">{v}</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Revenue Opportunity")
        data2 = [("Year 1 ACV","$500K–$1.5M"),("Year 2 ACV","$1.5M–$3.5M"),("Year 3 ACV","$3M–$8M"),("3-Year TCV","$5M–$13M"),("Primary Driver","Platform + Native App/Marketplace consumption"),("Upside","Each bank client = downstream Snowflake customer"),("Deal Risk","Medium — no active RFP"),("Competition","Databricks, MS Fabric, AWS native tools"),]
        for k, v in data2:
            st.markdown(f"""<div style="display:flex;gap:12px;padding:8px;border-bottom:1px solid #E2E8F0;font-size:13px">
<div style="width:160px;color:#718096;flex-shrink:0">{k}</div><div style="font-weight:600;color:#0D2B4E">{v}</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="callout-blue" style="margin-top:12px">
<strong>Network Effect:</strong> Every AML RightSource client bank that adopts the Snowflake-powered advisory model is a potential new Snowflake FSI customer — exponential pipeline impact.
</div>""", unsafe_allow_html=True)
    notes_comments_block("s02")

# ── SECTION 03 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[2]:
    st.markdown("""<div class="section-hero"><h1>03 — Stakeholders Engaged</h1><p>Names, titles, email estimates, and focus priorities for each stakeholder.</p></div>""", unsafe_allow_html=True)

    stakeholders = [
        ("AM","Abhishek Mittal","EVP & Chief Product and AI Officer","abhishek.mittal@amlrightsource.com (est.)","Champion · Sponsor · Technical Buyer","tag-green","Enterprise AI/data transformation mandate, board-level accountability, PE value creation. Deeply technical — asks probing architecture questions. Has executive authority. Key champion across all three tracks."),
        ("SC","Sabrina Chen","Head of Analytics Practice, FCA","sabrina.chen@amlrightsource.com (est.)","User Champion · Influencer","tag-blue","Reducing ETL friction in model validation and advisory analytics. Wants hands-on sandbox access before committing. Must see real-world improvement in the iterative model tuning cycle."),
        ("DL","David Lutz","Associate Director, Financial Crimes Advisory","david.lutz@amlrightsource.com (est.)","User Champion · Influencer","tag-blue","Delivery quality and efficiency on FCA advisory engagements. Understands data governance and access control workflows. Day-to-day SME for Track 1."),
        ("JM","Jonathan McIsaac","Global SVP, Head Client Operations","jonathan.mcisaac@amlrightsource.com (est.)","Business Buyer · Influencer","tag-orange","14 years at AML RS — institutional memory. Owns the large internal operational data asset (Track 2). Needs to see how Snowflake can surface benchmarking intelligence without exposing client PII."),
        ("IY","Isabel Yeung","VP Tech Operations (BloomBrella)","isabel.yeung@amlrightsource.com (est.)","Technical Buyer · User Champion","tag-purple","Building data products and scoring algorithms. Former BloomBrella (~15 yrs). Track 3 owner. Interested in Native App Framework, IP protection, deployment acceleration."),
    ]

    for initials, name, title, email, roles, role_tag, notes in stakeholders:
        with st.expander(f"**{name}** — {title}"):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"""<div style="background:linear-gradient(135deg,#29B5E8,#0D2B4E);color:white;border-radius:50%;width:60px;height:60px;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;margin:0 auto 12px">{initials}</div>
<div style="text-align:center;font-size:12px;color:#718096">{email}</div>
<div style="text-align:center;margin-top:8px">{''.join(f'<span class="tag {role_tag}">{r.strip()}</span>' for r in roles.split('·'))}</div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"**Focus Priorities:** {notes}")

    st.markdown("""<div class="callout-orange">
<strong>⚠ Missing Stakeholders:</strong> CFO (economic buyer) not yet engaged. CISO/IT security not identified. Both required for contracting. AE Action: Ask Abhishek "Who would need to sign a Snowflake contract?"
</div>""", unsafe_allow_html=True)
    notes_comments_block("s03")

# ── SECTION 04 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[3]:
    st.markdown("""<div class="section-hero"><h1>04 — Company Priorities</h1><p>The strategic imperatives driving every technology decision at AML RightSource.</p></div>""", unsafe_allow_html=True)

    priorities = [
        ("🏗️","Platform Transformation","Transition from manual, analyst-heavy service delivery to a technology-native, AI-augmented compliance intelligence platform. Every strategic investment is evaluated against 'does this accelerate our platform journey?'"),
        ("⚡","Time-to-Value Compression","Client onboarding cycles for advisory engagements currently take weeks due to manual data collection, ETL, and normalization. Leadership target: compress to days. Snowflake's zero-copy sharing is a direct enabler."),
        ("🤖","AI & ML Productization","Isabel's team is building scoring algorithms, case prioritization models, and QA automation logic. The priority is to get these deployed into client environments at scale without creating per-client integration overhead."),
        ("📊","Data Monetization","AML RightSource possesses a rare aggregate view of AML/BSA process and outcomes data across 200+ FIs. Board-level priority: convert this asset into a monetizable benchmark intelligence product."),
        ("🔒","Regulatory & Security Confidence","All technology decisions must clear security and compliance review at client financial institutions. Platform must support FedRAMP, SOC 2 Type II, and data residency requirements."),
        ("🌐","Competitive Differentiation","Growing competition from RegTech startups and Big 4 advisory firms. AML RS needs a technology-led, defensible moat. AI + data network effects are the strategy."),
    ]
    c1, c2 = st.columns(2)
    for i, (icon, title, desc) in enumerate(priorities):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""<div class="card"><div class="card-title">{icon} {title}</div><div style="font-size:13px;color:#4A5568">{desc}</div></div>""", unsafe_allow_html=True)
    notes_comments_block("s04")

# ── SECTION 05 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[4]:
    st.markdown("""<div class="section-hero"><h1>05 — Company Profile & Financials</h1><p>Estimated financial profile for internal sizing and business case development.</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> AML RightSource is privately held and PE-backed. No public 10-K. All financial estimates are based on employee count, client base, and comparable RegTech/managed services firms. Treat as internal estimates only.</div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Company Overview")
        for k, v in [("Founded","~2004 (Cincinnati, OH origins)"),("HQ","Overland Park, KS"),("Ownership","Private — PE backed"),("PE Sponsors","Gridiron Capital + Clarion Capital Partners"),("Employees","~1,200–1,500 (post-BloomBrella)"),("Clients","200+ FIs globally"),("Key Acquisitions","BloomBrella (3P risk mgmt, ~2023–24)"),("Core Services","AML/BSA managed services, advisory, due diligence"),]:
            st.markdown(f"""<div style="display:flex;gap:12px;padding:8px;border-bottom:1px solid #E2E8F0;font-size:13px"><div style="width:160px;color:#718096;flex-shrink:0">{k}</div><div style="font-weight:600;color:#0D2B4E">{v}</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Estimated Financial Profile")
        for k, v in [("Est. Revenue (2025)","$150M–$250M ARR"),("Revenue Model","Subscription + T&M advisory + project fees"),("Est. EBITDA Margin","15–22%"),("Growth Rate","Est. 15–25% YoY"),("PE Exit Horizon","2–4 years (creates urgency for tech transformation)"),("Tech Budget (Est.)","$15M–$30M annually"),]:
            st.markdown(f"""<div style="display:flex;gap:12px;padding:8px;border-bottom:1px solid #E2E8F0;font-size:13px"><div style="width:200px;color:#718096;flex-shrink:0">{k}</div><div style="font-weight:600;color:#0D2B4E">{v}</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="callout-green" style="margin-top:12px">
<strong>PE Value Creation:</strong> A services firm exits at 8–10× EBITDA. A data/SaaS firm exits at 15–25× ARR. Snowflake enables new recurring data product revenue — fundamentally shifting the exit multiple and enterprise value.
</div>""", unsafe_allow_html=True)
    notes_comments_block("s05")

# ── SECTION 06 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[5]:
    st.markdown("""<div class="section-hero"><h1>06 — Business Units</h1><p>Three distinct business lines with different Snowflake use cases and timelines.</p></div>""", unsafe_allow_html=True)

    bus = [
        ("#29B5E8","BU 1 — Managed Services","Jonathan McIsaac","Core AML/BSA managed services — providing banks with outsourced transaction monitoring, alert review, case management, and SAR filing. Primary revenue driver, 200+ FI clients, thousands of analysts.","Internal benchmarking intelligence, operational analytics, AI-augmented alert triage.","Moderate","Track 2"),
        ("#00C96F","BU 2 — Financial Crimes Advisory (FCA)","Sabrina Chen + David Lutz","Project-based advisory engagements — model validation, AML program assessments, algorithm tuning, regulatory remediation. Highest-margin product line.","ETL-free data access, secure data sharing, collaborative model environment. FASTEST TIME TO VALUE.","High","Track 1 — PRIMARY FOCUS"),
        ("#FF7A00","BU 3 — Blue Umbrella (Third-Party Due Diligence)","Isabel Yeung","Third-party risk management due diligence — acquired BloomBrella. Isabel has 15 years experience. Building scoring algorithms and data products.","Algorithm deployment via Native App, data product monetization via Marketplace, scoring engine infrastructure.","Medium-Long","Track 3"),
    ]
    for color, name, owner, what, relevance, ttv, track in bus:
        st.markdown(f"""<div class="card" style="border-left:4px solid {color}">
<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
<div style="font-size:15px;font-weight:700;color:#0D2B4E">{name}</div>
<span class="tag tag-blue">{track}</span></div>
<div style="font-size:12px;color:#718096;margin-bottom:6px"><strong>Owner:</strong> {owner} &nbsp;|&nbsp; <strong>Time to Value:</strong> {ttv}</div>
<div style="font-size:13px;color:#4A5568;margin-bottom:8px"><strong>What they do:</strong> {what}</div>
<div style="font-size:13px;color:#065F46"><strong>Snowflake Relevance:</strong> {relevance}</div>
</div>""", unsafe_allow_html=True)
    notes_comments_block("s06")

# ── SECTION 07 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[6]:
    st.markdown("""<div class="section-hero"><h1>07 — Market Headwinds & Tailwinds</h1><p>External forces accelerating or complicating the deal.</p></div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🌬️ Tailwinds (Opportunity Accelerators)")
        for t in ["**Regulatory Escalation:** FinCEN's AML Act of 2020, increased BSA enforcement, and beneficial ownership requirements driving banks to spend more on compliance infrastructure.",
                  "**AI Mandate in Compliance:** Federal regulators explicitly encouraging supervised ML in AML/transaction monitoring.",
                  "**Analyst Shortage:** AML analyst turnover 30–40% annually; labor cost inflation makes automation a financial necessity.",
                  "**FSI Ecosystem:** 10 of 12 largest US banks already on Snowflake — strongest possible proof for bank-facing use cases.",
                  "**RegTech Market Growth:** Global RegTech market growing at 22%+ CAGR.",
                  "**Core Banking on Cloud:** Fiserv, FIS, Jack Henry all building Snowflake data sharing capabilities."]:
            st.markdown(f"""<div style="padding:8px 12px;background:#E6FBF3;border-radius:8px;margin-bottom:6px;font-size:13px">✅ {t}</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("#### ⚡ Headwinds (Deal & Execution Risks)")
        for t in ["**Bank Infosec/Procurement Cycles:** Even after AML RS decides, each bank client may need their own Snowflake evaluation — adding 3–9 months to Track 1 deployment.",
                  "**No Active RFP/Urgency:** AML RS is exploring, not in a defined evaluation. AE must create urgency around PE exit timeline.",
                  "**Internal Bandwidth:** AML RS team is capacity-constrained running existing client engagements.",
                  "**Competition — Databricks:** Strong ML narrative, Python-native — resonates with Isabel's engineering team.",
                  "**Competition — Microsoft Fabric:** Mid-tier banks with heavy Microsoft footprint may default to Fabric.",
                  "**Budget Timing:** PE-backed companies run tight budget cycles — must align pilot completion with budget approval."]:
            st.markdown(f"""<div style="padding:8px 12px;background:#FEF2F2;border-radius:8px;margin-bottom:6px;font-size:13px">⚠️ {t}</div>""", unsafe_allow_html=True)
    notes_comments_block("s07")

# ── SECTION 08 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[7]:
    st.markdown("""<div class="section-hero"><h1>08 — Leadership, Org Chart & Power Center Analysis</h1><p>Decision-making structure and influence map.</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-orange"><strong>Note:</strong> Org chart is estimated from meeting transcript and standard PE-backed managed services firm structures. Validate with Abhishek in next call.</div>""", unsafe_allow_html=True)

    st.markdown("#### Power Center Analysis")
    st.markdown("""
| Stakeholder | Power Level | Buy-In Status | Snowflake Risk | Action Required |
|---|---|---|---|---|
| Abhishek Mittal | 🔴 Very High | 🟢 Champion | 🟢 Low | Keep enabled; feed internal business case content |
| Jonathan McIsaac | 🟠 High | 🟡 Evaluating | 🟡 Medium | Separate discovery call on Track 2 — urgent |
| Isabel Yeung | 🟡 Medium-High | 🔵 Technical Curiosity | 🟡 Medium | Native App demo + Jordan technical deep-dive |
| Sabrina Chen | 🟡 Medium | 🟡 Needs Proof | 🟡 Medium | Hands-on sandbox access — most critical immediate action |
| David Lutz | 🟡 Medium | 🟢 Supportive | 🟢 Low | Keep close to pilot planning |
| CFO [TBD] | 🔴 Very High | 🔴 Not Engaged | 🔴 High | Must identify and engage — economic buyer gap is critical |
| CISO/CTO [TBD] | 🟠 High | 🔴 Not Engaged | 🔴 High | Snowflake security package required for contracting |
""")
    notes_comments_block("s08")

# ── SECTION 09 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[8]:
    st.markdown("""<div class="section-hero"><h1>09 — Stakeholder Map</h1><p>Full stakeholder engagement matrix with communication strategy.</p></div>""", unsafe_allow_html=True)

    st.markdown("""
| Name | Title | Track | Role in Deal | Priority Concern | Communication Approach |
|---|---|---|---|---|---|
| Abhishek Mittal | EVP, CPAIO | All 3 | Executive Champion | Platform ROI, board visibility | Executive briefing, joint business case, Snowflake exec alignment |
| Jonathan McIsaac | Global SVP, Client Ops | Track 2 | Data asset owner | Monetize/leverage internal data | Discovery call, data architecture conversation |
| Isabel Yeung | VP Tech Ops | Track 3 | Technical evaluator | Dev velocity, IP protection | Jordan-led technical call, Native App deep-dive |
| Sabrina Chen | Head Analytics, FCA | Track 1 | User champion | ETL reduction, platform ease | Hands-on sandbox, AE-supported demo walkthrough |
| David Lutz | Assoc. Director, FCA | Track 1 | User champion | Data governance, workflow | Regular check-ins, pilot planning participation |
| CFO [TBD] | Chief Financial Officer | All 3 | Economic buyer | ROI, budget allocation | Executive ROI deck, consumption pricing, PE narrative |
""")
    notes_comments_block("s09")

# ── SECTION 10 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[9]:
    st.markdown("""<div class="section-hero"><h1>10 — IT & Data Spending Estimates</h1><p>Estimated technology budget and current stack analysis.</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> All spending estimates derived from comparable managed services/RegTech firms. Not confirmed — use for internal sizing only.</div>""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (label, val, sub) in zip([c1,c2,c3,c4],[("Total IT Budget (Est.)","$15M–$30M","~8–12% of estimated revenue"),("Data Infrastructure","$3M–$7M","Storage, cloud compute, ETL tooling"),("Analytics/BI Tools","$500K–$1.5M","BI, reporting, dashboard tools"),("AI/ML Investment","$2M–$5M","Growing rapidly; board priority")]):
        with col:
            st.markdown(f"""<div class="card" style="text-align:center"><div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#29B5E8;margin-bottom:6px">{label}</div><div style="font-size:22px;font-weight:900;color:#0D2B4E">{val}</div><div style="font-size:11px;color:#718096;margin-top:4px">{sub}</div></div>""", unsafe_allow_html=True)

    st.markdown("#### Current Technology Stack (Estimated)")
    st.markdown("""
| Category | Likely Current Tool | Snowflake Displacement? | Notes |
|---|---|---|---|
| Cloud Provider | AWS and/or Azure | No — Snowflake runs on both | Cloud-agnostic, no migration risk |
| Data Warehouse | Redshift / Azure Synapse | ✅ Yes — direct displacement | ETL/ELT complexity, scaling limits |
| ETL/Pipeline | Talend, dbt, Python scripts | Partial — Snowflake reduces ETL burden | Data sharing eliminates most client ETL |
| BI/Reporting | Power BI / Tableau | No — Snowflake integrates natively | Snowflake as backend, existing BI on top |
| ML Platform | Python/Jupyter, possibly SageMaker | Partial — Snowpark + Cortex compete | Snowpark ML, Cortex AI native |
| File Sharing | Secure FTP, SharePoint, email | ✅ Yes — core displacement | Snowflake Data Sharing eliminates FTP workflows |
""")
    notes_comments_block("s10")

# ── SECTION 11 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[10]:
    st.markdown("""<div class="section-hero"><h1>11 — Data Sources</h1><p>All known data sources across AML RightSource's business units.</p></div>""", unsafe_allow_html=True)

    st.markdown("""
| # | Data Source | Origin | Business Unit | Currently Stored In |
|---|---|---|---|---|
| 1 | TM Alert Data | Client banks (core banking / TMS) | FCA Advisory + Managed Services | Client-side; manually exported per engagement |
| 2 | KYC / CDD Data | Client banks (onboarding systems) | FCA Advisory + Managed Services | Client-side; encrypted export per engagement |
| 3 | SAR Data | Client banks + FinCEN | Managed Services | Secure internal repositories |
| 4 | Case Management / Operational Data | Internal AML RightSource systems | Managed Services (Jonathan) | Internal case management platforms (not on Snowflake) |
| 5 | AML Model / Algorithm Output Data | Internal — Isabel's team | Blue Umbrella / Product | Python environments, model serving infrastructure |
| 6 | Third-Party Risk / Due Diligence Data | Public records, Experian, sanctions | Blue Umbrella | BloomBrella legacy systems, data vendor APIs |
| 7 | Benchmarking / Aggregate Process Data | Synthesized from 200+ client engagements | All — Jonathan leads | Fragmented; no unified warehouse today |
| 8 | Regulatory Reference Data | FinCEN, OFAC, FATF, state regulators | All | Manual downloads, shared drives |
| 9 | Client Onboarding Data | New advisory client data requests | FCA Advisory | Email, secure FTP, SharePoint — highly manual |
| 10 | Analyst Performance / Workflow Data | Internal ticketing/workflow systems | Managed Services | Internal ITSM / workflow tools |
""")
    notes_comments_block("s11")

# ── SECTION 12 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[11]:
    st.markdown("""<div class="section-hero"><h1>12 — Estimated Data Volumes</h1><p>Volume estimates by data source — drives Snowflake sizing and ROI models.</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> All volume estimates based on industry benchmarks for comparable AML/BSA programs at 200+ mid-tier FIs. Validate with Abhishek/Jonathan/Isabel during discovery.</div>""", unsafe_allow_html=True)

    st.markdown("""
| Data Source | Est. Volume (Current) | Growth Rate | Est. Snowflake Storage | Key Considerations |
|---|---|---|---|---|
| TM Alert Data | 50M–200M records/year | 15–20% YoY | 2–8 TB/year | Each bank = 50K–500K alerts/month avg |
| KYC / CDD Data | 10M–50M records | 10% YoY | 1–4 TB | Mixed structured + unstructured (PDFs, IDs) |
| SAR Data | Hundreds of thousands/year | 5–10% YoY | 100–500 GB/year | Semi-structured, contains PII |
| Case Management (Internal) | 1M–5M cases historically | 10–15% YoY | 500GB–2TB total | Jonathan's crown jewel — not yet in data platform |
| Model Outputs | Millions of scored records/month | 30–50% YoY | 1–3 TB/year | High growth as AI products scale |
| 3P Risk / Due Diligence | 500K–2M entity records | 20% YoY | 500GB–1.5TB | BloomBrella legacy migration needed |
| Benchmarking / Aggregate | 10–20 years of historical data | Steady | 2–5 TB (historical) | Highest strategic value for monetization |
| **Totals (Estimated)** | — | — | **8–25 TB Year 1 / 30–60 TB Year 3** | Growing with AI/ML output volumes |
""")
    notes_comments_block("s12")

# ── SECTION 13 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[12]:
    st.markdown("""<div class="section-hero"><h1>13 — Current Challenges & Downstream Impact</h1><p>Pain by data source and its business consequence.</p></div>""", unsafe_allow_html=True)

    challenges = [
        ("TM Alert / Client Data","Manual data requests per engagement: email → secure FTP → normalization → ETL. Takes days to weeks per client per project.","Advisory engagements start late, cost more (labor), client satisfaction suffers. Analysts spend 40–60% of engagement time on data prep vs. analysis."),
        ("KYC / CDD Data","Data arrives in disparate formats (CSVs, Excel, PDFs, API dumps). Each bank has different table structures — requires custom normalization per client.","Scaling advisory beyond current client count is structurally constrained. Each new client adds linear cost rather than marginal cost."),
        ("Case Management (Internal)","Valuable operational data across 200+ clients sits in siloed systems with no unified analytics layer. Jonathan cannot easily produce cross-client benchmarks.","AML RightSource is sitting on a $50M+ potential data asset that is currently generating $0 in revenue. Missed product opportunity."),
        ("Model / Algorithm Outputs","Isabel's team builds models in isolated environments; deploying logic into client systems requires custom per-client integrations. No standard deployment framework.","Each algorithm deployment is a 3–6 month custom project. Revenue from data products is capped by deployment capacity."),
        ("Benchmarking / Aggregate Data","No unified view of cross-client data. Each BU has its own siloed data. Benchmarking requires manual assembly by senior analysts.","Cannot offer clients real-time performance benchmarking vs. peers. Industry peers (Quantifind, NICE Actimize) already offer benchmark products."),
    ]
    for source, challenge, impact in challenges:
        st.markdown(f"""<div class="card">
<div class="card-title">📁 {source}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px">
<div style="background:#FEF2F2;border-radius:8px;padding:10px;font-size:13px"><strong style="color:#991B1B">Current Challenge:</strong><br>{challenge}</div>
<div style="background:#FFF8E6;border-radius:8px;padding:10px;font-size:13px"><strong style="color:#92400E">Downstream Impact:</strong><br>{impact}</div>
</div></div>""", unsafe_allow_html=True)
    notes_comments_block("s13")

# ── SECTION 14 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[13]:
    st.markdown("""<div class="section-hero"><h1>14 — Use Cases by Data Source</h1><p>Mapping Snowflake use cases to each data source.</p></div>""", unsafe_allow_html=True)

    st.markdown("""
| Data Source | Snowflake Use Cases | Track | Priority |
|---|---|---|---|
| TM Alert Data | Alert triage model validation; real-time alert scoring; false positive reduction; Cortex AI investigation assistant | Track 1, 3 | 🔴 High |
| KYC / CDD Data | Customer risk scoring; adverse media enrichment via Marketplace; identity verification; KYC refresh automation | Track 1, 3 | 🔴 High |
| SAR Data | SAR narrative generation (Cortex AI); pattern recognition; filing quality scoring | Track 1 | 🟠 Medium |
| Case Management | Cross-client benchmarking; process analytics; peer performance intelligence; SLA monitoring; staffing optimization | Track 2 | 🔵 Strategic |
| Model/Algorithm Outputs | Native App deployment; algorithm marketplace distribution; client-side scoring without data movement; model versioning | Track 3 | 🟠 Medium-High |
| 3P Risk / Due Diligence | Entity resolution; corporate graph analytics; sanctions screening; third-party risk scores as data product | Track 3 | 🟠 Medium |
| Benchmarking Data | Anonymized peer benchmarking product; Data Marketplace listing; aggregate intelligence product | Track 2 | 🔵 Highest Revenue Potential |
| Regulatory Reference | Snowflake Marketplace OFAC/FinCEN feeds; automated sanctions refresh | All Tracks | 🟠 Medium |
""")
    notes_comments_block("s14")

# ── SECTION 15 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[14]:
    st.markdown("""<div class="section-hero"><h1>15 — Focused Use Cases</h1><p>The three use cases we are actively pursuing with AML RightSource.</p></div>""", unsafe_allow_html=True)

    use_cases = [
        ("#29B5E8","🔍","UC-1: Advisory Intelligence","ETL-Free Client Data Collaboration","Track 1 · Sabrina Chen + David Lutz · Fastest Time to Value","AML RightSource advisory engagements require banks to share TM, KYC, and lookback data for model validation and program assessments. Today this is done via secure FTP, SharePoint, or email — taking days to weeks. Snowflake's zero-copy data sharing eliminates this: banks expose a read-only share, AML RightSource runs advisory analysis without moving any data. Engagement time-to-start drops from 2–3 weeks to 24–48 hours.",["Engagement time-to-start: 2–3 weeks → 24–48 hours","Analyst data prep time: 40–60% → <10% of engagement","Scale 2–3x advisory engagements without adding headcount"]),
        ("#00C96F","📊","UC-2: Data Assets","Cross-Client Benchmarking Intelligence Platform","Track 2 · Jonathan McIsaac · High Strategic Value","Jonathan's operations team manages aggregate AML process data across 200+ FIs — case resolution rates, false positive rates, analyst productivity metrics, SAR volumes. Unified on Snowflake and appropriately anonymized, this represents a category-defining benchmark intelligence product no competitor can replicate. Banks would pay meaningful SaaS fees for real-time peer benchmarking.",["New recurring data product revenue stream ($5–15M ARR potential)","Marketplace listing accessible to 10,000+ potential FSI Snowflake customers","Strengthens advisory value prop with data-driven benchmarking"]),
        ("#FF7A00","⚙️","UC-3: Algorithms","Native App–Powered Algorithm Deployment","Track 3 · Isabel Yeung · High Growth Potential","Isabel's engineering team is building proprietary AML scoring algorithms, case prioritization models, and QA automation logic. Today deploying these into a client environment requires a multi-month custom integration. Snowflake's Native App Framework changes this: AML RightSource packages algorithms as a Native App, banks install it with one click — running the algorithm on their data, inside their Snowflake environment, with full IP protection.",["Algorithm deployment: 3–6 months/client → days","Create scalable recurring revenue model from IP (SaaS subscriptions)","IP fully protected — clients cannot see or extract algorithm logic"]),
    ]
    for color, icon, name, subtitle, meta, desc, outcomes in use_cases:
        st.markdown(f"""<div class="card" style="border-top:4px solid {color}">
<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
<span style="font-size:28px">{icon}</span>
<div><div style="font-size:16px;font-weight:800;color:#0D2B4E">{name}: {subtitle}</div>
<div style="font-size:12px;color:{color};font-weight:600">{meta}</div></div>
</div>
<p style="font-size:13px;color:#4A5568;margin-bottom:10px">{desc}</p>
<div style="display:grid;grid-template-columns:{'1fr '*len(outcomes)};gap:8px">
{"".join(f'<div style="background:#E6FBF3;border-radius:8px;padding:8px 10px;font-size:12px;color:#065F46">✅ {o}</div>' for o in outcomes)}
</div></div>""", unsafe_allow_html=True)
    notes_comments_block("s15")

# ── SECTION 16 ────────────────────────────────────────────────────────────────
elif selected == SECTIONS[15]:
    st.markdown("""<div class="section-hero"><h1>16 — MEDDPICC Analysis</h1><p>Detailed qualification across all three use cases with gaps and assumptions flagged.</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="callout-blue">
<strong>Legend:</strong> 🟡 = Assumption used (not confirmed) &nbsp;|&nbsp; 🔴 = Gap — action required &nbsp;|&nbsp; 🟢 = Confirmed
</div>""", unsafe_allow_html=True)

    uc_sel = st.radio("Select Use Case", ["UC-1: Advisory","UC-2: Data Assets","UC-3: Algorithms"], horizontal=True)

    if "Advisory" in uc_sel:
        medd = [
            ("M","Metrics","Advisory engagement time-to-start: 2–3 weeks → 24–48 hours (85%+ reduction). Analyst data prep time: 40–60% → <10% of engagement. Advisory engagements per analyst per quarter: 2× increase.","🟡 % of engagement time on data prep estimated from comparable AML advisory firms. Confirm with Sabrina/David during pilot scoping.","assumption"),
            ("E","Economic Buyer","Abhishek Mittal (CPAIO) has budget authority for technology platform decisions. CFO approval likely required for contracts >$250K.","🔴 CFO not identified or engaged. Ask Abhishek: 'Who would be required to sign the final contract?'","gap"),
            ("D","Decision Criteria","(1) Security certs meet FSI requirements. (2) Ease of use for advisory analysts. (3) Reduction in time-to-data. (4) Consumption-based pricing aligns with project-based revenue model.","🟡 Decision criteria inferred from meeting transcript. No formal RFP or scorecard shared.","assumption"),
            ("D","Decision Process","Pilot → Internal evaluation → Business case to Abhishek → CFO/PE board approval → Contract.","🔴 Formal decision process not documented. AE should ask: 'If we delivered a successful pilot in 60 days, what would the path to contract signature look like?'","gap"),
            ("P","Paper Process","NDA signed ✅. MSA and Order Form standard Snowflake process. PE-backed firms typically require legal review and finance sign-off. Est. 30–60 days from pilot readout to signature.","🟡 Paper process timeline estimated from comparable PE-backed deals.","assumption"),
            ("I","Identify Pain","Manual FTP/email data sharing. Data normalization per client takes days. Engagements start late. Analysts over-indexed on data prep vs. analysis.","🟢 Pain clearly identified and verbalized by Sabrina, David, and Abhishek in April 29 meeting.","confirmed"),
            ("C","Champion","Abhishek Mittal is the primary champion. Has executive authority, strategic mandate, and clear motivation. Engaged across all three tracks.","🔴 Champion has not explicitly said 'I will sponsor this internally.' AE should ask: 'What would you need from us to make the internal business case?'","gap"),
            ("C","Competition","Primary: Databricks (strong ML narrative). Secondary: MS Fabric. Tertiary: Building in-house on AWS native tooling.","🟡 Competition not directly stated in transcript. AE should ask: 'Are you evaluating any other platforms in parallel?'","assumption"),
        ]
    elif "Data Assets" in uc_sel:
        medd = [
            ("M","Metrics","New product revenue from benchmark data product: $2–10M ARR potential. Current benchmark product revenue: $0. Time to produce cross-client benchmarking report: days (manual) → minutes (automated).","🟡 Revenue potential estimated based on comparable benchmarking data products in FSI. Must validate with Jonathan.","assumption"),
            ("I","Identify Pain","Abhishek confirmed: 'John has a huge data asset internally. It's not on Snowflake. There's an opportunity in process insights, benchmarking, operational data.'","🔴 Jonathan has NOT independently confirmed his pain or urgency. Separate discovery call with Jonathan is #1 priority action for Track 2.","gap"),
            ("E","Economic Buyer","Jonathan McIsaac as SVP likely has limited budget authority for new platform investments. Routes to Abhishek and CFO.","🔴 Economic buyer for a new data product initiative not confirmed.","gap"),
            ("C","Champion","Jonathan McIsaac is a strong candidate champion for Track 2 — 14 years tenure, institutional ownership of the data asset. Not yet deeply engaged.","🔴 Champion for Track 2 not yet secured. AE action: schedule dedicated discovery call with Jonathan before next group meeting.","gap"),
            ("D","Decision Process","Track 2 is likely 3–6 months behind Track 1 in maturity. Jonathan needs a discovery call before this can progress.","🟡 Timeline estimated. Jonathan's priorities and urgency not yet confirmed.","assumption"),
            ("D","Decision Criteria","Not yet established for Track 2. Likely: ease of data migration, anonymization approach, time to first benchmark product.","🔴 Must be established in Jonathan discovery call.","gap"),
            ("P","Paper Process","Same as UC-1 — Snowflake MSA. Track 2 would likely be included in same contract as Track 1.","🟡 Assumption — contracting approach not confirmed.","assumption"),
            ("C","Competition","Less direct competition for the benchmarking product concept. Main risk is 'do nothing' or in-house build.","🟡 Competitive landscape for Track 2 not assessed.","assumption"),
        ]
    else:
        medd = [
            ("M","Metrics","Algorithm deployment time: 3–6 months/client → days. Revenue per algorithm as SaaS vs. one-time consulting fees: 5–10× improvement in LTV.","🟡 Deployment timeline estimated. Isabel needs to validate in technical discovery call.","assumption"),
            ("I","Identify Pain","Abhishek: 'If I have built some logic and I want to deploy that logic in a client's environment, is it a faster path for us to deploy those through you guys?' Isabel confirmed algorithm product roadmap.","🟡 Current deployment friction is manually intensive. Must confirm with Isabel how algorithms are currently deployed.","assumption"),
            ("D","Decision Process","Isabel's engineering team evaluates technically, Abhishek approves platform decision, CFO/legal signs contract. Track 3 likely 6–12 months behind Track 1.","🔴 Isabel's product roadmap timeline not known. Technical discovery call with Isabel and Jordan is critical.","gap"),
            ("C","Competition","Databricks MLflow + Unity Catalog is direct competition for algorithm deployment. Isabel's team is likely Python-heavy.","🔴 Must understand Isabel's current technical stack and whether Databricks is already in the picture.","gap"),
            ("E","Economic Buyer","Same as other tracks — Abhishek/CFO. Isabel likely has engineering budget but not platform investment authority.","🟡 Budget authority not confirmed for product roadmap investments.","assumption"),
            ("P","Paper Process","Would be included in same Snowflake contract as Tracks 1/2. Native App development would require Professional Services engagement.","🟡 PSO scope and pricing not yet discussed.","assumption"),
            ("C","Champion","Isabel Yeung is the Track 3 champion candidate. Not yet deeply engaged — needs Jordan-led technical call.","🔴 Isabel champion status not confirmed. Technical call required.","gap"),
            ("D","Decision Criteria","Not yet established. Likely: Snowpark Python compatibility with existing code, IP protection validation, marketplace distribution reach.","🔴 Must be established in Isabel technical discovery call.","gap"),
        ]

    c1, c2 = st.columns(2)
    for i, (letter, word, content, flag, flag_type) in enumerate(medd):
        flag_bg = {"assumption":"#EDE9FE","gap":"#FFF8E6","confirmed":"#E6FBF3"}[flag_type]
        flag_color = {"assumption":"#5B21B6","gap":"#92400E","confirmed":"#065F46"}[flag_type]
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""<div class="medd-card">
<div style="display:flex;align-items:baseline;gap:8px;margin-bottom:4px">
<span class="medd-letter">{letter}</span>
<span class="medd-word">{word}</span>
</div>
<div style="font-size:13px;color:#4A5568;margin-bottom:8px">{content}</div>
<div style="background:{flag_bg};border-radius:6px;padding:8px 10px;font-size:12px;color:{flag_color}">{flag}</div>
</div>""", unsafe_allow_html=True)
    notes_comments_block("s16")

# ── SECTIONS 17–19 ────────────────────────────────────────────────────────────
elif selected == SECTIONS[16]:
    st.markdown("""<div class="section-hero"><h1>17 — Why These Use Cases Matter</h1><p>Business justification for each use case prioritization.</p></div>""", unsafe_allow_html=True)
    for color, title, body in [
        ("#29B5E8","Advisory (UC-1): Mission-Critical Revenue Enablement","Advisory engagements are AML RightSource's highest-margin product line. Every week shaved off an engagement start time is direct margin improvement. More importantly, if AML RightSource can deliver advisory projects 2× faster at the same quality — enabled by Snowflake — they can take on more clients with the same headcount, fundamentally changing unit economics and unlocking revenue growth without proportional headcount growth."),
        ("#00C96F","Data Assets (UC-2): New $10M+ Revenue Category","AML RightSource's aggregate view across 200+ banks is an asset no competitor can replicate. Building a benchmarking intelligence product on Snowflake creates a new recurring SaaS revenue stream that dramatically increases company valuation ahead of the PE exit. A company with recurring data product revenue commands a fundamentally different multiple than a services-only firm — this is a PE board-level priority."),
        ("#FF7A00","Algorithms (UC-3): Product-Led Growth at Scale","Isabel's algorithm roadmap is the company's future as an AI-native intelligence firm. Without Snowflake's Native App framework, each deployment is a bespoke consulting project. With Native Apps + Marketplace, AML RightSource transforms from a services firm into a SaaS product company — the difference between a 3× and 15× revenue multiple at exit."),
    ]:
        st.markdown(f"""<div class="card" style="border-top:3px solid {color}"><div class="card-title">{title}</div><p style="font-size:13px;color:#4A5568">{body}</p></div>""", unsafe_allow_html=True)
    notes_comments_block("s17")

elif selected == SECTIONS[17]:
    st.markdown("""<div class="section-hero"><h1>18 — How Snowflake Solves Each Use Case</h1><p>Capability-to-use-case mapping with competitive differentiation.</p></div>""", unsafe_allow_html=True)
    st.markdown("""
| Use Case | Snowflake Capability | How It Works | Differentiation vs. Competition |
|---|---|---|---|
| Advisory (UC-1) | Data Sharing + Clean Rooms + Cortex AI | Bank clients expose read-only share of TM/KYC data from their Snowflake environment. AML RS analysts query in-place — no ETL, no FTP. Cortex AI generates narrative summaries and alert investigation drafts. | Databricks requires data movement. MS Fabric requires Azure. Only Snowflake offers zero-copy sharing across AWS/Azure/GCP with full data residency compliance. |
| Data Assets (UC-2) | Unified Data Platform + Marketplace + Clean Rooms | Migrate Jonathan's internal case management data to Snowflake. Build anonymized analytics layer for cross-client benchmarking. Publish benchmark intelligence product to Snowflake Marketplace — 10,000+ FSI customers. | No other platform offers clean room anonymization + built-in FSI marketplace + governance controls banks require. |
| Algorithms (UC-3) | Native App Framework + Marketplace + Snowpark ML | Isabel's team packages scoring algorithms as Native Apps with Snowpark Python. Bank clients install from Marketplace into their own Snowflake environment — algorithm runs on their data, in their compute, with IP protection. AML RS charges subscription fee per install. | Databricks does not have an equivalent app packaging/distribution model. Native Apps are purpose-built for exactly this use case. 10 of 12 largest US banks already on Snowflake. |
""")
    notes_comments_block("s18")

elif selected == SECTIONS[18]:
    st.markdown("""<div class="section-hero"><h1>19 — Business Impact Measurement</h1><p>KPIs, baselines, and targets for each use case.</p></div>""", unsafe_allow_html=True)
    st.markdown("""
| Use Case | KPI / Metric | Baseline (Current) | Target (12 months) | Business Value |
|---|---|---|---|---|
| UC-1 | Time to first data access | 10–20 days | <48 hours | Earlier starts = earlier revenue recognition |
| UC-1 | % of engagement time on data prep | 40–60% | <10% | 2–3× analyst productivity per engagement |
| UC-1 | Advisory engagements per analyst/quarter | Baseline TBD | +50–100% | Same headcount, more revenue |
| UC-1 | Client NPS for advisory engagements | Baseline TBD | +15–20 points | Improved retention and expansion |
| UC-2 | New benchmarking product ARR | $0 | $1–3M (Year 2) | Net new recurring revenue stream |
| UC-2 | Time to produce cross-client benchmarking report | Days–Weeks (manual) | Minutes (automated) | Enables new product category |
| UC-2 | % of internal data unified on platform | ~0% (fragmented) | 80%+ | Enables AI/ML at scale |
| UC-3 | Algorithm deployment time per client | 3–6 months | <1 week | 10× more deployments with same team |
| UC-3 | Algorithm/product ARR from Native Apps | $0 (project-based) | $500K–$2M (Year 2) | SaaS multiple vs. project multiple |
| UC-3 | Active algorithm installs across client base | 0 | 20–50 (Year 2) | Network effect grows with each install |
""")
    notes_comments_block("s19")

# ── SECTIONS 20–22 ────────────────────────────────────────────────────────────
elif selected == SECTIONS[19]:
    st.markdown("""<div class="section-hero"><h1>20 — Snowflake Capacity Planning</h1><p>Estimated storage, compute, and user requirements by use case.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> All capacity estimates based on data volumes from Section 12 and typical Snowflake consumption for similar FSI workloads. Validate with Jordan during pilot sizing.</div>""", unsafe_allow_html=True)
    st.markdown("""
| Use Case | Storage (Year 1) | Compute (Est. Credits/Month) | Warehouse Size | Concurrent Users | Year 1 Est. Spend |
|---|---|---|---|---|---|
| UC-1: Advisory | 2–5 TB (client data shares; no storage charge for shared data) | 500–1,500 credits/mo | S–M | 10–30 advisory analysts | $75K–$200K/year |
| UC-2: Data Assets | 5–15 TB (internal case management migration) | 1,000–3,000 credits/mo | M–L | 20–50 internal users + client API queries | $150K–$450K/year |
| UC-3: Algorithms | 1–3 TB (algorithm metadata, outputs) | 500–2,000 credits/mo (client compute for installs) | S–M | Engineering team (10–20) + unlimited client installs | $75K–$250K/year |
| **Total (Year 1)** | **8–23 TB** | **2,000–6,500 credits/mo** | — | **50–100 core users** | **$300K–$900K/year** |
""")
    notes_comments_block("s20")

elif selected == SECTIONS[20]:
    st.markdown("""<div class="section-hero"><h1>21 — Investment & ROI (3-Year)</h1><p>Business value quantification and PE exit value creation narrative.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> All ROI figures are estimates built from capacity planning and business impact metrics. Intended for internal AE use in building a CFO-facing business case. Validate assumptions with champion before presenting externally.</div>""", unsafe_allow_html=True)
    st.markdown("#### 3-Year Business Value")
    st.markdown("""
| Value Driver | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Advisory Productivity Gain | $500K–$1M | $1.5M–$3M | $3M–$5M |
| Benchmarking Product Revenue (New) | $0 | $1M–$3M | $3M–$8M |
| Algorithm SaaS Revenue (New) | $0 | $500K–$1.5M | $2M–$5M |
| COGS Reduction (ETL/data ops) | $200K–$500K | $400K–$800K | $600K–$1.2M |
| **Total Business Value** | **$700K–$1.5M** | **$3.4M–$8.3M** | **$8.6M–$19.2M** |
""")
    st.markdown("""<div class="callout-green">
<strong>PE Exit Value Creation:</strong> A managed services firm exits at ~8–10× EBITDA. A data/SaaS firm exits at 15–25× ARR. If AML RightSource builds $5M in new data product ARR on Snowflake by Year 3, and exit multiple improves from 10× to 15× on that incremental ARR, the enterprise value impact is $75M+ — the single most important business case narrative for the CFO and PE board.
</div>""", unsafe_allow_html=True)
    notes_comments_block("s21")

elif selected == SECTIONS[21]:
    st.markdown("""<div class="section-hero"><h1>22 — Migration & Architecture Planning</h1><p>Recommended architecture, migration sequence, and resource estimates.</p></div>""", unsafe_allow_html=True)
    for color, title, period, items in [
        ("#29B5E8","Phase 1: Advisory Foundation","Months 1–3",["Provision AML RightSource Snowflake account (Business Critical edition — FSI compliance)","Set up advisory analytics environment with role-based access for analysts","Pilot: onboard 1–2 bank clients with Snowflake accounts; establish first data share","Stand up Cortex AI capabilities for narrative generation","Baseline metrics: time-to-data, analyst productivity"]),
        ("#00C96F","Phase 2: Data Assets Migration","Months 3–9",["Migrate Jonathan's internal case management data to Snowflake","Build unified analytics layer for cross-client operational data","Implement data anonymization / clean room infrastructure","Build first version of benchmarking intelligence dashboard","Begin Marketplace listing preparation for data product"]),
        ("#FF7A00","Phase 3: Algorithm Productization","Months 6–18",["Isabel's team builds first algorithm as Snowpark Python Native App","Internal testing in dev environment against pilot bank data","Marketplace listing review and certification","Launch to 2–5 pilot bank clients as Native App install","Scale to full client base (Months 12–18)"]),
    ]:
        st.markdown(f"""<div class="card" style="border-left:4px solid {color}">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<div class="card-title">{title}</div><span class="tag tag-blue">{period}</span>
</div>
<ul style="margin:0 0 0 20px;padding:0">
{"".join(f'<li style="font-size:13px;color:#4A5568;margin-bottom:4px">{item}</li>' for item in items)}
</ul></div>""", unsafe_allow_html=True)
    st.markdown("#### Migration Resource & Budget Estimate")
    st.markdown("""<div class="callout-orange"><strong>⚠ Assumption:</strong> Based on comparable FSI/managed services Snowflake implementations. Validate with Snowflake professional services team before sharing with AML RightSource.</div>""", unsafe_allow_html=True)
    st.markdown("""
| Phase | Duration | AML RS Resources | Snowflake Resources | Budget (PSO) |
|---|---|---|---|---|
| Phase 1 — Advisory Pilot | 6–8 weeks | Sabrina (0.5 FTE), David (0.25 FTE), 1 data engineer (0.5 FTE) | Jordan Ude (SE), 1 Snowflake PSO architect (0.25 FTE) | $50K–$100K (optional) |
| Phase 2 — Data Migration | 4–6 months | 1–2 data engineers (1.0 FTE), Jonathan (0.25 FTE) | Snowflake PSO (data migration), SE support | $150K–$300K |
| Phase 3 — Native App Build | 6–12 months | Isabel's engineering team (2–3 engineers), 1 PM | Snowflake Native App specialist, SE support | $100K–$200K |
| **Total (3-year build)** | **12–18 months** | **~4–5 FTE equivalent** | **SE + PSO team** | **$300K–$600K PSO** |
""")
    notes_comments_block("s22")

# ── SECTIONS 23–29 ────────────────────────────────────────────────────────────
elif selected == SECTIONS[22]:
    st.markdown("""<div class="section-hero"><h1>23 — Strategic Execution Analysis</h1><p>Snowflake strengths and key deal risks.</p></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ✅ Snowflake Strengths in This Deal")
        for s in ["**FSI Ecosystem:** 10 of 12 largest US banks already on Snowflake — strongest possible proof for bank-facing use cases","**Native App Framework:** Unique capability with no direct equivalent in Databricks/Fabric — directly addresses Isabel's use case","**Data Clean Rooms:** Industry-standard for double-blind FSI data collaboration — differentiator for Track 2","**Consumption-Based Pricing:** Aligns perfectly with AML RS's project-based revenue model — no waste on idle compute","**Security Posture:** FedRAMP High, SOC 2 Type II, HITRUST — passes bank infosec review","**Eric's Background:** 6+ years of experience with managed application deployments — unique credibility in this exact use case"]:
            st.markdown(f"""<div style="padding:8px 12px;background:#E6FBF3;border-radius:8px;margin-bottom:6px;font-size:13px">✅ {s}</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("#### 🔴 Key Deal Risks")
        for r in ["**No Economic Buyer Engaged:** CFO and PE board are not in the conversation. Without their buy-in, even a successful pilot can stall at contracting.","**No Active RFP/Urgency:** AML RightSource is exploring — not in a defined evaluation. AE must create urgency around the PE exit timeline.","**Bank Client Dependencies (Track 1):** Even after AML RS contracts, getting first bank client on Snowflake is a separate sales motion.","**Databricks Risk (Track 3):** Isabel's engineering team is Python-first — Jordan must run a Native App technical proof before Databricks gets in front of Isabel.","**Internal Bandwidth:** AML RS leadership acknowledged they're busy. Pilot execution requires dedicated internal resources that may be hard to secure."]:
            st.markdown(f"""<div style="padding:8px 12px;background:#FEF2F2;border-radius:8px;margin-bottom:6px;font-size:13px">⚠️ {r}</div>""", unsafe_allow_html=True)
    notes_comments_block("s23")

elif selected == SECTIONS[23]:
    st.markdown("""<div class="section-hero"><h1>24 — Next Actions & Pursuit Strategy</h1><p>Prioritized action list with owners and deadlines.</p></div>""", unsafe_allow_html=True)
    actions = [
        ("🔴","Critical","Kala Boudreaux","Within 1 week","Schedule 30-min discovery call with Jonathan McIsaac — focus: internal data asset, pain points, and benchmarking vision (Track 2)"),
        ("🔴","Critical","Kala + Jordan","Within 1 week","Schedule technical deep-dive with Isabel Yeung + Jordan Ude — Native App Framework walkthrough, current algorithm stack, product roadmap"),
        ("🔴","Critical","Jordan Ude","Within 3 days","Send Sabrina Chen sandbox/trial access to Snowflake with preloaded synthetic AML dataset"),
        ("🟠","High","Kala Boudreaux","Next call with Abhishek","Identify and request intro to CFO — ask: 'As we think about formalizing a Snowflake investment, who would need to be involved?'"),
        ("🟠","High","Kala + Jordan + Eric","Within 2 weeks","Prepare Track 1 POC/Pilot plan — detailed success criteria, synthetic data setup, 60-day timeline"),
        ("🟠","High","Eric Szenderski","Within 1 week","Identify 2–3 Snowflake FSI customers with similar profiles for reference calls"),
        ("🟠","High","Eric Szenderski","Within 2 weeks","Identify mutual Snowflake customers (banks) who are already AML RightSource clients"),
        ("🔵","Medium","Kala Boudreaux","Within 1 week","Prepare and send AML RightSource executive-facing deck with ROI narrative for PE board"),
        ("🔵","Medium","Eric Szenderski","Within 2 weeks","Engage Snowflake FSI vertical team for co-sell support and customer introduction introductions"),
        ("🔵","Medium","Jordan + Deal Desk","Before contracting","Draft Snowflake security and compliance package for AML RightSource infosec/legal review"),
    ]
    for priority, level, owner, deadline, action in actions:
        st.markdown(f"""<div style="display:flex;gap:14px;padding:12px;background:white;border:1px solid #D1E8F5;border-radius:10px;margin-bottom:8px;align-items:flex-start">
<span style="font-size:18px;flex-shrink:0">{priority}</span>
<div style="flex:1">
<div style="font-size:13px;font-weight:600;color:#0D2B4E">{action}</div>
<div style="font-size:11px;color:#718096;margin-top:4px">Owner: <strong>{owner}</strong> &nbsp;|&nbsp; Deadline: <strong>{deadline}</strong> &nbsp;|&nbsp; Priority: <strong>{level}</strong></div>
</div></div>""", unsafe_allow_html=True)
    notes_comments_block("s24")

elif selected == SECTIONS[24]:
    st.markdown("""<div class="section-hero"><h1>25 — Step-by-Step Win Plan</h1><p>What the Snowflake team needs to do to win this deal.</p></div>""", unsafe_allow_html=True)
    steps = [
        ("Land the Sandbox — Immediately","Sabrina Chen said she needs to 'play around and see a significant improvement.' Jordan creates a Snowflake trial environment with preloaded synthetic AML/TM data (realistic to their use case) and sends it to Sabrina and David within 3 business days. This keeps momentum and demonstrates responsiveness."),
        ("Secure Individual Discovery Calls for Tracks 2 & 3","Jonathan McIsaac (Track 2) and Isabel Yeung (Track 3) need dedicated discovery calls before the next group call. Each stakeholder has different priorities — group calls lose these threads. AE schedules these within 1 week."),
        ("Lock in Pilot Success Criteria in Writing","Present a written pilot plan to Abhishek/Sabrina/David with specific, agreed-upon success metrics. 'If we deliver X, Y, Z outcomes in 60 days, will you have what you need to recommend Snowflake?' Getting written sign-off on success criteria eliminates ambiguity and creates a clear conversion event."),
        ("Bring FSI Peer References to Life","Eric's strongest asset is Snowflake's FSI network. Identify 2–3 comparable AML/compliance-focused customers and arrange a reference call within the pilot period. No more powerful sales tool in enterprise FSI than peer credibility."),
        ("Identify and Engage the Economic Buyer (CFO)","Abhishek is the champion, not the economic buyer. Ask directly in the next call: 'Who would need to be involved in approving a Snowflake investment?' Get a name, and ask Abhishek for an introduction during or after the pilot readout."),
        ("Frame the PE Value Creation Story","AML RightSource's PE sponsors have a clear exit mandate. The Snowflake story needs a CFO/PE board narrative: 'Snowflake is not a cost — it's a value creation engine that increases your exit multiple by enabling new recurring data product revenue.'"),
        ("Execute a Flawless 60-Day Pilot","The pilot for Track 1 must be tight (1–2 success criteria max), fast (60 days), and undeniably successful. Jordan leads technical execution; Kala owns stakeholder management; Eric owns executive-level engagement. Formal readout at day 60 with Abhishek present."),
        ("Mobilize Snowflake's FSI Co-Sell Network","Eric has direct relationships with Snowflake's FSI account teams. If AML RightSource's bank clients are already Snowflake customers, those relationships can dramatically accelerate the client-side buy-in needed for Track 1."),
    ]
    for i, (title, desc) in enumerate(steps, 1):
        st.markdown(f"""<div class="step-item">
<div class="step-num">{i}</div>
<div><div style="font-size:14px;font-weight:700;color:#0D2B4E;margin-bottom:4px">{title}</div>
<div style="font-size:13px;color:#4A5568">{desc}</div></div>
</div>""", unsafe_allow_html=True)
    notes_comments_block("s25")

elif selected == SECTIONS[25]:
    st.markdown("""<div class="section-hero"><h1>26 — Path to Contracting</h1><p>Step-by-step contracting timeline from pilot to signature.</p></div>""", unsafe_allow_html=True)
    timeline = [
        ("Week 1–2","Pilot Scoping & Agreement","Kala + Jordan finalize pilot plan document with success criteria. Share with Abhishek, Sabrina, David for sign-off. Agree on data source (synthetic or real), timeline (60 days), and point contacts on both sides. NDA already signed — begin pilot setup."),
        ("Week 2","Snowflake Trial Account Provisioning","Jordan provisions a Snowflake Business Critical trial account. Load synthetic AML dataset. Set up access for Sabrina, David, and Abhishek. Provide onboarding materials and a kick-off call."),
        ("Weeks 2–8","Pilot Execution","AML RightSource team tests core advisory use case. Snowflake SE provides bi-weekly office hours. Weekly 30-min check-in call between Kala and Sabrina/David. Track metrics against agreed baseline."),
        ("Week 8–10","Pilot Readout","Formal readout meeting with Abhishek, Sabrina, David, Jonathan, Isabel. Present results against success criteria. Quantify business impact. Present ROI model and 3-year roadmap."),
        ("Week 10–12","Internal Business Case","Abhishek takes Snowflake business case to CFO and PE board. Kala provides CFO-ready ROI summary deck. AE attends CFO meeting — request this directly."),
        ("Week 12–16","Procurement & Legal Review","Snowflake Order Form + MSA shared with AML RightSource legal. Jordan supports technical due diligence. AE manages deal desk for pricing and commercial structure."),
        ("Week 16–20","Contract Signature & Go-Live","MSA and initial Order Form signed. Provision production Snowflake environment. PSO kickoff for Phase 1 production deployment."),
    ]
    for period, title, desc in timeline:
        st.markdown(f"""<div style="display:flex;gap:16px;margin-bottom:14px;align-items:flex-start">
<div style="background:#29B5E8;color:white;border-radius:8px;padding:6px 10px;font-size:11px;font-weight:700;white-space:nowrap;flex-shrink:0">{period}</div>
<div><div style="font-size:14px;font-weight:700;color:#0D2B4E;margin-bottom:3px">{title}</div>
<div style="font-size:13px;color:#4A5568">{desc}</div></div>
</div>""", unsafe_allow_html=True)
    notes_comments_block("s26")

elif selected == SECTIONS[26]:
    st.markdown("""<div class="section-hero"><h1>27 — Making Contracting as Easy as Possible</h1><p>Proactive steps the AE can take to reduce friction and accelerate signature.</p></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    items = [
        ("✅ Procurement Preparation",["Have Jordan pre-prepare the security questionnaire response package before legal asks — proactive beats reactive","Share Snowflake's SOC 2 Type II report, FedRAMP High authorization, and standard DPA early in the process","Engage Snowflake Deal Desk before pilot readout to pre-build pricing options for CFO review","Request a 'contract-ready' Order Form template early — avoid 4-week legal review by pre-clearing standard language"]),
        ("💰 Commercial Flexibility",["Structure Year 1 as a 'starter' commitment ($300–500K) with expansion triggers — reduces initial risk for AML RS finance team","Offer consumption-based pricing with an annual floor — predictability for CFO, flexibility for AML RS ops","Consider a 'build-to-marketplace' commercial incentive — Snowflake waives/discounts compute for Native App development","Leverage Snowflake's ISV partnership program — AML RS qualifies as a Snowflake ISV partner"]),
        ("⚡ Speed to Signature",["Get Abhishek to name the CFO (or signing authority) at the pilot scoping meeting","Ask 'What does the contract approval process look like here?' — understand all gates before they appear","Offer to attend the internal business case presentation alongside Abhishek","Set a target signature date at the pilot readout: 'Can we target [date] for contract execution?'"]),
        ("🤝 Relationship Leverage",["Eric's FSI network: if AML RS bank clients are Snowflake customers, those teams can advocate internally at AML RS client organizations","Arrange a Snowflake executive briefing (VP or above) for Abhishek — demonstrates Snowflake's commitment","Leverage Snowflake's Financial Services vertical team for joint go-to-market planning session"]),
    ]
    for i, (title, bullets) in enumerate(items):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""<div class="card"><div class="card-title">{title}</div>
<ul style="margin:8px 0 0 18px;padding:0">
{"".join(f'<li style="font-size:13px;color:#4A5568;margin-bottom:6px">{b}</li>' for b in bullets)}
</ul></div>""", unsafe_allow_html=True)
    notes_comments_block("s27")

elif selected == SECTIONS[27]:
    st.markdown("""<div class="section-hero"><h1>28 — Open Questions</h1><p>Questions that still need to be answered to progress the deal.</p></div>""", unsafe_allow_html=True)
    questions = [
        ("Who is the economic buyer / signing authority for a Snowflake contract?","Abhishek","Critical for contracting path","Next call with Abhishek"),
        ("Are you currently evaluating any other data platforms (Databricks, MS Fabric, AWS)?","Abhishek / Isabel","Understand competitive landscape and urgency","Pilot scoping meeting"),
        ("What does your technology infrastructure look like today? Cloud provider(s), data warehouse, ETL tools?","Isabel Yeung","Required for migration planning","Isabel technical discovery call"),
        ("Jonathan — what are your top 3 insights you wish you could get from your internal data today but can't?","Jonathan McIsaac","Unlocks Track 2 pain and builds the business case","Jonathan discovery call"),
        ("What is AML RightSource's current data sharing process with advisory clients? How many days from request to first analysis?","Sabrina / David","Establishes the baseline metric for UC-1 ROI","Pilot planning call"),
        ("Does AML RightSource have any existing Snowflake customer relationships among your top 50 bank clients?","Jonathan / Abhishek","Identifies warm Track 1 pilot candidates","Next group call"),
        ("What is AML RightSource's budget cycle? When are technology investments approved for 2027?","Abhishek / CFO","Aligns pilot timeline to budget approval window","CFO engagement meeting"),
        ("Isabel — what is the current deployment process for algorithms/models into client environments?","Isabel Yeung","Validates Track 3 pain and sizes the Native App opportunity","Isabel technical discovery call"),
        ("Does AML RightSource have an infosec/CISO function? Who is that person?","Abhishek","Must engage security team early — late-stage security review is a common deal-killer","Pilot scoping meeting"),
        ("What does the PE board's investment thesis require in terms of technology transformation milestones?","Abhishek","Aligns Snowflake's value story directly to the PE board's exit criteria","Executive alignment meeting"),
    ]
    for i, (q, directed_to, why, when) in enumerate(questions, 1):
        st.markdown(f"""<div style="padding:12px 14px;background:white;border:1px solid #D1E8F5;border-radius:10px;margin-bottom:8px">
<div style="display:flex;gap:10px;align-items:flex-start">
<div style="background:#0D2B4E;color:white;border-radius:6px;padding:2px 8px;font-size:11px;font-weight:700;flex-shrink:0">Q{i}</div>
<div style="flex:1">
<div style="font-size:13px;font-weight:600;color:#0D2B4E;margin-bottom:4px">{q}</div>
<div style="font-size:12px;color:#718096">Ask: <strong>{directed_to}</strong> &nbsp;|&nbsp; Why: {why} &nbsp;|&nbsp; When: <em>{when}</em></div>
</div></div></div>""", unsafe_allow_html=True)
    notes_comments_block("s28")

elif selected == SECTIONS[28]:
    st.markdown("""<div class="section-hero"><h1>29 — Accelerating to Signature</h1><p>Proactive AE playbook to maximize close probability and speed.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="callout-green">
<strong>Core Principle:</strong> Every day that passes after a successful pilot without a contract is a risk that the momentum cools. The AE's job is to never let a day go by without a forward-moving action.
</div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 📅 During Pilot (Weeks 1–8)")
        for item in ["Weekly 30-min check-in call with Sabrina/David (primary pilot users)","Biweekly async update to Abhishek — share metrics, milestones, wins","Proactively resolve any blockers within 24 hours","Document all results and testimonials in real-time (future readout content)","Identify and remove any administrative friction before the users feel it","Arrange 1 reference call with a comparable Snowflake customer during weeks 4–6"]:
            st.markdown(f"""<div style="padding:8px 10px;background:#E8F7FD;border-radius:6px;margin-bottom:6px;font-size:13px">📌 {item}</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("#### 🏁 Post-Pilot (Weeks 9–20)")
        for item in ["Deliver pilot readout within 5 business days of pilot completion — do not let this slip","At readout: present quantified results, ROI model, 3-year roadmap, and proposed pricing","Ask Abhishek directly: 'Based on what you've seen, are you ready to move forward?'","Send draft Order Form within 48 hours of positive readout — paper in hand creates urgency","Offer to attend CFO/finance meeting alongside Abhishek — AEs in the room close 2× faster","Use deal desk creatively: phased payment options, lower Year 1 commitment with Year 2 expansion triggers","Set a mutual close date with Abhishek: 'We'd love to have this in place by [date]'"]:
            st.markdown(f"""<div style="padding:8px 10px;background:#E6FBF3;border-radius:6px;margin-bottom:6px;font-size:13px">✅ {item}</div>""", unsafe_allow_html=True)
    st.markdown("#### Final Checklist: AE Actions to Maximize Close Probability")
    for item in [("✅","Sandbox delivered to Sabrina within 3 business days","The single most important immediate action. An engaged user in the platform is the strongest deal accelerator."),("✅","Individual discovery calls with Jonathan and Isabel scheduled within 1 week","Both must have their own clear value narrative before the group reconvenes."),("✅","Economic buyer (CFO) identified and introduced","Without the economic buyer engaged, no pilot result can turn into a signed contract."),("✅","PE value creation narrative embedded in all executive communications","Frame every conversation in the context of exit multiple improvement and recurring data product revenue."),("✅","FSI co-sell introductions initiated through Eric's network","A warm intro to a mutual bank customer can unlock Track 1 client-side buy-in that would otherwise take months."),("✅","Pilot success criteria signed off in writing before pilot begins","Written success criteria prevent post-pilot 'goalpost moving' and create a clear conversion trigger."),]:
        st.markdown(f"""<div style="display:flex;gap:14px;padding:12px;background:white;border:1px solid #D1E8F5;border-radius:10px;margin-bottom:8px;align-items:flex-start">
<span style="font-size:20px;flex-shrink:0">{item[0]}</span>
<div><div style="font-size:14px;font-weight:700;color:#0D2B4E">{item[1]}</div>
<div style="font-size:12px;color:#4A5568;margin-top:2px">{item[2]}</div></div>
</div>""", unsafe_allow_html=True)
    notes_comments_block("s29")

# ── ALL NOTES SUMMARY ─────────────────────────────────────────────────────────
elif selected == SECTIONS[29]:
    st.markdown("""<div class="section-hero"><h1>📊 All Notes & Comments Summary</h1><p>Compiled view of all account team notes and comments across all 29 sections.</p></div>""", unsafe_allow_html=True)

    has_content = False
    for i, section in enumerate(SECTIONS[:-1]):
        sec_key = f"s{str(i+1).zfill(2)}"
        note = st.session_state.section_notes.get(sec_key, "")
        comments = st.session_state.comments.get(sec_key, [])
        if note.strip() or comments:
            has_content = True
            with st.expander(f"**{section}** — {len(comments)} comment(s)"):
                if note.strip():
                    st.markdown(f"""<div class="callout-blue"><strong>📝 Account Team Notes:</strong><br>{note}</div>""", unsafe_allow_html=True)
                for c in comments:
                    st.markdown(f"""<div style="background:white;border:1px solid #D1E8F5;border-left:3px solid #29B5E8;border-radius:0 8px 8px 0;padding:10px 14px;margin:6px 0">
<span style="font-size:11px;color:#718096">👤 <strong>{c['author']}</strong> · {c['ts']}</span><br>
<span style="font-size:13px;color:#2D3748">{c['text']}</span></div>""", unsafe_allow_html=True)

    if not has_content:
        st.markdown("""<div style="text-align:center;padding:60px;color:#718096">
<div style="font-size:48px">📝</div>
<div style="font-size:18px;font-weight:600;margin-top:12px">No notes yet</div>
<div style="font-size:14px;margin-top:8px">Navigate to any section and add notes, comments, or questions. They'll all appear here.</div>
</div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="background:#0D2B4E;color:rgba(255,255,255,0.5);text-align:center;padding:18px;border-radius:12px;font-size:12px">
🔒 Snowflake Confidential — Internal Use Only — Not for Distribution<br>
Prepared by: Kala Boudreaux · Eric Szenderski · Jordan Ude — Snowflake Enterprise Acquisition
</div>
""", unsafe_allow_html=True)
