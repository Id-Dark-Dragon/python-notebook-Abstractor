from bs4 import BeautifulSoup

with open("Python Notebook.html", encoding="UTF-8") as main_contents:
    content = main_contents.read()
with open("contents/1.raw-page.html", encoding="UTF-8") as raw:
    raw_code = raw.read()

soup = BeautifulSoup(content, 'html.parser')

sections = soup.find_all(name="section")

str_of_cont = ""
try:
    for section in sections:
        sec_id = section.get("id")
        with open(f"contents/{sec_id}.html", mode='w', encoding="UTF-8") as file:
            polished_code = raw_code.replace("*section*", f"{section}").replace("*title*", f"{section.h3.text}")
            file.write(polished_code)
        str_of_cont += f"<li><a target='_blank' href='contents/{sec_id}.html'>{section.h3.text}</a></li>"

finally:
    with open(f"pybook.html", mode='w', encoding="UTF-8") as content_table:
        content_table.write(raw_code.replace("*section*", str_of_cont))

