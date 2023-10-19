import requests
from bs4 import BeautifulSoup

def scrape_play_store_reviews(app_id, num_pages=5):
    base_url = f'https://play.google.com/store/apps/details?id=com.app.cumobileonline&showAllReviews=true'
    
    for page in range(1, num_pages + 1):
        url = f'{base_url}&hl=en&gl=US&reviewSortOrder=recent&page={page}'
        
        # Send a GET request
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            reviews = soup.find_all('div', class_='d15Mdf')

            for review in reviews:
                # Extract relevant information from the review
                user = review.find('span', class_='X43Kjb').text
                rating = review.find('div', class_='pf5lIe').find('div')['aria-label']
                comment = review.find('span', jsname='fbQN7e').text
                
                print(f'User: {user}')
                print(f'Rating: {rating}')
                print(f'Comment: {comment}')
                print('-' * 50)
        else:
            print(f'Failed to fetch page {page}')

if __name__ == "__main__":
    app_id = "com.app.cumobileonline"  # Replace with the package name of the app you want to scrape.
    num_pages = 5  # Number of pages of reviews to scrape

    scrape_play_store_reviews(app_id, num_pages)
