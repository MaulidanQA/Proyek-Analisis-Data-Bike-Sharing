# Import Library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

st.write("""
<style>
.big-title {
    font-size: 3em;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.write('<h1 class="big-title">Dashboard Data Analysis Bike Sharing</h1>', unsafe_allow_html=True)

st.write('<hr class="hr">', unsafe_allow_html=True)

st.sidebar.title("Bike Sharing")
st.sidebar.image('dashboard/sidebarlogo.png')
selected_dataset = st.sidebar.selectbox("Show Dataset", ["Hide Dataset", "Day Dataset", "Hour Dataset", "Summary Statistics"])
if selected_dataset == "Day Dataset":
    st.subheader("Raw Data (Day Dataset)")
    st.write(day_df)
elif selected_dataset == "Hour Dataset":
    st.subheader("Raw Data (Hour Dataset)")
    st.write(hour_df)
elif selected_dataset == "Summary Statistics":
    st.subheader("Summary Statistics")
    st.write(hour_df.describe())



st.sidebar.markdown("## Visualization")
selected_weather = st.sidebar.multiselect(
    "Select Weather Conditions",
    ["Clear", "Mist + Cloudy", "Light Snow"],
)
filtered_data = day_df[day_df["weathersit"].isin(selected_weather)]

if len(selected_weather) > 0:
    st.subheader(f"Visualization of Data Based on Clear Weather")
    weather_1_data = day_df[day_df['weathersit'] == 1]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(data=weather_1_data, x="mnth", y="cnt", ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Bike Rentals')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    st.pyplot(fig)

if len(selected_weather) > 1:
    st.subheader(f"Visualization of Data Based on Mist + Cloudy Weather")
    weather_2_data = day_df[day_df['weathersit'] == 2]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(data=weather_2_data, x="mnth", y="cnt", ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Bike Rentals')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    st.pyplot(fig)

if len(selected_weather) > 2:
    st.subheader(f"Visualization of Data Based on Light Snow Weather")
    weather_3_data = day_df[day_df['weathersit'] == 3]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(data=weather_3_data, x="mnth", y="cnt", ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Bike Rentals')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    st.pyplot(fig)

on = st.sidebar.toggle('Comparison Based On Weather')

if on:
    st.markdown("### Comparison Total Bike Rentals by Weather Condition")
    cnt_rename = day_df.rename(columns={'cnt': 'Total Bike Rentals'})
    weather_totals = cnt_rename.groupby("weathersit")["Total Bike Rentals"].sum().reset_index()
    weather_totals = weather_totals.rename(columns={'weathersit': 'Weather Condition'})
    st.bar_chart(weather_totals, x="Weather Condition", y="Total Bike Rentals")

    st.markdown("### Weather Sit Labels:")
    st.markdown("- **Weather Sit 1**: Clear")
    st.markdown("- **Weather Sit 2**: Mist + Cloudy")
    st.markdown("- **Weather Sit 3**: Light Snow")

def convert_daydf(day_df):
    return day_df.to_csv().encode('utf-8')

def convert_hourdf(hour_df):
    return hour_df.to_csv().encode('utf-8')

st.sidebar.markdown("### Download Data")
csv_data = convert_daydf(day_df)
st.sidebar.download_button(
    label="Download Day data as CSV",
    data=csv_data,
    file_name='day_df.csv',
    mime='text/csv',
    help="Click to download the DataFrame as a CSV file."
)

csv_data = convert_hourdf(hour_df)
st.sidebar.download_button(
    label="Download Hour data as CSV",
    data=csv_data,
    file_name='hour_df.csv',
    mime='text/csv',
    help="Click to download the DataFrame as a CSV file."
)

st.sidebar.caption("<div style='text-align: center; margin-top: 50px;'>Aldi Putra Miftaqull Ullum\nDICODING</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center;'><a href='https://github.com/AldiPutra24' target='_blank'>GitHub 🦝</a></div>", unsafe_allow_html=True)
