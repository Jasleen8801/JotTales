# Adding Posts to Database

To use posts.json and enter the data, open the terminal and input the command:

```bash
python manage.py shell
```

Then use the following script:

```python
import json
from blogs.models import Posst
with open('posts.json') as f:
    posts_json = json.load(f)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()

exit()
```

After this exit the shell and run the server using:

```bash
python manage.py runserver
```