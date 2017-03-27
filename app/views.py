from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

site_url = os.environ['site_url']
oauth_key = os.environ['oauth_key']
oauth_secret = os.environ['oauth_secret']

def index(request):
	return HttpResponse('Site Url: {}/nKey: {}/nSecret: {}'.format(site_url, oauth_key, oauth_secret))

#################################################
#  In environment variables store the:
#  site_url
#  oauth_key
#  oauth_secret
#
#
# POST:
# Make payments
# Create a user account
# 
#
#
# GET:
# Get products
# Get orders
# 
#
#################################################