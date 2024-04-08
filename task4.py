import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_imdb_top_movies(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        # Requesting the webpage
        page = requests.get(url, headers=headers)
        page.raise_for_status()  # Raise HTTPError for bad status codes
        
        movie_soup = BeautifulSoup(page.content, "html.parser")
        
        # Lists to store movie information
        movie_name = []
        movie_years = []
        imdb_ratings = []
        
        # Scraping movie names
        movie_div = movie_soup.find_all('h3', class_='ipc-title__text')
        for h3 in movie_div:
            if h3.text != "IMDb Charts":
                movie_name.append(h3.text.split('. ')[-1])
            if len(movie_name) == 20:
                break
        
        # Scraping movie years
        span_elements = movie_soup.find_all('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item')
        for span in span_elements:
            if span.text.isdigit():
                movie_years.append(span.text)
            if len(movie_years) == 20:
                break
        
        # Scraping IMDb ratings
        span_ele = movie_soup.find_all('span', {'data-testid': 'ratingGroup--imdb-rating'})
        for span in span_ele:
            imdb_rating = span.text.strip().split()[:-1]
            imdb_ratings.append(imdb_rating)
            if len(imdb_ratings) == 20:
                break
        
        # Converting list of lists to a 1D list for IMDb ratings
        imdb_ratings_1d = pd.DataFrame(imdb_ratings).iloc[:, 0].tolist()
        
        return movie_name, movie_years, imdb_ratings_1d
    
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None, None, None

def write_to_csv(movie_name, movie_years, imdb_ratings, filename):
    try:
        # Creating a DataFrame to store movie information
        movie_df = pd.DataFrame({
            'Title': movie_name,
            'Year': movie_years,
            'Rating': imdb_ratings
        })
        
        # Writing movie information to a CSV file
        movie_df.to_csv(filename, index=False)
    
    except Exception as e:
        print("Error writing to CSV:", e)

def calculate_average_rating(imdb_ratings):
    try:
        # Data analysis: Finding the average rating of the top-rated movies
        average_rating = pd.Series(imdb_ratings).astype(float).mean()
        return average_rating
    
    except Exception as e:
        print("Error calculating average rating:", e)
        return None

# Main function to orchestrate the process
def main():
    imdb_url = "https://www.imdb.com/chart/top/"
    movie_name, movie_years, imdb_ratings = scrape_imdb_top_movies(imdb_url)
    
    if movie_name and movie_years and imdb_ratings:
        write_to_csv(movie_name, movie_years, imdb_ratings, 'top_movies.csv')
        average_rating = calculate_average_rating(imdb_ratings)
        if average_rating is not None:
            print("Average IMDb Rating of Top 20 Movies:", round(average_rating, 2))
    
if __name__ == "__main__":
    main()
