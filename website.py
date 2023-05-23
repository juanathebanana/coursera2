

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import datetime
from storing.data import create_usertable
from storing.data import add_userdata
from storing.data import login_user
from storing.dirit import make_hashes
from storing.dirit import check_hashes


nuevo=open('/home/juana/Desktop/coursera/storing/subject_list.pkl','rb')
cursos_nuevo=pickle.load(open('subject_list.pkl','rb')
completo=list(set(cursos_nuevo['Course Subject'].values()))



# <==== Code starts here ====>
st.balloons()

def main():
	"""Simple Login App"""

	st.title("Simple Login App")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("select",["sex","Course selection"])
				if task == "sex":
					st.radio('Pick your gender',['Male','Female','Other'])

				if task =="Course selection":
					filter_subject=st.radio("What do you want to learn?",completo)
					if st.button('Show Recommended Courses'):
						st.write("Recommended Courses based on your interests are :")
					if filter_subject == completo[0]:
						st.write("\n Top 5 Rated Courses in:",completo[0])











			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")





