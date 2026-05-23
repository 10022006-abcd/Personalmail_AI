import streamlit as st
import requests

BACKEND_URL = "https://scribe-padded-skincare.ngrok-free.dev/generate-email"

st.set_page_config(
    page_title="PersonaMail AI",
    page_icon="📧",
    layout="wide"
)

st.title("📧 PersonaMail AI")
st.subheader("AI-Powered Personalized Email Generator")

st.markdown("---")

# USER PROFILE
st.header("👤 User Profile")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )
    location = st.text_input("Location")

with col2:
    profession = st.text_input("Profession")
    income_level = st.selectbox(
        "Income Level",
        ["Low", "Medium", "High"]
    )

st.markdown("---")

# EMAIL DETAILS
st.header("✉️ Email Details")

col3, col4 = st.columns(2)

with col3:
    purpose = st.selectbox(
        "Purpose",
        [
            "Job Application",
            "Business Proposal",
            "Leave Request",
            "Complaint",
            "Follow-Up",
            "Invitation",
            "Thank You",
            "Apology",
            "Academic Request",
            "General"
        ]
    )

    recipient_type = st.text_input(
        "Recipient Type",
        placeholder="Manager, Professor, Friend, Client"
    )

    relationship = st.text_input(
        "Relationship with Recipient",
        placeholder="Professional, Personal, Academic"
    )

with col4:
    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Casual",
            "Persuasive",
            "Simple"
        ]
    )

    length = st.selectbox(
        "Email Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    urgency = st.selectbox(
        "Urgency",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

language = st.selectbox(
    "Language",
    [
        "English"
    ]
)

additional_context = st.text_area(
    "Additional Context",
    height=150,
    placeholder="Enter extra information here..."
)

st.markdown("---")

if st.button("🚀 Generate Email"):

    payload = {
        "name": name,
        "age": age,
        "gender": gender,
        "location": location,
        "profession": profession,
        "income_level": income_level,

        "purpose": purpose,
        "recipient_type": recipient_type,
        "relationship": relationship,
        "tone": tone,
        "length": length,
        "urgency": urgency,
        "language": language,

        "additional_context": additional_context
    }

    with st.spinner("Generating AI Email..."):

        try:
            response = requests.post(BACKEND_URL, json=payload)

            if response.status_code == 200:

                result = response.json()

                generated_email = result["generated_email"]

                st.success("Email Generated Successfully!")

                st.markdown("## Generated Email")

                st.text_area(
                    "Output",
                    value=generated_email,
                    height=400
                )

            else:
                st.error("Failed to generate email")

        except Exception as e:
            st.error(f"Error: {e}")