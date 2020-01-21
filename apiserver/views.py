from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

from apiserver import models
from models import Article

# Create your views here.
def index(request):
    return JsonResponse({
        "Name" : "Prakhar"
    })

@api_view(["POST"])
def postArticle(request):
    title = request.data.get("title")
    body = request.data.get("body")

    new_article=Article(
        title=title,
        body=body
    )

    new_article.save()

    return JsonResponse(
        {
            "status" : "success"
        }
    )
