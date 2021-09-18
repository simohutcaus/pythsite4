from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
import pandas as pd
import json

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    


def hornsby(request):
    df = pd.read_csv('https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv')
    cases = df
    local = cases.loc[cases['lga_name19'] == 'Hornsby (A)']
    local2 = local.loc[local['notification_date'] > '2021-06-16'] 
    local2 = local2.iloc[::-1]
    table = local2.to_html()
    json_records = local2.reset_index().to_json(orient = 'records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'polls/hornsby.html', context)

def nsydney(request):
    df = pd.read_csv('https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv')
    cases = df
    local = cases.loc[cases['lhd_2010_code'] == 'X760']
    local2 = local.loc[local['notification_date'] > '2021-06-16'] 
    local2 = local2.iloc[::-1]
    table = local2.to_html()
    json_records = local2.reset_index().to_json(orient = 'records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'polls/nsydney.html', context)

def postcode(request):
    df = pd.read_csv('https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv')
    cases = df
    local = cases.loc[cases['postcode'] == '2077']
    local2 = local.loc[local['notification_date'] > '2021-06-16'] 
    local2 = local2.iloc[::-1]
    table = local2.to_html()
    json_records = local2.reset_index().to_json(orient = 'records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'polls/postcode.html', context)

def unknown(request):
    df = pd.read_csv('https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv')
    cases = df
    local = cases.loc[cases['likely_source_of_infection'] == 'Locally acquired - no links to known case or cluster']
    local2 = local.loc[local['notification_date'] > '2021-06-16'] 
    local2 = local2.iloc[::-1]
    json_records = local2.reset_index().to_json(orient = 'records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    
    return render(request, 'polls/unknown.html', context)