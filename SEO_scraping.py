import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Set The Url of the site that we need to scrap
url = "https://p-f1c19bd9-9411-4552-b872-607c2ee68f46.presencepreview.site/"

#========================================================================================================
# Funton to count how many pages retur a status code of 404 (how many pages are not found).

def cout_404_pages(response, count_404):

  if response.status_code == 404:
    count_404 += 1

  else:
    pass

  return count_404

#========================================================================================================
# Function to append the data to a list but only adding one not found page since this info would be redundant if is showed more than once.

def append_data(count_404, data, response, path, seo_title, title_len):

  if response.status_code == 404:
    if count_404 <= 1:
      data.append([path, seo_title, title_len])

    else:
      pass

  else:
    data.append([path, seo_title, title_len])

  return data

#========================================================================================================
# Main Function

# Here are the sub-pages of the site that need to be scraped
paths = ("" , "about", "team", "properties","properties/sale", "properties/sold", "home-valuation", "buyers", "sellers", "testimonials", "neighborhoods", "developments", "blog" ,"vlog", "contact", "about-sir", "auction")

# Initialicing variables.
# data is a list where will be stored the scraped data.
# count_404 is a number that represent how many pages returned a 404 code.
data = []
count_404 = 0

for path in paths:
  page = url+path

  response = requests.get(page)
  soup = BeautifulSoup(response.text, 'html.parser')

  count_404 = cout_404_pages(response, count_404)

  seo_title = soup.find('title').text

  title_len = len(seo_title)

  data = append_data(count_404, data, response, path, seo_title, title_len)

#========================================================================================================
# Print the results

print(count_404)
print(tabulate(data))