from django.shortcuts import render

from .models import Data
from .forms import DataForm

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect



from django.template import Context, Template
from django.http import HttpResponse, HttpRequest, StreamingHttpResponse



def domainindex(request):

	return render(request, 'sschool/index.html', {})

