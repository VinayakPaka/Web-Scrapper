import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

def get_product_details_snapdeal(url, user_agent):
    status_code = 503

    while status_code == 503:
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            title_element = soup.find("h1", {"class": "pdp-e-i-head"})
            title = title_element.get_text().strip() if title_element else "Title not found"

            price_element = soup.find("span", {"class": "pdp-final-price"})
            price = price_element.get_text().strip() if price_element else "Price not found"

            image_element = soup.find("img", {"class": "cloudzoom"})
            image = image_element["src"] if image_element else "Image not found"

            description_element = soup.find("div", {"class": "col-xs-18"})
            description = description_element.get_text().strip() if description_element else "Description not found"
            status_code = 200

            return {
                "title": title,
                "price": price,
                "image": image,
                "description": description
            }
        else:
            print("Failed to retrieve Snapdeal product details. Retrying...")

def get_product_details_amazon(url, user_agent):
    status_code = 503

    while status_code == 503:
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            title_element = soup.find("span", {"id": "productTitle"})
            title = title_element.get_text().strip() if title_element else "Title not found"

            price_element = soup.find("span", {"class": "a-price-whole"})
            price = price_element.get_text().strip() if price_element else "Price not found"

            image_element = soup.find("img", {"id": "landingImage"})
            image = image_element["src"] if image_element else "Image not found"

            description_element = soup.find("div", {"id": "productDescription"})
            description = description_element.get_text().strip() if description_element else "Description not found"
            status_code = 200

            return {
                "title": title,
                "price": price,
                "image": image,
                "description": description
            }
        else:
            print("Failed to retrieve Amazon product details. Retrying...")

def get_product_details_flipkart(url, user_agent):
    status_code = 503

    while status_code == 503:
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            title_element = soup.find("span", {"class": "_35KyD6"})
            title = title_element.get_text().strip() if title_element else "Title not found"

            price_element = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
            price = price_element.get_text().strip() if price_element else "Price not found"

            image_element = soup.find("img", {"class": "_396cs4 _3exPp9"})
            image = image_element["src"] if image_element else "Image not found"

            description_element = soup.find("div", {"class": "_2FbOxw"})
            description = description_element.get_text().strip() if description_element else "Description not found"
            status_code = 200

            return {
                "title": title,
                "price": price,
                "image": image,
                "description": description
            }
        else:
            print("Failed to retrieve Flipkart product details. Retrying...")

def compare_prices(url_snapdeal, url_amazon, url_flipkart):
    snapdeal_details = get_product_details_snapdeal(url_snapdeal, user_agent)
    amazon_details = get_product_details_amazon(url_amazon, user_agent)
    flipkart_details = get_product_details_flipkart(url_flipkart, user_agent)

    prices = {
        "Snapdeal": snapdeal_details["price"],
        "Amazon": amazon_details["price"],
        "Flipkart": flipkart_details["price"]
    }

    try:
        prices = {seller: float(price.replace("Rs.", "").replace(",", "")) for seller, price in prices.items()}
    except ValueError:
        prices = {seller: float("inf") for seller in prices}

    cheapest_seller = min(prices, key=prices.get)

    return {
        cheapest_seller: prices[cheapest_seller],
        "Product Details": {
            "Title": snapdeal_details["title"],
            "Image": snapdeal_details["image"],
            "Description": snapdeal_details["description"]
        }
    }

if __name__ == "__main__":
    snapdeal_url = input("Enter Snapdeal Product Link: ")
    amazon_url = input("Enter Amazon Product Link: ")
    flipkart_url = input("Enter Flipkart Product Link: ")

    cheapest_product = compare_prices(snapdeal_url, amazon_url, flipkart_url)

    if cheapest_product:
        print(f"The cheapest seller is {list(cheapest_product.keys())[0]} with a price of {cheapest_product[list(cheapest_product.keys())[0]]}")
        print("Product Details:")
        print("Title:", cheapest_product["Product Details"]["Title"])
        print("Image:", cheapest_product["Product Details"]["Image"])
        print("Description:", cheapest_product["Product Details"]["Description"])
    else:
        print("Failed to retrieve product details or URLs are incorrect.")
