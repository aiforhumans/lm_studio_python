# lm_studio_python

# if needed, install and/or upgrade to the latest version of the OpenAI Python library
%pip install --upgrade openai

# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")