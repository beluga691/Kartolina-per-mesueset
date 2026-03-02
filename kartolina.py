import streamlit as st
st.set_page_config(page_title="Kartoline per 7 Marsin")
st.subheader("😁 Nje kartoline per ju! 🤩")
urim_per_mesuesit={
    "Xheni":"Ju falenderojme per dijet qe na jepni ne teknologji!",
    "Yllka":"Ju falenderojme per dijet qe na jepni ne biologji!",
    "Gladiola":"Ju falenderojme per dijet qe na jepni ne Anglisht!",
    "Egla":"Ju falenderojme per dijet qe na jepni ne Gjuhe Shqipe!",
    "Andi":"Ju falenderojme per dijet qe na jepni ne Muzike!",
    "Liza":"Ju falenderojme per dijet qe na jepni ne Matematike!",
    "Sava":"Ju falenderojme per dijet qe na jepni ne Histori!",
}

emri=st.text_input("Vendosni emrin tuaj: ")
if st.button("Shfaq urimin! 💌"):
    elif not emri:
        st.warning("Ju lutemi, vendosni emrin tuaj!")
        if emri not in urim_per_mesuesit
        st.error("Ky mesues nuk punon ne shkollen 22 Tetori")
        
        else:
            urimi_personal=urim_per_mesuesit[emri]
            st.markdown(f""")
            <div style="
                text-align;center;
                background: linear-gradient(135deg, #d4edda, #e6f7e6);
                padding:20px;
                border:3px solid #28a745;
                font-size:20px;
                box-shadow:0 6px 15px rgba(0,0,0,0.15);
                ">
                
                <h4> GEZUAR FESTEN! </h4> <br>
                <p> {urimi_personal} </p> <br>
                <p> Me dashuri nga Klubi i Kodimit! </p>
                <p>Shkolla 22 Tetori </p>
                </div>

                """, unsafe_allow_html=True)

