

import serpapi
from serpapi import GoogleSearch
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# """____________________________________________________""""

page_setup = st.set_page_config(page_title="Price Comparison",page_icon="🔎",layout="centered")

# """------------------------------------------------------------------"""



#"""-------------------------------------------------------------------------

c1,c2,c3,c4= st.columns([1,2,2,2.5])
c1.image("images.png",width = 400)
c4.markdown("# E-Pharmacy Price compairsion system")

"""----------------------------------------------------------------------"""

st.sidebar.header("Enter the name of medicine:")
medicine_name = st.sidebar.text_input("Enter name here 👇:")
option_no = st.sidebar.text_input("Enter the no.of options here 👇:")

def price_compare(name):
    params = { "engine": "google_shopping",
                "q": name,
                "api_key": "5f037e5beae35b499e82ca5ef113fbe75b9b389b557f156c0d856bbc5e75659a",
                "gl": "in",
             }

    search=serpapi.GoogleSearch(params)
    result=search.get_dict()
    shopping_results=result["shopping_results"]
    return shopping_results

medicine_company=[]
price=[]
if medicine_name is not None:
    if st.sidebar.button("show Compare"):

        results=price_compare(medicine_name)
        st.sidebar.image(results[0].get("thumbnail"))
        lowest_price = float(results[0].get("price")[1:])
        print(lowest_price)
        lowest_price_index = 0

        for i in range(int(option_no)):
            st.title(f"Option {i + 1}")
            current_price = float(results[i].get("price")[1:])
            medicine_company.append(results[i].get("source"))
            price.append(float(results[i].get("price")[1:10]))

            c1,c2 = st.columns(2)

            c1.write("Company")
            c2.write(results[i].get("source"))
            c1.write("title")
            c2.write(results[i].get("title"))

            print(current_price)
            print(lowest_price)
            lowest_price = min(current_price, lowest_price)
            print(lowest_price)
            if current_price <= lowest_price:
                lowest_price = current_price
                lowest_price_index = i

            c1.write("price")
            c2.write(results[i].get("price")[1:])
            url = results[i].get("product_link")
            c1.write("Buy Link:")
            c2.write("[link](%s)"%url)

            """ __________________________________________________________________________"""
        st.title("best option:")
        c1,c2 = st.columns(2)
        c1.write("company")
        c2.write(results[lowest_price_index].get("source"))
        c1.write("title")
        c2.write(results[lowest_price_index].get("title"))
        c1.write("price")
        c2.write(results[lowest_price_index].get("price"))
        url = results[i].get("product_link")
        c1.write("Buy Link:")
        c2.write("[link](%s)"%url)
        """----------------------------------------------------------"""


df = pd.DataFrame(price,medicine_company)
st.title("Chart omparison:")
st.bar_chart(df)

fig,ax=plt.subplots()
ax.pie(price,labels=medicine_company,shadow=True)
st.pyplot(fig)













