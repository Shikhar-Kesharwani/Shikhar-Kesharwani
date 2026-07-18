with open('C:/Users/HP/Downloads/ascii/andrew_style.py', 'r') as f:
    text = f.read()
text = text.replace('repeatCount="250"', 'fill="freeze"')
with open('C:/Users/HP/Downloads/ascii/andrew_style.py', 'w') as f:
    f.write(text)
