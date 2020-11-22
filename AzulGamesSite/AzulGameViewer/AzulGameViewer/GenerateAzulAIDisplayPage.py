from django.template import Template, Context
from django.conf import settings
settings.configure() # We have to do this to use django templates standalone


template = """
<html>
<head>
<title>Template {{ title }}</title>
</head>
<body>
Body with {{ mystring }}.
</body>
</html>
"""

t = Template(template)
c = Context({"title": "title from code",
             "mystring":"string from code"})

with open("test.txt", "w+") as f:
    f.write(t.render(c))