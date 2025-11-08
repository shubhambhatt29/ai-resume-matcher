import streamlit as st
import openai

st.set_page_config(page_title="AI Resume Match Checker", page_icon="🧠")

st.title("🧠 AI Resume Match Checker")
st.write("Paste your resume and job description to see match % and improvements.")

resume = st.text_area("Your Resume")
jd = st.text_area("Job Description")

if st.button("Analyze"):
    if resume and jd:
        with st.spinner("Analyzing..."):
            prompt = f"""
            Compare this resume and job description.
            Output:
            1. Match percentage (0–100)
            2. Missing keywords
            3. Improvements to resume summary.
            Resume: {resume}
            Job Description: {jd}
            """
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
            st.markdown(response['choices'][0]['message']['content'])
    else:
        st.error("Please paste both resume and job description.")
