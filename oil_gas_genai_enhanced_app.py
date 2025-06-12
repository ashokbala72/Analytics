import streamlit as st
import pandas as pd
import openai
import altair as alt
import os
from dotenv import load_dotenv
load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def genai_response(prompt):
    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'❌ Error: {e}'

st.set_page_config(page_title='O&G Analytics Mixed Charts', layout='wide')
tabs = st.tabs([
    '🗂 Overview', '🚜 Drilling Efficiency', '📈 Lift Optimization', '🌦 Weather Sensitivity',
    '💰 Netback Margin', '🔧 Maintenance Prediction', '💥 Frac Efficiency',
    '🧩 Completion Impact', '👷 Human Factor', '⚠️ Risk Prediction',
    '🔄 Compression Optimization', '📘 Compliance Planner'
])

with tabs[0]:
    st.markdown('''
    ## 🛢️ Oil & Gas GenAI Analytics Suite

    This app is a prototype that combines **mock-simulated oilfield datasets** with **OpenAI-powered summaries** and **smart visualizations**. It is designed to demonstrate how various upstream datasets can be combined for smarter operational decisions.

    ### 🔍 What Does This App Do?
    It:
    - Presents synthetic multi-well production, drilling, completion, maintenance, and compliance data
    - Uses GenAI (GPT-3.5) to auto-summarize trends
    - Shows relevant graphs for every metric
    - Demonstrates how multiple factors can be jointly analyzed to improve field outcomes

    ### 📁 What Each Tab Represents (in layman terms):
    - **Drilling Efficiency**: Which rocks and fluids let us drill faster?
    - **Lift Optimization**: What well tweaks help pull more oil out?
    - **Weather Sensitivity**: How does bad weather affect output and safety?
    - **Netback Margin**: Which wells are most profitable after costs?
    - **Maintenance Prediction**: What’s about to break based on past issues?
    - **Frac Efficiency**: Which fracs produced the best early results?
    - **Completion Impact**: Did extra frack stages improve production?
    - **Human Factor**: Do crew shifts or hours affect drilling delays?
    - **Risk Prediction**: Which field conditions could cause incidents?
    - **Compression Optimization**: Are compressors matched to gas flow?
    - **Compliance Planner**: Are we close to violating emissions rules?

    ### 🧪 What is Real-Time vs. Simulated?
    - **All data is mocked in this prototype**, but structured like real telemetry feeds
    - Real-time integrations can easily plug into:
      - SCADA systems
      - Daily drilling/production reports
      - Weather APIs
      - Emissions logs
      - Regulatory feeds

    ### 🚀 Production Readiness
    To make this production-ready:
    - Replace mock data with real-time API connectors (SCADA, sensors, EBS, EMS)
    - Enable secure login and field/operator-level data filtering
    - Schedule background refresh or batch ETL pipelines
    - Add alerts and email/push notifications for high-risk trends
    - Plug into BI tools or corporate dashboards
    ''')
with tabs[1]:
    st.header('Drilling Efficiency')
    df = pd.DataFrame({'Well': {0: 'W1', 1: 'W2', 2: 'W3', 3: 'W4', 4: 'W5', 5: 'W6', 6: 'W7', 7: 'W8', 8: 'W9', 9: 'W10', 10: 'W11', 11: 'W12', 12: 'W13', 13: 'W14', 14: 'W15', 15: 'W16', 16: 'W17', 17: 'W18', 18: 'W19', 19: 'W20'}, 'Lithology': {0: 'Limestone', 1: 'Carbonate', 2: 'Shale', 3: 'Carbonate', 4: 'Shale', 5: 'Shale', 6: 'Carbonate', 7: 'Sandstone', 8: 'Sandstone', 9: 'Sandstone', 10: 'Carbonate', 11: 'Shale', 12: 'Sandstone', 13: 'Sandstone', 14: 'Carbonate', 15: 'Carbonate', 16: 'Sandstone', 17: 'Carbonate', 18: 'Carbonate', 19: 'Sandstone'}, 'ROP (m/hr)': {0: 31.79, 1: 27.05, 2: 27.18, 3: 15.58, 4: 17.36, 5: 19.03, 6: 25.28, 7: 20.37, 8: 23.51, 9: 31.05, 10: 22.25, 11: 26.02, 12: 29.49, 13: 18.05, 14: 19.67, 15: 20.71, 16: 34.4, 17: 23.23, 18: 34.53, 19: 30.56}, 'Mud Type': {0: 'WBM', 1: 'OBM', 2: 'WBM', 3: 'WBM', 4: 'Synthetic', 5: 'WBM', 6: 'WBM', 7: 'WBM', 8: 'Synthetic', 9: 'Synthetic', 10: 'OBM', 11: 'Synthetic', 12: 'OBM', 13: 'WBM', 14: 'Synthetic', 15: 'Synthetic', 16: 'Synthetic', 17: 'OBM', 18: 'OBM', 19: 'OBM'}, 'Efficiency Score': {0: 70.04, 1: 63.12, 2: 89.53, 3: 64.55, 4: 85.61, 5: 71.44, 6: 68.63, 7: 61.53, 8: 84.02, 9: 70.65, 10: 80.28, 11: 85.46, 12: 61.94, 13: 69.96, 14: 78.95, 15: 84.74, 16: 66.81, 17: 81.87, 18: 77.71, 19: 71.19}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the drilling efficiency dataset.')
        st.info(summary)
    bar = alt.Chart(df).mark_bar().encode(x='Well:N', y='ROP (m/hr):Q'); scatter = alt.Chart(df).mark_circle(size=100).encode(x='Well:N', y='Efficiency Score:Q', color='Mud Type:N'); st.altair_chart((bar + scatter).properties(title='ROP vs. Efficiency'), use_container_width=True)

with tabs[2]:
    st.header('Lift Optimization')
    df = pd.DataFrame({'Well': {0: 'W1', 1: 'W2', 2: 'W3', 3: 'W4', 4: 'W5', 5: 'W6', 6: 'W7', 7: 'W8', 8: 'W9', 9: 'W10', 10: 'W11', 11: 'W12', 12: 'W13', 13: 'W14', 14: 'W15', 15: 'W16', 16: 'W17', 17: 'W18', 18: 'W19', 19: 'W20'}, 'Intervention': {0: 'Gas Lift', 1: 'PCP', 2: 'Rod Pump', 3: 'Rod Pump', 4: 'PCP', 5: 'Rod Pump', 6: 'Rod Pump', 7: 'Rod Pump', 8: 'ESP', 9: 'PCP', 10: 'Rod Pump', 11: 'Gas Lift', 12: 'Rod Pump', 13: 'ESP', 14: 'ESP', 15: 'ESP', 16: 'PCP', 17: 'Gas Lift', 18: 'ESP', 19: 'PCP'}, 'Choke Size (mm)': {0: 23, 1: 20, 2: 19, 3: 38, 4: 25, 5: 20, 6: 21, 7: 28, 8: 28, 9: 32, 10: 26, 11: 32, 12: 19, 13: 23, 14: 37, 15: 26, 16: 19, 17: 25, 18: 19, 19: 29}, 'Flow Rate (bbl/d)': {0: 1381, 1: 1187, 2: 1208, 3: 1395, 4: 750, 5: 915, 6: 867, 7: 1235, 8: 1253, 9: 1062, 10: 987, 11: 1172, 12: 1398, 13: 1305, 14: 1121, 15: 1055, 16: 1088, 17: 750, 18: 755, 19: 772}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the lift optimization dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_line(point=True).encode(x='Choke Size (mm):Q', y='Flow Rate (bbl/d):Q', color='Intervention:N').properties(title='Flow vs. Choke Size'), use_container_width=True)

with tabs[3]:
    st.header('Weather Sensitivity')
    df = pd.DataFrame({'Weather Event': {0: 'Rain', 1: 'Fog', 2: 'Storm', 3: 'Heatwave', 4: 'Rain', 5: 'Rain', 6: 'Heatwave', 7: 'Rain', 8: 'Heatwave', 9: 'Fog', 10: 'Fog', 11: 'Storm', 12: 'Snow', 13: 'Storm', 14: 'Snow', 15: 'Heatwave', 16: 'Storm', 17: 'Fog', 18: 'Heatwave', 19: 'Fog'}, 'Flow Impact (%)': {0: -19.6, 1: -19.1, 2: -4.8, 3: -18.8, 4: -7.6, 5: -4.3, 6: -10.0, 7: -13.5, 8: -9.6, 9: -12.3, 10: -19.8, 11: -10.6, 12: -10.3, 13: -15.5, 14: -4.6, 15: -5.7, 16: -4.3, 17: -12.8, 18: -6.1, 19: -15.1}, 'Safety Incident Risk': {0: 'Medium', 1: 'High', 2: 'High', 3: 'Low', 4: 'Medium', 5: 'High', 6: 'Medium', 7: 'High', 8: 'High', 9: 'High', 10: 'Low', 11: 'Low', 12: 'Medium', 13: 'High', 14: 'Low', 15: 'Low', 16: 'High', 17: 'Low', 18: 'Medium', 19: 'High'}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the weather sensitivity dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_bar().encode(x='Weather Event:N', y='Flow Impact (%):Q', color='Safety Incident Risk:N').properties(title='Impact by Weather'), use_container_width=True)

with tabs[4]:
    st.header('Netback Margin')
    df = pd.DataFrame({'Well': {0: 'W1', 1: 'W2', 2: 'W3', 3: 'W4', 4: 'W5', 5: 'W6', 6: 'W7', 7: 'W8', 8: 'W9', 9: 'W10', 10: 'W11', 11: 'W12', 12: 'W13', 13: 'W14', 14: 'W15', 15: 'W16', 16: 'W17', 17: 'W18', 18: 'W19', 19: 'W20'}, 'Intervention': {0: 'Gas Lift', 1: 'PCP', 2: 'Rod Pump', 3: 'Rod Pump', 4: 'PCP', 5: 'Rod Pump', 6: 'Rod Pump', 7: 'Rod Pump', 8: 'ESP', 9: 'PCP', 10: 'Rod Pump', 11: 'Gas Lift', 12: 'Rod Pump', 13: 'ESP', 14: 'ESP', 15: 'ESP', 16: 'PCP', 17: 'Gas Lift', 18: 'ESP', 19: 'PCP'}, 'Choke Size (mm)': {0: 23, 1: 20, 2: 19, 3: 38, 4: 25, 5: 20, 6: 21, 7: 28, 8: 28, 9: 32, 10: 26, 11: 32, 12: 19, 13: 23, 14: 37, 15: 26, 16: 19, 17: 25, 18: 19, 19: 29}, 'Flow Rate (bbl/d)': {0: 1381, 1: 1187, 2: 1208, 3: 1395, 4: 750, 5: 915, 6: 867, 7: 1235, 8: 1253, 9: 1062, 10: 987, 11: 1172, 12: 1398, 13: 1305, 14: 1121, 15: 1055, 16: 1088, 17: 750, 18: 755, 19: 772}, 'Price ($/bbl)': {0: 83.22, 1: 77.23, 2: 83.9, 3: 79.73, 4: 77.09, 5: 84.34, 6: 76.93, 7: 80.48, 8: 83.21, 9: 81.23, 10: 82.36, 11: 83.35, 12: 83.35, 13: 75.59, 14: 82.88, 15: 80.71, 16: 84.28, 17: 80.85, 18: 83.68, 19: 83.91}, 'Transport Cost': {0: 3, 1: 8, 2: 3, 3: 6, 4: 6, 5: 7, 6: 5, 7: 3, 8: 7, 9: 7, 10: 3, 11: 5, 12: 4, 13: 7, 14: 4, 15: 5, 16: 5, 17: 4, 18: 5, 19: 8}, 'Netback ($)': {0: 110783.81999999999, 1: 82176.01000000001, 2: 97727.20000000001, 3: 102853.35, 4: 53317.5, 5: 70766.1, 6: 62363.310000000005, 7: 95687.8, 8: 95491.12999999999, 9: 78832.26000000001, 10: 78328.31999999999, 11: 91826.2, 12: 110931.29999999999, 13: 89509.95000000001, 14: 88424.48, 15: 79874.04999999999, 16: 86256.64, 17: 57637.49999999999, 18: 59403.40000000001, 19: 58602.52}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the netback margin dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_bar().encode(x='Well:N', y='Netback ($):Q', color='Intervention:N').properties(title='Netback by Well'), use_container_width=True)

with tabs[5]:
    st.header('Maintenance Prediction')
    df = pd.DataFrame({'Component': {0: 'Sensor', 1: 'Compressor', 2: 'Sensor', 3: 'Compressor', 4: 'Pump', 5: 'Pump', 6: 'Compressor', 7: 'Sensor', 8: 'Pump', 9: 'Pump', 10: 'Valve', 11: 'Sensor', 12: 'Compressor', 13: 'Compressor', 14: 'Sensor', 15: 'Pump', 16: 'Sensor', 17: 'Pump', 18: 'Sensor', 19: 'Compressor'}, 'Failure Logs': {0: 13, 1: 11, 2: 4, 3: 7, 4: 1, 5: 2, 6: 8, 7: 11, 8: 11, 9: 13, 10: 11, 11: 14, 12: 9, 13: 3, 14: 9, 15: 6, 16: 10, 17: 4, 18: 3, 19: 11}, 'Maintenance Events': {0: 3, 1: 2, 2: 4, 3: 7, 4: 5, 5: 3, 6: 9, 7: 3, 8: 4, 9: 8, 10: 8, 11: 0, 12: 2, 13: 1, 14: 0, 15: 0, 16: 7, 17: 9, 18: 0, 19: 0}, 'Failure Probability (%)': {0: 85.2, 1: 36.2, 2: 17.9, 3: 31.3, 4: 25.8, 5: 17.8, 6: 86.2, 7: 51.6, 8: 45.6, 9: 53.6, 10: 41.4, 11: 66.8, 12: 10.7, 13: 42.5, 14: 57.2, 15: 55.7, 16: 34.9, 17: 60.0, 18: 19.3, 19: 24.4}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the maintenance prediction dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_circle(size=100).encode(x='Failure Logs:Q', y='Failure Probability (%):Q', color='Component:N').properties(title='Failure Prob vs Logs'), use_container_width=True)

with tabs[6]:
    st.header('Frac Efficiency')
    df = pd.DataFrame({'Frac Type': {0: 'Crosslinked Gel', 1: 'Hybrid', 2: 'Crosslinked Gel', 3: 'Slickwater', 4: 'Slickwater', 5: 'Slickwater', 6: 'Hybrid', 7: 'Hybrid', 8: 'Slickwater', 9: 'Slickwater', 10: 'Hybrid', 11: 'Hybrid', 12: 'Crosslinked Gel', 13: 'Slickwater', 14: 'Slickwater', 15: 'Hybrid', 16: 'Slickwater', 17: 'Crosslinked Gel', 18: 'Hybrid', 19: 'Slickwater'}, 'IP30 (bbl/d)': {0: 863, 1: 847, 2: 842, 3: 964, 4: 891, 5: 831, 6: 826, 7: 928, 8: 896, 9: 917, 10: 945, 11: 855, 12: 833, 13: 954, 14: 868, 15: 895, 16: 867, 17: 982, 18: 867, 19: 905}, 'EUR (MBOE)': {0: 346, 1: 302, 2: 326, 3: 331, 4: 314, 5: 349, 6: 313, 7: 354, 8: 367, 9: 320, 10: 369, 11: 334, 12: 295, 13: 298, 14: 336, 15: 342, 16: 370, 17: 336, 18: 353, 19: 351}, 'Frac Score': {0: 89.62, 1: 74.41, 2: 84.47, 3: 81.34, 4: 86.54, 5: 79.75, 6: 73.57, 7: 71.65, 8: 77.47, 9: 83.91, 10: 73.57, 11: 70.47, 12: 72.96, 13: 81.46, 14: 81.61, 15: 85.11, 16: 76.13, 17: 78.28, 18: 72.78, 19: 79.66}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the frac efficiency dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_bar().encode(x='Frac Type:N', y='Frac Score:Q', color='Frac Type:N').properties(title='Frac Score by Type'), use_container_width=True)

with tabs[7]:
    st.header('Completion Impact')
    df = pd.DataFrame({'Stage Count': {0: 23, 1: 32, 2: 31, 3: 35, 4: 17, 5: 33, 6: 27, 7: 29, 8: 26, 9: 24, 10: 30, 11: 18, 12: 17, 13: 15, 14: 34, 15: 30, 16: 32, 17: 31, 18: 33, 19: 23}, 'Proppant (tons)': {0: 319, 1: 233, 2: 269, 3: 156, 4: 296, 5: 202, 6: 167, 7: 164, 8: 247, 9: 175, 10: 155, 11: 242, 12: 278, 13: 196, 14: 166, 15: 168, 16: 279, 17: 193, 18: 155, 19: 208}, 'Post-Frac Output (bbl/d)': {0: 1177, 1: 1028, 2: 1019, 3: 897, 4: 946, 5: 1165, 6: 854, 7: 1096, 8: 1113, 9: 1113, 10: 843, 11: 1196, 12: 982, 13: 1007, 14: 877, 15: 1150, 16: 962, 17: 817, 18: 1054, 19: 849}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the completion impact dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_line(point=True).encode(x='Stage Count:Q', y='Post-Frac Output (bbl/d):Q').properties(title='Output by Stage Count'), use_container_width=True)

with tabs[8]:
    st.header('Human Factor')
    df = pd.DataFrame({'Crew': {0: 'B', 1: 'D', 2: 'D', 3: 'B', 4: 'B', 5: 'C', 6: 'C', 7: 'B', 8: 'C', 9: 'A', 10: 'D', 11: 'B', 12: 'C', 13: 'A', 14: 'B', 15: 'A', 16: 'D', 17: 'D', 18: 'C', 19: 'B'}, 'Shift Hours': {0: 12, 1: 10, 2: 12, 3: 12, 4: 8, 5: 12, 6: 8, 7: 10, 8: 12, 9: 10, 10: 12, 11: 10, 12: 12, 13: 8, 14: 10, 15: 10, 16: 10, 17: 10, 18: 10, 19: 10}, 'NPT (hrs)': {0: 3.72, 1: 3.54, 2: 3.06, 3: 4.06, 4: 1.04, 5: 4.58, 6: 4.92, 7: 0.88, 8: 2.09, 9: 0.97, 10: 3.68, 11: 4.72, 12: 4.14, 13: 0.97, 14: 3.86, 15: 1.0, 16: 2.31, 17: 0.9, 18: 3.45, 19: 2.58}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the human factor dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_boxplot().encode(x='Crew:N', y='NPT (hrs):Q').properties(title='NPT by Crew'), use_container_width=True)

with tabs[9]:
    st.header('Risk Prediction')
    df = pd.DataFrame({'Incident Type': {0: 'H2S', 1: 'Spill', 2: 'Spill', 3: 'H2S', 4: 'H2S', 5: 'Gas Leak', 6: 'Spill', 7: 'Kick', 8: 'Gas Leak', 9: 'Spill', 10: 'Gas Leak', 11: 'H2S', 12: 'H2S', 13: 'Spill', 14: 'H2S', 15: 'Spill', 16: 'Kick', 17: 'Gas Leak', 18: 'Gas Leak', 19: 'H2S'}, 'Historical Frequency': {0: 1, 1: 1, 2: 10, 3: 5, 4: 6, 5: 4, 6: 1, 7: 2, 8: 6, 9: 2, 10: 1, 11: 1, 12: 8, 13: 4, 14: 1, 15: 3, 16: 10, 17: 8, 18: 9, 19: 5}, 'Current Risk Level': {0: 'High', 1: 'Low', 2: 'High', 3: 'High', 4: 'High', 5: 'Low', 6: 'Low', 7: 'Medium', 8: 'High', 9: 'Low', 10: 'Medium', 11: 'High', 12: 'High', 13: 'High', 14: 'High', 15: 'Low', 16: 'High', 17: 'Medium', 18: 'Low', 19: 'Medium'}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the risk prediction dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_bar().encode(x='Incident Type:N', y='Historical Frequency:Q', color='Current Risk Level:N').properties(title='Incidents by Type'), use_container_width=True)

with tabs[10]:
    st.header('Compression Optimization')
    df = pd.DataFrame({'Compressor': {0: 'C1', 1: 'C2', 2: 'C3', 3: 'C4', 4: 'C5', 5: 'C6', 6: 'C7', 7: 'C8', 8: 'C9', 9: 'C10', 10: 'C11', 11: 'C12', 12: 'C13', 13: 'C14', 14: 'C15', 15: 'C16', 16: 'C17', 17: 'C18', 18: 'C19', 19: 'C20'}, 'Well Output (mcf/d)': {0: 355, 1: 654, 2: 454, 3: 315, 4: 458, 5: 314, 6: 342, 7: 371, 8: 613, 9: 407, 10: 669, 11: 461, 12: 388, 13: 690, 14: 332, 15: 579, 16: 412, 17: 514, 18: 605, 19: 452}, 'Compression Load (%)': {0: 79, 1: 78, 2: 63, 3: 77, 4: 90, 5: 63, 6: 76, 7: 86, 8: 67, 9: 75, 10: 84, 11: 66, 12: 88, 13: 70, 14: 81, 15: 85, 16: 64, 17: 80, 18: 87, 19: 64}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the compression optimization dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_line(point=True).encode(x='Well Output (mcf/d):Q', y='Compression Load (%):Q', color='Compressor:N').properties(title='Load vs Output'), use_container_width=True)

with tabs[11]:
    st.header('Compliance Planning')
    df = pd.DataFrame({'Rule': {0: 'Flare Limit', 1: 'Water Disposal', 2: 'Emission Cap', 3: 'Emission Cap', 4: 'Permit Renewal', 5: 'Emission Cap', 6: 'Emission Cap', 7: 'Emission Cap', 8: 'Permit Renewal', 9: 'Water Disposal', 10: 'Flare Limit', 11: 'Flare Limit', 12: 'Permit Renewal', 13: 'Permit Renewal', 14: 'Emission Cap', 15: 'Permit Renewal', 16: 'Emission Cap', 17: 'Permit Renewal', 18: 'Flare Limit', 19: 'Water Disposal'}, 'Current Value': {0: 1694, 1: 918, 2: 761, 3: 698, 4: 2097, 5: 360, 6: 687, 7: 2178, 8: 1264, 9: 487, 10: 439, 11: 492, 12: 1752, 13: 1729, 14: 308, 15: 1149, 16: 1820, 17: 597, 18: 1439, 19: 1453}, 'Limit': {0: 1317, 1: 2060, 2: 1164, 3: 1087, 4: 1456, 5: 1730, 6: 352, 7: 1400, 8: 1796, 9: 2047, 10: 459, 11: 999, 12: 282, 13: 1999, 14: 1858, 15: 2152, 16: 1487, 17: 1375, 18: 1701, 19: 2165}, 'Status': {0: 'Warning', 1: 'Warning', 2: 'Warning', 3: 'OK', 4: 'Warning', 5: 'Warning', 6: 'Breach', 7: 'OK', 8: 'OK', 9: 'Warning', 10: 'OK', 11: 'Breach', 12: 'Breach', 13: 'Warning', 14: 'OK', 15: 'OK', 16: 'Warning', 17: 'Warning', 18: 'Breach', 19: 'Breach'}})
    st.dataframe(df)
    with st.spinner('Generating GenAI summary...'):
        summary = genai_response('Summarize trends in the compliance planning dataset.')
        st.info(summary)
    st.altair_chart(alt.Chart(df).mark_rect().encode(x='Rule:N', y='Status:N', color='Current Value:Q').properties(title='Compliance Heatmap'), use_container_width=True)

