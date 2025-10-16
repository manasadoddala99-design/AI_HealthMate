import streamlit as st

st.set_page_config(page_title="AI HealthMate", page_icon="🏥", layout="wide")
st.title("🏥 AI HealthMate Chatbot")
st.write("Multi-domain healthcare assistant (Mental Health, Wound Care, Medical).")

# Sidebar for role
role = st.sidebar.selectbox("Select your role:", ["Patient", "Doctor", "Care Team"])

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_area("💬 Type your message here:")

# Function to generate response
def generate_response(user_input, role):
    msg = user_input.lower()
    responses = []

    # Mental Health
    if any(word in msg for word in ["stress", "anxiety", "sad", "depressed", "tired", "sleep"]):
        if role == "Patient":
            responses.append("It seems you are experiencing mental stress. Try breathing exercises, meditation, or speak to a counselor if needed.")
        elif role == "Doctor":
            responses.append("Patient reports signs of stress or anxiety. Consider counseling, therapy, or relaxation techniques.")
        else:
            responses.append("Monitor patient for stress or anxiety symptoms. Provide support or resources.")

    # Wound Management
    if any(word in msg for word in ["cut", "burn", "infection", "wound", "bleeding"]):
        if role == "Patient":
            responses.append("For your wound, clean it gently, apply antiseptic, and keep it covered. Seek medical attention if severe.")
        elif role == "Doctor":
            responses.append("Patient reports a wound or injury. Evaluate severity, infection risk, and provide instructions.")
        else:
            responses.append("Check the patient's wound care status, ensure proper hygiene, assist as needed.")

    # General Medical
    if any(word in msg for word in ["fever", "temperature"]):
        responses.append("You seem to have a fever. Stay hydrated, rest, and consult a doctor if it persists.")
    if any(word in msg for word in ["headache", "migraine"]):
        responses.append("Headache can have many causes. Rest, drink water, and monitor symptoms.")
    if any(word in msg for word in ["cough", "cold", "sore throat"]):
        responses.append("You might have a cold or cough. Drink warm fluids and consult a doctor if it worsens.")
    if any(word in msg for word in ["pain", "stomach", "stomachache", "back pain"]):
        responses.append("Please specify the type and location of the pain for better advice.")
    if any(word in msg for word in ["fatigue", "weakness"]):
        responses.append("Feeling fatigued? Ensure rest and proper hydration. Seek medical advice if persistent.")

    if not responses:
        if role == "Patient":
            responses.append("Thank you for your message. Provide more details or consult a healthcare professional.")
        else:
            responses.append(f"Message received for {role}. Further clarification may be needed.")

    return " ".join(responses)

# Send button
if st.button("Send"):
    if user_input.strip():
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Generate AI response
        ai_response = generate_response(user_input, role)
        st.session_state.messages.append({"role": "ai", "content": ai_response})
    else:
        st.warning("Please type a message first!")

# Display chat history with colored bubbles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='background-color:#D0E1FF; padding:10px; border-radius:10px; margin:5px 0;'><b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        # AI bubble color depends on role
        color = "#D0FFD6" if role == "Patient" else "#FFF3D0" if role == "Doctor" else "#FFD0D0"
        st.markdown(f"<div style='background-color:{color}; padding:10px; border-radius:10px; margin:5px 0;'><b>AI ({role} Assistant):</b> {msg['content']}</div>", unsafe_allow_html=True)

st.caption("Built by Manasa | Advanced Multi-domain AI Healthcare Prototype")
