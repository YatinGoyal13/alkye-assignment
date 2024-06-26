# Alkye Assignment 

This repository contains Python scripts for performing various tasks related to the Alkye assignment.

## Tasks

1. **task1.py**: Data Manipulation and Analysis

Problem Statement: You are given a CSV file data.csv containing data about customers, including their names, ages, and email addresses. Write a Python script to read the data from the CSV file, calculate the average age of the customers, and find the most common domain name in the email addresses.

Input: CSV file data.csv with columns: firstname, lastname, email, age.

Output: The average age of the customers and the most common domain name in the email addresses.

Example Output:
Average Age: 35.5
Most Common Domain: gmail.com

Test Cases:
Verify that the script reads the CSV file correctly.
Verify that the script calculates the correct average age.
Verify that the script identifies the most common domain name accurately.

2. **task2.py**: Algorithm Implementation and Optimization

Problem Statement: You are given a list of integers representing stock prices on consecutive days. Write a Python function max_profit(prices) that calculates the maximum profit that can be achieved by buying and selling the stock once. Additionally, optimize the function to minimize time complexity.

Input: A list of integers prices [7, 1, 5, 3, 6, 4, 9, 2, 8] where prices[i] represents the price of the stock on the ith day.

Output: The maximum profit that can be achieved by buying and selling the stock once.

Example Output: 
5 (Buy on day x (price = 1) and sell on day y (price = 6))

Test Cases:
Verify that the function returns the correct maximum profit for a list of stock prices with an increasing trend.
Verify that the function returns the correct maximum profit for a list of stock prices with a decreasing trend.
Verify that the function returns 0 if it's not possible to make a profit (i.e., all stock prices are decreasing).

3. **task3.py**: File Handling and Text Processing

Problem Statement: You are given a text file words.txt containing a list of words, one word per line. Write a Python script to read the file, find all the anagrams present in the list, and group them together. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. Write the grouped anagrams to an output file anagrams.txt.

Input: A text file words.txt containing a list of words, one word per line.

Output: An output file anagrams.txt containing grouped anagrams, one group per line.

Example Input and Output

Input (words.txt):
listen
silent
enlist
paint
inapt
piano

Output (anagrams.txt):
listen silent enlist
paint inapt
piano

4. **task4.py**:  Web Scraping and Data Analysis

Problem Statement: Write a Python script to scrape data from a website (e.g., IMDb) to retrieve information about 20 top-rated movies. Extract the movie title, year of release and IMDb rating for each movie, and store this information in a CSV file. Perform data analysis to find the average rating of the top-rated movies.

Input: https://www.imdb.com/chart/top/

Output: A CSV file top_movies.csv containing information about the top-rated movies.

Title,Year,Rating
The Shawshank Redemption,1994,9.3
The Godfather,1972,9.2
The Dark Knight,2008,9.0

5. **task5.py**: Design and Implement a RESTful API
Problem Statement: Design and implement a RESTful API using Python and a web framework such as Flask or Django. The API should provide CRUD (Create, Read, Update, Delete) operations for a resource (e.g., users, products). Implement errors handling gracefully with appropriate status codes and error messages.

Requirements:

Design an API with well-defined endpoints, request/response formats, and HTTP methods.
Implement CRUD operations for managing resources.
Implement error handling with appropriate status codes and error messages.
Write unit tests to ensure the functionality and reliability of the API.

## How to Run

To execute any of the tasks, follow the instructions below:

1. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

2. Clone this repository to your local machine using the following command:
   git clone https://github.com/yourusername/alkye-assignment.git


3. To run a specific task, execute the corresponding Python script. For example, to run task 1:
   python task1.py 


   

