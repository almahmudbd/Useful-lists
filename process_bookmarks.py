import os
from html.parser import HTMLParser

class BookmarkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.bookmarks = []
        self.current_folder = []
        self.current_data = ""
        self.current_item = None

    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            self.current_data = ""
        elif tag == "a":
            attrs_dict = dict(attrs)
            self.current_item = {
                "url": attrs_dict.get("href", ""),
                "title": "",
                "folder": list(self.current_folder),
                "desc": ""
            }
            self.current_data = ""
        elif tag == "dd":
            self.current_data = ""

    def handle_endtag(self, tag):
        if tag == "h3":
            self.current_folder.append(self.current_data.strip())
        elif tag == "a":
            if self.current_item:
                self.current_item["title"] = self.current_data.strip()
                self.bookmarks.append(self.current_item)
                self.current_item = None
        elif tag == "dl":
            if self.current_folder:
                self.current_folder.pop()
        elif tag == "dd":
            if self.bookmarks:
                self.bookmarks[-1]["desc"] = self.current_data.strip()

    def handle_data(self, data):
        self.current_data += data

def slugify(name):
    return name.lower().replace(" & ", "-and-").replace(" ", "-")

def process_file(html_file):
    parser = BookmarkParser()
    with open(html_file, 'r', encoding='utf-8') as f:
        parser.feed(f.read())

    categories = {}
    
    for item in parser.bookmarks:
        if not item['folder']:
            continue
            
        top_level = item['folder'][0]
        
        # Skip 'imp:Bookmarks' as requested
        if top_level == "imp:Bookmarks":
            continue
            
        if top_level not in categories:
            categories[top_level] = []
        categories[top_level].append(item)

    for cat_name, items in categories.items():
        filename = f"{slugify(cat_name)}.md"
        print(f"Generating {filename}...")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {cat_name}\n\n")
            
            if cat_name == "Download Portal":
                f.write("> [!CAUTION]\n")
                f.write("**This bookmark list is created solely for archival purposes. We are not promoting any pirated content. We are not responsible if your PC gets affected, any accidents occur, or even if a world war breaks out as a result of downloading cracks, patches, or mods from here. Use everything at your own risk.**\n\n")
            
            last_sub_folders = None
            for item in items:
                # Sub folders (excluding top level)
                sub_folders = item['folder'][1:]
                if sub_folders != last_sub_folders:
                    if sub_folders:
                        f.write(f"## {' > '.join(sub_folders)}\n")
                    last_sub_folders = sub_folders
                
                line = f"1. [{item['title']}]({item['url']})"
                if item['desc']:
                    line += f" - {item['desc']}"
                f.write(line + "\n")

if __name__ == "__main__":
    html_input = "booky_backup_2026-03-01.html"
    if os.path.exists(html_input):
        process_file(html_input)
        print("Done!")
    else:
        print(f"Error: {html_input} not found.")
