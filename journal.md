I am going to add this file as a journal to add notes as I make commits. This should make it easier to look back through the commit history and understand what exactly I was doing at that point. I can also include links to documentation here.

## adding static files
- I am adding a directory called 'static' in our 'polls' directory. This is where django will look for static assets. [Docs](https://docs.djangoproject.com/en/4.0/intro/tutorial06/#customize-your-app-s-look-and-feel)
> - create another directory called polls and within that create a file called style.css. In other words, your stylesheet should be at polls/static/polls/style.css. Because of how the AppDirectoriesFinder staticfile finder works, you can refer to this static file in Django as polls/style.css, similar to how you reference the path for templates
- yes, this seemingly duplicative folder naming is intentional, in case of projects that contain multiple apps with similarly-named static files.

### linking the style sheet
- add a style to the .css (in this case, green links)

- the `{% load static %}` template tag generates the absolute URL of static files
- so we can just use `"{% static 'polls/style.css' %}"` as the href for the styleshet

that's it! Links are now green on the index.html page. I wonder if there is a way to apply that style site-wide. 

### static images
- made a new folder:  /polls/static/polls/images, and put an image inside
- add `
body {
    background: white url("images/holodeck.jpg") no-repeat;
}
`
 to stylesheet. So, you can just use a relative path from the stylesheet file. (oh yeah actually, the docs have a note, 
 > You should always use relative paths to link your static files between each other, because then you can change STATIC_URL (used by the static template tag to generate its URLs) without having to modify a bunch of paths in your static files as well.)