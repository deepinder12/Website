def top():
    top = open('templates/top.html').read()
    print(top)

def bottom():
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
]

for page in pages:
    print(page)
    index_content = open(page["filename"]).read()
    page_title = page['title']
    print(page_title)

# Read in the entire template
template = open("base.html").read()

# Read in the content of the index HTML page
index_content = open("content/index.html").read()
about_content = open("content/index.html").read()

# Use the string replace
finished_index_page = template.replace("{{content}}", index_content)
open("docs/index.html", "w+").write(finished_index_page)