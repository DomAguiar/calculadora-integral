import streamlit as st
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Calculadora de Integrais", layout="centered")

st.title("Calculadora de Integrais")

inpute = st.text_input("f(x) =", value="x**3")

def f(x):
    return eval(inpute, {"x": x, "sen": np.sin, "cos": np.cos, "tan":np.tan, "sqrt": np.sqrt, "log": np.log, "pi":np.pi,"np":np, "e":np.e, "exp":np.exp})

f_vec = np.vectorize(f)

col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Valor inicial (a):", value=-10.0)

with col2:
    b = st.number_input("Valor final (b):", value=10.0)

if st.button("Calcule"):
    try:
        integral, _ = quad(f, a, b)

        st.success(f"Resultado da integral ≈ **{integral:.5f}**")

        x = np.linspace(a, b, 400)

        fig, ax = plt.subplots()
        ax.plot(x, f_vec(x))
        ax.fill_between(x, f_vec(x), alpha=0.3)
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Erro ao processar a função: {e}")





