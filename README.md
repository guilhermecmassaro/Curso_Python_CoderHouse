
Author:
Guilherme Crivellenti Massaro

Creation Date:
14/10/2023

Update Date:
23/11/2023

Version:
Python 3.11.6

Notes:
Below are some tips for better understanding the code and its application.

--------------------------------------------------------------------------------------------------------

Documentation: API Connection and Data Manipulation

# Introduction

This code is an example of a Python script that connects to external APIs to collect data and then performs some data manipulation operations using the Pandas library. Additionally, it demonstrates how to store the data in an SQLite database. This documentation provides an overview of the code, its main functionalities, and how to implement it.

# Libraries Used:

1. Pandas: For table-format data manipulation.
2. Requests: For making HTTP requests and obtaining data from the API.
3. Plyer: For notifying the status of the API connection.

# Requirements:

Ensure that the libraries mentioned in the `requirements.txt` file are installed to run the script.

# Step-by-Step:

1. Install the Libraries:
Ensure the main libraries mentioned above and all from the 'requirements.txt' file are installed.

2. Define the API URLs:
Define the URLs of the external APIs you want to access. Replace the variables url_1, url_2, and url_3 with the actual URLs.

3. Execute the Script:
Run the Python script. It will connect to the APIs, notify about the connection status, and create DataFrames with the data.

4. Data Processing (Optional):
If desired, you can perform additional processing on the DataFrames, such as renaming columns, converting data types, filling in missing values, etc.

5. Data Storage in Database:
The code includes a function `salvar_base_de_dados` that allows saving the DataFrames in an SQLite database. Ensure to define the desired database name and the table where you want to store the DataFrame data.
