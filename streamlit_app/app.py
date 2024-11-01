import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def get_clientes():
    response = requests.get(f"{BASE_URL}/clientes/")
    return response.json()

def create_cliente(nombre, apellido, email, telefono):
    cliente_data = {"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono}
    response = requests.post(f"{BASE_URL}/clientes/", json=cliente_data)
    return response.json()

st.title("Gestión de Clientes")

if st.button("Ver Clientes"):
    clientes = get_clientes()
    st.write(clientes)

with st.form("create_cliente_form"):
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    email = st.text_input("Email")
    telefono = st.text_input("Teléfono")
    if st.form_submit_button("Crear Cliente"):
        cliente = create_cliente(nombre, apellido, email, telefono)
        st.write(cliente)
