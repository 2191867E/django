import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/2/tutorial/','views':128,'likes':64},
        {'title': 'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/','views':256,'likes':32},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/','views':128,'likes':0}
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'http://docs.djangoproject.com/en/1.9/intro/tutorial01/','views':256,'likes':100},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':90,'likes':28},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/','views':512,'likes':256}

    ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/','views':28,'likes':56},
        {'title':'Flask',
         'url':'http://flask.pocoo.org','views':100,'likes':28
        }

    ]

    cats = {'Python':{'pages': python_pages},
            'Django':{'pages':django_pages},
            'Other Frameworks':{'pages':other_pages}}

    for cat,cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print("- {0} - {1}".format(str(c),str(p)))

def add_page(cat,title,url):
    p = Page.objects.get_or_create(category=cat,title=title)[0]
    p.url = url
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()