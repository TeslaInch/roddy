from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Define word-based sentiment analysis
POSITIVE_WORDS = {"good", "happy", "excellent", "great", "awesome", "fantastic", "love","everton","igala","patience","joy","enjoy"}
NEGATIVE_WORDS = {"bad", "sad", "terrible", "awful", "worst", "hate", "horrible","fuck","Liverpool","anger","punch","Ebira"}

def analyze_sentiment(text):
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in POSITIVE_WORDS)
    neg_count = sum(1 for word in words if word in NEGATIVE_WORDS)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def home(request):
    sentiment = None
    if request.method == "POST":
        text = request.POST.get("text", "")
        sentiment = analyze_sentiment(text)
    
    return render(request, "body/home.html", {"sentiment": sentiment})
