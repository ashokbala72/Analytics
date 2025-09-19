import streamlit as st
import pandas as pd
import altair as alt
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# -------------------------------
# Azure OpenAI Setup
# -------------------------------
load_dotenv()

def get_secret(name):
    return st.secrets.get(name) or os.getenv(name)

client = AzureOpenAI(
    api_key=get_secret("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=get_secret("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = "gpt-4o-raj"

def genai_response(prompt: str, df: pd.DataFrame = None):
    """Call Azure OpenAI to generate dataset-specific response"""
    try:
        if df is not None and not df.empty:
            table_str = df.to_csv(index=False)
            prompt = f"""{prompt}

Here is the dataset:
{table_str}

Please summarize trends, anomalies, and insights based ONLY on this dataset."""
        
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ GenAI Error: {e}"

# -------------------------------
# Streamlit App Layout
# -------------------------------
st.set_page_config(page_title='O&G Analytics Mixed Charts', layout='wide')

tabs = st.tabs([
    '🗂 Overview', '🚜 Drilling Efficiency', '📈 Lift Optimization', '🌦 Weather Sensitivity',
    '💰 Netback Margin', '🔧 Maintenance Prediction', '💥 Frac Efficiency',
    '🧩 Completion Impact', '👷 Human Factor', '⚠️ Risk Prediction',
    '🔄 Compression Optimization', '📘 Compliance Planner'
])

# -------------------------------
# Tab 0 - Overview
# -------------------------------
with tabs[0]:
    st.markdown('''
    ## 🛢️ Oil & Gas GenAI Analytics Suite

    This app combines **mock oilfield datasets** with **Azure OpenAI (gpt-4o-raj)** for smart, dataset-specific summaries and visualizations.
    ''')

# -------------------------------
# Tab 1 - Drilling Efficiency
# -------------------------------
with tabs[1]:
    st.header('🚜 Drilling Efficiency')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 11)],
        'Lithology': ['Limestone','Carbonate','Shale','Sandstone','Shale','Sandstone','Carbonate','Shale','Sandstone','Carbonate'],
        'ROP (m/hr)': [31.8,27.0,27.2,20.4,17.4,19.0,25.3,26.0,29.5,18.1],
        'Mud Type': ['WBM','OBM','WBM','WBM','Synthetic','WBM','OBM','Synthetic','OBM','Synthetic'],
        'Efficiency Score': [70,63,89,61,85,71,80,85,62,70]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize drilling efficiency dataset.", df))
    bar = alt.Chart(df).mark_bar().encode(x='Well:N', y='ROP (m/hr):Q')
    scatter = alt.Chart(df).mark_circle(size=100).encode(x='Well:N', y='Efficiency Score:Q', color='Mud Type:N')
    st.altair_chart((bar + scatter).properties(title='ROP vs Efficiency'), use_container_width=True)

# -------------------------------
# Tab 2 - Lift Optimization
# -------------------------------
with tabs[2]:
    st.header('📈 Lift Optimization')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 11)],
        'Intervention': ['Gas Lift','PCP','Rod Pump','ESP','PCP','Rod Pump','ESP','Gas Lift','PCP','ESP'],
        'Choke Size (mm)': [23,20,19,38,25,20,28,32,26,19],
        'Flow Rate (bbl/d)': [1381,1187,1208,1395,750,915,1253,1062,987,1172]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize lift optimization dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(x='Choke Size (mm):Q', y='Flow Rate (bbl/d):Q', color='Intervention:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 3 - Weather Sensitivity
# -------------------------------
with tabs[3]:
    st.header('🌦 Weather Sensitivity')
    df = pd.DataFrame({
        'Weather Event': ['Rain','Fog','Storm','Heatwave','Snow','Storm','Fog','Heatwave','Rain','Storm'],
        'Flow Impact (%)': [-19.6,-19.1,-4.8,-18.8,-10.3,-15.5,-12.8,-6.1,-13.5,-4.3],
        'Safety Incident Risk': ['Medium','High','High','Low','Medium','High','High','Medium','High','Low']
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize weather sensitivity dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Weather Event:N', y='Flow Impact (%):Q', color='Safety Incident Risk:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 4 - Netback Margin
# -------------------------------
with tabs[4]:
    st.header('💰 Netback Margin')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 11)],
        'Price ($/bbl)': [83,77,84,80,77,84,77,80,83,81],
        'Transport Cost': [3,8,3,6,6,7,5,3,7,7],
        'Flow Rate (bbl/d)': [1381,1187,1208,1395,750,915,867,1235,1253,1062]
    })
    df['Netback ($)'] = (df['Price ($/bbl)'] - df['Transport Cost']) * df['Flow Rate (bbl/d)']
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize netback margin dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Well:N', y='Netback ($):Q', color='Price ($/bbl):Q'),
        use_container_width=True
    )

# -------------------------------
# Tab 5 - Maintenance Prediction
# -------------------------------
with tabs[5]:
    st.header('🔧 Maintenance Prediction')
    df = pd.DataFrame({
        'Component': ['Sensor','Compressor','Pump','Valve','Compressor','Pump','Sensor','Pump','Valve','Sensor'],
        'Failure Logs': [13,11,1,11,14,3,9,11,2,7],
        'Failure Probability (%)': [85.2,36.2,25.8,41.4,66.8,42.5,10.7,24.4,17.8,31.3]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize maintenance prediction dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_circle(size=100).encode(x='Failure Logs:Q', y='Failure Probability (%):Q', color='Component:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 6 - Frac Efficiency
# -------------------------------
with tabs[6]:
    st.header('💥 Frac Efficiency')
    df = pd.DataFrame({
        'Frac Type': ['Crosslinked Gel','Hybrid','Slickwater','Slickwater','Hybrid','Crosslinked Gel','Hybrid','Slickwater','Slickwater','Hybrid'],
        'Frac Score': [89.6,74.4,81.3,79.7,71.6,83.9,85.1,76.1,72.7,79.6]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize frac efficiency dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Frac Type:N', y='Frac Score:Q', color='Frac Type:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 7 - Completion Impact
# -------------------------------
with tabs[7]:
    st.header('🧩 Completion Impact')
    df = pd.DataFrame({
        'Stage Count': [23,32,31,35,17,33,27,29,26,24],
        'Post-Frac Output (bbl/d)': [1177,1028,1019,897,946,1165,854,1096,1113,1113]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize completion impact dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(x='Stage Count:Q', y='Post-Frac Output (bbl/d):Q'),
        use_container_width=True
    )

# -------------------------------
# Tab 8 - Human Factor
# -------------------------------
with tabs[8]:
    st.header('👷 Human Factor')
    df = pd.DataFrame({
        'Crew': list("ABCDABCDAB"),
        'Shift Hours': [12,10,12,12,8,12,8,10,12,10],
        'NPT (hrs)': [3.7,3.5,3.1,4.1,1.0,4.6,4.9,0.9,2.1,1.0]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize human factor dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_boxplot().encode(x='Crew:N', y='NPT (hrs):Q'),
        use_container_width=True
    )

# -------------------------------
# Tab 9 - Risk Prediction
# -------------------------------
with tabs[9]:
    st.header('⚠️ Risk Prediction')
    df = pd.DataFrame({
        'Incident Type': ['H2S','Spill','Gas Leak','Kick','Spill','H2S','Kick','Gas Leak','Spill','H2S'],
        'Historical Frequency': [1,10,4,2,6,1,9,5,8,3],
        'Current Risk Level': ['High','High','Medium','Low','High','Low','High','Medium','High','Low']
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize risk prediction dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Incident Type:N', y='Historical Frequency:Q', color='Current Risk Level:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 10 - Compression Optimization
# -------------------------------
with tabs[10]:
    st.header('🔄 Compression Optimization')
    df = pd.DataFrame({
        'Compressor': [f"C{i}" for i in range(1, 11)],
        'Well Output (mcf/d)': [355,654,454,315,458,314,342,371,613,407],
        'Compression Load (%)': [79,78,63,77,90,63,76,86,67,75]
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize compression optimization dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(x='Well Output (mcf/d):Q', y='Compression Load (%):Q', color='Compressor:N'),
        use_container_width=True
    )

# -------------------------------
# Tab 11 - Compliance Planner
# -------------------------------
with tabs[11]:
    st.header('📘 Compliance Planner')
    df = pd.DataFrame({
        'Rule': ['Flare Limit','Water Disposal','Emission Cap','Permit Renewal','Emission Cap','Flare Limit','Permit Renewal','Water Disposal','Emission Cap','Flare Limit'],
        'Current Value': [1694,918,761,2097,360,439,1752,1453,761,2097],
        'Limit': [1317,2060,1164,1456,1730,459,282,1999,1858,2152],
        'Status': ['Warning','Warning','Warning','OK','Warning','OK','Breach','Warning','OK','Breach']
    })
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize compliance planner dataset.", df))
    st.altair_chart(
        alt.Chart(df).mark_rect().encode(x='Rule:N', y='Status:N', color='Current Value:Q'),
        use_container_width=True
    )
