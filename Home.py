import streamlit as st
import time


# Set the page configuration
st.set_page_config(
    page_title="Explore the World",
    page_icon=":earth_americas:",
    layout="wide"
)

# Add a title and subtitle
st.title("Explore the World")


# Define a function to create the capital city page
def create_capital_city():
    # Add code to create the capital city page here
    st.title("Capital Cities")
    st.write("Here's a list of some of the world's capital cities:")
    st.write("- Washington D.C.")
    st.write("- Tokyo")
    st.write("- Paris")
    st.write("- Beijing")
    st.write("- London")

# Define a function to create the mega cities page
def create_mega_cities():
    # Add code to create the mega cities page here
    st.title("Mega Cities")
    st.write("Here's a list of some of the world's largest cities by population:")
    st.write("- Tokyo, Japan")
    st.write("- Delhi, India")
    st.write("- Shanghai, China")
    st.write("- Sao Paulo, Brazil")
    st.write("- Mumbai, India")

# Define a function to create the mountain page
def create_mountain():
    # Add code to create the mountain page here
    st.title("Mountains of the World")
    st.write("Here's a list of some of the highest mountains in the world:")
    st.write("- Mount Everest (Nepal/Tibet)")
    st.write("- K2 (Pakistan/China)")
    st.write("- Kangchenjunga (Nepal/India)")
    st.write("- Lhotse (Nepal/Tibet)")
    st.write("- Makalu (Nepal/Tibet)")




capital_cities_button = st.button("Capital Cities", key="capital_cities")
mega_cities_button = st.button("Mega Cities", key="mega_cities")
mountains_button = st.button("Mountains", key="mountains")

# Add buttons to link to different pages
if capital_cities_button:
    st.write("Loading Capital Cities page...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    create_capital_city()

if mega_cities_button:
    st.write("Loading Mega Cities page...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    create_mega_cities()

if mountains_button:
    st.write("Loading Mountains page...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    create_mountain()


# Add some additional information to the home page
st.header("Check out these fun facts about the world:")

col1_btn = st.button("Did You Know?")
col2_btn = st.button("Fun Fact!")
col3_btn = st.button("Trivia")

if col1_btn:
    st.subheader("Did You Know?")
    st.write("The Great Wall of China is not actually visible from space.")
    st.write("The Canary Islands are named after dogs, not birds.")
    st.write("There is a species of jellyfish that is immortal.")
    st.write("New York City is home to more billionaires than any other city in the world.")
    
if col2_btn:
    st.subheader("Fun Fact!")
    st.write("The world's largest iceberg ever recorded was roughly the size of Jamaica.")
    st.write("The smallest country in the world is Vatican City.")
    st.write("The longest river in the world is the Nile.")
    st.write("The world's largest desert is the Sahara in Africa.")
    
if col3_btn:
    st.subheader("Trivia")
    st.write("What is the highest mountain in Africa? (Mount Kilimanjaro)")
    st.write("What is the largest country by land area? (Russia)")
    st.write("What is the smallest country in the world? (Vatican City)")
    st.write("What is the largest ocean on Earth? (Pacific Ocean)")
    st.write("What is the tallest building in the world? (Burj Khalifa)")
    st.write("What is the longest river in the world? (Nile River)")
    
st.header("About Me ")
st.markdown(":wave: Hi there! I'm a data scientist who loves to explore new technologies and build cool stuff with data. I'm passionate about machine learning, natural language processing, and computer vision. :rocket:")
st.markdown("If you'd like to connect, you can find me on [LinkedIn](https://www.linkedin.com/in/snehay2606//)")

