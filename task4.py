import requests
from bs4 import BeautifulSoup
import csv

try:
    url =input("Enter URL : ")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    #Change the tags and Classes as per the website and use the HTML of website to see the tags
    name = soup.find_all("a",class_ = "title")
    price = soup.find_all("h4", class_ = "price float-end card-title pull-right")
    discription = soup.find_all("p", class_ = "description card-text")
    review = soup.find_all("p", class_ ="review-count float-end")

    if not name or not price or not discription or not review:
        print("Change the class or tags as per the website")
        print("Use HTML of Website to Inspect the Class and tag")
    else:
        with open('Details.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product_Name', 'Price', 'Description', 'Review']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # It wil write Header only Once.
            writer.writeheader()
            if True:
                for i in range(len(name)):  # Iterate through extracted data
                    writer.writerow({
                        'Product_Name': name[i].text.strip(), 
                        'Price': price[i].text.strip(), 
                        'Description': discription[i].text.strip(), 
                        'Review': review[i].text.strip()
                    })
                print("The data is successfully written to the file.")
except:
    print("Invalid Input...!")
    raise ValueError("The Input is Encorrect. Try Again...!")