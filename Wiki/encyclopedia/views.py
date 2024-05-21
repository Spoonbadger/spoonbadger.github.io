# from django.http import HttpResponse
from django.shortcuts import render
from . import util
from markdown2 import Markdown 


def convert_md_to_html(title):
    entry = util.get_entry(title)
    if entry == None:
        return None
    else:
        markdowner = Markdown()
        return markdowner.convert(entry)


def index(request):
    entries = util.list_entries()

    return render(request, "encyclopedia/index.html")


def title(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "html_content": html_content
        })