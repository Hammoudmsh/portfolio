# https://gist.github.com/rxaviers/7360908
# https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634
# https://icons8.com/icons/set/google-scholar

# https://arnaudmiribel.github.io/streamlit-extras/extras/app_logo/

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
# from bs4 import BeautifulSoup
# from streamlit_extras.echo_expander import echo_expander


import pandas as pd
import numpy as np
from common import *

from common import ICONS_IMAGES
ICONS_IMAGES_LOADED = ICONS_IMAGES
#{k:Image.open(v) for k,v in ICONS_IMAGES.items() if 'http' not in k else v}

def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="600" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

def get_icon(width=24, height=24, name="Missed", link = ""):
	icon_template = '''
	<a href="{url}" target="_blank" style="margin-right: 20px;">
	<img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
	</a>
	'''


	icons_html = icon_template.format(url="", icon_src=link, alt_text=name.capitalize(), width=width, height=height)

	return icons_html


def social_icons(width=24, height=24, icon_images = {}, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = icon_images.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)
                print(icons_html)



        return icons_html
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )







if __name__ == "__main__":
	# Set page title
	st.set_page_config(page_title=page_title, page_icon = page_icon, layout = "wide", initial_sidebar_state = "auto")
	# Use the following line to include your style.css file
	st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
	local_css("style/style.css")
	footer = """
		footer{
			visibility:visible;
		}
		footer:after{
			content:'Copyright © 2023 Mohammed Hammoud';
			position:relative;
			color:black;
		}
	"""
	add_bg_from_local('bg.png')
	# Load assets
	#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
	# Assets for about me
	# img_utown = Image.open("images/utown.JPG")
	


	img_lh = Image.open(ICONS_IMAGES_LOADED["ABOUT_ME_IMAGE"])

	img_ifg = Image.open(ICONS_IMAGES_LOADED["ABOUT_ME_IMAGE"])
	# #Assets for competitions
	# img_lit = Image.open("images/legalease.jpg")
	# img_lifehack2 = Image.open("images/lifehack2.jpg")
	# img_lifehack = Image.open("images/lifehack.jpg")
	# img_he4d = Image.open("images/he4d.jpg")
	# img_ecc = Image.open("images/ecc.jpg")
	# img_shopee = Image.open("images/shopee.png")
	# img_sbcc = Image.open("images/sbcc.png")
	# img_runes = Image.open("images/runes.png")
	# # Assets for education
	# img_sji = Image.open("images/sji.jpg")
	# img_tpjc = Image.open("images/tpjc.jpg")
	# img_nus = Image.open("images/nus.jpeg")
	# img_poc = Image.open("images/poc.jpg")
	# img_gmss = Image.open("images/gmss.jpg")
	# img_sjij = Image.open("images/sjij.jpg")
	# img_dsa = Image.open("images/dsa.jpg")
	# # Assets for experiences
	# img_quest = Image.open("images/questlogo.jpg")
	# img_scor = Image.open("images/scor.jpg")
	# img_iasg = Image.open("images/iasg.jpg")
	# img_sshsph = Image.open("images/sshsph.jpg")
	# img_yll = Image.open("images/yll.jpg")
	# img_saf = Image.open("images/saf.jpg")
	# img_bitmetrix = Image.open("images/company_name1.jpg")
	# img_groundup = Image.open("images/groundup.jpg")
	# img_hedgedrip = Image.open("images/hedgedrip.jpg")


	# # Assets for projects
	# image_names_projects = ["ecom", "chatgpt", "videogames", "health", 
	#                          "biopics", "anime", "word2vec", "cellphone", 
	#                          "spotify", "map", "gephi", "fob", "get", "ttdb",
	#                          "blockchain"]
	# images_projects = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
	# # Assets for volunteering
	# image_names_vol = ["sdslogo", "sportslogo", "gdsclogo", "csclogo", 
	#                          "nussulogo", "sklogo", "simlogo", "tpjclogo", 
	#                          "sjilogo", "nuspc", "hcs", "fintech"]
	# images_vol = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]
	# # Assets for blog
	# img_qb = Image.open("images/qb.jpg")
	# img_mayans = Image.open("images/mayans.jpg")
	# img_outlier = Image.open("images/outlier.png")
	# img_dac = Image.open("images/dac.png")
	# img_raffles = Image.open("images/raffles.jpg")
	# img_covid = Image.open("images/covid.jpg")
	# img_gender = Image.open("images/gender.jpg")
	# img_hci = Image.open("images/hci.jpg")
	# img_wordcloud = Image.open("images/wordcloud.jpg")
	# img_taste = Image.open("images/taste.jpg")
	# img_measles = Image.open("images/measles.jpeg")
	# img_bmsaew = Image.open("images/bmsaew.png")
	# img_dac1 = Image.open("images/dac1.png")
	# img_dac2 = Image.open("images/dac2.png")
	# # Assets for gallery
	# # 2005
	# img_2005_1 = Image.open("gallery/2005_1.jpg")
	# img_2005_2 = Image.open("gallery/2005_2.jpg")
	# # 2006
	# img_2006_1 = Image.open("gallery/2006_1.jpg")
	# # 2008
	# img_2008_1 = Image.open("gallery/2008_1.jpg")
	# # 2009
	# img_2009_1 = Image.open("gallery/2009_1.jpg")
	# # 2011
	# image_dict = {}
	# num_images = 4
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2011_{i}"
	#     image_path = f"gallery/2011_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2012 
	# image_dict = {}
	# num_images = 7
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2012_{i}"
	#     image_path = f"gallery/2012_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2013
	# image_dict = {}
	# num_images = 11
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2013_{i}"
	#     image_path = f"gallery/2013_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2014
	# image_dict = {}
	# num_images = 13
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2014_{i}"
	#     image_path = f"gallery/2014_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2015
	# image_dict = {}
	# num_images = 48
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2015_{i}"
	#     image_path = f"gallery/2015_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2016
	# image_dict = {}
	# num_images = 25
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2016_{i}"
	#     image_path = f"gallery/2016_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2017
	# image_dict = {}
	# num_images = 4
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2017_{i}"
	#     image_path = f"gallery/2017_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2018
	# image_dict = {}
	# num_images = 16
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2018_{i}"
	#     image_path = f"gallery/2018_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# # 2019
	# image_dict = {}
	# num_images = 20
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2019_{i}"
	#     image_path = f"gallery/2019_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# #2020
	# image_dict = {}
	# num_images = 3
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2020_{i}"
	#     image_path = f"gallery/2020_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# #2021
	# image_dict = {}
	# num_images = 14
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2021_{i}"
	#     image_path = f"gallery/2021_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# #2022
	# image_dict = {}
	# num_images = 19
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2022_{i}"
	#     image_path = f"gallery/2022_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# #2023
	# image_dict = {}
	# num_images = 22
	# for i in range(1, num_images + 1):
	#     image_key = f"img_2023_{i}"
	#     image_path = f"gallery/2023_{i}.jpg"
	#     image_dict[image_key] = Image.open(image_path)
	# #img_lottie_animation = Image.open("images/lottie_animation.gif")
	# Assets for contact
	lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

	img_linkedin = Image.open("images/linkedin.png")
	img_github = Image.open("images/github.png")
	img_email = Image.open("images/email.png")



	with st.sidebar:
	    with st.container():
	        l, m, r = st.columns((1,3,1))
	        with l:
	            st.empty()
	        with m:
	            st.image(img_lh, width=190)
	        with r:
	            st.empty()

	    menu = {
	    "About Me":"person fill",
	    "Experience":"globe",
	    "Skills":"clock history",
	    "Education":"book half",
	    "Projects":"book half",
	    "Publications":"clipboard",
	    # "Papers":"clipboard",
	    # "Conferences":"clipboard",
	    "Rewards":"Award fill",#"trophy fill",
	    "Resume":"pencil square",
	    "Contact":"house"#"link",
	    }


	    choose = option_menu(
	                        PERSON_NAME, 
	                        list(menu.keys()),
	                         icons=list(menu.values()),
	                         menu_icon="mortarboard",
	                         orientation = "vertical", 
	                         default_index=4,
	                         styles={
	        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
	        "icon": {"color": "darkblue", "font-size": "25px"}, 
	        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
	        "nav-link-selected": {"background-color": "#f5f5dc"},
	    }
	    )
	
	    with st.container():
	        l, m, r = st.columns((0.11,2,0.1))
	        with l:
	            st.empty()
	        with m:
	            st.markdown(
                    social_icons(25, 25, icon_images = ICONS_IMAGES, LinkedIn=linkedin_url, GitHub=github_url, Email=f"mailto:{email_url}", GoogleScholar = GoogleScholar_url, ResearchGate = ResearchGate_url, ORCID = ORCID_url),
	                unsafe_allow_html=True)
	        with r:
	            st.empty()


	st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
	st.title(PERSON_NAME)

	df_experience = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Experience")
	df_eeducation = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Education")

	df_papers1 = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Publications")
	
	df_papers = df_papers1[
							# (df_papers1["State"]!="Inprogress") &&
							(df_papers1["Type"]=="paper")
							]


	df_confs = df_papers1[
							# (df_papers1["State"]!="Inprogress") &&
							(df_papers1["Type"]=="conference")
							]


	df_rewards = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Rewards")

	df_projects = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Projects")

	df_skills = pd.read_excel('PersonInfo.xlsx', engine='openpyxl', sheet_name="Skills")


	# Create header
	if choose == "About Me":
	    #aboutme.createPage()
	    with st.container():
	        left_column, middle_column, right_column = st.columns((1.5,0.2,0.4))
	        with left_column:
	            # st.header(ABOUT_ME_TEXT_HEADER)
	            st.subheader(ABOUT_ME_TEXT_SUB_HEAD)
	            st.write(ABOUT_ME_TEXT)
	            st.write(ABOUT_ME_RESUME)
	            
	        with middle_column:
	            st.empty()
	        with right_column:
	            st.image(Image.open(ICONS_IMAGES_LOADED["ABOUT_ME_IMAGE"]))
	# Create section for Work Experience
	elif choose == "Experience":

	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			for idx, i in enumerate(list(df_experience.index)):
				START_DATAE = df_experience.loc[i, 'From']
				END_DATAE = df_experience.loc[i, 'To']
				COMPANY_NAME = df_experience.loc[i, 'Name']
				COMPANY_URL = df_experience.loc[i, 'Link']
				COMPANY_POS = df_experience.loc[i, 'Location']
				WORK_POSITION = df_experience.loc[i, 'Position']
				WORK_LEARNT= df_experience.loc[i, 'Learned']
				if WORK_LEARNT!="None":
					WORK_LEARNT = WORK_LEARNT.split("\n")


				COMPANY_IMAGE = df_experience.loc[i, 'image']

				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						print("COMPANY_IMAGE", COMPANY_IMAGE)
						if COMPANY_IMAGE!="None": 
							image_column, company_column, company_link, company_pos_column = st.columns((0.5, 1,0.1, 0.5))
							COMPANY_IMAGE = Image.open(f"images/{COMPANY_IMAGE}")
							with image_column:
								st.image(COMPANY_IMAGE)
						else:
							company_column, company_link, company_pos_column = st.columns((2,0.1, 0.5))

				# COMPANY_IMAGE = None
				# WORK_ID = idx+1
				# if 1:
				# # with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
				# 	# st.header("Experience", divider=True)
				# 	with st.container():
				# 		if COMPANY_IMAGE: 
				# 			image_column, company_column, company_link, company_pos_column = st.columns((0.5, 1,0.1, 0.5))
				# 			with image_column:
				# 				st.image(img_bitmetrix)
				# 		else:
				# 			company_column, company_link, company_pos_column = st.columns((2,0.1, 0.5))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if COMPANY_NAME !="None":
							with company_column:
								st.subheader(f"{WORK_ID}.\t{COMPANY_NAME}")
								# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						if COMPANY_URL!="None":
							with company_link:
								st.markdown(f"[:link:]({COMPANY_URL})")
						if COMPANY_POS!="None":
							with company_pos_column:
								st.markdown(f"{COMPANY_POS}")


						margine, role_column, date_column = st.columns((0.1, 2,0.5))
						
						with date_column:
							st.write(f"{START_DATAE}-{END_DATAE}")
						with role_column:
							st.markdown(f"{WORK_POSITION}")
							
							if WORK_LEARNT !="None":				
								points = ""
								for p in WORK_LEARNT:
									st.markdown(f"""- {p}""")

							SKILLS = df_experience.loc[i, 'Skills']
							if SKILLS!="None":				
								SKILLS = SKILLS.split(";")
								skills_txt = ''
								for s in SKILLS:
									skills_txt += f'`{s}` '
								st.markdown(f"""
									\t{skills_txt}
								""")
						st.divider()

	elif choose == "Education":
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_eeducation.index)):
				START_DATAE = df_eeducation.loc[i, 'From']
				END_DATAE = df_eeducation.loc[i, 'To']
				COMPANY_NAME = df_eeducation.loc[i, 'Name']
				COMPANY_URL = df_eeducation.loc[i, 'Link']
				COMPANY_POS = df_eeducation.loc[i, 'Location']
				WORK_POSITION = df_eeducation.loc[i, 'Position']
				WORK_LEARNT= df_eeducation.loc[i, 'Learned']
				if WORK_LEARNT !="None":# not np.isnan(WORK_LEARNT):
					WORK_LEARNT = WORK_LEARNT.split("\n")

				FINAL_GRADE = df_eeducation.loc[i, 'Final grade']
				THESIS_TITLE = df_eeducation.loc[i, 'Thesis title']


				COMPANY_IMAGE = df_eeducation.loc[i, 'image']

				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						print("COMPANY_IMAGE", COMPANY_IMAGE)
						if COMPANY_IMAGE!="None": 
							image_column, company_column, company_link, company_pos_column = st.columns((0.25, 1,0.1, 0.5))
							COMPANY_IMAGE = Image.open(f"images/{COMPANY_IMAGE}")
							with image_column:
								st.image(COMPANY_IMAGE, use_column_width=True)

						else:
							company_column, company_link, company_pos_column = st.columns((0.2,0.1, 0.5))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if COMPANY_NAME !="None":
							with company_column:
								st.subheader(f"{WORK_ID}.\t{COMPANY_NAME}")
								# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						if COMPANY_URL !="None":
							with company_link:
								# st.markdown(f"[:link:]({COMPANY_URL})")
								st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["certificate"])}]({COMPANY_URL})""", unsafe_allow_html=True)

						if COMPANY_POS !="None":
							with company_pos_column:
								st.markdown(f"{COMPANY_POS}")


						# margine, role_column, date_column = st.columns((0.1, 2,0.5))
						margine, role_column, _, date_column = st.columns((0.25, 1,0.1,0.5))

						# 0.25, 1,0.1, 0.5
						with date_column:
							st.write(f"{START_DATAE}-{END_DATAE}")
						with role_column:
							st.markdown(f"{WORK_POSITION}")
							
							# points = ""
							# for p in WORK_LEARNT:
							# 	st.markdown(f"""- {p}""")


							if FINAL_GRADE !="None":
								st.markdown(f"""**Final grade:** {FINAL_GRADE}""")
							if THESIS_TITLE !="None":
								st.markdown(f"""**Thesis title:** {THESIS_TITLE}""")

							SKILLS = df_eeducation.loc[i, 'Skills']
							# print("&&&&&&&&&", SKILLS)
							if SKILLS != "None":				
								SKILLS = SKILLS.split(";")
								skills_txt = ''
								for s in SKILLS:
									skills_txt += f'`{s}` '
								st.markdown(f"""
									**Course work:** {skills_txt}
								""")
						st.divider()
	elif choose in ["Publications"]:
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header("Papers")
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_papers.index)):
				PUBLICATION_DATAE = df_papers.loc[i, 'publicationDate']
				PUBLICATION_NAME = df_papers.loc[i, 'PublicationName']
				PUBLICATION_URL = df_papers.loc[i, 'PublicationLink']
				PUBLICATION_JOURNAL = df_papers.loc[i, 'JournalName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_id, publication_name, publication_state, publication_url, publication_date = st.columns((0.1,1.9,0.1,0.1,0.3))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_id:
								st.markdown(f"{WORK_ID}.")

							with publication_name:
								st.markdown(f"{PUBLICATION_NAME}")

								# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						

						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"[:link:]({PUBLICATION_URL})")
								# st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["paper"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
								st.markdown(f"""[:link:]({PUBLICATION_URL})""", unsafe_allow_html=True)

						
						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")
						st.divider()


			#------------------Conferences
		with st.container():
			st.header("Conferences")

			# https://img.icons8.com/color/100/politician.png
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_confs.index)):
				PUBLICATION_DATAE = df_confs.loc[i, 'publicationDate']
				PUBLICATION_NAME = df_confs.loc[i, 'PublicationName']
				PUBLICATION_URL = df_confs.loc[i, 'PublicationLink']
				PUBLICATION_JOURNAL = df_confs.loc[i, 'JournalName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_id, publication_name, publication_state, publication_url, publication_date = st.columns((0.1,1.9,0.1,0.1,0.3))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_id:
								st.markdown(f"{WORK_ID}.")

							with publication_name:
								st.markdown(f"{PUBLICATION_NAME}")
						

						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"[:link:]({PUBLICATION_URL})")
								st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["paper"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
						
						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")
						st.divider()

	elif choose in ["Papers"]:
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_papers.index)):
				PUBLICATION_DATAE = df_papers.loc[i, 'publicationDate']
				PUBLICATION_NAME = df_papers.loc[i, 'PublicationName']
				PUBLICATION_URL = df_papers.loc[i, 'PublicationLink']
				PUBLICATION_JOURNAL = df_papers.loc[i, 'JournalName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_id, publication_name, publication_state, publication_url, publication_date = st.columns((0.1,1.9,0.1,0.1,0.3))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_id:
								st.markdown(f"{WORK_ID}.")

							with publication_name:
								st.markdown(f"{PUBLICATION_NAME}")

								# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						

						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"[:link:]({PUBLICATION_URL})")
								# st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["paper"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
								st.markdown(f"""[:link:]({PUBLICATION_URL})""", unsafe_allow_html=True)

						
						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")


						st.markdown("""
						<style>
						.block-container {
						padding-top: 0rem;
						padding-bottom: 0rem;
						padding-left: 5rem;
						padding-right: 5rem;
						}
						</style>
						""", unsafe_allow_html=True)

						st.divider()

	elif choose == "Conferences":
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)

			# https://img.icons8.com/color/100/politician.png
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_confs.index)):
				PUBLICATION_DATAE = df_confs.loc[i, 'publicationDate']
				PUBLICATION_NAME = df_confs.loc[i, 'PublicationName']
				PUBLICATION_URL = df_confs.loc[i, 'PublicationLink']
				PUBLICATION_JOURNAL = df_confs.loc[i, 'JournalName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_id, publication_name, publication_state, publication_url, publication_date = st.columns((0.1,1.9,0.1,0.1,0.3))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_id:
								st.markdown(f"{WORK_ID}.")

							with publication_name:
								st.markdown(f"{PUBLICATION_NAME}")
						

						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"[:link:]({PUBLICATION_URL})")
								st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["paper"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
						
						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")


						st.markdown("""
						<style>
						.block-container {
						padding-top: 0rem;
						padding-bottom: 0rem;
						padding-left: 5rem;
						padding-right: 5rem;
						}
						</style>
						""", unsafe_allow_html=True)

						st.divider()

						# hide = """
						# <style>
						# ul.streamlit-expander {
						#     border: 0 !important;
						# </style>
						# """

						# st.markdown(hide, unsafe_allow_html=True)


		# st.markdown(
		#     """<style>
		#                     .streamlit-expander {
		#                         border: none;
		#                         box-shadow: none;
		#                     }
		            
		#                     .streamlit-expanderHeader {
		#                         border-bottom: none;
		#                     }
		            
		#                     .streamlit-expanderClosed .streamlit-expanderHeader,
		#                     .streamlit-expanderClosed .streamlit-expanderContent {
		#                         border: none;
		#                     }
		#                 </style>""",
		#     unsafe_allow_html=True
		# )
	elif choose == "Rewards":
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_rewards.index)):

				PUBLICATION_DATAE = df_rewards.loc[i, 'RewardDate']
				PUBLICATION_NAME = df_rewards.loc[i, 'RewardName']
				PUBLICATION_URL = df_rewards.loc[i, 'RewardLink']
				PUBLICATION_JOURNAL = df_rewards.loc[i, 'OrganName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_name, publication_state, publication_url, publication_date = st.columns((2,0.1,0.1,0.5))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_name:
								st.markdown(f"""{WORK_ID}.\t{PUBLICATION_NAME}
									""")
								# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						


						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"[:link:]({PUBLICATION_URL})")
								st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["certificate"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)

						
						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")
						

						_,organ_details, _ = st.columns((0.1,2.2,0.5))
						if PUBLICATION_JOURNAL !="None":
							with organ_details:
								st.markdown(f"    {PUBLICATION_JOURNAL}")

						st.markdown("""
						<style>
						.block-container {
						padding-top: 0rem;
						padding-bottom: 0rem;
						padding-left: 5rem;
						padding-right: 5rem;
						}
						</style>
						""", unsafe_allow_html=True)

						st.divider()
	elif choose == "Projects":
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_projects.index)):

				PUBLICATION_DATAE = df_projects.loc[i, 'ProjectDate']
				PUBLICATION_NAME = df_projects.loc[i, 'ProjectTitle']
				PUBLICATION_URL = df_projects.loc[i, 'ProjectLink']
				# PUBLICATION_JOURNAL = df_projects.loc[i, 'OrganName']
				WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_id, publication_name, publication_state, publication_url, publication_date = st.columns((0.1,1.9,0.1,0.1,0.3))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						if PUBLICATION_NAME !="None":
							with publication_id:
								st.markdown(f"{WORK_ID}.")

							with publication_name:
								st.markdown(f"{PUBLICATION_NAME}")
						

						if PUBLICATION_URL !="None":
							with publication_url:
								# st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["github"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
								st.markdown(f"""[:link:]({PUBLICATION_URL})""", unsafe_allow_html=True)

								# https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png
								# st.markdown(
								# 	get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["github"]),
								# 	unsafe_allow_html=True
								# )

								# st.components.v1.html(
								# 	"""
								# 		<!-- awesome.html -->
								# 		<script src="https://kit.fontawesome.com/2c74303849.js" crossorigin="anonymous"></script>
								# 		<i class="fa-solid fa-paw"></i>
								# 	"""
								# 	)

						if PUBLICATION_DATAE !="None":
							with publication_date:
								st.markdown(f"{PUBLICATION_DATAE}")

						_,pro_details, pro_media = st.columns((0.1, 2.2,0.5))
						columns_list = list(df_projects.columns)
						with pro_details:
							for c in columns_list:
								if c not in ["ProjectDate", "ProjectTitle", "ProjectLink", "media"]:
									# st.markdown(f"- **{c}:** {df_projects.loc[i, c]}")
									if df_projects.loc[i, c]!="None":										
										st.markdown(f"""\t- **{c}** {df_projects.loc[i, c]}""")
						with pro_media:
							if df_projects.loc[i, "media"]!="None":
								if 'PNG' in df_projects.loc[i, "media"] or 'png' in df_projects.loc[i, "media"] or 'jpg' in df_projects.loc[i, "media"] or 'JPG' in df_projects.loc[i, "media"]:#.capitalize():
									xxx = Image.open(df_projects.loc[i, "media"])
									st.image(xxx, caption='')
								elif 'mp4' in df_projects.loc[i, "media"]:
									video_file = open(df_projects.loc[i, "media"], 'rb')
									video_bytes = video_file.read()
									st.video(video_bytes)


								# elif if '' in df_projects.loc[i, "media"].capitalize():		



						st.markdown("""
						<style>
						.block-container {
						padding-top: 0rem;
						padding-bottom: 0rem;
						padding-left: 5rem;
						padding-right: 5rem;
						}
						</style>
						""", unsafe_allow_html=True)

						st.divider()

	elif choose == "Skills":
	    #st.write("---")
		# with st.expander(st.header("Experience"), expanded = False):
		with st.container():
			st.header(choose)
			# START_DATAE = '01.01.2022'
			# END_DATAE = "01.01.2023"
			# COMPANY_NAME = "Company Name"
			# COMPANY_URL = 'https://bitmetrix.ai'
			# COMPANY_POS = "Moscow"
			# WORK_POSITION = "Embedded system Engineer"
			# COMPANY_IMAGE = None
			# WORK_ID = 1	
			for idx, i in enumerate(list(df_skills.index)):

				# PUBLICATION_DATAE = df_skills.loc[i, 'ProjectDate']
				# PUBLICATION_NAME = df_skills.loc[i, 'ProjectTitle']
				# PUBLICATION_URL = df_skills.loc[i, 'ProjectLink']
				# PUBLICATION_JOURNAL = df_projects.loc[i, 'OrganName']
				# WORK_ID = idx+1
				if 1:
				# with st.expander(f"{WORK_POSITION} at {COMPANY_NAME}", expanded = True):
					# st.header("Experience", divider=True)
					with st.container():
						publication_name, publication_state, publication_url, publication_date = st.columns((2,0.1,0.1,0.5))

						# image_column, company_column, company_pos_column, text_column, date_column = st.columns((0.5,5,0.5))
						# if PUBLICATION_NAME !="None":
						# 	with publication_name:
						# 		st.markdown(f"#### {WORK_ID}.\t{PUBLICATION_NAME}")
						# 		# st.markdown(f"{WORK_ID}\t{COMPANY_NAME}[:link:]({COMPANY_URL})")
						

						# if PUBLICATION_URL !="None":
						# 	with publication_url:
						# 		st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["github"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
								# https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png
								# st.markdown(
								# 	get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["github"]),
								# 	unsafe_allow_html=True
								# )

								# st.components.v1.html(
								# 	"""
								# 		<!-- awesome.html -->
								# 		<script src="https://kit.fontawesome.com/2c74303849.js" crossorigin="anonymous"></script>
								# 		<i class="fa-solid fa-paw"></i>
								# 	"""
								# 	)

						# if PUBLICATION_DATAE !="None":
						# 	with publication_date:
						# 		st.markdown(f"{PUBLICATION_DATAE}")


						columns_list = list(df_skills.columns)
						for c in columns_list:
							# if c not in ["ProjectDate", "ProjectTitle", "ProjectLink"]:
								# st.markdown(f"- **{c}:** {df_projects.loc[i, c]}")
							
							if df_skills.loc[i, c]!="None":
								if df_skills.loc[i, c].capitalize()=="LANGUAGES":
									st.markdown(f"""\t- **{c} {get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["github"])}** {df_skills.loc[i, c]}""", unsafe_allow_html=True)
								else:
									st.markdown(f"""\t- **{c}** {df_skills.loc[i, c]}""")



						# st.markdown("""
						# <style>
						# .block-container {
						# padding-top: 0rem;
						# padding-bottom: 0rem;
						# padding-left: 5rem;
						# padding-right: 5rem;
						# }
						# </style>
						# """, unsafe_allow_html=True)

						st.divider()


	elif choose == "Contact":
	# Create section for Contact
	    #st.write("---")
	    st.header("Contact")
	    with st.container():
	        text_column, mid, image_column = st.columns((1.3,0.1,0.3))
	        with text_column:
	            st.write(f"Use this {email_url} or contact me from below.")
	            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
	                #st.write('Please help us improve!')
	                #Name=st.text_input(label='Your Name',
	                                    #max_chars=100, type="default") #Collect user feedback
	                #Email=st.text_input(label='Your Email', 
	                                    #max_chars=100,type="default") #Collect user feedback
	                #Message=st.text_input(label='Your Message',
	                                        #max_chars=500, type="default") #Collect user feedback
	                #submitted = st.form_submit_button('Submit')
	                #if submitted:
	                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
	            def create_database_and_table():
	                conn = sqlite3.connect('contact_form.db')
	                c = conn.cursor()
	                c.execute('''CREATE TABLE IF NOT EXISTS contacts
	                            (name TEXT, email TEXT, message TEXT)''')
	                conn.commit()
	                conn.close()
	            create_database_and_table()

	            st.subheader("Contact Form")
	            if "name" not in st.session_state:
	                st.session_state["name"] = ""
	            if "email" not in st.session_state:
	                st.session_state["email"] = ""
	            if "message" not in st.session_state:
	                st.session_state["message"] = ""
	            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
	            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
	            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


	            column1, column2= st.columns([1,5])
	            if column1.button("Submit"):
	                conn = sqlite3.connect('contact_form.db')
	                c = conn.cursor()
	                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
	                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
	                conn.commit()
	                conn.close()
	                st.success("Your message has been sent!")
	                # Clear the input fields
	                st.session_state["name"] = ""
	                st.session_state["email"] = ""
	                st.session_state["message"] = ""
	            def fetch_all_contacts():
	                conn = sqlite3.connect('contact_form.db')
	                c = conn.cursor()
	                c.execute("SELECT * FROM contacts")
	                rows = c.fetchall()
	                conn.close()
	                return rows
	            
	            if "show_contacts" not in st.session_state:
	                st.session_state["show_contacts"] = False
	            if column2.button("View Submitted Forms"):
	                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
	            
	            if st.session_state["show_contacts"]:
	                all_contacts = fetch_all_contacts()
	                if len(all_contacts) > 0:
	                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
	                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
	                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
	                    st.markdown(markdown_table)
	                else:
	                    st.write("No contacts found.")


                # social_icons(30, 30, icon_images = ICONS_IMAGES, Youtube=youtube_url, LinkedIn=linkedin_url, GitHub=github_url, Wordpress=wordpress_url, Email=f"mailto:{email_url}", GoogleScholar = GoogleScholar_url, ResearchGate = ResearchGate_url, ORCID = ORCID_url),

	            st.markdown(
                    social_icons(80, 80, icon_images = ICONS_IMAGES, LinkedIn=linkedin_url, GitHub=github_url, Email=f"mailto:{email_url}", GoogleScholar = GoogleScholar_url, ResearchGate = ResearchGate_url, ORCID = ORCID_url),
	                unsafe_allow_html=True)
	            st.markdown("")
	            #st.write("© 2023 Harry Chang")
	            #st.write("[LinkedIn](https://linkedin.com/in/harrychangjr) | [Github](https://github.com/harrychangjr) | [Linktree](https://linktr.ee/harrychangjr)")
	        with mid:
	            st.empty()
	        with image_column:
	            st.image(img_ifg)
            # with st.container():
            #     l, m, r = st.columns((0.11,2,0.1))
            #     with l:
            #         st.empty()
            #     with m:
            #         st.markdown(
            #             social_icons(30, 30, icon_images = ICONS_IMAGES, Youtube=youtube_url, LinkedIn=linkedin_url, GitHub=github_url, Wordpress=wordpress_url, Email=email_url, GoogleScholar = GoogleScholar_url, ResearchGate = ResearchGate_url, ORCID = ORCID_url), unsafe_allow_html=True)
            #     with r:
            #         st.empty()
	elif choose == "Resume":   
		st.header("Resume")
		_,pdf_download_btn, _ = st.columns((0.35,0.2,0.5))
		with pdf_download_btn:
			with open("Mohammed_Hammoud_CV.pdf", "rb") as file:
				btn = st.download_button(
					label="Download Resume",
					data=file,
					file_name="Mohammed_Hammoud_CV.pdf",
					mime="application/pdf"
					)

		_,pdf_col, _ = st.columns((0.1,1,0.1))
		with pdf_col:
			# st.markdown(pdf_link(RESUME_LINK, "Download resume "+get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["download"])), unsafe_allow_html=True)
			# st.markdown(f"""[{get_icon(width=24, height=24, name="Missed", link=ICONS_IMAGES["certificate"])}]({PUBLICATION_URL})""", unsafe_allow_html=True)
			show_pdf("Mohammed_Hammoud_CV.pdf")





















