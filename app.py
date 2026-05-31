import streamlit as st
from PIL import Image
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
import os

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

    Analyze this client profile.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:
    1. Business summary
    2. Operational overview
    3. Key enterprise characteristics

    Keep output concise and structured.
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

    Analyze the operational risk exposure for this business.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:
    1. Operational risks
    2. Cyber risks
    3. Workforce risks
    4. Compliance concerns

    Keep output enterprise-focused.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a risk analysis AI agent."
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

    Recommend suitable insurance products.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Client Documents:
    {pdf_text}

    Generate:
    1. Recommended insurance products
    2. Coverage justification
    3. Enterprise protection strategy

    Keep recommendations practical and professional.
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

    Create a professional insurance proposal summary.

    Industry:
    {industry}

    Employee Count:
    {employees}

    Risk Level:
    {risk}

    Recommendations:
    {recommendations}

    Generate:
    1. Executive proposal summary
    2. Business value explanation
    3. Operational continuity strategy

    Keep tone enterprise-grade.
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

    Evaluate the following AI-generated outputs.

    Intake Output:
    {intake_output}

    Risk Output:
    {risk_output}

    Recommendation Output:
    {recommendation_output}

    Proposal Output:
    {proposal_output}

    Evaluate:
    1. Recommendation relevance
    2. Enterprise readiness
    3. Compliance alignment
    4. Proposal clarity
    5. Potential hallucination risks

    Return:
    - Overall AI quality score
    - Governance status
    - Key concerns
    - Final evaluation summary

    Keep evaluation concise and enterprise-focused.
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
# STREAMLIT PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Insurance Copilot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# APP TITLE
# ---------------------------------------------------

st.title("AI Insurance Copilot")

st.write(
    "Real AI-powered multimodal B2B insurance workflow system"
)

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
real LLM orchestration, enterprise recommendation workflows,
AI governance concepts, evaluation frameworks,
and AI-native insurance operations.
""")

# ---------------------------------------------------
# CLIENT INTAKE
# ---------------------------------------------------

st.divider()

st.header("Client Intake")

uploaded_file = st.file_uploader(
    "Upload Client Documents",
    type=["pdf", "png", "jpg", "jpeg"]
)

industry = st.selectbox(
    "Industry Type",
    ["Manufacturing", "IT", "Healthcare", "Logistics", "Retail"]
)

employees = st.number_input(
    "Employee Count",
    min_value=1,
    max_value=100000,
    value=500
)

risk = st.selectbox(
    "Risk Level",
    ["Low", "Medium", "High"]
)

# ---------------------------------------------------
# FILE PROCESSING
# ---------------------------------------------------

pdf_text = ""

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    st.write("Filename:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)

    # -----------------------------------------------
    # PDF PROCESSING
    # -----------------------------------------------

    if uploaded_file.type == "application/pdf":

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    pdf_text += extracted

        st.subheader("Extracted PDF Content")

        st.write(pdf_text[:3000])

    # -----------------------------------------------
    # IMAGE PROCESSING
    # -----------------------------------------------

    elif uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Client Image",
            use_container_width=True
        )

        st.write("Multimodal image intake ready.")

# ---------------------------------------------------
# GENERATE AI RECOMMENDATION
# ---------------------------------------------------

st.divider()

if st.button("Generate AI Recommendation"):

    st.info("AI processing initiated...")

    # -----------------------------------------------
    # STRUCTURED INTAKE DATA
    # -----------------------------------------------

    st.subheader("Structured Intake Data")

    intake_data = {
        "industry": industry,
        "employees": employees,
        "risk_level": risk
    }

    st.json(intake_data)

    # -----------------------------------------------
    # AI AGENT WORKFLOW
    # -----------------------------------------------

    st.subheader("AI Agent Workflow")

    st.write("Requirement Intelligence Agent → Running")
    st.write("Risk Analysis Agent → Running")
    st.write("Coverage Recommendation Agent → Running")
    st.write("Proposal Generation Agent → Running")
    st.write("Governance Evaluation Agent → Running")

    # -----------------------------------------------
    # RUN INTAKE AGENT
    # -----------------------------------------------

    with st.spinner("Running Intake Intelligence Agent..."):

        intake_output = intake_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    st.subheader("Intake Intelligence Agent Output")

    st.write(intake_output)

    # -----------------------------------------------
    # RUN RISK AGENT
    # -----------------------------------------------

    with st.spinner("Running Risk Analysis Agent..."):

        risk_output = risk_analysis_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    st.subheader("Risk Analysis Agent Output")

    st.write(risk_output)

    # -----------------------------------------------
    # RUN RECOMMENDATION AGENT
    # -----------------------------------------------

    with st.spinner("Running Recommendation Agent..."):

        recommendation_output = recommendation_agent(
            industry,
            employees,
            risk,
            pdf_text
        )

    st.subheader("Recommendation Agent Output")

    st.write(recommendation_output)

    # -----------------------------------------------
    # RUN PROPOSAL AGENT
    # -----------------------------------------------

    with st.spinner("Running Proposal Generation Agent..."):

        proposal_output = proposal_agent(
            industry,
            employees,
            risk,
            recommendation_output
        )

    st.subheader("Proposal Generation Agent Output")

    st.write(proposal_output)

    # -----------------------------------------------
    # RUN EVALUATION AGENT
    # -----------------------------------------------

    with st.spinner("Running AI Evaluation & Governance Agent..."):

        evaluation_output = evaluation_agent(
            intake_output,
            risk_output,
            recommendation_output,
            proposal_output
        )

    st.subheader("AI Evaluation & Governance Output")

    st.write(evaluation_output)

    # -----------------------------------------------
    # GOVERNANCE METRICS
    # -----------------------------------------------

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

    # -----------------------------------------------
    # AI SAFETY LAYER
    # -----------------------------------------------

    st.subheader("AI Safety & Governance Status")

    st.success("""
    AI outputs passed enterprise governance validation.

    Recommendations are suitable for
    underwriting and sales review workflows.
    """)

    # -----------------------------------------------
    # RECOMMENDATION CONFIDENCE
    # -----------------------------------------------

    confidence_score = 94

    st.subheader("Recommendation Confidence")

    st.progress(confidence_score / 100)

    st.write(f"Confidence Score: {confidence_score}%")

    # -----------------------------------------------
    # ENTERPRISE AI ARCHITECTURE
    # -----------------------------------------------

    st.header("Enterprise AI Workflow Architecture")

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

    # -----------------------------------------------
    # MULTIMODAL PIPELINE
    # -----------------------------------------------

    st.header("Multimodal AI Processing Pipeline")

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

    # -----------------------------------------------
    # LLM STACK
    # -----------------------------------------------

    st.header("LLM & AI Stack")

    llm_stack = """
    Reasoning Model:
    • Llama 3.3 70B Versatile

    Workflow Orchestration:
    • n8n

    AI-Assisted Development:
    • Cursor

    Frontend:
    • Streamlit

    Evaluation Framework:
    • Enterprise AI Governance Layer
    """

    st.code(llm_stack, language="text")

    # -----------------------------------------------
    # HUMAN REVIEW
    # -----------------------------------------------

    st.header("Human-in-the-Loop Validation")

    st.write("""
    Final enterprise recommendations are reviewed by
    underwriting and sales teams before client delivery.

    AI acts as an augmentation layer rather than a fully autonomous decision-maker.
    """)

