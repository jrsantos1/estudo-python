from jinja2 import Environment, FileSystemLoader

from weasyprint import HTML, CSS

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('index.html')

html = template.render(titulo='deu certo')

with open('outputs/index.html', 'w') as f:
    f.write(html)


# C CONVERT TO PDF

css = CSS(string =
          ''' 
          @page {size : A4; margin:1cm;}
          th, td{border : 1px solid black;}
          ''')
HTML('outputs/index.html').write_pdf('saida.pdf', stylesheets=[css])