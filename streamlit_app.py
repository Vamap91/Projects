import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vinícius Paschoa – AI Project Portfolio", layout="wide")

# Load profile image
profile_image = Image.open("c2d5af97-1e95-4314-826e-b6d5f05d609a.jpg")

# Sidebar menu
st.sidebar.title("Project Portfolio")
project = st.sidebar.radio("Select a section", ["Profile", "MirrorGlass", "HeatGlass"])

# PROFILE PAGE
if project == "Profile":
    st.title("👤 About Vinícius Paschoa")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_image, width=160)
    with col2:
        st.markdown("### **Vinícius Paschoa**")
        st.markdown("*AI Specialist | Business-Oriented Artificial Intelligence*")
        st.markdown("📍 São Paulo, Brazil | 🇪🇺 EU Citizen")
        st.markdown("[🔗 LinkedIn Profile](https://www.linkedin.com/in/viniciuspaschoa)")
        st.markdown("📧 viniciuspaschoa1@hotmail.com")
        st.markdown("📱 +55 (11) 93801-2431")

    st.markdown("---")
    st.subheader("🧠 Summary")
    st.markdown(\""" 
Artificial Intelligence Specialist focused on delivering measurable impact through intelligent automation.  
Led multiple AI initiatives at Carglass and Vallourec using GPT, Streamlit, vision systems, and automation tools.  
\""")
    st.markdown("---")
    st.subheader("🎓 Education")
    st.markdown(\""" 
- Postgraduate in AI for Business Strategy – Centro Universitário Senac  
- Postgraduate in Agile Models – UNIMAIS  
- Bachelor's in Production Engineering – Senac  
- Successful Negotiation – University of Michigan  
\""")
    st.markdown("---")
    st.subheader("🌐 Languages")
    st.markdown("- Portuguese: Native\n- English: Full Professional\n- French: Professional Working")

# MIRRORGLASS PAGE
elif project == "MirrorGlass":
    st.title("🔍 MirrorGlass: Image Fraud Detection System")
    st.markdown(\""" 
MirrorGlass detects visual fraud in customer-submitted images using AI.  
Techniques include SSIM, LBP, and deep image comparison.  
\""")
    col1, col2 = st.columns(2)
    with col1:
        st.image("239788e1-26f9-4c94-bcbf-7eb93fe76f59.png", caption="Upload interface and detection settings")
    with col2:
        st.image("e5130d9d-966d-451e-a050-f5b79a473dd2.png", caption="Texture analysis with Heat Map")

    st.markdown(\""" 
### Similarity Thresholds  
- 100%: Identical images  
- 90–99%: Possibly altered duplicates  
- 70–89%: Potential manipulation  
- Below 50%: Likely unrelated  
\""")  

# HEATGLASS PAGE
elif project == "HeatGlass":
    st.title("🔥 HeatGlass: Emotional Call Analysis System")
    st.markdown(\""" 
HeatGlass uses GPT-4 to analyze emotional tone and quality in service calls.  
It includes transcription, checklist scoring, and business risk analysis.  
\""")
    st.image("895cb66e-da1d-4458-b5ec-2ae2dd25ae7b.png", caption="Audio upload and analysis interface")
    st.image("3c4269e5-34ea-4ce5-b8d5-bdb45bad833c.png", caption="Checklist summary and sentiment results")

    st.markdown(\""" 
### Metrics Evaluated  
- Client Sentiment: calm, neutral, critical  
- Legal Compliance (LGPD)  
- Script Usage & Closing Phrases  
- Overall Score (out of 81 points)  
\""")
