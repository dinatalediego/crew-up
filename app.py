import streamlit as st
from pathlib import Path

# Configuración general
st.set_page_config(
    page_title="Crew-Up Macroproceso",
    page_icon="🚀",
    layout="wide"
)

# Inyectar CSS corporativo (colores, tipografía)
st.markdown("""
<style>
  .css-1d391kg {  /* cuerpo */
    font-family: 'Segoe UI', Tahoma, sans-serif;
  }
  .css-18e3th9 { /* sidebar */
    background-color: #0d47a1;
  }
  .css-1v0mbdj { /* headers */
    color: #0d47a1;
  }
</style>
""", unsafe_allow_html=True)

# Sidebar de navegación
section = st.sidebar.radio(
    "📂 Secciones",
    ["Macroproceso", "Juntas Gerenciales"]
)

base = Path(__file__).parent / "crew-up"

if section == "Macroproceso":
    st.title("🚀 Macroproceso")
    md_files = sorted((base/"macroprocess").glob("*.md"))
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        st.markdown(f"---\n## {md.stem.replace('_',' ')}")
        st.markdown(text)

else:
    st.title("📅 Juntas Gerenciales")
    md_files = sorted((base/"meetings").glob("*.md"))
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        st.markdown(f"---\n## {md.stem.replace('_',' ')}")
        st.markdown(text)
