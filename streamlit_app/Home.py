import streamlit as st

# Page config (must be first Streamlit command)
st.set_page_config(page_title="EmojiWave", page_icon="🤖", layout="centered")

# Title and intro
st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'> Welcome to EmojiWave!</h1>
    <p style='text-align: center; font-size: 20px; color: #333;'>Let’s have some fun recognizing hand gestures ✋✨</p>
""", unsafe_allow_html=True)

# Display centered and larger GIF
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("EmojiWave-unscreen (1).gif", width=900)

# Add more vertical space
st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center;'>
        <h3 style='margin: 0;'>Select Your Gesture Mode</h3>
        <img src='https://i.postimg.cc/MXX2MHbS/hand-puzzle.png' width='26' style='margin-left: 4px; vertical-align: middle;'/>
    </div>
""", unsafe_allow_html=True)



# Button layout in three columns
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📷 Capture Gesture"):
        st.switch_page("pages/CameraInput.py")

with col2:
    if st.button("🖼️ Upload Image"):
        st.switch_page("pages/UploadImage.py")

with col3:
    if st.button("📚 Learn More"):
        st.switch_page("pages/MoreResources.py")

# Add vertical space before footer to push it down
st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Crafted with ❤️ and 🤖 to Bring Hand Gestures to Life  ©️ 2025</p>", unsafe_allow_html=True)
