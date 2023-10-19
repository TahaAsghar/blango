from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html")