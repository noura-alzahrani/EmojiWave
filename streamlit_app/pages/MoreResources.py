import streamlit as st

# Page configuration
st.set_page_config(
    page_title="The Magical World of Gestures! 🎉",
    layout="centered"
)

# Custom CSS with elegant styling
st.markdown("""
<style>
  .stApp {
    background: #FFF9ED;
}
    /* Original title gradient */
    .header-gradient {
        background: #6C63FF; #linear-gradient(90deg, #8EC5FC 0%, #E0C3FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Subheader */
    .subheader {
        font-size: 1rem !important;
        text-align: center;
        color: #666;
        margin-bottom: 1.5rem;
    }

    /* Compact cards */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.8rem 0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        border-left: 4px solid;
        cursor: pointer;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }

    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }

    .card-1 { border-color: #8EC5FC; }
    .card-2 { border-color: #E0C3FC; }
    .card-3 { border-color: #A18CD1; }

    /* Card title */
    .card-title {
        font-size: 1.1rem !important;
        font-weight: 600;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
    }

    /* Emoji animation */
    .emoji {
        font-size: 1.1rem;
        margin-right: 0.6rem;
        animation: bounce 1.8s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-4px); }
    }

    /* Button style */
    .btn {
        display: inline-block;
        background: #FFE4C4; #linear-gradient(90deg, #8EC5FC, #E0C3FC);
        color: white !important;
        padding: 0.4rem 1rem;
        border-radius: 16px;
        text-decoration: none;
        font-weight: 500;
        margin-top: 0.6rem;
        font-size: 0.8rem;
        transition: all 0.2s;
    }

    .btn:hover {
        transform: scale(1.03);
        box-shadow: 0 2px 8px rgba(142, 197, 252, 0.3);
    }

    /* Highlight text */
    .highlight {
        font-weight: 600;
        color: #6a11cb;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 1.5rem;
        color: #999;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="header-gradient">Feeling Curious? Go Deeper! 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader"> You have seen gesture magic now discover the AI and computer vision powering it! </div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">If this sparked your curiosity even a little these resources will take you further </div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Curious minds are always welcome 🤓</div>', unsafe_allow_html=True)

# Compact cards
st.markdown("""
<div class="card card-1">
    <div class="card-title">
        <span class="emoji">🤖</span> How Machines See Gestures
    </div>
    <p style="font-size:0.85rem;">The <span class="highlight">computer vision</span> technology that interprets human movements.</p>
    <a href="https://towardsdatascience.com" class="btn">Learn More</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card card-2">
    <div class="card-title">
        <span class="emoji">🧠</span> Neural Networks
    </div>
    <p style="font-size:0.85rem;">How <span class="highlight">deep learning</span> models recognize complex patterns.</p>
    <a href="https://deepai.org" class="btn">Explore</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card card-3">
    <div class="card-title">
        <span class="emoji">💡</span> Source of Simplicity
    </div>
    <p style="font-size:0.85rem;">When things suddenly made senseand everything started <span class="highlight">moving forward</span>.</p>
    <a href="https://analyticsvidhya.com" class="btn">Discover</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>
Enjoy the read and who knows?
Your next idea might start here!🚀</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Crafted with ❤️ and 🤖 to Bring Hand Gestures to Life  ©️ 2025</p>", unsafe_allow_html=True)
