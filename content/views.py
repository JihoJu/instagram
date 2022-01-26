from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        # 피드에 있는 모든 데이터들을 가져온다. => 쿼리셋 => select * from content_feed
        feed_list = Feed.objects.all().order_by('-id')  # id 역순 (최신부터)

        return render(request, "instagram/main.html", context=dict(feeds=feed_list))
