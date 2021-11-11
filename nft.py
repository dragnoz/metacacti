import streamlit as st
import requests, json


add_slider = st.sidebar.slider('Select Rarity', 0.0,100.0,(25.0,75.0))


st.sidebar.subheader("Filter")
collection = st.sidebar.text_input("Collection")
owner = st.sidebar.text_input("Owner")

endpoint = st.sidebar.selectbox("Select Option", ['Assets', 'JSON', 'Events', 'Rarity'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

st.sidebar.write("Meta Cacti")

params = {}
if collection:
    params['collection'] = collection
if owner:
    params['owner'] = owner

if endpoint == 'Assets':
    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)
    response = r.json()

    for asset in response["assets"]:
        st.write(f"{asset['name']} #{asset['token_id']}")
        if asset['image_url'].endswith('.mp4'):
            st.video(asset['image_url'])
        st.image(asset['image_url'])

elif endpoint == 'JSON':
    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)
    response = r.json()
    st.write(r.json())

