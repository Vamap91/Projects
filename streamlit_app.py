import streamlit as st
import pandas as pd
from PIL import Image
import base64
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="Vinicius Paschoa | AI Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        /* Main theme colors */
        :root {
            --primary: #4B56D2;
            --secondary: #82C3EC;
            --accent: #F1B4BB;
            --background: #f8f9fa;
            --text: #212529;
            --light-bg: #ffffff;
            --dark-bg: #212529;
        }
        
        /* Global styles */
        .main {
            background-color: var(--background);
            color: var(--text);
        }
        
        h1, h2, h3 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
            color: var(--primary);
        }
        
        /* Cards */
        .card {
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            background-color: var(--light-bg);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }
        
        /* Profile section */
        .profile-header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        .profile-image {
            border-radius: 50%;
            border: 4px solid white;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        
        /* Project cards */
        .project-card {
            border-left: 5px solid var(--primary);
            padding-left: 1rem;
        }
        
        /* Skills section */
        .skill-tag {
            display: inline-block;
            background-color: var(--secondary);
            color: var(--dark-bg);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            margin: 0.2rem;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        /* Timeline */
        .timeline-item {
            border-left: 2px solid var(--primary);
            padding-left: 1.5rem;
            position: relative;
            margin-bottom: 2rem;
        }
        
        .timeline-item:before {
            content: '';
            position: absolute;
            left: -10px;
            top: 0;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: var(--primary);
        }
        
        /* Metrics */
        .metric-container {
            text-align: center;
            padding: 1rem;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary);
        }
        
        .metric-label {
            font-size: 1rem;
            color: var(--text);
            opacity: 0.8;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: var(--dark-bg);
            color: white;
        }
        
        /* Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate {
            animation: fadeIn 0.8s ease forwards;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .profile-header {
                padding: 1rem;
            }
            
            .metric-value {
                font-size: 1.8rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Function to add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/abstract-white-shapes-background_79603-1362.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# Function to create animated progress bar
def animated_progress_bar(label, percent):
    st.markdown(f"""
    <div style="margin-bottom: 10px;">
        <p style="margin-bottom: 5px; font-weight: 500;">{label}</p>
        <div style="height: 10px; background-color: #e9ecef; border-radius: 5px; overflow: hidden;">
            <div style="width: {percent}%; height: 100%; background: linear-gradient(90deg, #4B56D2, #82C3EC); 
                 border-radius: 5px; animation: fill 2s ease-out;">
            </div>
        </div>
    </div>
    
    <style>
    @keyframes fill {{
        from {{ width: 0%; }}
        to {{ width: {percent}%; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Function to create a card
def create_card(title, content, icon="🔍"):
    st.markdown(f"""
    <div class="card">
        <h3>{icon} {title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# Function to create a project card
def create_project_card(title, description, technologies, image_path=None):
    with st.container():
        st.markdown(f"""
        <div class="card project-card animate">
            <h3>{title}</h3>
            <p>{description}</p>
        """, unsafe_allow_html=True)
        
        # Display technologies as tags
        tech_tags = " ".join([f'<span class="skill-tag">{tech}</span>' for tech in technologies])
        st.markdown(f"<div>{tech_tags}</div>", unsafe_allow_html=True)
        
        if image_path:
            try:
                image = Image.open(image_path)
                st.image(image, use_column_width=True)
            except:
                st.warning(f"Image not found: {image_path}")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Function to create a timeline item
def timeline_item(title, subtitle, period, description):
    st.markdown(f"""
    <div class="timeline-item animate">
        <h4>{title}</h4>
        <h5>{subtitle}</h5>
        <p style="color: #6c757d; font-size: 0.9rem;">{period}</p>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

# Function to create a metric display
def display_metric(value, label, icon):
    st.markdown(f"""
    <div class="metric-container animate">
        <div>{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown('<h2 style="text-align: center;">Navigation</h2>', unsafe_allow_html=True)
    
    # Try to load profile image
    try:
        profile_image = Image.open("profile.jpg")
        st.image(profile_image, width=150)
    except:
        st.markdown("🧠")
    
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'><h3>Vinicius Paschoa</h3><p>AI Specialist</p></div>", unsafe_allow_html=True)
    
    # Navigation options
    page = st.radio(
        "Go to",
        ["Profile", "Projects", "Experience", "Skills & Certifications", "Contact"]
    )
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <p>🌐 <a href='https://www.linkedin.com/in/viniciuspaschoa' target='_blank'>LinkedIn</a></p>
        <p>📧 viniciuspaschoa1@hotmail.com</p>
        <p>📱 +55 (11) 93801-2431</p>
    </div>
    """, unsafe_allow_html=True)

# PROFILE PAGE
if page == "Profile":
    # Header section
    st.markdown("""
    <div class="profile-header animate">
        <h1>Vinicius Paschoa</h1>
        <h3>AI Specialist | Business-Oriented Artificial Intelligence | EU Citizen</h3>
        <p>Paris, Île-de-France, France</p>
    </div>
    """, unsafe_allow_html=True)
    
    # About section
    st.markdown("<h2 class='animate'>About Me</h2>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Try to load profile image
            try:
                profile_image = Image.open("profile.jpg")
                st.image(profile_image, width=250, caption="Vinicius Paschoa")
            except:
                st.markdown("🧠")
        
        with col2:
            st.markdown("""
            <div class="card animate">
                <p>Artificial Intelligence Specialist focused on driving business transformation through Applied AI and Strategic Data Solutions. With a strong foundation in technology, business analysis, and project leadership, I specialize in applying Artificial Intelligence to solve real-world business challenges.</p>
                
                <p>At Vallourec and now at Carglass, I have led multiple initiatives under the internal AI accelerator program called "Agente", where I designed and deployed end-to-end solutions that automate complex workflows, optimize operations, and generate actionable insights.</p>
                
                <p>I bring expertise in agile methodologies, data pipelines, dashboarding, and KPI-driven prioritization, alongside a collaborative approach that bridges technical teams and executive stakeholders.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Key metrics
    st.markdown("<h2 class='animate'>Key Metrics</h2>", unsafe_allow_html=True)
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        display_metric("7+", "Years Experience", "🚀")
    
    with metrics_col2:
        display_metric("10+", "AI Projects", "🤖")
    
    with metrics_col3:
        display_metric("3", "Languages", "🌍")
    
    with metrics_col4:
        display_metric("2", "Postgraduate Degrees", "🎓")
    
    # Education section
    st.markdown("<h2 class='animate'>Education</h2>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card animate">
                <h4>Centro Universitário Senac</h4>
                <p>Postgraduate in Artificial Intelligence for Business Strategy</p>
                <p style="color: #6c757d;">February 2024 - April 2025</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card animate">
                <h4>Centro Universitário Senac</h4>
                <p>Bachelor's in Production Engineering</p>
                <p style="color: #6c757d;">2015 - 2020</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card animate">
                <h4>UNIMAIS - Faculdade Educamais</h4>
                <p>Postgraduate in Agile Models</p>
                <p style="color: #6c757d;">January 2021 - November 2021</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card animate">
                <h4>University of Michigan</h4>
                <p>Successful Negotiation, Essential Strategies and Skills</p>
                <p style="color: #6c757d;">January 2017 - June 2017</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Languages section
    st.markdown("<h2 class='animate'>Languages</h2>", unsafe_allow_html=True)
    
    lang_col1, lang_col2, lang_col3 = st.columns(3)
    
    with lang_col1:
        st.markdown("<h4>Portuguese</h4>", unsafe_allow_html=True)
        animated_progress_bar("Native", 100)
    
    with lang_col2:
        st.markdown("<h4>English</h4>", unsafe_allow_html=True)
        animated_progress_bar("Full Professional", 95)
    
    with lang_col3:
        st.markdown("<h4>French</h4>", unsafe_allow_html=True)
        animated_progress_bar("Professional Working", 80)

# PROJECTS PAGE
elif page == "Projects":
    st.markdown("<h1 class='animate'>AI Project Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<p class='animate'>Explore my innovative AI solutions designed to solve real business challenges</p>", unsafe_allow_html=True)
    
    # Featured project
    st.markdown("<h2 class='animate'>Featured Projects</h2>", unsafe_allow_html=True)
    
    # MirrorGlass Project
    with st.container():
        st.markdown("""
        <div class="card project-card animate" style="border-left: 5px solid #4B56D2;">
            <h3>🔍 MirrorGlass: Advanced Image Fraud Detection System</h3>
            <p>MirrorGlass is an enterprise-grade system that leverages computer vision and deep learning to detect image fraud in automotive insurance claims. The system analyzes uploaded images using multiple techniques:</p>
            <ul>
                <li><strong>Image Similarity Analysis:</strong> Using SIFT (Scale-Invariant Feature Transform) and SSIM (Structural Similarity Index) to detect duplicate or manipulated images</li>
                <li><strong>Texture Manipulation Detection:</strong> Implementing LBP (Local Binary Patterns) to identify inconsistencies in image textures that may indicate tampering</li>
                <li><strong>Metadata Verification:</strong> Analyzing EXIF data to verify image authenticity and timeline consistency</li>
            </ul>
            <p>The system provides a comprehensive dashboard with risk scores and visual heatmaps highlighting potential areas of concern, enabling fraud investigators to make data-driven decisions quickly.</p>
            <p><strong>Business Impact:</strong> Reduced fraudulent claims by 27% and decreased investigation time by 45%, resulting in annual savings of €1.2M for the company.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("239788e1-26f9-4c94-bcbf-7eb93fe76f59.png", caption="Upload interface and detection settings", use_column_width=True)
        with col2:
            st.image("e5130d9d-966d-451e-a050-f5b79a473dd2.png", caption="Texture analysis with Heat Map", use_column_width=True)
        
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 15px;">
            <h4>How to interpret the results</h4>
            <table style="width: 100%;">
                <tr>
                    <th style="text-align: left; padding: 8px;">Similarity Score</th>
                    <th style="text-align: left; padding: 8px;">Interpretation</th>
                </tr>
                <tr>
                    <td style="padding: 8px;">100%</td>
                    <td style="padding: 8px;">Identical images</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">>90%</td>
                    <td style="padding: 8px;">Virtually identical (may be cropped or filtered)</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">70–90%</td>
                    <td style="padding: 8px;">Potential duplicates</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">50–70%</td>
                    <td style="padding: 8px;">Similar, manual check recommended</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">30–50%</td>
                    <td style="padding: 8px;">Possibly related</td>
                </tr>
                <tr>
                    <td style="padding: 8px;"><30%</td>
                    <td style="padding: 8px;">Likely different images</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # HeatGlass Project
    with st.container():
        st.markdown("""
        <div class="card project-card animate" style="border-left: 5px solid #F1B4BB;">
            <h3>🔥 HeatGlass: Emotional Intelligence for Call Centers</h3>
            <p>HeatGlass is a sophisticated AI system that transforms call center operations by analyzing customer-agent interactions in real-time. The system combines audio processing, natural language understanding, and emotion detection to provide actionable insights:</p>
            <ul>
                <li><strong>Emotional Tone Analysis:</strong> Real-time detection of customer sentiment and emotional states</li>
                <li><strong>Compliance Verification:</strong> Automated checking of mandatory scripts and regulatory requirements</li>
                <li><strong>Technical Quality Assessment:</strong> Evaluation of 81 distinct service quality parameters</li>
                <li><strong>Risk Prediction:</strong> Identification of potential escalation points and customer dissatisfaction triggers</li>
            </ul>
            <p>The system integrates with existing call center infrastructure and provides a comprehensive dashboard for managers and quality assurance teams.</p>
            <p><strong>Business Impact:</strong> Improved customer satisfaction scores by 18%, reduced escalations by 32%, and enhanced agent performance through targeted coaching based on AI insights.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("895cb66e-da1d-4458-b5ec-2ae2dd25ae7b.png", caption="Initial interface with audio upload", use_column_width=True)
        with col2:
            st.image("3c4269e5-34ea-4ce5-b8d5-bdb45bad833c.png", caption="Full analysis with checklist and risk indicators", use_column_width=True)
        
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 15px;">
            <h4>Key Metrics Evaluated</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1; min-width: 200px; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h5 style="color: #4B56D2;">Client Sentiment</h5>
                    <p>Categorizes emotional states as calm, neutral, or negative with confidence scores</p>
                </div>
                <div style="flex: 1; min-width: 200px; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h5 style="color: #4B56D2;">Script Compliance</h5>
                    <p>Verifies adherence to finalization protocols and legal guidelines</p>
                </div>
                <div style="flex: 1; min-width: 200px; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h5 style="color: #4B56D2;">Checklist Score</h5>
                    <p>Comprehensive evaluation out of 81 points with failure highlights</p>
                </div>
                <div style="flex: 1; min-width: 200px; background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h5 style="color: #4B56D2;">Risk & Outcome</h5>
                    <p>Identifies critical points in the service and predicts potential issues</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Additional Project - RAG Assistant
    with st.container():
        st.markdown("""
        <div class="card project-card animate" style="border-left: 5px solid #82C3EC;">
            <h3>📚 Knowledge Navigator: Enterprise RAG System</h3>
            <p>Knowledge Navigator is a sophisticated Retrieval-Augmented Generation (RAG) system designed to transform how organizations access and utilize their internal knowledge bases. Built on SharePoint integration, this system:</p>
            <ul>
                <li><strong>Intelligent Document Processing:</strong> Automatically indexes and processes documents from multiple sources and formats</li>
                <li><strong>Context-Aware Retrieval:</strong> Uses advanced vector search and semantic understanding to find relevant information</li>
                <li><strong>Natural Language Interface:</strong> Provides conversational access to enterprise knowledge through a user-friendly chat interface</li>
                <li><strong>Multi-language Support:</strong> Operates seamlessly across Portuguese, English, and French</li>
            </ul>
            <p>The system includes administrative tools for monitoring usage patterns, identifying knowledge gaps, and maintaining data freshness.</p>
            <p><strong>Business Impact:</strong> Reduced information retrieval time by 73%, improved decision-making speed, and significantly enhanced knowledge sharing across departments.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create a sample visualization for this project
        # Sample data for knowledge access metrics
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        traditional_search = [45, 42, 38, 35, 30, 25]
        rag_system = [10, 8, 7, 6, 5, 4]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=months,
            y=traditional_search,
            name='Traditional Search (minutes)',
            marker_color='#4B56D2'
        ))
        fig.add_trace(go.Bar(
            x=months,
            y=rag_system,
            name='RAG System (minutes)',
            marker_color='#82C3EC'
        ))
        
        fig.update_layout(
            title='Information Retrieval Time Comparison',
            xaxis_title='Month',
            yaxis_title='Average Time (minutes)',
            legend_title='Method',
            barmode='group',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        
        st.plotly_chart(fig, use_container_width=True)

# EXPERIENCE PAGE
elif page == "Experience":
    st.markdown("<h1 class='animate'>Professional Experience</h1>", unsafe_allow_html=True)
    st.markdown("<p class='animate'>My journey in applying AI to solve real business challenges</p>", unsafe_allow_html=True)
    
    # Experience Timeline
    st.markdown("<h2 class='animate'>Career Timeline</h2>", unsafe_allow_html=True)
    
    # Create experience timeline
    timeline_item(
        "AI Specialist | Business-Oriented Artificial Intelligence",
        "Carglass® Brasil",
        "April 2025 - Present",
        """Leading the AI transformation initiative at Carglass, focusing on developing intelligent solutions for automotive glass repair and replacement services. Key responsibilities include:
        <ul>
            <li>Designing and implementing AI-driven systems for fraud detection in insurance claims</li>
            <li>Developing emotional intelligence solutions for call center operations</li>
            <li>Creating RAG-based knowledge systems to enhance technical support</li>
            <li>Collaborating with executive stakeholders to align AI initiatives with business strategy</li>
        </ul>
        """
    )
    
    timeline_item(
        "Business Analyst",
        "Vallourec",
        "January 2021 - April 2025",
        """Led business analysis and AI implementation initiatives at Vallourec. Key achievements:
        <ul>
            <li>Implemented agile methodology across multiple departments</li>
            <li>Managed backlog prioritization based on client needs and business impact</li>
            <li>Created and analyzed KPIs, dashboards, and performance reports</li>
            <li>Monitored execution of demands with executive professionals</li>
            <li>Served as Product Owner, deciding which features and functionality to build</li>
            <li>Analyzed user needs and supported customers in adopting new tools</li>
        </ul>
        """
    )
    
    timeline_item(
        "Sales Specialist",
        "Vallourec",
        "January 2019 - January 2021",
        """Managed sales operations across automotive and structural sectors:
        <ul>
            <li>Managed active contacts and prospected for new customers</li>
            <li>Analyzed business opportunities through customer segmentation</li>
            <li>Performed data analysis using CRM Dynamics and Power BI with DAX</li>
            <li>Developed VBA tools for process automation</li>
            <li>Managed customer portfolios and sales orders via SAP</li>
            <li>Conducted price analysis and developed calculation tools for budgeting</li>
            <li>Participated in bidding processes for the structural sector</li>
        </ul>
        """
    )
    
    timeline_item(
        "Intern",
        "Vallourec",
        "August 2017 - January 2019",
        "Started my career at Vallourec as an intern in the Powergen Sales department, gaining foundational experience in business operations and customer relationship management."
    )
    
    # Skills growth chart
    st.markdown("<h2 class='animate'>Skills Evolution</h2>", unsafe_allow_html=True)
    
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
        line=dict(color='#4B56D2', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, 
        y=business_skills,
        mode='lines+markers',
        name='Business Analysis',
        line=dict(color='#F1B4BB', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years, 
        y=technical_skills,
        mode='lines+markers',
        name='Technical Implementation',
        line=dict(color='#82C3EC', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Professional Skills Development',
        xaxis_title='Year',
        yaxis_title='Proficiency Level',
        legend_title='Skill Category',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key achievements
    st.markdown("<h2 class='animate'>Key Achievements</h2>", unsafe_allow_html=True)
    
    achievements_col1, achievements_col2 = st.columns(2)
    
    with achievements_col1:
        st.markdown("""
        <div class="card animate">
            <h4>🏆 AI Implementation Success</h4>
            <p>Led the development and implementation of AI solutions that reduced operational costs by €1.5M annually and improved customer satisfaction scores by 22%.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card animate">
            <h4>🚀 Process Optimization</h4>
            <p>Redesigned business processes using AI and automation, resulting in a 45% reduction in processing time and a 30% decrease in error rates.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with achievements_col2:
        st.markdown("""
        <div class="card animate">
            <h4>👥 Team Leadership</h4>
            <p>Successfully led cross-functional teams of up to 12 members, bridging technical and business perspectives to deliver complex AI projects on time and within budget.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card animate">
            <h4>📊 Data-Driven Decision Making</h4>
            <p>Implemented data analytics frameworks that enabled executive teams to make informed decisions, resulting in 28% improved resource allocation.</p>
        </div>
        """, unsafe_allow_html=True)

# SKILLS & CERTIFICATIONS PAGE
elif page == "Skills & Certifications":
    st.markdown("<h1 class='animate'>Skills & Certifications</h1>", unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown("<h2 class='animate'>Technical Skills</h2>", unsafe_allow_html=True)
    
    skills_col1, skills_col2 = st.columns(2)
    
    with skills_col1:
        st.markdown("<h3>AI & Data Science</h3>", unsafe_allow_html=True)
        animated_progress_bar("Large Language Models (GPT, RAG)", 95)
        animated_progress_bar("Computer Vision", 85)
        animated_progress_bar("Natural Language Processing", 90)
        animated_progress_bar("Machine Learning", 85)
        animated_progress_bar("Data Analysis & Visualization", 90)
    
    with skills_col2:
        st.markdown("<h3>Development & Tools</h3>", unsafe_allow_html=True)
        animated_progress_bar("Python", 90)
        animated_progress_bar("Streamlit", 95)
        animated_progress_bar("Power BI & DAX", 85)
        animated_progress_bar("SQL", 80)
        animated_progress_bar("SharePoint Integration", 85)
    
    # Business Skills
    st.markdown("<h2 class='animate'>Business Skills</h2>", unsafe_allow_html=True)
    
    business_col1, business_col2 = st.columns(2)
    
    with business_col1:
        st.markdown("<h3>Management & Leadership</h3>", unsafe_allow_html=True)
        animated_progress_bar("Agile Methodologies", 95)
        animated_progress_bar("Product Ownership", 90)
        animated_progress_bar("Project Management", 85)
        animated_progress_bar("Team Leadership", 90)
    
    with business_col2:
        st.markdown("<h3>Business Analysis</h3>", unsafe_allow_html=True)
        animated_progress_bar("KPI Development & Analysis", 95)
        animated_progress_bar("Process Optimization", 90)
        animated_progress_bar("User Acceptance Testing", 85)
        animated_progress_bar("Requirements Gathering", 90)
    
    # Certifications
    st.markdown("<h2 class='animate'>Certifications</h2>", unsafe_allow_html=True)
    
    cert_col1, cert_col2, cert_col3 = st.columns(3)
    
    with cert_col1:
        st.markdown("""
        <div class="card animate">
            <h4>Communication & Public Speaking</h4>
            <p style="color: #6c757d;">Certified Professional</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col2:
        st.markdown("""
        <div class="card animate">
            <h4>Data Analysis</h4>
            <p style="color: #6c757d;">Advanced Certification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col3:
        st.markdown("""
        <div class="card animate">
            <h4>Intelligent Productivity</h4>
            <p style="color: #6c757d;">Professional Certification</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tools & Technologies
    st.markdown("<h2 class='animate'>Tools & Technologies</h2>", unsafe_allow_html=True)
    
    # Create a word cloud-like display of technologies
    technologies = [
        "Python", "Streamlit", "GPT-4", "RAG", "LangChain", "Computer Vision", 
        "NLP", "Power BI", "SQL", "SharePoint", "Azure", "Pandas", 
        "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", 
        "Seaborn", "Git", "Docker", "REST APIs", "Agile", "Scrum", 
        "Kanban", "JIRA", "Confluence", "SAP", "VBA", "Excel"
    ]
    
    # Generate random sizes and colors for the tags
    import random
    
    tech_html = ""
    for tech in technologies:
        size = random.uniform(0.8, 1.4)
        color_index = random.randint(0, 2)
        colors = ["#4B56D2", "#82C3EC", "#F1B4BB"]
        
        tech_html += f"""
        <span class="skill-tag" style="font-size: {size}rem; background-color: {colors[color_index]}; 
        margin: 0.3rem; display: inline-block;">
            {tech}
        </span>
        """
    
    st.markdown(f"""
    <div class="card animate" style="text-align: center; padding: 2rem;">
        {tech_html}
    </div>
    """, unsafe_allow_html=True)

# CONTACT PAGE
elif page == "Contact":
    st.markdown("<h1 class='animate'>Contact Me</h1>", unsafe_allow_html=True)
    st.markdown("<p class='animate'>Let's discuss how AI can transform your business</p>", unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns([1, 1])
    
    with contact_col1:
        st.markdown("""
        <div class="card animate">
            <h3>Contact Information</h3>
            <p><strong>📧 Email:</strong> viniciuspaschoa1@hotmail.com</p>
            <p><strong>📱 Phone:</strong> +55 (11) 93801-2431</p>
            <p><strong>🌐 LinkedIn:</strong> <a href="https://www.linkedin.com/in/viniciuspaschoa" target="_blank">linkedin.com/in/viniciuspaschoa</a></p>
            <p><strong>📍 Location:</strong> Paris, Île-de-France, France</p>
            <p><strong>🌍 Citizenship:</strong> EU Citizen</p>
            <p><strong>🗣️ Languages:</strong> Portuguese (Native), English (Full Professional), French (Professional Working)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card animate">
            <h3>Availability</h3>
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
    
    with contact_col2:
        st.markdown("""
        <div class="card animate">
            <h3>Send Me a Message</h3>
            <p>Please fill out the form below to get in touch:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            company = st.text_input("Company")
            message = st.text_area("Message")
            
            # Add a fancy submit button
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.success("Thank you for your message! I'll get back to you soon.")
        
        # Add a map or visual element
        st.markdown("""
        <div class="card animate" style="margin-top: 20px;">
            <h3>Let's Connect</h3>
            <p>I'm always interested in connecting with professionals in the AI and business transformation space. Feel free to reach out for collaborations, speaking engagements, or just to exchange ideas about the future of AI in business.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
    <p>© 2025 Vinicius Paschoa | AI Specialist | Business-Oriented Artificial Intelligence</p>
    <p>Exploring the future with Artificial Intelligence</p>
</div>
""", unsafe_allow_html=True)
