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

def genai_response(prompt: str):
    """Call Azure OpenAI to generate a response"""
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
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

    This app combines **mock oilfield datasets** with **Azure OpenAI (gpt-4o-raj)** for smart summaries and visualizations.

    ### Tabs:
    - Drilling Efficiency → Which rocks & fluids drill faster?
    - Lift Optimization → What tweaks help extract more oil?
    - Weather Sensitivity → Impact of weather on output & safety
    - Netback Margin → Profitable wells after costs
    - Maintenance Prediction → Failures & downtime risks
    - Frac Efficiency → Best performing fracs
    - Completion Impact → Effect of more frac stages
    - Human Factor → Crew & shift impacts
    - Risk Prediction → Incident likelihood
    - Compression Optimization → Match compressors to gas flow
    - Compliance Planner → Regulatory risks
    ''')

# -------------------------------
# Tab 1 - Drilling Efficiency
# -------------------------------
with tabs[1]:
    st.header('🚜 Drilling Efficiency')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 21)],
        'Lithology': ['Limestone','Carbonate','Shale','Carbonate','Shale','Shale','Carbonate',
                      'Sandstone','Sandstone','Sandstone','Carbonate','Shale','Sandstone',
                      'Sandstone','Carbonate','Carbonate','Sandstone','Carbonate','Carbonate','Sandstone'],
        'ROP (m/hr)': [31.79,27.05,27.18,15.58,17.36,19.03,25.28,20.37,23.51,31.05,22.25,
                       26.02,29.49,18.05,19.67,20.71,34.4,23.23,34.53,30.56],
        'Mud Type': ['WBM','OBM','WBM','WBM','Synthetic','WBM','WBM','WBM','Synthetic','Synthetic',
                     'OBM','Synthetic','OBM','WBM','Synthetic','Synthetic','Synthetic','OBM','OBM','OBM'],
        'Efficiency Score': [70.04,63.12,89.53,64.55,85.61,71.44,68.63,61.53,84.02,70.65,
                             80.28,85.46,61.94,69.96,78.95,84.74,66.81,81.87,77.71,71.19]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize trends in drilling efficiency dataset."))

    bar = alt.Chart(df).mark_bar().encode(x='Well:N', y='ROP (m/hr):Q')
    scatter = alt.Chart(df).mark_circle(size=100).encode(x='Well:N', y='Efficiency Score:Q', color='Mud Type:N')
    st.altair_chart((bar + scatter).properties(title='ROP vs Efficiency'), use_container_width=True)

# -------------------------------
# Tab 2 - Lift Optimization
# -------------------------------
with tabs[2]:
    st.header('📈 Lift Optimization')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 21)],
        'Intervention': ['Gas Lift','PCP','Rod Pump','Rod Pump','PCP','Rod Pump','Rod Pump',
                         'Rod Pump','ESP','PCP','Rod Pump','Gas Lift','Rod Pump','ESP',
                         'ESP','ESP','PCP','Gas Lift','ESP','PCP'],
        'Choke Size (mm)': [23,20,19,38,25,20,21,28,28,32,26,32,19,23,37,26,19,25,19,29],
        'Flow Rate (bbl/d)': [1381,1187,1208,1395,750,915,867,1235,1253,1062,987,1172,
                              1398,1305,1121,1055,1088,750,755,772]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize trends in lift optimization dataset."))

    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(
            x='Choke Size (mm):Q', y='Flow Rate (bbl/d):Q', color='Intervention:N'
        ).properties(title='Flow vs Choke Size'),
        use_container_width=True
    )

# -------------------------------
# Tab 3 - Weather Sensitivity
# -------------------------------
with tabs[3]:
    st.header('🌦 Weather Sensitivity')
    df = pd.DataFrame({
        'Weather Event': ['Rain','Fog','Storm','Heatwave','Rain','Rain','Heatwave','Rain','Heatwave','Fog',
                          'Fog','Storm','Snow','Storm','Snow','Heatwave','Storm','Fog','Heatwave','Fog'],
        'Flow Impact (%)': [-19.6,-19.1,-4.8,-18.8,-7.6,-4.3,-10.0,-13.5,-9.6,-12.3,
                            -19.8,-10.6,-10.3,-15.5,-4.6,-5.7,-4.3,-12.8,-6.1,-15.1],
        'Safety Incident Risk': ['Medium','High','High','Low','Medium','High','Medium','High','High','High',
                                 'Low','Low','Medium','High','Low','Low','High','Low','Medium','High']
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize weather sensitivity dataset."))

    st.altair_chart(
        alt.Chart(df).mark_bar().encode(
            x='Weather Event:N', y='Flow Impact (%):Q', color='Safety Incident Risk:N'
        ).properties(title='Impact by Weather'),
        use_container_width=True
    )

# -------------------------------
# Tab 4 - Netback Margin
# -------------------------------
with tabs[4]:
    st.header('💰 Netback Margin')
    df = pd.DataFrame({
        'Well': [f"W{i}" for i in range(1, 21)],
        'Price ($/bbl)': [83.22,77.23,83.9,79.73,77.09,84.34,76.93,80.48,83.21,81.23,
                          82.36,83.35,83.35,75.59,82.88,80.71,84.28,80.85,83.68,83.91],
        'Transport Cost': [3,8,3,6,6,7,5,3,7,7,3,5,4,7,4,5,5,4,5,8],
        'Flow Rate (bbl/d)': [1381,1187,1208,1395,750,915,867,1235,1253,1062,
                              987,1172,1398,1305,1121,1055,1088,750,755,772]
    })
    df['Netback ($)'] = (df['Price ($/bbl)'] - df['Transport Cost']) * df['Flow Rate (bbl/d)']
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize netback margin dataset."))

    st.altair_chart(
        alt.Chart(df).mark_bar().encode(
            x='Well:N', y='Netback ($):Q', color='Price ($/bbl):Q'
        ).properties(title='Netback by Well'),
        use_container_width=True
    )

# -------------------------------
# Tab 5 - Maintenance Prediction
# -------------------------------
with tabs[5]:
    st.header('🔧 Maintenance Prediction')
    df = pd.DataFrame({
        'Component': ['Sensor','Compressor','Pump','Valve']*5,
        'Failure Logs': [13,11,1,11,14,3,9,11,2,7,6,10,3,11,8,9,5,2,4,7],
        'Failure Probability (%)': [85.2,36.2,25.8,41.4,66.8,42.5,10.7,24.4,17.8,31.3,
                                    86.2,34.9,19.3,53.6,57.2,60.0,55.7,71.4,45.6,51.6]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize maintenance prediction dataset."))

    st.altair_chart(
        alt.Chart(df).mark_circle(size=100).encode(
            x='Failure Logs:Q', y='Failure Probability (%):Q', color='Component:N'
        ).properties(title='Failure Prob vs Logs'),
        use_container_width=True
    )

# -------------------------------
# Tab 6 - Frac Efficiency
# -------------------------------
with tabs[6]:
    st.header('💥 Frac Efficiency')
    df = pd.DataFrame({
        'Frac Type': ['Crosslinked Gel','Hybrid','Slickwater']*7,
        'Frac Score': [89.6,74.4,81.3,79.7,71.6,83.9,85.1,76.1,72.7,79.6,86.5,77.4,73.6,81.5,83.2,84.7,78.9,80.3,82.1,79.0]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize frac efficiency dataset."))

    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Frac Type:N', y='Frac Score:Q', color='Frac Type:N')
        .properties(title='Frac Score by Type'),
        use_container_width=True
    )

# -------------------------------
# Tab 7 - Completion Impact
# -------------------------------
with tabs[7]:
    st.header('🧩 Completion Impact')
    df = pd.DataFrame({
        'Stage Count': [23,32,31,35,17,33,27,29,26,24,30,18,17,15,34,30,32,31,33,23],
        'Post-Frac Output (bbl/d)': [1177,1028,1019,897,946,1165,854,1096,1113,1113,
                                     843,1196,982,1007,877,1150,962,817,1054,849]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize completion impact dataset."))

    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(
            x='Stage Count:Q', y='Post-Frac Output (bbl/d):Q'
        ).properties(title='Output by Stage Count'),
        use_container_width=True
    )

# -------------------------------
# Tab 8 - Human Factor
# -------------------------------
with tabs[8]:
    st.header('👷 Human Factor')
    df = pd.DataFrame({
        'Crew': list("ABCDABCDABCDABCDABCD"),
        'Shift Hours': [12,10,12,12,8,12,8,10,12,10,12,10,12,8,10,10,10,10,10,10],
        'NPT (hrs)': [3.7,3.5,3.1,4.1,1.0,4.6,4.9,0.9,2.1,1.0,3.7,4.7,4.1,1.0,3.9,1.0,2.3,0.9,3.5,2.6]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize human factor dataset."))

    st.altair_chart(
        alt.Chart(df).mark_boxplot().encode(x='Crew:N', y='NPT (hrs):Q')
        .properties(title='NPT by Crew'),
        use_container_width=True
    )

# -------------------------------
# Tab 9 - Risk Prediction
# -------------------------------
with tabs[9]:
    st.header('⚠️ Risk Prediction')
    df = pd.DataFrame({
        'Incident Type': ['H2S','Spill','Gas Leak','Kick']*5,
        'Historical Frequency': [1,10,4,2,6,1,9,5,8,3,7,6,10,2,5,9,4,6,3,8],
        'Current Risk Level': ['High','High','Medium','Low','High','Low','High','Medium',
                               'High','Low','Medium','High','High','Medium','Low','High','Low','Medium','High','Low']
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize risk prediction dataset."))

    st.altair_chart(
        alt.Chart(df).mark_bar().encode(x='Incident Type:N', y='Historical Frequency:Q', color='Current Risk Level:N')
        .properties(title='Incidents by Type'),
        use_container_width=True
    )

# -------------------------------
# Tab 10 - Compression Optimization
# -------------------------------
with tabs[10]:
    st.header('🔄 Compression Optimization')
    df = pd.DataFrame({
        'Compressor': [f"C{i}" for i in range(1, 21)],
        'Well Output (mcf/d)': [355,654,454,315,458,314,342,371,613,407,669,461,388,690,332,579,412,514,605,452],
        'Compression Load (%)': [79,78,63,77,90,63,76,86,67,75,84,66,88,70,81,85,64,80,87,64]
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize compression optimization dataset."))

    st.altair_chart(
        alt.Chart(df).mark_line(point=True).encode(
            x='Well Output (mcf/d):Q', y='Compression Load (%) :Q', color='Compressor:N'
        ).properties(title='Load vs Output'),
        use_container_width=True
    )

# -------------------------------
# Tab 11 - Compliance Planner
# -------------------------------
with tabs[11]:
    st.header('📘 Compliance Planner')
    df = pd.DataFrame({
        'Rule': ['Flare Limit','Water Disposal','Emission Cap','Permit Renewal']*5,
        'Current Value': [1694,918,761,2097,360,2178,1264,487,439,1752,308,1149,1820,597,1439,1453,761,2097,1264,487],
        'Limit': [1317,2060,1164,1456,1730,1400,1796,2047,459,999,1858,2152,1487,1375,1701,2165,1164,1456,1796,2047],
        'Status': ['Warning','Warning','Warning','OK','Warning','OK','OK','Warning','OK','Breach',
                   'Breach','Warning','OK','Warning','Warning','Breach','Warning','OK','OK','Breach']
    })
    st.dataframe(df)

    with st.spinner('Generating GenAI summary...'):
        st.info(genai_response("Summarize compliance planning dataset."))

    st.altair_chart(
        alt.Chart(df).mark_rect().encode(x='Rule:N', y='Status:N', color='Current Value:Q')
        .properties(title='Compliance Heatmap'),
        use_container_width=True
    )
