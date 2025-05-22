import streamlit as st
import pandas as pd 
from PIL import Image 
import plotly.graph_objects as go 
import plotly.express as px 
import numpy as np
import os

# Page configuration with professional settings
st.set_page_config(
    page_title="Vinícius Paschoa | AI Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean, professional design with improved contrast
def load_css():
    st.markdown("""
    <style>
        /* Main color scheme - professional dark theme with high contrast */
        :root {
            --primary: #1E40AF;
            --secondary: #3B82F6;
            --accent: #60A5FA;
            --light: #93C5FD;
            --background: #F8FAFC;
            --text: #1E293B;
            --card-bg: #FFFFFF;
            --sidebar-bg: #1E3A8A;
            --sidebar-text: #FFFFFF;
        }
        
        /* Base styling */
        .main {
            background-color: var(--background);
            color: var(--text);
            font-family: 'Inter', 'Segoe UI', Helvetica, sans-serif;
        }
        
        h1, h2, h3, h4, h5 {
            font-family: 'Inter', 'Segoe UI', Helvetica, sans-serif;
            color: var(--primary);
            font-weight: 600;
        }
        
        /* Header styling with improved contrast */
        .header-container {
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            padding: 2.5rem;
            border-radius: 0.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .header-container h1, .header-container h3, .header-container p {
            color: white !important;
            text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2);
        }
        
        /* Card styling with better shadows and borders */
        .card {
            background-color: var(--card-bg);
            border-radius: 0.75rem;
            padding: 1.75rem;
            margin-bottom: 1.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border-left: 4px solid var(--secondary);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
        }
        
        /* Project card styling */
        .project-card {
            background-color: var(--card-bg);
            border-radius: 0.75rem;
            padding: 1.75rem;
            margin-bottom: 1.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border-left: 4px solid var(--accent);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .project-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
        }
        
        /* Skill bar styling */
        .skill-container {
            margin-bottom: 1.25rem;
        }
        
        .skill-bar {
            height: 10px;
            background-color: #e9ecef;
            border-radius: 5px;
            overflow: hidden;
        }
        
        .skill-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 5px;
            transition: width 1s ease-in-out;
        }
        
        /* Tag styling */
        .tag {
            display: inline-block;
            background-color: var(--secondary);
            color: white;
            padding: 0.35rem 0.75rem;
            border-radius: 1rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            font-size: 0.85rem;
            font-weight: 500;
            transition: background-color 0.2s ease;
        }
        
        .tag:hover {
            background-color: var(--primary);
        }
        
        /* Sidebar styling with improved contrast */
        section[data-testid="stSidebar"] {
            background-color: var(--sidebar-bg) !important;
            color: white !important;
        }
        
        section[data-testid="stSidebar"] .stRadio label {
            color: white !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: white !important;
        }
        
        /* Timeline styling */
        .timeline-item {
            padding-left: 1.75rem;
            border-left: 2px solid var(--secondary);
            margin-bottom: 1.75rem;
            position: relative;
            padding-bottom: 1.5rem;
        }
        
        .timeline-item:last-child {
            border-left: 2px solid transparent;
        }
        
        .timeline-item:before {
            content: '';
            position: absolute;
            left: -9px;
            top: 0;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background-color: var(--secondary);
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
        }
        
        .timeline-date {
            color: var(--secondary);
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        /* Metric box styling */
        .metric-box {
            text-align: center;
            padding: 1.25rem;
            background-color: var(--card-bg);
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .metric-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
        }
        
        .metric-value {
            font-size: 2.75rem;
            font-weight: 700;
            color: var(--primary);
        }
        
        .metric-label {
            font-size: 1rem;
            color: var(--text);
            margin-top: 0.5rem;
        }
        
        /* Animation for skill bars */
        @keyframes skillAnimation {
            from { width: 0; }
            to { width: 100%; }
        }
        
        .animate-skill {
            animation: skillAnimation 1s ease-out forwards;
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            margin-top: 2.5rem;
            padding: 1.5rem;
            background-color: #f8f9fa;
            border-radius: 0.75rem;
            color: var(--text);
        }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Sidebar navigation
with st.sidebar:
    st.markdown('<h3 style="color: white; text-align: center;">Vinícius Paschoa</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: white; text-align: center;">AI Specialist | EU Citizen</p>', unsafe_allow_html=True)
    
    # Try to load profile image
    try:
        profile_image = Image.open("profile.jpg")
        st.image(profile_image, width=150)
    except:
        st.markdown('<div style="display:flex; justify-content:center; color:white; font-size:48px;">🧠</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="margin: 15px 0; border-color: rgba(255,255,255,0.2);">', unsafe_allow_html=True)
    
    # Navigation
    st.markdown('<p style="color: white; font-weight: 500;">Navigation</p>', unsafe_allow_html=True)
    page = st.radio(
        "",
        ["Profile", "Projects", "Experience", "Skills", "Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown('<hr style="margin: 15px 0; border-color: rgba(255,255,255,0.2);">', unsafe_allow_html=True)
    
    # Contact information with improved visibility
    st.markdown('<p style="color: white; font-weight: 500;">Contact Information</p>', unsafe_allow_html=True)
    st.markdown("""
    <div>
        <p style="color: white; margin-bottom: 8px;">📧 <a href="mailto:viniciuspaschoa1@hotmail.com" style="color: #93C5FD; text-decoration: none;">viniciuspaschoa1@hotmail.com</a></p>
        <p style="color: white; margin-bottom: 8px;">📱 +55 (11) 93801-2431</p>
        <p style="color: white; margin-bottom: 8px;">🌐 <a href="https://www.linkedin.com/in/viniciuspaschoa" target="_blank" style="color: #93C5FD; text-decoration: none;">LinkedIn Profile</a></p>
    </div>
    """, unsafe_allow_html=True)

# PROFILE PAGE
if page == "Profile":
    # Header
    st.markdown("""
    <div class="header-container">
        <h1>Vinícius Paschoa</h1>
        <h3>AI Specialist | Business-Oriented Artificial Intelligence | EU Citizen</h3>
        <p>Paris, Île-de-France, France</p>
    </div>
    """, unsafe_allow_html=True)
    
    # About section
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Try to load profile image
        try:
            profile_image = Image.open("profile.jpg")
            st.image(profile_image, width=250)
        except Exception as e:
            st.markdown('<div style="display:flex; justify-content:center; font-size:100px; color:#1E40AF;">🧠</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <p>Artificial Intelligence Specialist focused on driving business transformation through Applied AI and Strategic Data Solutions. With a strong foundation in technology, business analysis, and project leadership, I specialize in applying Artificial Intelligence to solve real-world business challenges. At Vallourec and now at Carglass, I have led multiple initiatives under the internal AI accelerator program called "Agente", where I designed and deployed end-to-end solutions that automate complex workflows, optimize operations, and generate actionable insights. From structuring RAG-based assistants that interpret SharePoint knowledge bases to developing AI systems for emotional analysis of customer service interactions, my focus is always on delivering measurable impact. I manage the full lifecycle of AI-driven products — from identifying business needs and building prototypes in Streamlit to deploying scalable solutions and driving user adoption.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key metrics
    st.markdown("<h2>Key Metrics</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">7+</div>
            <div class="metric-label">Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">10+</div>
            <div class="metric-label">AI Projects</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">3</div>
            <div class="metric-label">Languages</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">2</div>
            <div class="metric-label">Postgraduate Degrees</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Education
    st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Centro Universitário Senac</h4>
            <p>Postgraduate in Artificial Intelligence for Business Strategy</p>
            <p style="color: #6c757d;">February 2024 - April 2025</p>
        </div>
        
        <div class="card">
            <h4>Centro Universitário Senac</h4>
            <p>Bachelor's in Production Engineering</p>
            <p style="color: #6c757d;">2015 - 2020</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>UNIMAIS - Faculdade Educamais</h4>
            <p>Postgraduate in Agile Models</p>
            <p style="color: #6c757d;">January 2021 - November 2021</p>
        </div>
        
        <div class="card">
            <h4>University of Michigan</h4>
            <p>Successful Negotiation, Essential Strategies and Skills</p>
            <p style="color: #6c757d;">January 2017 - June 2017</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Languages
    st.markdown("<h2>Languages</h2>", unsafe_allow_html=True)
    
    languages = {
        "Portuguese": 100,
        "English": 95,
        "French": 80
    }
    
    for lang, level in languages.items():
        st.markdown(f"""
        <div class="skill-container">
            <div style="display: flex; justify-content: space-between;">
                <span>{lang}</span>
                <span>{level}%</span>
            </div>
            <div class="skill-bar">
                <div class="skill-fill animate-skill" style="width: {level}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS PAGE
elif page == "Projects":
    # Header section
    st.markdown("""
    <div class="header-container">
        <h1>Project Portfolio</h1>
        <p>A showcase of my AI and business transformation projects</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 1: HeatGlass
    st.markdown("""
    <div class="project-card">
        <h3>🔥 HeatGlass - Emotional Call Analysis System</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("HeatGlass is an automated analysis system for audio calls (.mp3) created for Carglass. It uses AI (GPT-4 Turbo) to transcribe speech, identify sentiments, and classify the emotional temperature of conversations (calm, neutral, or critical).")
    
    st.markdown("**Key Features:**", unsafe_allow_html=True)
    st.markdown("""
    - Automated transcription and sentiment analysis of customer calls
    - Emotional temperature classification with confidence scores
    - Strategic call summary based on the most sensitive segments
    - Technical scoring through an objective checklist
    - Visual representation with red indicators for negative impacts
    """)
    
    st.markdown("**Business Impact:**", unsafe_allow_html=True)
    st.write("Reduced friction in customer service interactions and provided valuable insights for commercial and quality teams, leading to improved customer satisfaction and more effective training programs.")
    
    # Tags for HeatGlass
    st.markdown("""
    <div>
        <span class="tag">GPT-4 Turbo</span>
        <span class="tag">Sentiment Analysis</span>
        <span class="tag">Streamlit</span>
        <span class="tag">Audio Processing</span>
        <span class="tag">Customer Service</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Images for HeatGlass
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.image("895cb66e-da1d-4458-b5ec-2ae2dd25ae7b.png", caption="Initial interface with audio upload", use_column_width=True)
        except Exception as e:
            st.image("https://via.placeholder.com/800x450?text=HeatGlass+Interface", caption="Initial interface with audio upload", use_column_width=True)
    with col2:
        try:
            st.image("3c4269e5-34ea-4ce5-b8d5-bdb45bad833c.png", caption="Full analysis with checklist and risk indicators", use_column_width=True)
        except Exception as e:
            st.image("https://via.placeholder.com/800x450?text=HeatGlass+Analysis", caption="Full analysis with checklist and risk indicators", use_column_width=True)
    
    # Project 2: MirrorGlass
    st.markdown("""
    <div class="project-card">
        <h3>🔍 MirrorGlass - Image Fraud Detection System</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("MirrorGlass was created to detect visual inconsistencies in images sent by Carglass customers during service processes. The tool compares received images with a previous database, detecting duplications, inconsistencies, or abnormal patterns.")
    
    st.markdown("**Key Features:**", unsafe_allow_html=True)
    st.markdown("""
    - Advanced image comparison using computer vision techniques
    - Detection of duplicated or manipulated images
    - Metadata analysis for authenticity verification
    - Identification of suspicious patterns in customer submissions
    - Visual heatmaps highlighting potential areas of concern
    """)
    
    st.markdown("**Business Impact:**", unsafe_allow_html=True)
    st.write("Enhanced fraud prevention capabilities and improved service quality by ensuring the authenticity of customer-submitted images, resulting in significant cost savings and increased trust in the claims process.")
    
    # Tags for MirrorGlass
    st.markdown("""
    <div>
        <span class="tag">Computer Vision</span>
        <span class="tag">YOLOv8</span>
        <span class="tag">Metadata Analysis</span>
        <span class="tag">Machine Learning</span>
        <span class="tag">Fraud Prevention</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Images for MirrorGlass
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.image("239788e1-26f9-4c94-bcbf-7eb93fe76f59.png", caption="Upload interface and detection settings", use_column_width=True)
        except Exception as e:
            st.image("https://via.placeholder.com/800x450?text=MirrorGlass+Interface", caption="Upload interface and detection settings", use_column_width=True)
    with col2:
        try:
            st.image("e5130d9d-966d-451e-a050-f5b79a473dd2.png", caption="Texture analysis with Heat Map", use_column_width=True)
        except Exception as e:
            st.image("https://via.placeholder.com/800x450?text=MirrorGlass+Analysis", caption="Texture analysis with Heat Map", use_column_width=True)
    
    # Project 3: Oráculo
    st.markdown("""
    <div class="project-card">
        <h3>📚 Oráculo - Enterprise RAG System</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Oráculo is an intelligent platform based on RAG (Retrieval-Augmented Generation) that answers questions based on company documents hosted on SharePoint. The tool accesses content via Microsoft Graph API and also uses OCR and scraping with Selenium to navigate and extract data from dynamically rendered pages.")
    
    st.markdown("**Key Features:**", unsafe_allow_html=True)
    st.markdown("""
    - Integration with SharePoint via Microsoft Graph API
    - OCR and web scraping capabilities for comprehensive data access
    - Support for multiple document formats (PDF, images, Word, HTML)
    - Contextually precise responses to user queries
    - Multi-language support across Portuguese, English, and French
    """)
    
    st.markdown("**Business Impact:**", unsafe_allow_html=True)
    st.write("Significantly reduced information retrieval time, improved decision-making speed, and enhanced knowledge sharing across departments, resulting in more efficient operations and better-informed staff.")
    
    # Tags for Oráculo
    st.markdown("""
    <div>
        <span class="tag">RAG</span>
        <span class="tag">Microsoft Graph API</span>
        <span class="tag">OCR</span>
        <span class="tag">Selenium</span>
        <span class="tag">Knowledge Management</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a sample visualization for RAG system
    labels = ['Traditional Search', 'RAG System']
    values = [45, 8]
    
    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker_color=['#1E40AF', '#3B82F6'],
            text=values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title='Information Retrieval Time (minutes)',
        xaxis_title='Method',
        yaxis_title='Minutes',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Project 4: Fast Track
    st.markdown("""
    <div class="project-card">
        <h3>⚡ Fast Track - Strategic Optimization Project (Vallourec)</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("At Vallourec, the Fast Track project aimed to reduce customer response time from 30 days to just 5 days. I served as Product Owner, leading an AI initiative that automated engineering calculations and optimized order prioritization.")
    
    st.markdown("**Key Features:**", unsafe_allow_html=True)
    st.markdown("""
    - Automated engineering calculations for faster technical responses
    - Intelligent order prioritization system
    - Integration with internal company workflows
    - Connection between technical, commercial, and customer service areas
    - Real-time status tracking and reporting
    """)
    
    st.markdown("**Business Impact:**", unsafe_allow_html=True)
    st.write("Dramatically increased service agility, reduced rework, and significantly improved customer satisfaction by delivering responses 6 times faster than the previous process.")
    
    # Tags for Fast Track
    st.markdown("""
    <div>
        <span class="tag">Process Optimization</span>
        <span class="tag">Workflow Automation</span>
        <span class="tag">Engineering Calculations</span>
        <span class="tag">Customer Response</span>
        <span class="tag">Product Ownership</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a comparison chart for Fast Track
    labels = ['Before', 'After']
    values = [30, 5]  # days
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        marker_color=['#DC2626', '#10B981'],
        text=[f"{val} days" for val in values],
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Response Time Improvement',
        xaxis_title='Implementation Phase',
        yaxis_title='Days',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Project 5: SmartCost
    st.markdown("""
    <div class="project-card">
        <h3>💰 SmartCost - Intelligent Cost Recommendation (Vallourec)</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Tool developed to support financial decisions in technical projects. SmartCost analyzes material costs and available alternatives based on engineering parameters, automatically recommending more economical options.")
    
    st.markdown("**Key Features:**", unsafe_allow_html=True)
    st.markdown("""
    - Automated cost analysis of materials and components
    - Engineering parameter-based recommendations
    - Detailed reports with financial insights
    - Alternative material suggestions with cost comparisons
    - Integration with existing engineering systems
    """)
    
    st.markdown("**Business Impact:**", unsafe_allow_html=True)
    st.write("Enabled faster decision-making with lower budgetary risk by providing engineers and managers with data-driven cost optimization recommendations, resulting in significant project savings.")
    
    # Tags for SmartCost
    st.markdown("""
    <div>
        <span class="tag">Cost Optimization</span>
        <span class="tag">Financial Analysis</span>
        <span class="tag">Engineering Parameters</span>
        <span class="tag">Decision Support</span>
        <span class="tag">Reporting</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a gauge chart for cost reduction
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=18,
        title={'text': "Average Cost Reduction (%)"},
        gauge={
            'axis': {'range': [None, 50]},
            'bar': {'color': "#10B981"},
            'steps': [
                {'range': [0, 10], 'color': "#EFF6FF"},
                {'range': [10, 20], 'color': "#DBEAFE"},
                {'range': [20, 30], 'color': "#BFDBFE"},
                {'range': [30, 50], 'color': "#93C5FD"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 18
            }
        },
        number={'suffix': "%"}
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)

# EXPERIENCE PAGE
elif page == "Experience":
    st.markdown("""
    <div class="header-container">
        <h1>Professional Experience</h1>
        <p>My journey in applying AI to solve real business challenges</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience Timeline
    st.markdown("## Career Timeline", unsafe_allow_html=True)
    
    # Timeline items
    st.markdown("""
    <div class="timeline-item">
        <h4>AI Specialist | Business-Oriented Artificial Intelligence</h4>
        <h5>Carglass® Brasil</h5>
        <p class="timeline-date">April 2025 - Present</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Leading the AI transformation initiative at Carglass, focusing on developing intelligent solutions for automotive glass repair and replacement services.")
    
    st.markdown("**Key responsibilities include:**")
    st.markdown("""
    - Designing and implementing AI-driven systems for fraud detection in insurance claims
    - Developing emotional intelligence solutions for call center operations
    - Creating RAG-based knowledge systems to enhance technical support
    - Collaborating with executive stakeholders to align AI initiatives with business strategy
    """)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Business Analyst</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">January 2021 - April 2025</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Led business analysis and AI implementation initiatives at Vallourec.")
    
    st.markdown("**Key achievements:**")
    st.markdown("""
    - Implemented agile methodology across multiple departments
    - Managed backlog prioritization based on client needs and business impact
    - Created and analyzed KPIs, dashboards, and performance reports
    - Monitored execution of demands with executive professionals
    - Served as Product Owner, deciding which features and functionality to build
    - Analyzed user needs and supported customers in adopting new tools
    """)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Sales Specialist</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">January 2019 - January 2021</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Managed sales operations across automotive and structural sectors:")
    
    st.markdown("""
    - Managed active contacts and prospected for new customers
    - Analyzed business opportunities through customer segmentation
    - Performed data analysis using CRM Dynamics and Power BI with DAX
    - Developed VBA tools for process automation
    - Managed customer portfolios and sales orders via SAP
    - Conducted price analysis and developed calculation tools for budgeting
    """)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Intern</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">August 2017 - January 2019</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Started my career at Vallourec as an intern in the Powergen Sales department, gaining foundational experience in business operations and customer relationship management.")
    
    # Key achievements
    st.markdown("## Key Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>AI Implementation Success</h4>
            <p>Led the development and implementation of AI solutions that reduced operational costs by €1.5M annually and improved customer satisfaction scores by 22%.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Process Optimization</h4>
            <p>Redesigned business processes using AI and automation, resulting in a 45% reduction in processing time and a 30% decrease in error rates.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Team Leadership</h4>
            <p>Successfully led cross-functional teams of up to 12 members, bridging technical and business perspectives to deliver complex AI projects on time and within budget.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Data-Driven Decision Making</h4>
            <p>Implemented data analytics frameworks that enabled executive teams to make informed decisions, resulting in 28% improved resource allocation.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills growth visualization
    st.markdown("## Skills Evolution")
    
    # Sample data for skills evolution
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ai_skills = [10, 15, 20, 30, 45, 60, 75, 85, 95]
    business_skills = [20, 35, 50, 65, 75, 80, 85, 90, 95]
    technical_skills = [15, 25, 40, 55, 65, 75, 80, 85, 90]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years, 
        y=ai_skills,
        mode='lines+markers',
        name='AI & Data Science',
        line=dict(color='#1E40AF', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, 
        y=business_skills,
        mode='lines+markers',
        name='Business Analysis',
        line=dict(color='#4F46E5', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, 
        y=technical_skills,
        mode='lines+markers',
        name='Technical Implementation',
        line=dict(color='#60A5FA', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Professional Skills Development Over Time',
        xaxis_title='Year',
        yaxis_title='Proficiency Level (%)',
        legend_title='Skill Category',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0, 100]),
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)

# SKILLS PAGE
elif page == "Skills":
    st.markdown("""
    <div class="header-container">
        <h1>Skills & Expertise</h1>
        <p>Professional capabilities and technical competencies</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown("## Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### AI & Data Science")
        
        ai_skills = {
            "Large Language Models (GPT, RAG)": 95,
            "Computer Vision": 85,
            "Natural Language Processing": 90,
            "Machine Learning": 85,
            "Data Analysis & Visualization": 90
        }
        
        for skill, level in ai_skills.items():
            st.markdown(f"""
            <div class="skill-container">
                <div style="display: flex; justify-content: space-between;">
                    <span>{skill}</span>
                    <span>{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill animate-skill" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Development & Tools")
        
        dev_skills = {
            "Python": 90,
            "Streamlit": 95,
            "Power BI & DAX": 85,
            "SQL": 80,
            "SharePoint Integration": 85
        }
        
        for skill, level in dev_skills.items():
            st.markdown(f"""
            <div class="skill-container">
                <div style="display: flex; justify-content: space-between;">
                    <span>{skill}</span>
                    <span>{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill animate-skill" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Business Skills
    st.markdown("## Business Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Management & Leadership")
        
        mgmt_skills = {
            "Agile Methodologies": 95,
            "Product Ownership": 90,
            "Project Management": 85,
            "Team Leadership": 90
        }
        
        for skill, level in mgmt_skills.items():
            st.markdown(f"""
            <div class="skill-container">
                <div style="display: flex; justify-content: space-between;">
                    <span>{skill}</span>
                    <span>{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill animate-skill" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Business Analysis")
        
        ba_skills = {
            "KPI Development & Analysis": 95,
            "Process Optimization": 90,
            "User Acceptance Testing": 85,
            "Requirements Gathering": 90
        }
        
        for skill, level in ba_skills.items():
            st.markdown(f"""
            <div class="skill-container">
                <div style="display: flex; justify-content: space-between;">
                    <span>{skill}</span>
                    <span>{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill animate-skill" style="width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("## Certifications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Communication & Public Speaking</h4>
            <p>Certified Professional</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Data Analysis</h4>
            <p>Advanced Certification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Intelligent Productivity</h4>
            <p>Professional Certification</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tools & Technologies
    st.markdown("## Tools & Technologies")
    
    # Define technologies
    technologies = [
        "Python", "Streamlit", "GPT-4", "RAG", "LangChain", "Computer Vision", 
        "NLP", "Power BI", "SQL", "SharePoint", "Azure", "Pandas", 
        "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", 
        "Seaborn", "Git", "Docker", "REST APIs", "Agile", "Scrum", 
        "Kanban", "JIRA", "Confluence", "SAP", "VBA", "Excel"
    ]
    
    # Display tech tags
    st.markdown('<div class="card" style="text-align: center; padding: 1.5rem;">', unsafe_allow_html=True)
    
    for tech in technologies:
        st.markdown(f'<span class="tag">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# CONTACT PAGE
elif page == "Contact":
    st.markdown("""
    <div class="header-container">
        <h1>Contact Information</h1>
        <p>Let's discuss how AI can transform your business</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Contact Details</h3>
            <p><strong>Email:</strong> viniciuspaschoa1@hotmail.com</p>
            <p><strong>Phone:</strong> +55 (11) 93801-2431</p>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/viniciuspaschoa" target="_blank" style="color: #1E40AF;">linkedin.com/in/viniciuspaschoa</a></p>
            <p><strong>Location:</strong> Paris, Île-de-France, France</p>
            <p><strong>Citizenship:</strong> EU Citizen</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Professional Interests</h3>
            <p>I'm currently open to discussing:</p>
            <ul>
                <li>Business Analyst roles</li>
                <li>Product Owner positions</li>
                <li>Product Manager opportunities</li>
                <li>AI Strategy consulting</li>
                <li>Speaking engagements on AI implementation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Languages section
    st.markdown("""
    <div class="card">
        <h3>Languages</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: space-around;">
            <div style="flex: 1; min-width: 150px; text-align: center;">
                <h4>Portuguese</h4>
                <p>Native</p>
            </div>
            <div style="flex: 1; min-width: 150px; text-align: center;">
                <h4>English</h4>
                <p>Full Professional</p>
            </div>
            <div style="flex: 1; min-width: 150px; text-align: center;">
                <h4>French</h4>
                <p>Professional Working</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("## Send me a message")
    
    with st.form(key="contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
        with col2:
            email = st.text_input("Email")
        
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and subject and message:
                st.success("Thank you for your message! I'll get back to you soon.")
            else:
                st.error("Please fill in all fields before submitting.")

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Vinícius Paschoa | AI Specialist | Business-Oriented Artificial Intelligence</p>
    <p>Exploring the future with Artificial Intelligence</p>
</div>
""", unsafe_allow_html=True)
