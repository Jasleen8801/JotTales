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

## Setting up Environment

Please generate a `.env` file in the root and use the following format:

```bash
EMAIL=<YOUR_EMAIL>
PASSWORD=<YOUR_PASSWORD_FOR_EMAIL>
```

If you've two atep authentication, create a password for the app using the following link: 
`https://myaccount.google.com/apppasswords`