import streamlit as st

st.set_page_config(
    page_title="AI Impact Hub",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar above to explore the AI tools!")

tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📝 Sign Up", "ℹ️ About Us", "📧 Contact"])

with tab1:
    st.title("🤖 Welcome to the AI Impact Hub")
    st.markdown("""
    Artificial Intelligence is no longer a concept of the future—it is actively transforming our world today. 
    This platform showcases how AI solves real-world problems across healthcare, media integrity, consumer tech, and agriculture.
    
    ### 🚀 Explore Our AI Modules (Available in the Sidebar):
    1. **🩺 Medical Diagnosis Assistant**: Preliminary symptom analysis for healthcare support. 
    2.**📱 Budget Smartphone Suggester**: Personalized, data-driven tech recommendations.
    """)
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800", caption="Empowering fields through Intelligence")

with tab2:
    st.header("📝 Create Your Account")
    with st.form("signup_form"):
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("Username")
            email = st.text_input("Email Address")
        with col2:
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
        
        agree = st.checkbox("I agree to the Terms of Service and Privacy Policy")
        submit = st.form_submit_button("Register")
        
        if submit:
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif not agree:
                st.warning("You must accept the terms to proceed.")
            elif username and email:
                st.success(f"Welcome aboard, {username}! Your account has been successfully simulated.")
            else:
                st.error("Please fill out all required fields.")

with tab3:
    st.header("ℹ️ About This Project")
    st.write("""
    The **AI Impact Hub** was built to demonstrate how machine learning and natural language processing 
    can be practical, accessible, and highly impactful. 
    
    Our mission is to bridge the gap between complex AI models and everyday utility, proving that technology 
    can be used responsibly to improve lives, protect truths, and make smarter everyday decisions.
    """)

with tab4:
    st.header("📧 Get in Touch")
    st.write("Have questions, feedback, or want to collaborate? Drop us a message below.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        user_email = st.text_input("Email")
        message = st.text_area("Your Message")
        send_btn = st.form_submit_button("Send Message")
        
        if send_btn:
            if name and user_email and message:
                st.success(f"Thank you, {name}! Your message has been sent successfully.")
            else:
                st.error("Please fill in all the details before sending.")
