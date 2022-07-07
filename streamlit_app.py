import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Mom's new healthy Diner")

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3 & blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocekt Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pandas.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# set the index
my_fruits_list = my_fruits_list.set_index("Fruit")

# pick list
fruits_selected = streamlit.multiselect("Pick some fruits", list(
    my_fruits_list.index), ['Avocado', 'Strawberries'])

fruit_to_show = my_fruits_list.loc[fruits_selected]
# display the table
streamlit.dataframe(fruit_to_show)


streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input(
    'What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get(
    "https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do?
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input(
    "what fruit would you like to add? ", "jackfruit")
'''my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list")
my_data_rows = my_cur.fetchall()'''
streamlit.text("Thanks for adding" + add_my_fruit)
