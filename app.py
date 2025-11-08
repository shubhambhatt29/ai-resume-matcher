import streamlit as st
from openai import OpenAI
import streamlit as st
import re

# ✅ Load API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ✅ App Configuration
st.set_page_config(
    page_title="HireSense AI | Resume Matcher",
    page_icon="logo.png",
    layout="wide"
)
st.markdown("""
    <div style='text-align:center; padding: 10px 0 30px 0;'>
        <h1 style='color:#2563EB;'>HireSense AI</h1>
        <p style='font-size:18px; color:#374151;'>Analyze resume fit for job descriptions in seconds.</p>
    </div>
""", unsafe_allow_html=True)

# ✅ Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f9fafb;
        font-family: 'Inter', sans-serif;
    }
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 1px solid #d1d5db;
        padding: 12px;
        font-size: 15px;
    }
    .match-score {
        font-size: 26px;
        font-weight: 700;
        text-align: center;
        margin-top: 10px;
    }
    .highlight {
        background-color: #fff3cd;
        padding: 2px 4px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ✅ Sidebar
st.sidebar.image("logo.png", width=140)
st.sidebar.markdown("### HireSense AI")
st.sidebar.caption("Smart Resume Match & Job Fit Analyzer")

# ✅ Inputs
st.header("📄 Job Description")
job_desc = st.text_area("Paste the Job Description", height=180)

st.header("🧑‍💼 Candidate Resume")
resume_text = st.text_area("Paste the Resume Text", height=180)

# ✅ Function to extract match score + keywords
def analyze_resume(job, resume):
    prompt = f"""
    You are an expert HR analyst. Compare this resume to the job description and give:
    1. A match percentage (0-100)
    2. Strengths
    3. Missing keywords or skills
    4. A 2-line summary feedback.

    Return response in JSON like:
    {{
      "match": 85,
      "strengths": ["Python", "Microservices", "AWS"],
      "missing": ["Kafka", "CI/CD"],
      "summary": "Strong backend skills but lacks DevOps exposure."
    }}

    JOB DESCRIPTION:
    {job}

    RESUME:
    {resume}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    text = response.choices[0].message.content
    return text

# ✅ On button click
if st.button("🔍 Analyze Match", use_container_width=True):
    if job_desc.strip() == "" or resume_text.strip() == "":
        st.warning("Please enter both Job Description and Resume.")
    else:
        with st.spinner("Analyzing resume... ⏳"):
            result_text = analyze_resume(job_desc, resume_text)

        # Extract numbers + text
        import json
        try:
            result = json.loads(result_text)
        except:
            st.error("Could not parse AI output. Please try again.")
            st.text(result_text)
            st.stop()

        # ✅ Match score section
        match_score = result["match"]
        bar_color = "green" if match_score >= 80 else "orange" if match_score >= 50 else "red"

        st.subheader("📊 Match Score")
        st.progress(match_score / 100)
        st.markdown(f"<div class='match-score' style='color:{bar_color};'>{match_score}%</div>", unsafe_allow_html=True)

        # ✅ Strengths & Missing
        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ Strengths")
            for s in result["strengths"]:
                st.markdown(f"- {s}")
        with col2:
            st.error("❌ Missing Keywords")
            for m in result["missing"]:
                st.markdown(f"- {m}")

        # ✅ Summary
        st.info(f"💡 Feedback: {result['summary']}")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 HireSense AI — Built with ❤️ using Streamlit + OpenAI</p>",
    unsafe_allow_html=True
)

