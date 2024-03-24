import streamlit as st

from shelter.core.parse import parse_immoscout_page

st.title("Gimme Shelter! :house_with_garden:")
st.write(
    "Diese Webapp hilft dir auf der Wohnungssuche. Sie generiert dir ein nettes Anschreiben für den potenziellen Vermieter auf der Basis einer Wohnungsanzeige."
)

page_content = st.text_area(
    "Bitte gib den rohen HTML Code der Wohnungsanzeige ein:",
    "Dazu einfach auf die Anzeige gehen -> Rechtsklick -> Seite anzeigen -> Rechtsklick -> Alles auswählen -> Rechtsklick -> Kopieren -> Hier einfügen.",
)

_, col2 = st.columns([0.8, 0.2])

if col2.button("Anschreiben generieren", type="primary"):
    st.write("Folgende Infos wurden gefunden:")
    st.write(parse_immoscout_page(page_content))
