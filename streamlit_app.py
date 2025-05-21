import streamlit as st
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Vinícius Paschoa | AI Specialist",
    page_icon="🤖",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    /* Estilos gerais */
    body {
        font-family: 'Inter', sans-serif;
        color: #1E293B;
        background-color: #F8FAFC;
    }
    
    /* Cabeçalho */
    .header-container {
        padding: 2rem 0;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .header-container h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #1E40AF;
    }
    
    .header-container p {
        font-size: 1.25rem;
        color: #64748B;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    /* Barras de habilidades */
    .skill-container {
        margin-bottom: 1rem;
    }
    
    .skill-bar {
        height: 0.5rem;
        background-color: #E2E8F0;
        border-radius: 9999px;
        overflow: hidden;
        margin-top: 0.25rem;
    }
    
    .skill-fill {
        height: 100%;
        background-color: #3B82F6;
        border-radius: 9999px;
    }
    
    @keyframes fillAnimation {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    .animate-skill {
        animation: fillAnimation 1.5s ease-out forwards;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 3px solid #3B82F6;
        padding-left: 1.5rem;
        position: relative;
        margin-bottom: 2rem;
    }
    
    .timeline-item:before {
        content: "";
        position: absolute;
        left: -0.75rem;
        top: 0.25rem;
        width: 1.5rem;
        height: 1.5rem;
        border-radius: 50%;
        background-color: #3B82F6;
    }
    
    .timeline-date {
        color: #64748B;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    
    /* Project cards */
    .project-card {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Tags */
    .tag {
        display: inline-block;
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin: 0.25rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #E2E8F0;
        color: #64748B;
    }
</style>
""", unsafe_allow_html=True)

# Navegação
pages = {
    "Home": "🏠",
    "Experience": "💼",
    "Skills": "🧠",
    "Projects": "🚀",
    "Contact": "📬"
}

# Barra lateral
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", list(pages.keys()), format_func=lambda x: f"{pages[x]} {x}")

# Definir conteúdo com base na página selecionada
if page == "Home":
    st.markdown("""
    <div class="header-container">
        <h1>Vinícius Paschoa</h1>
        <p>AI Specialist | Business-Oriented Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Conteúdo da página inicial aqui
    st.write("Conteúdo da página inicial")

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
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/viniciuspaschoa" target="_blank">linkedin.com/in/viniciuspaschoa</a></p>
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
        <div style="display: flex; flex-wrap: wrap; gap: 2rem;">
            <div style="flex: 1; min-width: 150px;">
                <h4>Portuguese</h4>
                <p>Native</p>
            </div>
            <div style="flex: 1; min-width: 150px;">
                <h4>English</h4>
                <p>Full Professional</p>
            </div>
            <div style="flex: 1; min-width: 150px;">
                <h4>French</h4>
                <p>Professional Working</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("<h2>Send me a message</h2>", unsafe_allow_html=True)
    
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
            st.success("Thank you for your message! I'll get back to you soon.")

    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Vinícius Paschoa | AI Specialist | Business-Oriented Artificial Intelligence</p>
        <p>Exploring the future with Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown("""
    <div class="header-container">
        <h1>Skills & Expertise</h1>
        <p>Professional capabilities and technical competencies</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3>AI & Data Science</h3>", unsafe_allow_html=True)
        
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
        st.markdown("<h3>Development & Tools</h3>", unsafe_allow_html=True)
        
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
    st.markdown("<h2>Business Skills</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3>Management & Leadership</h3>", unsafe_allow_html=True)
        
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
        st.markdown("<h3>Business Analysis</h3>", unsafe_allow_html=True)
        
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
    st.markdown("<h2>Certifications</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Communication & Public Speaking</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Certified Professional")
    
    with col2:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Data Analysis</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Advanced Certification")
    
    with col3:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h4>Intelligent Productivity</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Professional Certification")
    
    # Tools & Technologies
    st.markdown("<h2>Tools & Technologies</h2>", unsafe_allow_html=True)
    
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

elif page == "Experience":
    st.markdown("""
    <div class="header-container">
        <h1>Professional Experience</h1>
        <p>My journey in applying AI to solve real business challenges</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience Timeline
    st.markdown("<h2>Career Timeline</h2>", unsafe_allow_html=True)
    
    # Timeline items
    st.markdown("""
    <div class="timeline-item">
        <h4>AI Specialist | Business-Oriented Artificial Intelligence</h4>
        <h5>Carglass® Brasil</h5>
        <p class="timeline-date">April 2025 - Present</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Leading the AI transformation initiative at Carglass, focusing on developing intelligent solutions for automotive glass repair and replacement services.")
    
    st.markdown("<p>Key responsibilities include:</p>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Designing and implementing AI-driven systems for fraud detection in insurance claims</li>
        <li>Developing emotional intelligence solutions for call center operations</li>
        <li>Creating RAG-based knowledge systems to enhance technical support</li>
        <li>Collaborating with executive stakeholders to align AI initiatives with business strategy</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Business Analyst</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">January 2021 - April 2025</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Led business analysis and AI implementation initiatives at Vallourec.")
    
    st.markdown("<p>Key achievements:</p>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Implemented agile methodology across multiple departments</li>
        <li>Managed backlog prioritization based on client needs and business impact</li>
        <li>Created and analyzed KPIs, dashboards, and performance reports</li>
        <li>Monitored execution of demands with executive professionals</li>
        <li>Served as Product Owner, deciding which features and functionality to build</li>
        <li>Analyzed user needs and supported customers in adopting new tools</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Sales Specialist</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">January 2019 - January 2021</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Managed sales operations across automotive and structural sectors:")
    
    st.markdown("""
    <ul>
        <li>Managed active contacts and prospected for new customers</li>
        <li>Analyzed business opportunities through customer segmentation</li>
        <li>Performed data analysis using CRM Dynamics and Power BI with DAX</li>
        <li>Developed VBA tools for process automation</li>
        <li>Managed customer portfolios and sales orders via SAP</li>
        <li>Conducted price analysis and developed calculation tools for budgeting</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <h4>Intern</h4>
        <h5>Vallourec</h5>
        <p class="timeline-date">August 2017 - January 2019</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Started my career at Vallourec as an intern in the Powergen Sales department, gaining foundational experience in business operations and customer relationship management.")
    
    # Key achievements
    st.markdown("<h2>Key Achievements</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>AI Implementation Success</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Led the development and implementation of AI solutions that reduced operational costs by €1.5M annually and improved customer satisfaction scores by 22%.")
        
        st.markdown("""
        <div class="card">
            <h4>Process Optimization</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Redesigned business processes using AI and automation, resulting in a 45% reduction in processing time and a 30% decrease in error rates.")
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Team Leadership</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Successfully led cross-functional teams of up to 12 members, bridging technical and business perspectives to deliver complex AI projects on time and within budget.")
        
        st.markdown("""
        <div class="card">
            <h4>Data-Driven Decision Making</h4>
        </div>
        """, unsafe_allow_html=True)
        st.write("Implemented data analytics frameworks that enabled executive teams to make informed decisions, resulting in 28% improved resource allocation.")
    
    # Skills growth visualization
    st.markdown("<h2>Skills Evolution</h2>", unsafe_allow_html=True)
    
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
        title='Professional Skills Development',
        xaxis_title='Year',
        yaxis_title='Proficiency Level',
        legend_title='Skill Category',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0, 100]),
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Project 7: Vallourec Online
    st.markdown("""
    <div class="project-card">
        <h3>🌐 Vallourec Online - Order Tracking Portal</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Digital platform created for Vallourec customers to track the status of their orders and deliveries in real-time. The system consolidated data from various sources and presented clear, intuitive dashboards.")
    
    st.markdown("<h4>Key Features:</h4>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Real-time order status tracking</li>
        <li>Delivery timeline visualization</li>
        <li>Document access and management</li>
        <li>Consolidated data from multiple internal systems</li>
        <li>Intuitive dashboards for customer self-service</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4>Business Impact:</h4>", unsafe_allow_html=True)
    st.write("Provided greater autonomy to customers and reduced the volume of calls to the service team, improving customer experience while reducing operational overhead.")
    
    # Project 8: HeatGlass
    st.markdown("""
    <div class="project-card">
        <h3>🔥 HeatGlass - Emotional Call Analysis System</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("HeatGlass is an automated analysis system for audio calls (.mp3) created for Carglass. It uses AI (GPT-4 Turbo) to transcribe speech, identify sentiments, and classify the emotional temperature of conversations (calm, neutral, or critical).")
    
    st.markdown("<h4>Key Features:</h4>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Automated transcription and sentiment analysis of customer calls</li>
        <li>Emotional temperature classification with confidence scores</li>
        <li>Strategic call prioritization for customer service teams</li>
        <li>Integration with existing CRM systems</li>
        <li>Trend analysis and reporting dashboard</li>
    </ul>
    """, unsafe_allow_html=True)
    
# Adicione aqui o conteúdo para as páginas Projects e outras que possam faltar
elif page == "Projects":
    st.markdown("""
    <div class="header-container">
        <h1>Projects</h1>
        <p>Showcasing my work in AI and business solutions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Conteúdo da página de projetos aqui
    st.write("Conteúdo da página de projetos")
