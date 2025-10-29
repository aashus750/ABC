import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "log" not in st.session_state:
    st.session_state.log = []

# Set break interval (4 minutes)
BREAK_INTERVAL = 2 * 60  # 240 seconds

# Calculate elapsed time
elapsed = time.time() - st.session_state.start_time

st.title("Break Reminder App")

# Show elapsed time
st.write(f"Elapsed time: {int(elapsed // 60)} minutes")

# If time exceeds interval, show reminder
if elapsed >= BREAK_INTERVAL:
    st.warning("You've been active for over 4 minutes. Would you like to take a break?")
    
    col1, col2 = st.columns(2)
    if col1.button("Yes"):
        st.session_state.log.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Yes"])
        st.session_state.start_time = time.time()
        st.success("Great! Take a break 😊")
    if col2.button("No"):
        st.session_state.log.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "No"])
        st.session_state.start_time = time.time()
        st.info("Okay! Stay focused 💪")

# Show log
if st.session_state.log:
    df = pd.DataFrame(st.session_state.log, columns=["Timestamp", "Response"])
    st.write("Response Log:")
    st.dataframe(df)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Log", csv, "break_log.csv", "text/csv")
