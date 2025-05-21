import React, { useState, useEffect } from 'react';
import { User, Briefcase, LineChart, Flag, Award, Book, Globe, Clipboard, Mail, Phone, Linkedin, ChevronRight, ExternalLink, Github, ArrowRight, Zap, DollarSign, FileCheck } from 'lucide-react';

// Main application component
function Portfolio() {
  const [activeSection, setActiveSection] = useState('profile');
  const [isLoading, setIsLoading] = useState(true);
  const [animateContent, setAnimateContent] = useState(false);

  // Simulate initial page loading with effect
  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false);
      setTimeout(() => setAnimateContent(true), 100);
    }, 600);
  }, []);

  // Function to switch between sections with animation
  const switchSection = (section) => {
    setAnimateContent(false);
    setTimeout(() => {
      setActiveSection(section);
      setTimeout(() => setAnimateContent(true), 100);
    }, 300);
  };

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <div className="flex flex-col lg:flex-row min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      {/* Responsive Sidebar */}
      <Sidebar activeSection={activeSection} switchSection={switchSection} />
      
      {/* Main Content */}
      <main className={`flex-1 p-4 lg:p-6 overflow-y-auto transition-all duration-500 ease-in-out ${animateContent ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
        {activeSection === 'profile' && <ProfileContent />}
        {activeSection === 'projects' && <ProjectsContent />}
        {activeSection === 'experience' && <ExperienceContent />}
        {activeSection === 'skills' && <SkillsContent />}
        {activeSection === 'contact' && <ContactContent />}
        
        {/* Footer */}
        <footer className="mt-12 py-4 text-center text-gray-500 text-sm border-t border-gray-200">
          <p>© 2025 Vinícius Paschoa | AI Specialist | Business-Oriented Artificial Intelligence</p>
          <p className="mt-1">Exploring the future with Artificial Intelligence</p>
        </footer>
      </main>
    </div>
  );
}

// Loading screen component
function LoadingScreen() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <div className="w-24 h-24 border-t-4 border-blue-600 border-solid rounded-full animate-spin"></div>
      <h2 className="mt-8 text-2xl font-light text-blue-700">Loading AI Portfolio</h2>
    </div>
  );
}

// Sidebar component
function Sidebar({ activeSection, switchSection }) {
  return (
    <aside className="w-full lg:w-64 bg-blue-900 p-6 lg:min-h-screen">
      <div className="mb-8 text-center lg:text-left">
        <h1 className="text-2xl font-bold text-white">
          AI Portfolio
        </h1>
        <p className="text-sm text-blue-200 mt-1">Vinícius Paschoa</p>
      </div>
      
      <nav>
        <ul className="space-y-2">
          <SidebarItem 
            icon={<User size={18} />}
            title="Profile"
            isActive={activeSection === 'profile'}
            onClick={() => switchSection('profile')}
          />
          <SidebarItem 
            icon={<Clipboard size={18} />}
            title="Projects"
            isActive={activeSection === 'projects'}
            onClick={() => switchSection('projects')}
          />
          <SidebarItem 
            icon={<Briefcase size={18} />}
            title="Experience"
            isActive={activeSection === 'experience'}
            onClick={() => switchSection('experience')}
          />
          <SidebarItem 
            icon={<Award size={18} />}
            title="Skills"
            isActive={activeSection === 'skills'}
            onClick={() => switchSection('skills')}
          />
          <SidebarItem 
            icon={<Mail size={18} />}
            title="Contact"
            isActive={activeSection === 'contact'}
            onClick={() => switchSection('contact')}
          />
        </ul>
      </nav>
      
      <div className="mt-8 pt-6 border-t border-blue-800">
        <div className="flex flex-col space-y-2">
          <a 
            href="mailto:viniciuspaschoa1@hotmail.com"
            className="flex items-center text-sm text-blue-200 hover:text-white transition-colors"
          >
            <Mail size={14} className="mr-2" />
            viniciuspaschoa1@hotmail.com
          </a>
          <a 
            href="tel:+5511938012431" 
            className="flex items-center text-sm text-blue-200 hover:text-white transition-colors"
          >
            <Phone size={14} className="mr-2" />
            +55 (11) 93801-2431
          </a>
          <a 
            href="https://www.linkedin.com/in/viniciuspaschoa" 
            target="_blank" 
            rel="noopener noreferrer"
            className="flex items-center text-sm text-blue-200 hover:text-white transition-colors"
          >
            <Linkedin size={14} className="mr-2" />
            LinkedIn
          </a>
        </div>
        <div className="text-xs text-blue-400 mt-4">
          &copy; 2025 Vinícius Paschoa
        </div>
      </div>
    </aside>
  );
}

// Sidebar item component
function SidebarItem({ icon, title, isActive, onClick }) {
  return (
    <li>
      <button
        onClick={onClick}
        className={`flex items-center w-full p-3 rounded-lg transition-all duration-200 ${
          isActive 
            ? 'bg-blue-800 text-white border-l-4 border-blue-300 pl-2' 
            : 'text-blue-200 hover:bg-blue-800/50 hover:text-white'
        }`}
      >
        <span className="mr-3">{icon}</span>
        <span>{title}</span>
        {isActive && <ChevronRight size={16} className="ml-auto" />}
      </button>
    </li>
  );
}

// Section header component
function SectionHeader({ title, subtitle }) {
  return (
    <div className="bg-gradient-to-r from-blue-900 to-blue-600 rounded-xl p-6 mb-8 text-white">
      <h1 className="text-3xl font-bold">{title}</h1>
      <p className="mt-2 text-blue-100">{subtitle}</p>
    </div>
  );
}

// Profile section component
function ProfileContent() {
  return (
    <div className="max-w-4xl mx-auto">
      <SectionHeader 
        title="Vinícius Paschoa" 
        subtitle="AI Specialist | Business-Oriented Artificial Intelligence | EU Citizen"
      />

      <div className="flex flex-col md:flex-row gap-8 mb-8">
        <div className="md:w-1/3">
          {/* Profile photo placeholder */}
          <div className="w-40 h-40 mx-auto md:mx-0 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 p-1">
            <div className="w-full h-full rounded-full bg-white flex items-center justify-center text-3xl font-bold text-blue-600">
              VP
            </div>
          </div>
        </div>
        
        <div className="md:w-2/3">
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            <h2 className="text-xl font-bold text-blue-900 mb-4">About Me</h2>
            <p className="text-gray-700 mb-3">
              Artificial Intelligence Specialist focused on delivering measurable impact through intelligent automation.
              With a strong foundation in technology, business analysis, and project leadership, I specialize in applying
              Artificial Intelligence to solve real-world business challenges.
            </p>
            <p className="text-gray-700">
              At Vallourec and now at Carglass, I have led multiple initiatives under the internal AI accelerator program called "Agente",
              where I designed and deployed end-to-end solutions that automate complex workflows, optimize operations, and generate
              actionable insights.
            </p>
          </div>
        </div>
      </div>

      {/* Key metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <MetricCard value="7+" label="Years Experience" />
        <MetricCard value="10+" label="AI Projects" />
        <MetricCard value="3" label="Languages" />
        <MetricCard value="2" label="Postgraduate Degrees" />
      </div>

      {/* Education */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 mb-8">
        <div className="flex items-center mb-4">
          <Book className="text-blue-600 mr-2" size={20} />
          <h2 className="text-xl font-bold text-gray-800">Education</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <EducationCard 
            institution="Centro Universitário Senac"
            degree="Postgraduate in AI for Business Strategy"
            period="February 2024 - April 2025"
          />
          <EducationCard 
            institution="UNIMAIS - Faculdade Educamais"
            degree="Postgraduate in Agile Models"
            period="January 2021 - November 2021"
          />
          <EducationCard 
            institution="Centro Universitário Senac"
            degree="Bachelor's in Production Engineering"
            period="2015 - 2020"
          />
          <EducationCard 
            institution="University of Michigan"
            degree="Successful Negotiation, Essential Strategies and Skills"
            period="January 2017 - June 2017"
          />
        </div>
      </div>

      {/* Languages */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
        <div className="flex items-center mb-4">
          <Globe className="text-blue-600 mr-2" size={20} />
          <h2 className="text-xl font-bold text-gray-800">Languages</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <LanguageCard language="Portuguese" level="Native" percentage={100} />
          <LanguageCard language="English" level="Full Professional" percentage={95} />
          <LanguageCard language="French" level="Professional Working" percentage={80} />
        </div>
      </div>
    </div>
  );
}

// Metric card component
function MetricCard({ value, label }) {
  return (
    <div className="bg-white rounded-xl p-4 text-center shadow-sm border border-gray-100">
      <div className="text-3xl font-bold text-blue-600">{value}</div>
      <div className="text-sm text-gray-600 mt-1">{label}</div>
    </div>
  );
}

// Education card component
function EducationCard({ institution, degree, period }) {
  return (
    <div className="p-4 border-l-4 border-blue-500 bg-blue-50/50">
      <h3 className="font-bold text-gray-800">{institution}</h3>
      <p className="text-gray-700">{degree}</p>
      <p className="text-sm text-blue-600 mt-2">{period}</p>
    </div>
  );
}

// Language card component
function LanguageCard({ language, level, percentage }) {
  return (
    <div className="p-4">
      <div className="flex justify-between mb-2">
        <span className="font-medium text-gray-800">{language}</span>
        <span className="text-blue-600">{level}</span>
      </div>
      <div className="h-2 bg-gray-200 rounded-full">
        <div 
          className="h-full bg-gradient-to-r from-blue-600 to-blue-400 rounded-full" 
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  );
}

// Projects component
function ProjectsContent() {
  return (
    <div className="max-w-4xl mx-auto">
      <SectionHeader 
        title="Project Portfolio" 
        subtitle="A showcase of my AI and business transformation projects"
      />
      
      {/* Project: HeatGlass */}
      <ProjectCard
        title="HeatGlass"
        subtitle="Emotional Call Analysis System"
        description="HeatGlass is an automated analysis system for audio calls (.mp3) created for Carglass. It uses AI (GPT-4 Turbo) to transcribe speech, identify sentiments, and classify the emotional temperature of conversations (calm, neutral, or critical)."
        color="red"
        icon={<LineChart size={24} />}
        tags={["GPT-4 Turbo", "Sentiment Analysis", "Streamlit", "Audio Processing", "Customer Service"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Automated transcription and sentiment analysis of customer calls</li>
            <li>Emotional temperature classification with confidence scores</li>
            <li>Strategic call summary based on the most sensitive segments</li>
            <li>Technical scoring through an objective checklist</li>
            <li>Visual representation with red indicators for negative impacts</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Reduced friction in customer service interactions and provided valuable insights for commercial and quality teams, 
            leading to improved customer satisfaction and more effective training programs.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div className="bg-white p-2 rounded-lg shadow-sm border border-gray-200">
            <img src="/api/placeholder/500/300" alt="Initial interface with audio upload" className="w-full h-auto rounded" />
            <p className="text-sm text-center text-gray-500 mt-2">Initial interface with audio upload</p>
          </div>
          <div className="bg-white p-2 rounded-lg shadow-sm border border-gray-200">
            <img src="/api/placeholder/500/300" alt="Full analysis with checklist and risk indicators" className="w-full h-auto rounded" />
            <p className="text-sm text-center text-gray-500 mt-2">Full analysis with checklist and risk indicators</p>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: MirrorGlass */}
      <ProjectCard
        title="MirrorGlass"
        subtitle="Image Fraud Detection System"
        description="MirrorGlass was created to detect visual inconsistencies in images sent by Carglass customers during service processes. The tool compares received images with a previous database, detecting duplications, inconsistencies, or abnormal patterns."
        color="blue"
        icon={<Flag size={24} />}
        tags={["Computer Vision", "YOLOv8", "Metadata Analysis", "Machine Learning", "Fraud Prevention"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Advanced image comparison using computer vision techniques</li>
            <li>Detection of duplicated or manipulated images</li>
            <li>Metadata analysis for authenticity verification</li>
            <li>Identification of suspicious patterns in customer submissions</li>
            <li>Visual heatmaps highlighting potential areas of concern</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Enhanced fraud prevention capabilities and improved service quality by ensuring the authenticity of customer-submitted images, 
            resulting in significant cost savings and increased trust in the claims process.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div className="bg-white p-2 rounded-lg shadow-sm border border-gray-200">
            <img src="/api/placeholder/500/300" alt="Upload interface and detection settings" className="w-full h-auto rounded" />
            <p className="text-sm text-center text-gray-500 mt-2">Upload interface and detection settings</p>
          </div>
          <div className="bg-white p-2 rounded-lg shadow-sm border border-gray-200">
            <img src="/api/placeholder/500/300" alt="Texture analysis with Heat Map" className="w-full h-auto rounded" />
            <p className="text-sm text-center text-gray-500 mt-2">Texture analysis with Heat Map</p>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: Oráculo */}
      <ProjectCard
        title="Oráculo"
        subtitle="Enterprise RAG System"
        description="Oráculo is an intelligent platform based on RAG (Retrieval-Augmented Generation) that answers questions based on company documents hosted on SharePoint. The tool accesses content via Microsoft Graph API and also uses OCR and scraping with Selenium to navigate and extract data from dynamically rendered pages."
        color="indigo"
        icon={<Book size={24} />}
        tags={["RAG", "Microsoft Graph API", "OCR", "Selenium", "Knowledge Management"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Integration with SharePoint via Microsoft Graph API</li>
            <li>OCR and web scraping capabilities for comprehensive data access</li>
            <li>Support for multiple document formats (PDF, images, Word, HTML)</li>
            <li>Contextually precise responses to user queries</li>
            <li>Multi-language support across Portuguese, English, and French</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Significantly reduced information retrieval time, improved decision-making speed, and enhanced knowledge sharing 
            across departments, resulting in more efficient operations and better-informed staff.
          </p>
        </div>
        
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 mt-6">
          <h4 className="font-bold text-gray-800 mb-2 text-center">Information Retrieval Time</h4>
          <div className="h-64 flex items-end justify-center gap-12 p-4">
            <div className="flex flex-col items-center">
              <div className="h-52 w-20 bg-blue-900 rounded-t-lg flex items-center justify-center text-white font-bold">
                45 min
              </div>
              <p className="mt-2 text-sm text-gray-600">Traditional Search</p>
            </div>
            <div className="flex flex-col items-center">
              <div className="h-20 w-20 bg-blue-500 rounded-t-lg flex items-center justify-center text-white font-bold">
                8 min
              </div>
              <p className="mt-2 text-sm text-gray-600">RAG System</p>
            </div>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: Fast Track */}
      <ProjectCard
        title="Fast Track"
        subtitle="Strategic Optimization Project (Vallourec)"
        description="At Vallourec, the Fast Track project aimed to reduce customer response time from 30 days to just 5 days. I served as Product Owner, leading an AI initiative that automated engineering calculations and optimized order prioritization."
        color="blue"
        icon={<Zap size={24} />}
        tags={["Process Optimization", "Workflow Automation", "Engineering Calculations", "Customer Response", "Product Ownership"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Automated engineering calculations for faster technical responses</li>
            <li>Intelligent order prioritization system</li>
            <li>Integration with internal company workflows</li>
            <li>Connection between technical, commercial, and customer service areas</li>
            <li>Real-time status tracking and reporting</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Dramatically increased service agility, reduced rework, and significantly improved customer satisfaction 
            by delivering responses 6 times faster than the previous process.
          </p>
        </div>
        
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 mt-6">
          <h4 className="font-bold text-gray-800 mb-2 text-center">Response Time Improvement</h4>
          <div className="h-64 flex items-end justify-center gap-12 p-4">
            <div className="flex flex-col items-center">
              <div className="h-52 w-20 bg-blue-900 rounded-t-lg flex items-center justify-center text-white font-bold">
                30 days
              </div>
              <p className="mt-2 text-sm text-gray-600">Before</p>
            </div>
            <div className="flex flex-col items-center">
              <div className="h-10 w-20 bg-blue-500 rounded-t-lg flex items-center justify-center text-white font-bold">
                5 days
              </div>
              <p className="mt-2 text-sm text-gray-600">After</p>
            </div>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: SmartCost */}
      <ProjectCard
        title="SmartCost"
        subtitle="Intelligent Cost Recommendation (Vallourec)"
        description="Tool developed to support financial decisions in technical projects. SmartCost analyzes material costs and available alternatives based on engineering parameters, automatically recommending more economical options."
        color="green"
        icon={<DollarSign size={24} />}
        tags={["Cost Optimization", "Financial Analysis", "Engineering Parameters", "Decision Support", "Reporting"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Automated cost analysis of materials and components</li>
            <li>Engineering parameter-based recommendations</li>
            <li>Detailed reports with financial insights</li>
            <li>Alternative material suggestions with cost comparisons</li>
            <li>Integration with existing engineering systems</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Enabled faster decision-making with lower budgetary risk by providing engineers and managers with data-driven cost optimization recommendations, resulting in significant project savings.
          </p>
        </div>
        
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 mt-6">
          <h4 className="font-bold text-gray-800 mb-2 text-center">Average Cost Reduction</h4>
          <div className="flex justify-center items-center h-48">
            <div className="relative w-48 h-48">
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-3xl font-bold text-green-600">18%</div>
              </div>
              <div className="w-full h-full rounded-full border-8 border-green-500 opacity-20"></div>
              <div className="absolute top-0 left-0 w-full h-full rounded-full border-8 border-green-500 border-t-transparent border-l-transparent border-r-transparent transform rotate-45"></div>
            </div>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: FERT Workflow */}
      <ProjectCard
        title="FERT Workflow"
        subtitle="Technical Order Approval Management (Vallourec)"
        description="System developed to automate the approval of technical and industrial orders, with a focus on compliance and traceability. Includes different approval levels, change control, and automated alerts."
        color="indigo"
        icon={<FileCheck size={24} />}
        tags={["Workflow Automation", "Approval Management", "Compliance", "Traceability", "Process Governance"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Multi-level approval workflow automation</li>
            <li>Change tracking and version control</li>
            <li>Automated alerts and notifications</li>
            <li>Compliance documentation and audit trails</li>
            <li>Integration with enterprise resource planning systems</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Ensured governance, increased processing speed, and reduced errors in technical requisition processes (FERTs), leading to more efficient operations and better regulatory compliance.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <h5 className="font-medium text-gray-800 text-center mb-2">Process Efficiency</h5>
            <div className="flex justify-between items-center">
              <div className="text-center">
                <div className="text-xl font-bold text-red-500">72h</div>
                <div className="text-xs text-gray-500">Before</div>
              </div>
              <div className="w-20 h-0.5 bg-gray-300 relative">
                <div className="absolute -top-2 left-1/2 transform -translate-x-1/2 text-gray-500">
                  <ArrowRight size={20} />
                </div>
              </div>
              <div className="text-center">
                <div className="text-xl font-bold text-green-500">4h</div>
                <div className="text-xs text-gray-500">After</div>
              </div>
            </div>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <h5 className="font-medium text-gray-800 text-center mb-2">Error Reduction</h5>
            <div className="flex justify-center items-center h-24">
              <div className="text-center">
                <div className="text-2xl font-bold text-green-600">
                  -85%
                </div>
                <div className="text-xs text-gray-500 mt-1">in process errors</div>
              </div>
            </div>
          </div>
        </div>
      </ProjectCard>
      
      {/* Project: Vallourec Online */}
      <ProjectCard
        title="Vallourec Online"
        subtitle="Order Tracking Portal"
        description="Digital platform created for Vallourec customers to track the status of their orders and deliveries in real-time. The system consolidated data from various sources and presented clear, intuitive dashboards."
        color="blue"
        icon={<Globe size={24} />}
        tags={["Customer Portal", "Order Tracking", "Data Consolidation", "Dashboards", "Self-Service"]}
      >
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Key Features:</h4>
          <ul className="list-disc pl-5 text-gray-700 space-y-1">
            <li>Real-time order status tracking</li>
            <li>Delivery timeline visualization</li>
            <li>Document access and management</li>
            <li>Consolidated data from multiple internal systems</li>
            <li>Intuitive dashboards for customer self-service</li>
          </ul>
        </div>
        
        <div className="mt-4">
          <h4 className="font-bold text-gray-800 mb-2">Business Impact:</h4>
          <p className="text-gray-700">
            Provided greater autonomy to customers and reduced the volume of calls to the service team, improving customer experience while reducing operational overhead.
        
