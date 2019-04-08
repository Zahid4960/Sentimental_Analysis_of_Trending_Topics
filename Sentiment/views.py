from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # import library for http response
from django.shortcuts import render
from django.template import loader
from .forms import userinput
import tweepy
from textblob import TextBlob
import tweepy
from textblob import TextBlob



# http request for home page
def home(request):
	return render(request, 'Sentiment/home.html', { 'title': 'Home' })

# http request for trending page
@login_required
def trending(request):
	return render(request, 'Sentiment/trending.html', { 'title': 'Trending'})

# http request for Check Random page
@login_required
def checkRandom(request):
	return render(request, 'Sentiment/checkRandom.html', { 'title': 'Check Random'})

# http request for about page
def about(request):
	return render(request, 'Sentiment/about.html', { 'title': 'About'})

# http request for contact page
def contact(request):
	return render(request, 'Sentiment/contact.html', { 'title': 'Contact'})

# action after clicking search button 
# http request for search result
def search_result(request):
    #this file contains sensitive information like django secret key
    #edit this according to your requirement

    class Django_Secrets:
        def __init__(self):
            self.key = ''


    class Oauth_Secrets:
        def __init__(self):
            self.consumer_key = "Y2x9mSVrom9p4aP4j4GmWGy"
            self.consumer_secret = "peCyxeqB68YvMrcdjXiHbzbWe3KXZKD4cE6NzHnjxTd2GCm9u"
            self.access_token = "2186053585-zX6VIzWtTr9nNg72SXk9q0TWe6yV6VDy10TCaxF"
            self.access_token_secret = "T3NAV6vXeOzHXLwBRulUXyBxRQUP8cjdbepFkeFzQyMgh"

        def primary(input_hashtag):
            secrets = Oauth_Secrets()       #secrets imported from secrets.py
            auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
            auth.set_access_token(secrets.access_token, secrets.access_token_secret)

            api = tweepy.API(auth)

            N = 1000                          #Number of Tweets
            Tweets = tweepy.Cursor(api.search, search=input_hashtag).items(N)
            neg = 0.0
            pos = 0.0
            neg_count = 0
            neutral_count = 0
            pos_count = 0
            for tweet in Tweets:
                # print tweet.text
                blob = TextBlob(tweet.text)
                if blob.sentiment.polarity < 0:         #Negative
                    neg += blob.sentiment.polarity
                    neg_count += 1
                elif blob.sentiment.polarity == 0:      #Neutral
                    neutral_count += 1
                else:                                   #Positive
                    pos += blob.sentiment.polarity
                    pos_count += 1
            # print "Total tweets",N
            # print "Positive ",float(pos_count/N)*100,"%"
            # print "Negative ",float(neg_count/N)*100,"%"
            # print "Neutral ",float(neutral_count/N)*100,"%"
            return [['Sentiment', 'no. of tweets'],['Positive',pos_count]
                    ,['Neutral',neutral_count],['Negative',neg_count]]

    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['search']
        print (input_hastag)
        data = sentimeter.primary(input_hastag)
        return render(request, "Sentiment/search_result.html", {'data': data})
    return render(request, "Sentiment/trending.html", {'userinput': user_input})	
	
