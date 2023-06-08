# store-crud
A store crud with Django.

This CRUD is made to practice the basic concepts of Django as are URLS, MODELS, VIEWS, TEMPLATES, FORMS.

The request responses are returned as HTML

The CRUD have 3 classes. Category -> Campaing -> Product.

As Category is a super class of Campaing, and Campaing is a super class of Product.

Each Category can have one or more Campaing.
Each Campaing can have one or more Product.

In way to do a new entry a category and a campaing is needed.

Each model save the Foreing Key of the super class in order to have a filter and have data realtion.
