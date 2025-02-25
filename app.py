import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI
genai.configure(api_key=api_key)

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "Invalid conversion"

# ✅ Fixed AI function using a simple Gemini model
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use a free model
    response = model.generate_content(prompt)
    return response.text if response else "Error fetching response"

# Streamlit UI
st.set_page_config(page_title="Smart Unit Converter & AI Assistant", page_icon="🔄", layout="wide")

# Sidebar
st.sidebar.title("🔧 Options")
mode = st.sidebar.radio("Choose Mode", ["Unit Converter", "Ask AI"])

st.sidebar.markdown("🌟 **Made with Streamlit**")

st.title("🌍 Smart Unit Converter & AI Assistant")
st.write("Convert units easily or ask AI any question!")

# Unit Converter UI
if mode == "Unit Converter":
    st.subheader("🔄 Unit Converter")
    
    value = st.number_input("Enter value:", min_value=0.0, step=0.1, format="%.2f")
    from_unit = st.text_input("From unit (e.g., meters):")
    to_unit = st.text_input("To unit (e.g., feet):")

    if st.button("Convert"):
        if from_unit and to_unit:
            result = convert_units(value, from_unit, to_unit)
            st.success(f"✅ {result}")
        else:
            st.warning("⚠️ Please enter valid units.")

# AI Assistant UI
else:
    st.subheader("💬 Ask AI (Powered by Gemini)")
    
    user_query = st.text_area("Enter your question:")
    
    if st.button("Ask AI"):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.info(f"🤖 AI Response: {ai_response}")
        else:
            st.warning("⚠️ Please enter a question.")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed by **Mehmil Zeeshan** | 🚀 Powered by **Google Gemini AI & Streamlit**")


