import streamlit as st

st.title ('Hello World, This is my first webpage Application')

st.markdown('---')
name=st.text_input('Enter the name : ')
st.number_input('Enter the age : ',min_value=5,max_value=105)

st.selectbox('Gender : ',options=['Male','Female','Others'])
st.radio('Marital Status : ',options= ['Single','Married','Seperated'])
st.multiselect('Meal',options =['Vada Pav','Misal Pav','Pav Bhaji','Pulav'],
               max_selections=2)
st.feedback(options='stars')
st.segmented_control('Coach',options =['3 Tier','2 Tier','FirstClass','General'])

st.date_input('From Date :')
st.time_input('Board Time :')

st.date_input('To Date : ')
st.time_input('End Journey Time : ')

st.button('Click Me')
st.success(f'My name is {name}')







import streamlit as st
from datetime import date, time, datetime
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Railway Booking System",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ---------- Main Background ---------- */

    .stApp {
        background: #f4f7fb;
    }

    /* ---------- Header ---------- */

    .header {
        background: linear-gradient(135deg, #17365d, #2868a6);
        padding: 30px 35px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    }

    .header h1 {
        margin: 0;
        font-size: 34px;
        font-weight: 700;
    }

    .header p {
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 16px;
        opacity: 0.9;
    }


    /* ---------- Section Card ---------- */

    .section-card {
        background: white;
        padding: 22px 25px;
        border-radius: 15px;
        margin-bottom: 10px;
        border: 1px solid #e4e8ef;
        box-shadow: 0 3px 12px rgba(0,0,0,0.06);
    }

    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #17365d;
        margin-bottom: 18px;
    }


    /* ---------- Booking Summary ---------- */

    .summary-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #dce3ed;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        margin-top: 25px;
    }

    .summary-title {
        font-size: 22px;
        font-weight: 700;
        color: #17365d;
        margin-bottom: 15px;
    }

    .summary-row {
        padding: 8px 0;
        border-bottom: 1px solid #edf0f4;
        font-size: 15px;
    }

    .summary-label {
        font-weight: 600;
        color: #555;
    }


    /* ---------- Buttons ---------- */

    div.stButton > button,
    div.stFormSubmitButton > button {
        width: 100%;
        min-height: 48px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
    }


    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        color: #777;
        font-size: 13px;
        margin-top: 35px;
        padding: 15px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">
    <h1>🚆 Railway Booking System</h1>
    <p>Plan your journey, select your preferences and confirm your booking.</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# STATION LIST
# ============================================================

stations = [
    "Mumbai Central",
    "Chhatrapati Shivaji Maharaj Terminus",
    "Pune Junction",
    "Nashik Road",
    "Nagpur Junction",
    "Ahmedabad Junction",
    "Surat",
    "Vadodara Junction",
    "Bhopal Junction",
    "Delhi Junction",
    "New Delhi",
    "Jaipur Junction",
    "Bengaluru City",
    "Chennai Central",
    "Hyderabad Deccan",
    "Kolkata Howrah"
]


# ============================================================
# BOOKING FORM
# ============================================================

with st.form("railway_booking_form"):

    # ========================================================
    # JOURNEY DETAILS
    # ========================================================

    st.markdown("""
    <div class="section-card">
        <div class="section-title">🚉 Journey Details</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        from_station = st.selectbox(
            "From Station",
            stations,
            index=0
        )

        from_date = st.date_input(
            "Journey Date",
            value=date.today()
        )

        boarding_time = st.time_input(
            "Boarding Time",
            value=time(8, 0)
        )

    with col2:

        to_station = st.selectbox(
            "To Station",
            stations,
            index=2
        )

        to_date = st.date_input(
            "Arrival Date",
            value=date.today()
        )

        departure_time = st.time_input(
            "Departure Time",
            value=time(8, 30)
        )


    st.markdown("---")


    # ========================================================
    # PASSENGER DETAILS
    # ========================================================

    st.markdown("""
    <div class="section-card">
        <div class="section-title">👤 Passenger Details</div>
    </div>
    """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:

        name = st.text_input(
            "Full Name",
            placeholder="Enter passenger name"
        )

        age = st.number_input(
            "Age",
            min_value=5,
            max_value=105,
            value=18,
            step=1
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Others"]
        )

    with col4:

        marital_status = st.radio(
            "Marital Status",
            ["Single", "Married", "Separated"],
            horizontal=True
        )

        meal = st.multiselect(
            "Meal Preference",
            [
                "Vada Pav",
                "Pav Bhaji",
                "Misal Pav",
                "Samosa Pav"
            ],
            max_selections=2
        )

        feedback = st.feedback(
            "stars"
        )


    st.markdown("---")


    # ========================================================
    # TRAVEL PREFERENCES
    # ========================================================

    st.markdown("""
    <div class="section-card">
        <div class="section-title">🎫 Travel Preferences</div>
    </div>
    """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:

        coach = st.segmented_control(
            "Coach Type",
            [
                "3 Tier",
                "2 Tier",
                "First Class",
                "General"
            ],
            default="3 Tier"
        )

    with col6:

        berth = st.selectbox(
            "Berth Preference",
            [
                "No Preference",
                "Lower",
                "Middle",
                "Upper",
                "Side Lower",
                "Side Upper"
            ]
        )


    st.markdown("---")


    # ========================================================
    # SUBMIT
    # ========================================================

    submitted = st.form_submit_button(
        "🚆 Confirm Booking"
    )


# ============================================================
# VALIDATION + BOOKING SUMMARY
# ============================================================

if submitted:

    errors = []

    # -----------------------------------------
    # Name validation
    # -----------------------------------------

    if not name.strip():
        errors.append("Please enter the passenger name.")


    # -----------------------------------------
    # Station validation
    # -----------------------------------------

    if from_station == to_station:
        errors.append(
            "From Station and To Station cannot be the same."
        )


    # -----------------------------------------
    # Date validation
    # -----------------------------------------

    if to_date < from_date:
        errors.append(
            "Arrival Date cannot be before Journey Date."
        )


    # -----------------------------------------
    # Time validation
    # -----------------------------------------

    if from_date == to_date:

        if departure_time <= boarding_time:
            errors.append(
                "Departure/arrival time must be after boarding time "
                "when travelling on the same day."
            )


    # ========================================================
    # DISPLAY ERRORS
    # ========================================================

    if errors:

        for error in errors:
            st.error(error)


    # ========================================================
    # SUCCESS
    # ========================================================

    else:

        booking_id = (
            "RB"
            + str(datetime.now().year)
            + str(random.randint(100000, 999999))
        )

        st.success(
            f"✅ Booking submitted successfully! "
            f"Booking ID: {booking_id}"
        )


        # ====================================================
        # BOOKING SUMMARY
        # ====================================================

        st.markdown("""
        <div class="summary-card">

            <div class="summary-title">
                📋 Booking Summary
            </div>

        </div>
        """, unsafe_allow_html=True)


        # ----------------------------------------------------
        # Journey Summary
        # ----------------------------------------------------

        st.subheader("🚉 Journey")

        journey_col1, journey_col2 = st.columns(2)

        with journey_col1:

            st.markdown(
                f"""
                **From**  
                {from_station}

                **Journey Date**  
                {from_date.strftime("%d %B %Y")}

                **Boarding Time**  
                {boarding_time.strftime("%I:%M %p")}
                """
            )

        with journey_col2:

            st.markdown(
                f"""
                **To**  
                {to_station}

                **Arrival Date**  
                {to_date.strftime("%d %B %Y")}

                **Departure Time**  
                {departure_time.strftime("%I:%M %p")}
                """
            )


        st.divider()


        # ----------------------------------------------------
        # Passenger Summary
        # ----------------------------------------------------

        st.subheader("👤 Passenger")

        passenger_col1, passenger_col2 = st.columns(2)

        with passenger_col1:

            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Gender:** {gender}")

        with passenger_col2:

            st.write(
                f"**Marital Status:** {marital_status}"
            )

            st.write(
                f"**Coach:** {coach}"
            )

            st.write(
                f"**Berth:** {berth}"
            )


        st.divider()


        # ----------------------------------------------------
        # Meal
        # ----------------------------------------------------

        st.subheader("🍱 Meal Preference")

        if meal:
            st.write(", ".join(meal))
        else:
            st.write("No meal selected")


        # ----------------------------------------------------
        # Booking ID
        # ----------------------------------------------------

        st.divider()

        st.info(
            f"🎫 **Booking Reference:** {booking_id}"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    Railway Booking System • Built with Streamlit 🚆
</div>
""", unsafe_allow_html=True)

