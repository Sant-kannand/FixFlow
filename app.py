import pandas as pd
import streamlit as st
import joblib
st.set_page_config(
    page_title="FixFlow",
    page_icon="🛠️",
    layout="wide"
)

# Load models
category_model = joblib.load("models/category_model.pkl")
priority_model = joblib.load("models/priority_model.pkl")
st.sidebar.title("🛠️ FixFlow")

st.sidebar.success(
    "Complaint Management System"
)

st.sidebar.markdown("""
### Features
- AI Classification
- Priority Prediction
- Complaint Tracking
- Analytics Dashboard
- Status Management
""")

st.title("🛠️ FixFlow")

st.markdown("""
### AI-Powered Complaint Classification & Management System

Submit, track, and manage complaints using Machine Learning.
""")
st.markdown(
    "### AI-Powered Complaint Classification and Management System"
)
st.sidebar.title("FixFlow")

st.sidebar.info(
    "Submit, Track and Manage Complaints"
)
st.info(
    "FixFlow uses Machine Learning to classify complaints and predict priority levels automatically."
)

complaint = st.text_area("Enter your complaint")

if st.button("Analyze Complaint"):

    category = category_model.predict([complaint])[0]
    priority = priority_model.predict([complaint])[0]

    # Generate Complaint ID
    df = pd.read_csv("complaints.csv")

    complaint_id = f"FF{len(df)+1:03d}"

    # Save complaint
    new_row = pd.DataFrame([{
        "ComplaintID": complaint_id,
        "Complaint": complaint,
        "Category": category,
        "Priority": priority,
        "Status": "Pending"
    }])

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv("complaints.csv", index=False)

    st.subheader("FixFlow Analysis")

    st.write(f"🆔 Complaint ID: {complaint_id}")

    st.success(
    f"🔧 Issue Type: {category}")

    if priority == "High":

       st.error(
          f"🚨 Priority: {priority}"
         )

    elif priority == "Medium":

       st.warning(
          f"⚠️ Priority: {priority}"
    )
    else:

       st.info(
          f"ℹ️ Priority: {priority}"
    )

st.divider()

st.subheader("🔍 Track Complaint")

search_id = st.text_input("Enter Complaint ID")

if st.button("Track Complaint"):

    df = pd.read_csv("complaints.csv")

    result = df[df["ComplaintID"] == search_id]

    if not result.empty:

        st.write(f"Status: {result.iloc[0]['Status']}")
        st.write(f"Category: {result.iloc[0]['Category']}")
        st.write(f"Priority: {result.iloc[0]['Priority']}")

    else:
        st.error("Complaint ID not found")
st.divider()

st.subheader("📊 Admin Dashboard")

df = pd.read_csv("complaints.csv")

total_complaints = len(df)

pending_complaints = len(
    df[df["Status"] == "Pending"]
)

high_priority = len(
    df[df["Priority"] == "High"]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Complaints",
    total_complaints
)

col2.metric(
    "Pending",
    pending_complaints
)

col3.metric(
    "High Priority",
    high_priority
)

st.write(
    f"⏳ Pending Complaints: {pending_complaints}"
)

st.write(
    f"🚨 High Priority Complaints: {high_priority}"
)        
import matplotlib.pyplot as plt

st.divider()

st.subheader("📈 Complaint Analytics")

category_counts = df["Category"].value_counts()

fig, ax = plt.subplots()

category_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Complaints by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Count")

st.pyplot(fig)
st.subheader("⚡ Priority Analytics")

priority_counts = df["Priority"].value_counts()

fig2, ax2 = plt.subplots()

priority_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

ax2.set_ylabel("")

st.pyplot(fig2)
st.divider()

with st.expander(
    "📋 View All Complaints"
):

    st.dataframe(df)
st.divider()

st.subheader("🛠️ Update Complaint Status")

update_id = st.text_input(
    "Enter Complaint ID to Update"
)

new_status = st.selectbox(
    "Select New Status",
    ["Pending", "In Progress", "Resolved"]
)

if st.button("Update Status"):

    df = pd.read_csv("complaints.csv")

    if update_id in df["ComplaintID"].values:

        df.loc[
            df["ComplaintID"] == update_id,
            "Status"
        ] = new_status

        df.to_csv(
            "complaints.csv",
            index=False
        )

        st.success(
            "Status Updated Successfully!"
        )

    else:

        st.error(
            "Complaint ID not found"
        )
st.divider()

st.caption(
    "FixFlow © 2026 | AI-Powered Complaint Management System"
)        