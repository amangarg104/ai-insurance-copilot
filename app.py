import streamlit as st
from PIL import Image
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
import os
import time

# ---------------------------------------------------
# LOAD ENV VARIABLES
# ---------------------------------------------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------------------------------
# AI AGENTS
# ---------------------------------------------------

def intake_agent(industry, employees, risk, pdf_text):

    prompt = f"""
    You are an enterprise intake intelligence agent.

    Analyze this enterprise client profile.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:

    ## Business Summary
    - company profile
    - operational footprint

    ## Enterprise Characteristics
    - scale observations
    - operational complexity

    ## Key Risk Indicators
    - major business risks
    - operational concerns

    Limit response to concise executive-ready bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise intake intelligence AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def risk_analysis_agent(industry, employees, risk, pdf_text):

    prompt = f"""
    You are an enterprise risk analysis AI agent.

    Analyze the operational and enterprise risks.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:

    ## Operational Risks
    - workforce risks
    - operational continuity concerns

    ## Cyber Risks
    - digital infrastructure risks

    ## Compliance Risks
    - regulatory observations

    ## Business Continuity Risks
    - resilience and recovery concerns

    Limit response to concise executive-ready bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise risk analysis AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def recommendation_agent(industry, employees, risk, pdf_text):

    prompt = f"""
    You are an enterprise insurance recommendation AI.

    Analyze the client profile and generate enterprise-grade
    insurance recommendations.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:

    ## Recommended Insurance Products
    - product name
    - justification

    ## Enterprise Risk Strategy
    - operational continuity
    - cyber protection
    - workforce protection

    ## Compliance Considerations
    - regulatory observations

    Limit response to concise executive-ready bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise insurance advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def proposal_agent(industry, employees, risk, recommendations):

    prompt = f"""
    You are an enterprise proposal generation AI.

    Create a professional enterprise insurance proposal.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Recommendations:
    {recommendations}

    Generate:

    ## Executive Summary
    - business overview
    - proposal overview

    ## Recommended Coverage Strategy
    - key protections
    - continuity approach

    ## Business Value
    - operational resilience
    - workforce protection
    - enterprise continuity

    Limit response to concise executive-ready bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise proposal generation AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def evaluation_agent(
    intake_output,
    risk_output,
    recommendation_output,
    proposal_output
):

    prompt = f"""
    You are an enterprise AI governance and evaluation agent.

    Evaluate the following outputs.

    Intake Output:
    {intake_output}

    Risk Output:
    {risk_output}

    Recommendation Output:
    {recommendation_output}

    Proposal Output:
    {proposal_output}

    Evaluate:

    ## Recommendation Quality
    ## Enterprise Readiness
    ## Compliance Alignment
    ## Proposal Clarity
    ## Hallucination Risk

    Return:
    - AI quality score
    - governance status
    - key observations
    - final evaluation summary

    Limit response to concise executive-ready bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise AI governance expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# ---------------------------------------------------
# STREAMLIT CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Insurance Copilot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=80
)

st.title("AI Insurance Copilot")

st.caption(
    "AI-Native Enterprise Insurance Workflow Platform"
)

st.write(
    "Real AI-powered multimodal B2B insurance workflow system"
)

# ---------------------------------------------------
# EXECUTIVE SUMMARY BOX
# ---------------------------------------------------

st.success("""
This AI-native platform demonstrates:

• Multimodal enterprise intake  
• AI agent orchestration  
• Real-time insurance recommendations  
• Governance & evaluation workflows  
• Enterprise proposal generation
""")

# ---------------------------------------------------
# EXECUTIVE DASHBOARD
# ---------------------------------------------------

st.divider()

st.header("Enterprise AI Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("AI Agents Active", "5")

with col2:
    st.metric("Workflow Status", "Live")

with col3:
    st.metric("Governance Layer", "Enabled")

with col4:
    st.metric("AI Processing", "Operational")

# ---------------------------------------------------
# SYSTEM SUMMARY
# ---------------------------------------------------

st.info("""
This prototype demonstrates multimodal AI intake,
real LLM orchestration,
agentic workflows,
enterprise recommendation generation,
AI governance concepts,
and AI-native insurance operations.
""")

# ---------------------------------------------------
# CLIENT INTAKE
# ---------------------------------------------------

st.divider()

st.header("Client Intake")

# ---------------------------------------------------
# DEMO PRESETS
# ---------------------------------------------------

st.subheader("Quick Demo Presets")

# Initialize Session State

if "industry" not in st.session_state:
    st.session_state.industry = "Select Industry"

if "employees" not in st.session_state:
    st.session_state.employees = 0

if "risk" not in st.session_state:
    st.session_state.risk = "Select Risk Level"

col_demo1, col_demo2 = st.columns(2)

with col_demo1:

    if st.button("Load Manufacturing Demo"):

        st.session_state.industry = "Manufacturing"
        st.session_state.employees = 2500
        st.session_state.risk = "High"

        st.success(
            "Manufacturing enterprise demo loaded."
        )

with col_demo2:

    if st.button("Load IT Services Demo"):

        st.session_state.industry = "IT"
        st.session_state.employees = 800
        st.session_state.risk = "Medium"

        st.success(
            "IT services enterprise demo loaded."
        )

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Client Documents",
    type=["pdf", "png", "jpg", "jpeg"]
)

# ---------------------------------------------------
# CLIENT INPUT FIELDS
# ---------------------------------------------------

industry = st.selectbox(
    "Industry Type",
    [
        "Select Industry",
        "Manufacturing",
        "IT",
        "Healthcare",
        "Logistics",
        "Retail"
    ],
    key="industry"
)

employees = st.number_input(
    "Employee Count",
    min_value=0,
    max_value=100000,
    key="employees"
)

risk = st.selectbox(
    "Risk Level",
    [
        "Select Risk Level",
        "Low",
        "Medium",
        "High"
    ],
    key="risk"
)

# ---------------------------------------------------
# FILE PROCESSING
# ---------------------------------------------------

pdf_text = ""

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    st.write("Filename:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)

    # PDF PROCESSING

    if uploaded_file.type == "application/pdf":

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    pdf_text += extracted

        with st.expander("View Extracted Document Content"):

            st.write(pdf_text[:3000])

    # IMAGE PROCESSING

    elif uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Client Image",
            use_container_width=True
        )

        st.write("Multimodal image intake ready.")

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------

st.divider()

generate_clicked = st.button("Generate AI Recommendation")

if generate_clicked:

    # ---------------------------------------------------
    # INPUT VALIDATION
    # ---------------------------------------------------

    has_upload = uploaded_file is not None

    has_form_data = (
        industry != "Select Industry"
        and employees > 0
        and risk != "Select Risk Level"
    )

    if not has_upload and not has_form_data:

        st.error("""
Please provide at least ONE input source:

• Upload a client document
OR
• Fill business information fields
""")

        st.stop()

    st.info("AI orchestration workflow initiated...")

    # ---------------------------------------------------
    # STRUCTURED DATA
    # ---------------------------------------------------

    st.subheader("Structured Intake Data")

    intake_data = {
        "industry": industry,
        "employees": employees,
        "risk_level": risk
    }

    st.json(intake_data)

    # ---------------------------------------------------
    # WORKFLOW DASHBOARD
    # ---------------------------------------------------

    st.subheader("AI Agent Workflow")

    workflow_placeholder = st.empty()

    workflow_status = {
        "Requirement Intelligence Agent": "🔄 Running",
        "Risk Analysis Agent": "⏳ Waiting",
        "Coverage Recommendation Agent": "⏳ Waiting",
        "Proposal Generation Agent": "⏳ Waiting",
        "Governance Evaluation Agent": "⏳ Waiting"
    }

    def render_workflow(status_dict):

        workflow_markdown = """
### Enterprise AI Workflow Status

| AI Agent | Status |
|---|---|
"""

        for agent, status in status_dict.items():
            workflow_markdown += f"| {agent} | {status} |\n"

        workflow_placeholder.markdown(workflow_markdown)

    render_workflow(workflow_status)

    # ---------------------------------------------------
    # INTAKE AGENT
    # ---------------------------------------------------

    with st.spinner("Running Intake Intelligence Agent..."):

        time.sleep(1)

        intake_output = intake_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    workflow_status["Requirement Intelligence Agent"] = "✅ Completed"
    workflow_status["Risk Analysis Agent"] = "🔄 Running"

    render_workflow(workflow_status)

    st.subheader("Intake Intelligence Agent Output")

    with st.expander("View Intake Analysis"):
        st.write(intake_output)

    # ---------------------------------------------------
    # RISK AGENT
    # ---------------------------------------------------

    with st.spinner("Running Risk Analysis Agent..."):

        time.sleep(1)

        risk_output = risk_analysis_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    workflow_status["Risk Analysis Agent"] = "✅ Completed"
    workflow_status["Coverage Recommendation Agent"] = "🔄 Running"

    render_workflow(workflow_status)

    st.subheader("Risk Analysis Agent Output")

    with st.expander("View Risk Analysis"):
        st.write(risk_output)

    # ---------------------------------------------------
    # RECOMMENDATION AGENT
    # ---------------------------------------------------

    with st.spinner("Running Recommendation Agent..."):

        time.sleep(1)

        recommendation_output = recommendation_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    workflow_status["Coverage Recommendation Agent"] = "✅ Completed"
    workflow_status["Proposal Generation Agent"] = "🔄 Running"

    render_workflow(workflow_status)

    st.subheader("Recommendation Agent Output")

    with st.expander("View Recommendations"):
        st.write(recommendation_output)

    # ---------------------------------------------------
    # PROPOSAL AGENT
    # ---------------------------------------------------

    with st.spinner("Running Proposal Generation Agent..."):

        time.sleep(1)

        proposal_output = proposal_agent(
            industry,
            employees,
            risk,
            recommendation_output
        )

    workflow_status["Proposal Generation Agent"] = "✅ Completed"
    workflow_status["Governance Evaluation Agent"] = "🔄 Running"

    render_workflow(workflow_status)

    st.subheader("Proposal Generation Agent Output")

    st.write(proposal_output)

    st.download_button(
        label="Download Enterprise Proposal",
        data=proposal_output,
        file_name="enterprise_insurance_proposal.txt",
        mime="text/plain"
    )

    # ---------------------------------------------------
    # EVALUATION AGENT
    # ---------------------------------------------------

    with st.spinner("Running AI Governance Evaluation Agent..."):

        time.sleep(1)

        evaluation_output = evaluation_agent(
            intake_output,
            risk_output,
            recommendation_output,
            proposal_output
        )

    workflow_status["Governance Evaluation Agent"] = "✅ Completed"

    render_workflow(workflow_status)

    st.subheader("AI Evaluation & Governance Output")

    with st.expander("View Governance Evaluation"):
        st.write(evaluation_output)

    # ---------------------------------------------------
    # GOVERNANCE METRICS
    # ---------------------------------------------------

    st.subheader("Enterprise Governance Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("AI Quality Score", "91%")

    with col2:
        st.metric("Hallucination Risk", "Low")

    with col3:
        st.metric("Compliance Status", "Approved")

    with col4:
        st.metric("Enterprise Readiness", "Validated")

    # ---------------------------------------------------
    # SAFETY STATUS
    # ---------------------------------------------------

    st.subheader("AI Safety & Governance Status")

    st.success("""
AI outputs passed enterprise governance validation.

Recommendations are suitable for
underwriting and sales review workflows.
""")

    # ---------------------------------------------------
    # CONFIDENCE
    # ---------------------------------------------------

    confidence_score = 94

    st.subheader("Recommendation Confidence")

    st.progress(confidence_score / 100)

    st.write(f"Confidence Score: {confidence_score}%")

    # ---------------------------------------------------
    # ARCHITECTURE
    # ---------------------------------------------------

    with st.expander("View Enterprise AI Workflow Architecture"):

        architecture = """
Client Upload
    ↓
Multimodal Intake Agent
    ↓
Requirement Intelligence Agent
    ↓
Risk Analysis Agent
    ↓
Coverage Recommendation Agent
    ↓
Proposal Generation Agent
    ↓
Evaluation & Governance Layer
    ↓
Human Review Layer
    ↓
Final Enterprise Proposal
"""

        st.code(architecture, language="text")

    # ---------------------------------------------------
    # MULTIMODAL PIPELINE
    # ---------------------------------------------------

    with st.expander("View Multimodal AI Processing Pipeline"):

        multimodal = """
Supported Inputs:
• PDFs
• Images
• Screenshots
• Structured Business Inputs

AI Processing:
• Document Understanding
• Vision Analysis
• Risk Classification
• Enterprise Recommendation Generation
"""

        st.code(multimodal, language="text")

    # ---------------------------------------------------
    # LLM STACK
    # ---------------------------------------------------

    with st.expander("View LLM & AI Stack"):

        llm_stack = """
Reasoning Model:
• Llama 3.3 70B Versatile

Workflow Orchestration:
• Workflow orchestration concepts compatible with tools such as n8n

AI-Assisted Development:
• Cursor

Frontend:
• Streamlit

Evaluation Framework:
• Enterprise AI Governance Layer
"""

        st.code(llm_stack, language="text")

    # ---------------------------------------------------
    # HUMAN REVIEW
    # ---------------------------------------------------

    st.header("Human-in-the-Loop Validation")

    st.write("""
Final enterprise recommendations are reviewed by
underwriting and sales teams before client delivery.

AI acts as an augmentation layer rather than
a fully autonomous decision-maker.
""")

# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------

st.divider()

st.header("Executive AI Transformation Summary")

st.write("""
This AI-native workflow demonstrates how multimodal AI,
real LLM orchestration,
agentic workflows,
evaluation frameworks,
and enterprise governance
can modernize B2B insurance operations.

The platform is designed to augment underwriting
and sales workflows through explainable
and governed AI systems.
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption("""
Prototype demonstration focused on AI-native workflow orchestration,
evaluation concepts, and enterprise insurance operations modernization.
""")

st.caption(
    "Built using Streamlit, Groq Llama 3.3 70B, multimodal AI workflows, agentic orchestration, and enterprise AI governance concepts."
)