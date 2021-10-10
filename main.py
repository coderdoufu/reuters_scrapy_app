import subprocess
import streamlit as st
import os
import sys
import json
import pandas as pd

st.title('Reuters Crawling App')

data_dir = 'data'
reuters_output_file = os.path.join(data_dir,'reuters.json')

# if os.path.isfile(reuters_output_file):
#     os.remove(reuters_output_file)

# read section categories file
with open(os.path.join(data_dir, 'reuters_categories.json'),'rb') as f:
    section_categories_raw = json.load(f)
    section_categories = {}
    for section_cat in section_categories_raw:
        section_categories[section_cat['section_name']] = dict(zip(section_cat['section_cats'], section_cat['section_cats_url']))

# read section file
with open(os.path.join(data_dir,'reuters_sections.txt'),'r') as f:
    sections = f.readlines()[0].split(',')

option_left, option_right = st.columns(2)

# selector box for section
option_section = option_left.selectbox(
    'Which section you would like to crawl?',
    [section.capitalize() for section in sections]).lower()

# selector box for section categories
option_section_category = ""
if len(section_categories[option_section].keys()) != 0:
    option_section_category = option_right.selectbox(
        'Which category you would like to crawl?',
        section_categories[option_section].keys())

option_section_category_url = section_categories[option_section].get(option_section_category,f'/{option_section}')
st.write('ℹ️ Crawling url: www.reuters.com'+option_section_category_url)

crawl_start = st.button('Start crawling')
download_status = st.empty()


if crawl_start:
    download_status.write("Downloading ... Crawling takes quite a while. Please be patient!")
    subprocess.call([f"{sys.executable} spiders/reuters.py \
                      --section {option_section} \
                      --section_category_url {option_section_category_url}"], shell=True)

    download_status.empty()
    if os.path.isfile(reuters_output_file):
        
        download_status.write("Downloading done!")

        with open(reuters_output_file,'rb') as f:
            reuters_result = json.load(f)

        df = pd.DataFrame(reuters_result)
        df
    else:
        download_status.write("Downloading failed!")
