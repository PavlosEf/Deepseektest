import streamlit as st
import calculators.OffPricesCalculator as OffPricesCalculator
import calculators.SurebetCalculator as SurebetCalculator
import calculators.TopPriceBetfairCalculator as TopPriceBetfairCalculator
import calculators.MarginsRemoval as MarginsRemoval
import calculators.DifferentLines as AlternativeLinesConverter
import calculators.GeneralTab1 as GeneralTab1
import calculators.GeneralTab2 as GeneralTab2

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Theme and Styles
st.markdown("""
    <style>
        /* Global Styles */
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        /* Main Content Area */
        .main {
            background-color: #F5F5F5;
            padding: 20px;
            border-radius: 10px;
        }

        /* Sidebar Styles */
        section[data-testid="stSidebar"] {
            background-color: #4CAF50 !important;  /* Green */
            color: #FFFFFF !important;
            padding: 20px;
        }

        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
        }

        section[data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }

        /* Button Styles */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            border: none;
            transition: background-color 0.3s;
        }

        .stButton button:hover {
            background-color: #45a049;
        }

        /* Input Styles */
        .stNumberInput input, .stTextInput input {
            border-radius: 5px;
            border: 1px solid #4CAF50;
            padding: 10px;
        }

        /* Title and Header Styles */
        h1 {
            color: #4CAF50;
            text-align: center;
            margin-bottom: 20px;
        }

        h2 {
            color: #4CAF50;
            margin-bottom: 15px;
        }

        /* Success and Info Messages */
        .stSuccess {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }

        .stInfo {
            background-color: #d1ecf1;
            color: #0c5460;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("📊 Tools Menu")
    selected_tool = st.radio(
        "Select a Tool:",
        [
            "Off Prices Calculator",
            "Surebet Calculator",
            "Top Price / Betfair Calculator",
            "Margins Removal",
            "Alternative Lines Converter",
            "General Tab 1",
            "General Tab 2"
        ]
    )

# Main Content Area
st.title("Betting Tools Dashboard")
st.markdown("---")

# Display content based on selected tool
if selected_tool == "Off Prices Calculator":
    st.header("📉 Off Prices Calculator")
    OffPricesCalculator.run()

elif selected_tool == "Surebet Calculator":
    st.header("🎯 Surebet Calculator")
    SurebetCalculator.run()

elif selected_tool == "Top Price / Betfair Calculator":
    st.header("📈 Top Price / Betfair Calculator")
    TopPriceBetfairCalculator.run()

elif selected_tool == "Margins Removal":
    st.header("🧮 Margins Removal")
    MarginsRemoval.run()

elif selected_tool == "Alternative Lines Converter":
    st.header("🔄 Alternative Lines Converter")
    AlternativeLinesConverter.run()

elif selected_tool == "General Tab 1":
    st.header("📋 General Tab 1")
    GeneralTab1.run()

elif selected_tool == "General Tab 2":
    st.header("📋 General Tab 2")
    GeneralTab2.run()
