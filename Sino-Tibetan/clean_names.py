import json
import re

def clean_name(name):
    # Remove anything in brackets (and the preceding space)
    return re.sub(r'\s*\[[^\]]+\]', '', name)

def traverse(node):
    if isinstance(node, dict):
        if 'name' in node and isinstance(node['name'], str):
            node['name'] = clean_name(node['name'])
        if 'children' in node and isinstance(node['children'], list):
            for child in node['children']:
                traverse(child)

input_path = 'Sino-Tibetan/sino1245_tree_final.json'        # Path to your input file
output_path = 'Sino-Tibetan/sino1245_tree_final.json'        # Overwrites the original; change if you want a backup

with open(input_path, encoding='utf-8') as f:
    data = json.load(f)

traverse(data)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Cleaned file written to {output_path}')
