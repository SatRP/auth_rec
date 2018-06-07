# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404,render_to_response
# Create your views here.
from django.template.loader import render_to_string, get_template
import sys
import string
#from nltk.corpus import stopwords
import difflib
import pandas as pd
from django.db import connection
from django.forms import modelformset_factory,BaseModelFormSet
import json
from django.views.generic.edit import FormView
from django.http import HttpResponse
from dal import autocomplete
from django.urls import reverse_lazy
from django.views import generic

def auth_home(request):
	return render(request,'home.html')