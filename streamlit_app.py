import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🍋 Build Your Own Fruit Smoothie 🥝🍇' )

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)
#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
                
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment what does the next line do?
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

# write your own comment what does this do?

streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
2024-02-28 05:08:26.844 Uncaught app exception

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 535, in _run_script

    exec(code, module.__dict__)

  File "/mount/src/first_streamlit_app/streamlit_app.py", line 40, in <module>

    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/__init__.py", line 54, in Connect

    return SnowflakeConnection(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 429, in __init__

    self.connect(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 683, in connect

    self.__config(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 1180, in __config

    Error.errorhandler_wrapper(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 290, in errorhandler_wrapper

    handed_over = Error.hand_to_other_handler(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 348, in hand_to_other_handler

    connection.errorhandler(connection, cursor, error_class, error_value)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 221, in default_errorhandler

    raise error_class(

snowflake.connector.errors.ProgrammingError: 251006: Password is empty

2024-02-28 05:08:26.989 503 GET /script-health-check (10.13.59.71) 973.01ms

2024-02-28 05:08:31.704 Uncaught app exception

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 535, in _run_script

    exec(code, module.__dict__)

  File "/mount/src/first_streamlit_app/streamlit_app.py", line 40, in <module>

    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/__init__.py", line 54, in Connect

    return SnowflakeConnection(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 429, in __init__

    self.connect(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 683, in connect

    self.__config(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 1180, in __config

    Error.errorhandler_wrapper(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 290, in errorhandler_wrapper

    handed_over = Error.hand_to_other_handler(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 348, in hand_to_other_handler

    connection.errorhandler(connection, cursor, error_class, error_value)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 221, in default_errorhandler

    raise error_class(

snowflake.connector.errors.ProgrammingError: 251006: Password is empty

2024-02-28 05:08:31.836 503 GET /script-health-check (10.13.59.71) 904.35ms

2024-02-28 05:08:36.684 Uncaught app exception

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 535, in _run_script

    exec(code, module.__dict__)

  File "/mount/src/first_streamlit_app/streamlit_app.py", line 40, in <module>

    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/__init__.py", line 54, in Connect

    return SnowflakeConnection(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 429, in __init__

    self.connect(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 683, in connect

    self.__config(**kwargs)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/connection.py", line 1180, in __config

    Error.errorhandler_wrapper(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 290, in errorhandler_wrapper

    handed_over = Error.hand_to_other_handler(

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 348, in hand_to_other_handler

    connection.errorhandler(connection, cursor, error_class, error_value)

  File "/home/adminuser/venv/lib/python3.9/site-packages/snowflake/connector/errors.py", line 221, in default_errorhandler

    raise error_class(

snowflake.connector.errors.ProgrammingError: 251006: Password is empty

2024-02-28 05:08:36.835 503 GET /script-health-check (10.13.59.71) 906.38ms
