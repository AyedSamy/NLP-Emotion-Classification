import streamlit as st
import pickle
import sklearn

pickle_in = open("pipe_log_reg.pkl","rb")
pipe=pickle.load(pickle_in)

def welcome():
    return "Welcome All"
    

def predict_emotion(message):
    
    """Let's classify the messages 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: message
        in: query
        type: text
        required: true
    response:
        200:
            description: The output value
        
    """
   
    prediction=pipe.predict([message])
    return prediction

def main():
    emotions_dict = {'anger':'💢','fear':'😱','joy':'😀','love':'😍','sadness':'😥','surprise':'😮'}
    st.title("Emotion Classification with NLP ✒️")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Emotion Classifier - ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    text = st.empty()
    message = text.text_area("Message","")
    result=""
    if st.button("Predict"):
        result= "We felt " + predict_emotion(message)[0] + " in your message "
        result += emotions_dict[predict_emotion(message)[0]]
    st.success('Emotion : {}'.format(result))
    if st.button("About"):
        st.text("NLP Web app 📝")
        st.text("Built with Streamlit by Samy Ayed.")

if __name__=='__main__':
    main()