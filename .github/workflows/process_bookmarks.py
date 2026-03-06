import os
import re
import glob
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
    clean_name = name.lower().replace(" & ", "-and-").replace(" ", "-")
    # Remove characters that aren't alphanumeric or hyphens
    return re.sub(r'[^a-z0-9-]', '', clean_name)

# Configuration for exclusions
EXCLUDE_MAIN_FOLDERS = ["Download Portal", "imp:Bookmarks"]
EXCLUDE_SUB_FOLDERS_KEYWORDS = ["bdix", "personal links"]
EXCLUDE_LINK_KEYWORDS = ["red", "risk"]

def write_markdown_file(filename, title, items):
    print(f"Generating {filename}...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        
        last_sub_folders = None
        for item in items:
            # Sub folders (excluding top level for normal files)
            # For AI collection, the "top level" in the original file might be important.
            # We'll show the full path in subheaders if it's the AI file.
            sub_folders = item['folder'][1:] if title != "AI Collection" else item['folder']
            
            if sub_folders != last_sub_folders:
                if sub_folders:
                    f.write(f"## {' > '.join(sub_folders)}\n")
                last_sub_folders = sub_folders
            
            line = f"1. [{item['title']}]({item['url']})"
            if item['desc']:
                line += f" - {item['desc']}"
            f.write(line + "\n")

def process_file(html_file):
    parser = BookmarkParser()
    with open(html_file, 'r', encoding='utf-8') as f:
        parser.feed(f.read())

    categories = {}
    ai_items = []
    
    # Pre-compile regex for performance and word boundaries
    link_regex = re.compile(r'\b(' + '|'.join(EXCLUDE_LINK_KEYWORDS) + r')\b', re.IGNORECASE)
    ai_folder_regex = re.compile(r'\bai\b', re.IGNORECASE)

    for item in parser.bookmarks:
        if not item['folder']:
            continue
            
        top_level = item['folder'][0]
        
        # 1. Filter Main Folders
        if top_level in EXCLUDE_MAIN_FOLDERS:
            continue
            
        # 2. Filter Subcategories
        sub_folders = item['folder'][1:]
        is_excluded_sub = False
        for sf in sub_folders:
            sf_lower = sf.lower()
            # Sub-category filter (keyword match)
            if any(kw in sf_lower for kw in EXCLUDE_SUB_FOLDERS_KEYWORDS):
                is_excluded_sub = True
                break
        if is_excluded_sub:
            continue

        # 3. Filter Link Keywords (Whole words only)
        if link_regex.search(item['title']):
            continue

        # AI Detection: if any folder name contains the word "ai"
        if any(ai_folder_regex.search(f) for f in item['folder']):
            ai_items.append(item)

        # Normal Categorization
        if top_level not in categories:
            categories[top_level] = []
        categories[top_level].append(item)

    # Clean up old files for excluded categories if they exist
    for main_folder in EXCLUDE_MAIN_FOLDERS:
        old_file = f"{slugify(main_folder)}.md"
        if os.path.exists(old_file):
            print(f"Removing excluded category file: {old_file}")
            os.remove(old_file)

    # Generate normal category files
    for cat_name, items in categories.items():
        filename = f"{slugify(cat_name)}.md"
        write_markdown_file(filename, cat_name, items)
    
    # Generate AI Collection file separately
    if ai_items:
        write_markdown_file("ai-collection.md", "AI Collection", ai_items)

if __name__ == "__main__":
    # Find the latest booky_backup*.html file
    files = sorted(glob.glob("booky_backup*.html"), reverse=True)
    
    if files:
        html_input = files[0]
        print(f"Found input file: {html_input}")
        process_file(html_input)
        print("Done!")
    else:
        print("Error: No file matching 'booky_backup*.html' found.")
