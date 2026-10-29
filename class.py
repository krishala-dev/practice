# title = "Django docs"
# rating = 5
# # print(f"{title} is rated {rating}/5")
# print((title) + " is rated " + str(rating) + "/5")
# print(title.upper(), len(title))
# print(title)


# title = input("Link title: ")
# url = input("Link URL: ")
# rating = int(input("Rating (1-5): "))
# print(f"{title} - {url} - rated {rating}/5")
# print("*" * rating)


# title = input("Link title: ")
# url = input("Link URL: ")
# rating = int(input("Rating (1-5): "))
# print(f"{title} - {url} - rated {rating}/5 " + "*" * rating)
# # print("*" * rating)


# 1. Get input from the user
original_url = input("Paste a URL:")

# 2. Clean the URL (convert to lowercase)
clean_url = original_url.strip().lower()
print(f"Clean: {clean_url}")

# 3. Check if it starts with https
starts_https = clean_url.startswith("https")
print(f"Starts with https: {starts_https}")

# 4. Extract the domain
# Splitting the clean URL by "/" gives us: ['https:', '', 'example.com', 'path']
domain = clean_url.split("/")[2]
print(f"Domain: {domain}")

# 5. Check if it ends with .com
ends_com = domain.endswith(".com")
print(f"Ends with .com: {ends_com}")