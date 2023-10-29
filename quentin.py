import openai
import requests

# Set your API keys
openai.api_key = 'YOUR_OPENAI_API_KEY'
tmdb_api_key = 'YOUR_TMDB_API_KEY'

def generate_movie_recommendation():
    user_prompt = input("Ask me for a movie recommendation: ")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"I'm looking for a movie to watch. {user_prompt}",
        max_tokens=50,)
    recommendation = response.choices[0].text.strip()

    # Use TMDb API to get more details about the recommended movie
    tmdb_url = f'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': tmdb_api_key, 'query': recommendation, 'include_adult': 'false'}
    tmdb_response = requests.get(tmdb_url, params=params)
    movie_data = tmdb_response.json()

    if 'results' in movie_data and movie_data['results']:
        first_result = movie_data['results'][0]
        title = first_result.get('title', 'N/A')
        overview = first_result.get('overview', 'No overview available.')
        release_date = first_result.get('release_date', 'Release date not available')
        rating = first_result.get('vote_average', 'N/A')
        print(f"Recommended movie: {title}")
        print(f"Release Date: {release_date}")
        print(f"Rating: {rating}")
        print(f"Overview: {overview}")
    else:
        print("Sorry, I couldn't find a movie recommendation. Please try again.")

if __name__ == "__main__":
    generate_movie_recommendation()
