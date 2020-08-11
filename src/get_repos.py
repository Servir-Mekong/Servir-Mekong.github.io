import requests

md_file = "../docs/index.md"

url = "https://api.github.com/orgs/servir-mekong/repos"

r = requests.get(url)

repos = r.json()

doc_str = "## Repos\n\n"

for repo in repos:
    if not repo["private"]:
        doc_str += f"* [{repo['name']}]({repo['html_url']})\n"

with open(md_file,'w') as f:
    f.write(doc_str)