# Enterprise AI Lead Qualification Portal

An autonomous lead intake portal built with Streamlit and powered by an n8n workflow using Groq, Google Sheets, Slack, and Gmail.

## Architecture & Flow
1. **Streamlit UI**: Collects lead details (name, email, budget, scope).
2. **n8n Webhook**: Receives data and validates schema.
3. **Groq AI Agent**: Analyzes intent and scores leads (`Hot`, `Warm`, `Cold`).
4. **Google Sheets**: Logs all qualified lead submissions.
5. **Slack Alert**: Sends interactive Block Kit alerts with priority colors.
6. **Gmail Automation**: Sends personalized scheduling links to high-priority leads.

## 🏗️ Architecture Overview

```text
[ Streamlit Web UI ]
         │
         ▼ (POST Webhook)
[ n8n Workflow Engine ]
    ├── ⚙️ Sanitize & Validate (Schema Verification)
    ├── 🤖 Groq AI Lead Qualification Agent
    ├── 📊 Google Sheets Database (Hot / Cold Leads)
    ├── 💬 Slack Alert (Block Kit Notification)
    └── ✉️ Gmail Node (Automated Email Routing)
```

## Local Setup

1. **Clone repository:**
```bash
 git clone [https://github.com/zahra-qasmi/lead-qualification-agent.git](https://github.com/zahra-qasmi/lead-qualification-agent.git)
 cd lead-qualification-agent
```
Install dependencies:

```Bash
pip install -r requirements.txt
```
**Configure Environment:**

```Bash
cp .env.example .env
```

Add your active n8n webhook URL to .env.

**Import n8n Workflow:**

1. Import workflow/enterprise_lead_engine.json into your n8n instance.

2. Attach your Groq, Google Sheets, and Gmail credentials.

3. Activate the workflow.

**Run the Streamlit App:**

```Bash
streamlit run app.py
