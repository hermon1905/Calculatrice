import streamlit as st 
import math 

# configuration de la page
st.set_page_config(
    page_title = "CALCULATRICE",
    page_icon = "🔢",
    layout = "centered"
)

# titre de l'app
st.title("Calculatrice")


#----------------------------------Initialisation des variable de la session-------------------------------------
if 'result' not in st.session_state :
    st.session_state.result = 0
if 'display' not in st.session_state :
    st.session_state.display = '0'
if 'operation' not in st.session_state :
    st.session_state.operation = None 
if 'waitting_number' not in st.session_state :
    st.session_state.waitting_number = False





#------------------------------------fonction de la calculatrice-----------------------------------------
def clear():
    st.session_state.result = 0
    st.session_state.display = "0"
    st.session_state.operation = None
    st.session_state.waitting_number = False

def append_number(num):
    if st.session_state.waitting_number:
        st.session_state.display = str(num)
        st.session_state.waiting_for_number = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(num)
        else:
            st.session_state.display += str(num)

def append_decimal():
    if st.session_state.waitting_number:
        st.session_state.display = "0."
        st.session_state.waiting_for_number = False
    elif "." not in st.session_state.display:
        st.session_state.display += "."


def set_operation(op):
    try:
        if st.session_state.operation is not None and not st.session_state.waitting_number:
            calculate()
        st.session_state.result = float(st.session_state.display)
        st.session_state.operation = op
        st.session_state.waitting_number = True
    except ValueError:
        st.session_state.display = "Erreur"



def calculate():

    number = float(st.session_state.display)
    try :


        if st.session_state.operation == "+":
            result = st.session_state.result + number
        elif st.session_state.operation == "-":
            result = st.session_state.result - number
        elif st.session_state.operation == "*":
            result = st.session_state.result * number
        elif st.session_state.operation == "/":
            if number == 0 :
                st.session_state.display = "Erreur Division par zero !"
                return
            result = st.session_state.result / number

        else :
            return 

    # Gestion de l'affichage
        if result == int(result):
            st.session_state.display = str(int(result))
        else:
            st.session_state.display = f"{result:.10g}"
        
        st.session_state.result = result
        st.session_state.operation = None
        st.session_state.waitting_number = True
        
    except ValueError:
        st.session_state.display = "Erreur"
    except Exception as e:
        st.session_state.display = "Erreur"


            

# ---------------------------interface utilisateur-----------------------------
st.markdown(
    f"""
    <div style="
        background-color: #98A1BC;
        color: white;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: right;
        margin-bottom: 20px;
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    ">
        {st.session_state.display}
    </div>
    """,
    unsafe_allow_html=True
)

# premiere ligne
col1, col2, col3, col4, = st.columns(4)

with col1:
    if st.button(":orange[C]", use_container_width=True):
        clear()
        st.rerun()
with col2:
    if st.button(":red[±]", use_container_width=True):
        try :
            number = float(st.session_state.display)
            st.session_state.display = str(-number)
        except :
            pass
        st.rerun()
with col3 :
    if st.button(":red[%]", use_container_width=True):
        number = float(st.session_state.display)
        st.session_state.display = str(number /100)
        st.rerun()
with col4 :
    if st.button(":red[/]", use_container_width=True):
        set_operation("/")
        st.rerun()

# deuxieme ligne
col1, col2, col3, col4 = st.columns(4)

with col1 :
    if st.button("7", use_container_width=True):
        append_number(7)
        st.rerun()
with col2:
    if st.button("8", use_container_width=True):
        append_number(8)
        st.rerun()
with col3:
    if st.button("9", use_container_width=True):
        append_number(9)
        st.rerun()
with col4 :
    if st.button(":red[*]", use_container_width=True):
        set_operation("*")
        st.rerun()

# troisieme ligne
col1, col2, col3, col4 = st.columns(4)

with col1 :
    if st.button("4", use_container_width=True):
        append_number(4)
        st.rerun()
with col2:
    if st.button("5", use_container_width=True):
        append_number(5)
        st.rerun()
with col3:
    if st.button("6", use_container_width=True):
        append_number(6)
        st.rerun()
with col4 :
    if st.button(":red[-]", use_container_width=True):
        set_operation("-")
        st.rerun()

# quatrieme ligne
col1, col2, col3, col4 = st.columns(4)

with col1 :
    if st.button("1", use_container_width=True):
        append_number(1)
        st.rerun()
with col2:
    if st.button("2", use_container_width=True):
        append_number(2)
        st.rerun()
with col3:
    if st.button("3", use_container_width=True):
        append_number(3)
        st.rerun()
with col4 :
    if st.button(":red[+]", use_container_width=True):
        set_operation("+")
        st.rerun()

# cinquieme ligne 
col1, col2, col3, col4 = st.columns(4)

with col1 :
    st.write("")
with col2:
    if st.button("0", use_container_width=True):
        append_number(0)
        st.rerun()
with col3:
    if st.button(".", use_container_width=True):
        append_decimal()
        st.rerun()
with col4 :
    if st.button(":red[=]", use_container_width=True):
        calculate()
        st.rerun()

# --------------------------------Instructions-------------------------------------
st.markdown("---")
st.markdown("""
### Instructions d'utilisation :
- **C** : Efface tout
- **±** : Change le signe du nombre
- **%** : Convertit en pourcentage
""")