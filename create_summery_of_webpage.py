import requests
from bs4 import BeautifulSoup
import openai
import os

# OpenAI GPT-3 API key
api_key = os.environ['OPENAI_API_KEY'] 
client = openai.Člient(api_key=api_key)

# URL of the blog you want to scrape
blog_url = "https://en.wikipedia.org/wiki/Blog"

# Function to scrape the blog content def scrape_blog_content(url):
def scrape_blog_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.content, 'html.parser') 
            blog_content=""
            paragraph_counter = 0
            for paragraph in soup.find_all('p'):
                blog_content += paragraph.get_text() + "\n" 
                paragraph_counter += 1
                if paragraph_counter >= 10:
                    break
            return blog_content.strip()
        
    except Exception as e:
        print("Error: {e}")
        return None

# Function to summarize using OpenAI GPT API
def summarize_with_gpt(content):
    reponse = client.Completion.create(
        model = "gpt-3.5-turbo",
        prompt = f"Plese summarize the following blog post:\n{content}\n",
        temperature = 0.5
    )
    return response.choices[0].message.content


# Main function
def main():
    blog_url = "https://en.wikipedia.org/wiki/Blog"
    blog_content = scrape_blog_content(blog_url)

    if content:
        summary = summarize_with_gpt(content)
        print(summary)
    
if __name__ == "__main__":
    main()