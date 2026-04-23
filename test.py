import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r'C:\Users\Piyush Kumar\Desktop\lessgo\projects\predictive-maintenance-project\model.pkl')

# Page config
st.set_page_config(page_title="Predictive Maintenance Dashboard", 
                   page_icon="⚙️", 
                   layout="wide")

# Title
st.title("⚙️ Industrial Machine Failure Prediction")
st.subheader("Physics-Informed AI for Predictive Maintenance")
st.markdown("---")

# Input section
st.header("Enter Machine Parameters")

col1, col2 = st.columns(2)

with col1:
    air_temp = st.slider("Air Temperature (K)", 295.0, 305.0, 300.0)
    process_temp = st.slider("Process Temperature (K)", 305.0, 315.0, 310.0)
    rotational_speed = st.slider("Rotational Speed (RPM)", 1168, 2886, 1500)

with col2:
    torque = st.slider("Torque (Nm)", 3.8, 76.6, 40.0)
    tool_wear = st.slider("Tool Wear (min)", 0, 253, 100)
    machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

st.markdown("---")

# Calculate physics features
power_watts = torque * rotational_speed * (np.pi / 30)
temp_difference = process_temp - air_temp
wear_strain = tool_wear * torque

# Show physics features
st.header("Physics-Based Analysis")
col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Power Output", f"{power_watts:.0f} W", 
              delta="High Risk" if power_watts > 7282 else "Normal")

with col4:
    st.metric("Heat Dissipation", f"{temp_difference:.1f} K",
              delta="Poor Cooling" if temp_difference < 9.4 else "Normal")

with col5:
    st.metric("Wear Strain", f"{wear_strain:.0f}",
              delta="High Risk" if wear_strain > 7187 else "Normal")

st.markdown("---")


type_map = {"L": 0, "M": 1, "H": 2} 
type_numeric = type_map[machine_type]

input_data = pd.DataFrame({
    'Type': [type_numeric],
    'Air temperature [K]': [air_temp],
    'Process temperature [K]': [process_temp],
    'Rotational speed [rpm]': [rotational_speed],
    'Torque [Nm]': [torque],
    'Tool wear [min]': [tool_wear],
    'Power [Watts]': [power_watts],
    'Temp_Difference [K]': [temp_difference],
    'Wear_Progression': [wear_strain],
    
})
# Prediction
prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]

# Result
st.header("Prediction Result")

if prediction == 1:
    st.error(f"⚠️ WARNING: Machine Failure Predicted!")
    st.error(f"Failure Probability: {probability*100:.1f}%")
    st.markdown("### Recommended Actions:")
    if power_watts > 7282:
        st.write("🔴 Reduce rotational speed or torque immediately")
    if temp_difference < 9.4:
        st.write("🔴 Check cooling system and fans")
    if wear_strain > 7187:
        st.write("🔴 Replace tool immediately")
else:
    st.success(f"✅ Machine Operating Normally")
    st.success(f"Failure Probability: {probability*100:.1f}%")

# Footer
st.markdown("---")
st.markdown("Built by Piyush Kumar | IIT Goa Mechanical Engineering")
st.markdown("Physics-Informed ML for Industrial Predictive Maintenance")