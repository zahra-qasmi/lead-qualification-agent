import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Project Consultation | Intake Portal",
    page_icon="✨",
    layout="centered"
)

# High-Contrast CSS Styling
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%, #fdf4ff 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Container & High-Contrast Typography */
    .header-container {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
    }
    
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: #ffffff !important;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        padding: 0.4rem 1rem;
        border-radius: 9999px;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }
    
    .main-title {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: #0f172a !important; /* Deep Navy/Slate - High Visibility */
        margin-bottom: 0.6rem !important;
        letter-spacing: -0.02em;
    }
    
    .sub-title {
        color: #334155 !important; /* Dark Slate Gray - High Visibility */
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        max-width: 540px;
        margin: 0 auto !important;
        line-height: 1.6 !important;
    }
    
    /* Form Container */
    div[data-testid="stForm"] {
        background-color: #ffffff !important;
        border-radius: 20px;
        padding: 2.5rem;
        border: 1.5px solid #cbd5e1 !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.07);
    }
    
    /* Field Labels & Placeholders */
    label[data-testid="stWidgetLabel"] p {
        font-weight: 700 !important;
        color: #0f172a !important;
        font-size: 0.95rem !important;
    }
    
    input, textarea {
        border-radius: 10px !important;
        border: 1.5px solid #cbd5e1 !important;
        background-color: #f8fafc !important;
        color: #0f172a !important;
        font-size: 0.95rem !important;
    }
    
    input:focus, textarea:focus {
        border-color: #4f46e5 !important;
        background-color: #ffffff !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2) !important;
    }
    
    /* Submit Button */
    div[data-testid="stFormSubmitButton"] button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4) !important;
    }
    
    div[data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 24px -5px rgba(79, 70, 229, 0.5) !important;
    }
    
    #MainMenu, header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# High-Contrast Header Section
st.markdown("""
    <div class="header-container">
        <span class="badge">Project Consultation</span>
        <h1 class="main-title">Let's build something exceptional.</h1>
        <p class="sub-title">Tell us about your project vision, requirements, and budget. Our team will review your inquiry and connect with you shortly.</p>
    </div>
""", unsafe_allow_html=True)

N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/groq-lead-intake"

# Intake Form
with st.form(key="lead_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", placeholder="e.g. Sarah Khan")
    with col2:
        company = st.text_input("Company / Brand", placeholder="e.g. Acme Innovations")

    col3, col4 = st.columns(2)
    with col3:
        email = st.text_input("Email Address *", placeholder="sarah@example.com")
    with col4:
        phone = st.text_input("Phone Number", placeholder="+1 (555) 019-2834")

    budget = st.number_input("Estimated Budget (USD) *", min_value=0, step=500, value=2500)
    inquiry = st.text_area("Project Scope & Requirements *", placeholder="Describe deliverables, timelines, or specifications...", height=130)

    submitted = st.form_submit_button("Send Project Inquiry 🚀")

    if submitted:
        if not name or not email or "@" not in email:
            st.error("Please provide a valid Name and a complete Email address.")
        else:
            payload = {
                "name": name,
                "company": company,
                "email": email,
                "phone": phone,
                "budget": budget,
                "inquiry": inquiry
            }

            with st.spinner("Submitting your inquiry..."):
                try:
                    response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=15)

                    if response.status_code == 200:
                        st.balloons()
                        st.success(
                            f"✨ **Thank you, {name}! Your inquiry has been received.**\n\n"
                            f"Our team will review your project details and reach out to **{email}** shortly."
                        )
                    else:
                        st.error(f"Failed to submit: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Could not reach server: {e}")