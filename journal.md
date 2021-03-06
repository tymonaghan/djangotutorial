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

 I'm continuing to play around with the background - it seems like I should be able to add a layer of semi-transparent color (or white) to "fade" the background image (I've manually pre-processed the image first in the past, this would be better) but it's not working so I'm leaving it alone for now -- just lightening the image and ignoring the margins! 

 ## updating the admin site
 today we're updating the Admin site/form that Django automatically generates for us and is currently at [localhost:8000/admin](http://localhost:8000/admin).

 - for this commit, all I've done is make "Publication Date" come before "Question" field. Not a big deal here, but important for forms with a lot of fields.
 - in this commit, I split the question items into 'fieldsets', note how the first element of each touple in `fieldsets` gets a header with that name on the admin page.

 ## .pyc files
 real quick, on my own, I'm removing and ignoring .pyc files from the git repo. It's a little weird that they weren't auto-ignored by Django, so I'll keep an eye out for adverse effects, but it just seems like it can't be right to keep committing these files I'm never touching. 

 ### adding the ability to edit Choices
 this commit contains a naive way to do this, which is just registering our Choice model directly in the admin. At the commit, you can go in and edit Choices just like questions. Note how the foreign-key connection is picked up by the Choices form, we get a dropdown to select the matching question "for free."
 Actually, this is cooler than I realized - it not only has the ability to assign an existing question but it automatically includes the ability to add a NEW question through the admin page via a pop-up. Cool. 

 This commit has the newer, better method, where we can include the Choice options "inline" in the same form as the Questions! Yeah, this is dope.

 In this commit I switched from `StackedInline` to `TabularInline` for the ChoiceInline class. This takes up way less screen space and looks slick. 

 ## Questions List admin page
 By default, Django displays the str() of each object. But sometimes it???d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object... In this commit, I just added the `list_display` property to QuestionAdmin, which makes the publication date now appear. 

This certainly works. The column header for was_published_recently is, by default, the name of the method (with underscores replaced with spaces). Each line contains the string representation of the output.

We're gonna improve that by using the `display()` decorator on that method (in polls/models.py). In this commit, we change the "was published recently" heading to "Published Recently?" and we output the actual boolean as ???/??? icons which is nice. 

Wow, this is a cool one, we added a filter based on the pub_date. I guess it knows it's a date and automatically allows filtering by 1/7/30 days, etc.

Another cool one, we added a search bar based on the question text with one line of code.

## customizing admin l&f
added a "templates" directory (but these are *project* templates) and then added a path to that directory as `DIR` in settings.py.

then 
- create a directory called "admin" in that templates folder
- copy the `base_site.html` template from django source code into that admin folder
- update that template to replace the {{}} with my own site name

that's it! Kind of convoluted to access that template and copy it over but once it's in place, it's easy.   Unhelpfully, the docs then say: 
> We use this approach to teach you how to override templates. In an actual project, you would probably use the django.contrib.admin.AdminSite.site_header attribute to more easily make this particular customization.

but I don't really know how to set that site_header attribute. Oh well, this works! [Here's a link to where we are in the docs at this point](https://docs.djangoproject.com/en/4.0/intro/tutorial07/#customizing-your-application-s-templates)