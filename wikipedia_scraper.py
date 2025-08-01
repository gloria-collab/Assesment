import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_html_content(url):
    """Fetch and parse the HTML content from a Wikipedia page."""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_title(soup):
    """Extract the article title from the page."""
    return soup.find('h1', {'id': 'firstHeading'}).text.strip()

def extract_article_text(soup):
    """
    Extract article text and map each section heading to its respective paragraph(s).
    Returns a dictionary with headings as keys and paragraphs as values.
    """
    content = soup.find('div', {'class': 'mw-parser-output'})
    article = {}
    current_heading = "Introduction"
    article[current_heading] = []

    for tag in content.find_all(['h2', 'p']):
        if tag.name == 'h2':
            heading = tag.text.replace('[edit]', '').strip()
            current_heading = heading
            article[current_heading] = []
        elif tag.name == 'p' and tag.text.strip():
            article[current_heading].append(tag.text.strip())

    # Join paragraphs under each heading
    return {heading: ' '.join(paragraphs) for heading, paragraphs in article.items()}

def extract_internal_links(soup, base_url='https://en.wikipedia.org'):
    """Extract all internal Wikipedia links from the article."""
    internal_links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ':' not in href:
            full_url = urljoin(base_url, href)
            internal_links.add(full_url)
    return list(internal_links)

def scrape_wikipedia_page(url):
    """Main wrapper function to perform all tasks."""
    soup = get_html_content(url)
    title = extract_title(soup)
    article_text = extract_article_text(soup)
    internal_links = extract_internal_links(soup)

    return {
        'title': title,
        'article_text': article_text,
        'internal_links': internal_links
    }

# --- Test the Function on a Wikipedia Page ---
if __name__ == "__main__":
    test_url = "https://en.wikipedia.org/wiki/Web_scraping"
    data = scrape_wikipedia_page(test_url)

    print("Title:", data['title'])
    print("\nArticle Sections and Text:")
    for heading, text in data['article_text'].items():
        print(f"\n## {heading} ##\n{text[:500]}...")  # Show only first 500 characters

    print(f"\nFound {len(data['internal_links'])} internal links.")
    print("Sample internal links:")
    for link in data['internal_links'][:5]:
        print(link)
