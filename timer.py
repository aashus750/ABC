# Import necessary libraries
import streamlit as st  # Streamlit for building the web app
import pandas as pd  # Pandas for handling the log data
import time  # Time module to track elapsed time
from datetime import datetime  # For timestamping user responses

# Initialize session state variables to persist across reruns
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()  # Record the time when the app starts
if "log" not in st.session_state:
    st.session_state.log = []  # Create an empty list to store user responses

# Set the break interval to 4 minutes (in seconds)
BREAK_INTERVAL = 1 * 60  # 240 seconds

# Calculate how much time has passed since the timer started
elapsed = time.time() - st.session_state.start_time

# Display the app title
st.title("Break Reminder App")

# Show the elapsed time in minutes
st.write(f"Elapsed time: {int(elapsed // 60)} minutes")

# If the elapsed time exceeds the break interval, show a reminder
if elapsed >= BREAK_INTERVAL:
    st.warning("You've been active for over 1 minutes. Would you like to take a break?")
    
    # Create two columns for Yes and No buttons
    col1, col2 = st.columns(2)

    # If the user clicks "Yes"
    if col1.button("Yes"):
        # Log the response with the current timestamp
        st.session_state.log.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Yes"])
        # Reset the timer
        st.session_state.start_time = time.time()
        # Show a success message
        st.success("Great! Take a break 😊")

    # If the user clicks "No"
    if col2.button("No"):
        # Log the response with the current timestamp
        st.session_state.log.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "No"])
        # Reset the timer
        st.session_state.start_time = time.time()
        # Show an info message
        st.info("Okay! Stay focused 💪")

# If there are any logged responses, display them
if st.session_state.log:
    # Convert the log list to a DataFrame
    df = pd.DataFrame(st.session_state.log, columns=["Timestamp", "Response"])
    
    # Display the log table
    st.write("Response Log:")
    st.dataframe(df)

    # Convert the DataFrame to CSV format
    csv = df.to_csv(index=False).encode('utf-8')

    # Provide a download button for the log file
    st.download_button("Download Log", csv, "break_log.csv", "text/csv")
