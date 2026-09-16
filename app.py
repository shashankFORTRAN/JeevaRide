import streamlit as st

st.set_page_config(
    page_title="JeevaRide",
    page_icon="🚑"
)

st.title("🚑 JeevaRide")
st.subheader("Rural Emergency Transportation Network")

st.write(
    "JeevaRide is a concept designed to help people in rural areas "
    "find emergency transportation quickly."
)

st.divider()

st.header("📍 Request Emergency Transport")

name = st.text_input("Patient Name")
location = st.text_input("Pickup Location")

emergency = st.selectbox(
    "Type of Emergency",
    [
        "Heart Attack",
        "Stroke",
        "Pregnancy Emergency",
        "Accident",
        "Snake Bite",
        "Other"
    ]
)

hospital = st.text_input("Destination Hospital")

if st.button("🚑 Request Ride"):

    if name and location and hospital:

        st.success("Emergency request created!")

        st.write("### Request Details")
        st.write(f"**Patient:** {name}")
        st.write(f"**Pickup:** {location}")
        st.write(f"**Emergency:** {emergency}")
        st.write(f"**Hospital:** {hospital}")

        st.info(
            "Searching for nearby registered transport providers..."
        )

    else:
        st.warning("Please fill in all the required fields.")
