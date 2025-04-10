import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Maternal Mortality Analysis Dashboard", layout="wide")
st.title("Maternal Mortality Analysis Dashboard")

# Sidebar for navigation
analysis_options = [
    "Mortality Analysis Across Continents Over Years",
    "HDI Rank of Countries Over Years",
    "Mortality Analysis - Continents",
    "Mortality Analysis - Countries",
    "Maternal Mortality Ratio Vs Human Development Groups",
    "Maternal Mortality Ratio Across UNDP Developing Regions"
]

choice = st.sidebar.radio("Select Analysis Section", analysis_options)

# Based on the selection, display the corresponding content
if choice == analysis_options[0]:
    st.header("Mortality Analysis Across Continents Over Years")
    st.write("""
        This section shows the trends of maternal mortality across different continents over the years.
        *Key finding*: [Insert your key statistics and interpretations here.]
    """)
    # Display an image or an interactive plot
    st.image("images/maternal_mortality_ratio_trends.png", caption="Trends Across Continents")
    
elif choice == analysis_options[1]:
    st.header("HDI Rank of Countries Over Years")
    st.write("""
        Analysis of how the Human Development Index (HDI) ranking of various countries has changed over time.
        *Key finding*: [Insert your findings and numbers here.]
    """)
    st.image("images/HDI_Rank_of_Countries_Over_Years.png", caption="HDI Ranking Over Years")
    
elif choice == analysis_options[2]:
    st.header("Mortality Analysis - Continents")
    st.write("""
        Detailed statistics for maternal mortality rates per continent.
        *Key finding*: [Your insights can be added here.]
    """)
    st.image("images/average_maternal_mortality_ratio_continent.png", caption="Mortality by Continents")
    
elif choice == analysis_options[3]:
    st.header("Mortality Analysis - Countries")
    st.write("""
        Country-level analysis of maternal mortality with comparative statistics.
        *Key finding*: [Insert insights and numbers here.]
    """)
    st.image("images/average_maternal_mortality_ratio_country.png", caption="Mortality by Countries")
    
elif choice == analysis_options[4]:
    st.header("Maternal Mortality Ratio Vs Human Development Groups")
    st.write("""
        Comparison between maternal mortality ratios and various human development groups.
        *Key finding*: [Summarize your observations here.]
    """)
    st.image("images/Maternal_Mortality_Ratio_VS_Human_Development_Groups.png", caption="Mortality vs HDI Groups")
    
elif choice == analysis_options[5]:
    st.header("Maternal Mortality Ratio Across UNDP Developing Regions")
    st.write("""
        Analysis of maternal mortality ratios across different UNDP developing regions.
        *Key finding*: [Report the main conclusions here.]
    """)
    st.image("images/Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png", caption="Mortality across UNDP Regions")
