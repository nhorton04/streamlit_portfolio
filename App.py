
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import _pickle as pickle
from random import sample
from PIL import Image
from scipy.stats import halfnorm


st.title("Welcome to my Portfolio")

st.header("Nick Horton")
st.write("Data Analyst, Software Developer, Musician, Anthropologist")

image = Image.open('aaa.jpeg')
st.image(image, use_column_width=True)
