import requests
import streamlit
streamlit.title("My Mom\'s New Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega3 and blueberry oatmeal")
streamlit.text("Kale, Spinach and Rocket Smoothie")
streamlit.text("Hard Boiled Free-Range Egg")


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!!!')

fruityvice_responce = requests.get("https://fruityvice.com/api/fruit/watermelon" + "Kiwifruit")
fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
streamlit.dataframe(fruityvice_normalized)

