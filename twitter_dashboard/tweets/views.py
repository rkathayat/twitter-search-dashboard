from django.http import JsonResponse
from django.shortcuts import render
from .services import fetch_tweets

def search_tweets(request):
    query = request.GET.get("q", "")
    count = int(request.GET.get("count", 10))
    if not query:
        return JsonResponse({"error": "Query parameter is required"}, status=400)

    tweets = fetch_tweets(query, count)
    return JsonResponse({"tweets": tweets})

def index(request):
    return render(request, "tweets/index.html")
