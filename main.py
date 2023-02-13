import datetime
import os

if not os.path.exists('docs'):
    os.mkdir('docs')


with open('docs/index.html', 'w') as f:
    with open('template/index.html', 'r') as r:
        content = r.read()
        content = content.format(action_time=datetime.datetime.now())
        f.write(content)