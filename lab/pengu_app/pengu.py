import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


st.title('Penguins')
st.markdown('企鵝數據探索分析')
# import data
pengu_df = pd.read_csv('penguins.csv')

# st.write(pengu_df.head(10))


selected_species = st.selectbox('要看什麼物種？',
    ['Adelie', 'Gentoo', 'Chinstrap'])
pengu_df = pengu_df[pengu_df['species'] == selected_species]

selected_x_var = st.selectbox('X 軸是什麼？', 
  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 
selected_y_var = st.selectbox('Y 軸是什麼？', 
  ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']) 


## (in-class exercise) filter out by gender
# selected_gender = st.selectbox('What gender do you want to filter for?',
# ['all', 'male', 'female'])

# if selected_gender == 'male':
#     pengu_df = pengu_df[pengu_df['sex'] == 'male']
# elif selected_gender == 'female':
#     pengu_df = pengu_df[pengu_df['sex'] == 'female']
# else:
#     pass





# graph each species by hue and shape
sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
# 
fig, ax = plt.subplots()
# ax = sns.scatterplot(x = pengu_df[selected_x_var],
#                      y = pengu_df[selected_y_var])

ax = sns.scatterplot(data = pengu_df, x = selected_x_var, 
  y = selected_y_var, hue = 'species', markers = markers,
  style = 'species') 

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("scatterplot")
st.pyplot(fig)


