def top()
top = open('templates/top.html').read()

print(top)

def bottom()
bottom = open('templates/bottom.html').read()

print(bottom)

# page_title = page['title']
# print(page_title)

pages = [
{
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Deepinder Kaur",
},
{
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "About Me",
},
{
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Coming Soon",
},
{
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact Me",
}

for page in pages:
    print('Deepinder Kaur')
    print('About Me')
    print('Coming Soon')
    print('Contact Me')
