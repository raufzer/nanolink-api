from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import NanoLink
from .serailizers import NanoLinkSerailzer


