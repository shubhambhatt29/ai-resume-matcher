# 💼 HireSense AI — Smart Resume Match Analyzer

**HireSense AI** is an AI-powered web app that compares a resume and a job description to instantly show:
- ✅ Match Score  
- 💪 Strengths  
- 🚫 Missing Keywords  

Perfect for **job seekers, HRs, and recruiters** who want quick, data-driven insights.

## 🚀 Quick Start

Follow these simple steps to run the app on your own system — no coding experience required.

### 1️⃣ Download & Unzip
After purchase, download the `HireSenseAI.zip` file and unzip it anywhere on your computer.

### 2️⃣ Install Requirements
Open a terminal (Command Prompt / PowerShell / macOS Terminal) inside the unzipped folder and run:

```bash
pip install -r requirements.txt

This installs Streamlit and OpenAI SDK.

3️⃣ Add Your OpenAI API Key
HireSense AI uses GPT to analyze resumes — you need your own OpenAI API key.
Step-by-step:
Go to https://platform.openai.com/account/api-keys
Copy your Secret Key (starts with sk-...)
Inside the project folder, create a new folder named .streamlit
Inside that .streamlit folder, create a file named secrets.toml

👉 File structure should look like this:
HireSenseAI/
│
├── app.py
├── requirements.txt
├── logo.png
├── README.md
└── .streamlit/
    └── secrets.toml

Now open the secrets.toml file and paste:
[general]
OPENAI_API_KEY = "sk-your_api_key_here"

💡 Make sure you include the quotes around your API key.

4️⃣ Run the App
Once done, start the app locally with:
streamlit run app.py
Your browser will open automatically at:
http://localhost:8501

🎨 Features
#Clean, professional UI built with Streamlit
#Secure (your API key never leaves your system)
#AI-generated match insights using GPT
#Works on Windows, macOS, or Linux

💬 Support
If you face any issue, open a discussion or contact us at learniverse2910@gmail.com

© 2025 HireSense AI — All rights reserved.
