from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('./templates'))

template = env.get_template('index.html')

html = template.render()