I am going to add this file as a journal to add notes as I make commits. This should make it easier to look back through the commit history and understand what exactly I was doing at that point. I can also include links to documentation here.

## adding static files
- I am adding a directory called 'static' in our 'polls' directory. This is where django will look for static assets. [Docs](https://docs.djangoproject.com/en/4.0/intro/tutorial06/#customize-your-app-s-look-and-feel)
> - create another directory called polls and within that create a file called style.css. In other words, your stylesheet should be at polls/static/polls/style.css. Because of how the AppDirectoriesFinder staticfile finder works, you can refer to this static file in Django as polls/style.css, similar to how you reference the path for templates
- yes, this seemingly duplicative folder naming is intentional, in case of projects that contain multiple apps with similarly-named static files.