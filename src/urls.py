# Class in Python that takes an URL as the index and adds or deletes it from an array
# it will keep track of the number of url's in the array
# on success it will return the URL on failure it will return the boolean FALSE
# there needs to be a get method for the number of urls's in the array and for the last url in the array


class URLs:
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        if url not in self.urls:
            self.urls.append(url)
            return url
        else:
            raise ValueError("URL already exists")

    def delete_url(self, url):
        if url in self.urls:
            self.urls.remove(url)
            return url
        else:
            raise ValueError("URL not found")

    def get_num_urls(self):
        return len(self.urls)

    def get_last_url(self):
        try:
            return self.urls[-1]
        except IndexError:
            raise ValueError("No URLs available")


# From GPT-4:
# The URLs class has an __init__ method that initializes an empty list to store URLs.
#  The add_url method takes an URL as input and adds it to the list if it is not already present.
#  It returns the URL on success and boolean False on failure.
#  The delete_url method takes an URL as input and removes it from the list if it is present.
#  It returns the URL on success and boolean False on failure.
#  The get_num_urls method returns the number of URLs in the list.
#  The get_last_url method returns the last URL in the list if it exists, otherwise it returns boolean False.

# You can use the urllib.parse module to parse the URL and extract the index. Here’s an example usage:

# from urllib.parse import urlparse

# url = 'https://www.example.com/index.html'
# url_parsed = urlparse(url)
# url_index = url_parsed.path.split('/')[-1]

# url_array = URLs()
# url_array.add_url(url_index)
# print(url_array.get_num_urls()) # Output: 1
# print(url_array.get_last_url()) # Output: index.html
