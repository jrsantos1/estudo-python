import pdfkit 

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

pdfkit.from_url("https://jmbank.herokuapp.com/", 'github.pdf', configuration=config)
