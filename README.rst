====================
Django Transactional
====================

Easy package to add simple transactional ModelForm forms in your django app.

Usage
=====

urls.py
-------
Add django transactional to your urls.py. It will accept urls of the form: **/APP/MODEL/add/** to add new model objects and **/APP/MODEL/add/OBJECT_ID/** to edit data in model object with id *OBJECT_ID*.
    url(r'^', include('dtrans.urls')),

Templates
---------
The templates must be named *APP_MODEL*.html in lower case letters and it will get **obj_form** as a parameter that can be used in the template code.

Forms
-----
Forms should be named *ModelForm* where *Model* is capitalized.

Examples
========

foo/models.py
-------------

class Bar(models.Model):
    name = models.CharField(max_length=10)

foo_bar.html
------------
<form action=".">
  {{ obj_form.as_p }}
  <input type="submit" value="Submit">
</form>
