# **News Headlines and Sources Retrieval System**

## Project Description
The project is a client-server system that returns news headlines and sources using the News API. The system enables users to interact with the server by searching for headlines by keyword, category, or country, as well as listing all headlines. Users can also search for news sources by category, country, or language, or list all the sources.

---

## Semester 
2023-2024 2nd semester

---

## Group
Group No. : B13

Course code: ITNE352/ITCE320

Section No. : 02

Students Names: HAMZA NASER JASIM ALFAYEZ , YOUSSEF MOHAMED HELMY ABDELSALAM

Students IDs: 202204610 , 202105811 

---

## Table of Contents

1- [Requirements](#requirements)

2- [How to Run](#how-to-run)

3- [The Scripts](#the-scripts)

4- [Additional Concepts](#additional-concepts)

5- [Acknowledgments](#acknowledgments)

6- [Conclusion](#conclusion)

---

## Requirements

**To set up and run the project in a local environment, follow these steps:**

1- Install Python 3.x (the newest version is 3.12) from the official Python website: https://www.python.org/downloads/

2- Install the required Python packages by running the following command:

```
pip install requests 
```

3- Get an API key from news API website: https://NewsAPI.org and replace the "API_KEY" constant in the server.py file with your API key.

---

## How to Run

1- Start the server by running the server.py script:

```
python server.py
```

2- Once the server is running, start the client by running the client.py script:

```
python client.py
```

3- The client will ask you to enter your name and then display a menu with options to search for headlines, list sources, or quit the application.

4- Follow the instructions to interact with the server and retrieve the desired news data.

---

## The Scripts

### Client Script (client.py)

The client script (client.py) establishes a connection to the server and provides a user interface for interacting with the news retrieval system. It communicates over the network using the socket module and serializes and deserializes data using the json module.

**Client script main functions:**

- connect_to_server(): Establishes a connection with the server and handles menu options for the user.
```
connect_to_server()
```
- handle_headlines_menu(client_socket): Shows a menu for searching and retrieving news headlines based on various criteria.
```
handle_headlines_menu(client_socket)
```
- handle_sources_menu(client_socket): Shows a menu for searching and retrieving news sources based on categories, countries, and languages.
```
handle_sources_menu(client_socket)
```
- display_results(client_socket, menu_type): Receives and displays the search results from the server.
```
display_results(client_socket, menu_type)
```

### Server Script (server.py)

The server script (server.py) handles client connections, processes requests, and retrieves data from the news API. It uses the socket module for network communication, the calls module for performing HTTP requests to the news API, and the threading module to handle many client connections at the same time.

**Server script main functions:**

- handle_client(client_socket, client_address): Handles incoming client connections and processes their requests.
```
handle_client(client_socket, client_address)
```
- get_api_data(endpoint, params=None): Sends a GET request to the news API and returns the response's data.
```
get_api_data(endpoint, params=None)
```
- save_to_file(group_id, client_name, option, data): Saves the retrieved data to a file for logging.
```
save_to_file(group_id, client_name, option, data)
```

---

## Additional Concepts

The project includes the following additional concepts:

1- **Multithreading**: To manage many client connections at the same time, the server script makes use of the threading module. Since each client connection is managed by an individual thread, the server can handle requests from many clients at one time.

2- **File I/O**: A function called "save_to_file( )" in the server script stores the obtained data to a file for logging reasons. This function illustrates how to handle files in Python.

3- **Error Handling**: To properly manage and log any issues that might happen during program execution, the server script contains exception handling functions.

---

## Acknowledgments

This project was established as an educational project that gets news information from the NewsAPI https://newsapi.org. We would like to thank the NewsAPI team for making this useful resource available.

---

## Conclusion

In conclusion, a practical example of a client-server Python application is the News Headline Retrieval System. It shows how to use a variety of Python modules and ideas, including file I/O, multithreading, HTTP requests, network programming, and handling errors. You can build up and run the project locally to know the news of countries like the USA, Australia, and Egypt in English and Arabic and interact with the news system by following the instructions in this README file.