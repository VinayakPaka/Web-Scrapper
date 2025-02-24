# Web Scraper Price Comparison Tool

A Python tool that scrapes product details from major Indian e-commerce websites (Snapdeal, Amazon, and Flipkart) and compares prices to find the best deal.

## Features

- Extracts product details including title, price, image URL, and description
- Compares prices across three major e-commerce platforms
- Identifies the cheapest seller for a specific product
- Handles server errors with automatic retries
- User-friendly command-line interface

## Requirements

- Python 3.6+
- Required packages:
  - requests
  - beautifulsoup4

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/VinayakPaka/Web-Scrapper.git
   cd Web-Scrapper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. Enter the product URLs when prompted:
   - Snapdeal product URL
   - Amazon product URL
   - Flipkart product URL

3. The script will display:
   - The cheapest seller with the corresponding price
   - Product details (title, image URL, description)

## How It Works

The script uses web scraping techniques to extract product information:

1. Sends HTTP requests to the provided URLs with appropriate headers
2. Parses the HTML responses using BeautifulSoup
3. Extracts relevant product details using CSS selectors
4. Compares prices after normalizing the data
5. Returns the results to the user

## Limitations

- Web scraping is dependent on the website's HTML structure. If the websites change their layout or class names, the scraper may need to be updated.
- Some websites might block scraping attempts if too many requests are made in a short time.
- Price comparisons assume the products are identical across platforms.

## Future Improvements

- Add support for more e-commerce websites
- Implement price history tracking
- Create a graphical user interface
- Add product rating and review comparisons
- Implement proxy rotation to avoid blocking

## License

[MIT License](LICENSE)

## Disclaimer

This tool is for educational purposes only. Be sure to review the terms of service for any website before scraping it. The developer is not responsible for any misuse of this tool.
