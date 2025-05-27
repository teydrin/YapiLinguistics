import json
import re

def clean_name(name):
    # Removes anything in brackets (and the preceding space)
    return re.sub(r'\s*\[[^\]]+\]', '', name)

def traverse(node):
    if isinstance(node, dict):
        if 'name' in node and isinstance(node['name'], str):
            node['name'] = clean_name(node['name'])
        if 'children' in node and isinstance(node['children'], list):
            for child in node['children']:
                traverse(child)

input_file = 'Sino-Tibetan/sino1245_tree_final.json'
output_file = 'Sino-Tibetan/sino1245_tree_final.json'  # Overwrites original

with open(input_file, encoding='utf-8') as f:
    data = json.load(f)

traverse(data)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Cleaned file written to {output_file}')
