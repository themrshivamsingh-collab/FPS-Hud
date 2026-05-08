import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """
    A random joke generator that uses external APIs to fetch jokes.
    """
    
    # API endpoints for different joke types
    JOKES_API_URL = "https://official-joke-api.appspot.com/random_joke"
    JOKES_V2_URL = "https://official-joke-api.appspot.com/jokes/random"
    
    @staticmethod
    def get_random_joke() -> Optional[Dict[str, str]]:
        """
        Fetch a random joke from the Official Joke API.
        
        Returns:
            Dict with 'setup' and 'punchline' keys, or None if request fails
        """
        try:
            response = requests.get(JokeGenerator.JOKES_API_URL, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            return {
                'setup': joke_data.get('setup', ''),
                'punchline': joke_data.get('punchline', ''),
                'type': joke_data.get('type', 'general')
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    @staticmethod
    def get_joke_by_type(joke_type: str = "general") -> Optional[Dict[str, str]]:
        """
        Fetch a random joke of a specific type.
        
        Args:
            joke_type: Type of joke ('general', 'knock-knock', 'programming', etc.)
        
        Returns:
            Dict with joke details, or None if request fails
        """
        try:
            url = f"https://official-joke-api.appspot.com/jokes/{joke_type}/random"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            joke_data = response.json()
            return {
                'setup': joke_data.get('setup', ''),
                'punchline': joke_data.get('punchline', ''),
                'type': joke_data.get('type', joke_type)
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {joke_type} joke: {e}")
            return None
    
    @staticmethod
    def print_joke(joke: Optional[Dict[str, str]]) -> None:
        """
        Pretty print a joke in a readable format.
        
        Args:
            joke: Dictionary containing joke data
        """
        if joke:
            print("\n" + "="*50)
            print(f"Type: {joke.get('type', 'Unknown').upper()}")
            print("="*50)
            print(f"Setup: {joke.get('setup', '')}")
            print(f"Punchline: {joke.get('punchline', '')}")
            print("="*50 + "\n")
        else:
            print("Failed to fetch a joke. Please try again later.")


def main():
    """Main function to demonstrate the joke generator."""
    
    print("🎭 Welcome to the Random Joke Generator! 🎭\n")
    
    # Get a random joke
    print("Getting a random joke...")
    joke = JokeGenerator.get_random_joke()
    JokeGenerator.print_joke(joke)
    
    # Get jokes by specific types
    joke_types = ["general", "knock-knock", "programming"]
    
    for joke_type in joke_types:
        print(f"Getting a {joke_type} joke...")
        joke = JokeGenerator.get_joke_by_type(joke_type)
        JokeGenerator.print_joke(joke)


if __name__ == "__main__":
    main()
