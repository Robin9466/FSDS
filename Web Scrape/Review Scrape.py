from flask import Flask , render_template, jsonify
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq