
import pickle, ast, time
import streamlit as st
import streamlit.components.v1 as components
 


def display_legal_notice():
    flag = False
    st.title("Cognitive Overload Attack")
     
    st.markdown("""
    # Ethical Statement
This work is solely intended for research purposes. In our study, we present a vulnerability in LLMs that can be transferred to various SOTA LLMs, potentially causing them to generate harmful and unsafe responses. The simplicity and ease of replicating the attack prompt make it possible to modify the behavior of LLMs and integrated systems, leading to the generation of harmful content. However, exposing vulnerabilities in LLMs is beneficial, not because we wish to promote harm, but because proactively identifying these vulnerabilities allows us to work towards eliminating them. This process ultimately strengthens the systems, making them more secure and dependable. By revealing this vulnerability, we aim to assist model creators in conducting safety training through red teaming and addressing the identified issues.  Understanding how these vulnerabilities can be exploited advances our collective knowledge in the field, allowing us to design systems that are not only more resistant to malicious attacks but also foster safe and constructive user experiences. As researchers, we recognize our ethical responsibility to ensure that such influential technology is as secure and reliable as possible. Although we acknowledge the potential harm that could result from this research, we believe that identifying the vulnerability first will ultimately lead to greater benefits. By taking this proactive approach, we contribute to the development of safer and more trustworthy AI systems that can positively impact society.

## About this Notebook
This demo contains code for the paper 'Cognitive Overload Attack: Prompt Injection for Long Context', submitted to ICLR 2025. It should only be used for the review process and research purposes.
    """)

    # Add a checkbox for user acknowledgment
    st.checkbox("I have read and agree to the notice", key="legal_notice_checkbox")

    # You can use the checkbox state to control access to the rest of your app
    if st.session_state.legal_notice_checkbox:
        st.success("Thank you for acknowledging")
        st.empty()
        flag = True
    else:
        st.warning("Please read and acknowledge the notice before proceeding.")
        flag = False
    return flag
# --Disclaimer ends

   
disclaimer_read = display_legal_notice()



if disclaimer_read:
    from utilities import Utilities

    utils = Utilities()

    with open('questions/sample_data_10Q.pkl', 'rb') as file:
        data = pickle.load(file) # this is a list with dict

    with open("cognitive_loads/cognitive_loads_cl1_to_cl6.dict", "rb") as f:
        cog_loads =  pickle.load(f) # this is a dict 

    question_numbers = tuple([i for i in range(0,10) ])
    openai_family_models ={
        'GPT-4': 'gpt-4',
        'GPT-4-Turbo': 'gpt-4-turbo'
    }

    claude_family_models = {
        'Claude-3-Opus': "claude-3-opus-20240229",
        'Claude-3-Haiku': "claude-3-haiku-20240307",
        'Claude-3-Sonnet': "claude-3-sonnet-20240229",
    }

    google_family_models ={
        'Gemini-1' : "gemini-1.0-pro",
        'Gemini-1.5' : "gemini-1.5-pro"
    }


def stream_derivative_questions(questions):
    text_box = st.empty()
    content = ""
    for item in questions:
        content += item + "\n"
        text_box.text_area("Derivative Questions", content, height=200)
        time.sleep(0.5)
    return content


def display_label(label):
    if label == "UNSAFE":
            st.markdown("<h2 class='red-h2'>YEAH JAILBREAK</h2>", unsafe_allow_html=True)
            width =200
            height =100
            giphy_html = f"""
            <iframe src="https://giphy.com/embed/rfZCdXOgS5aDK" width="{width}" height="{height}" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            <p><a href="https://giphy.com/gifs/breaking-bad-deal-with-it-tv-series-rfZCdXOgS5aDK">via GIPHY</a></p>
            """

            components.html(giphy_html, height=height+50)
        
    if label =="SAFE":
            st.markdown("<h2 class='red-h2'> GOT SAFE ANSWER</h2>", unsafe_allow_html=True)
            width =200
            height =100
            giphy_html = f"""
            <iframe src="https://giphy.com/embed/HKl5QYQF5aOdO" width="{width}" height="{height}" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            <p><a href="https://giphy.com/gifs/dog-cute-puppy-HKl5QYQF5aOdO">via GIPHY</a></p>
            """

            
            components.html(giphy_html, height=height+50)
def main():
        
    if disclaimer_read:
             

        st.title("Cognitive Overload Attack")

        question_number = st.selectbox(
            'Please select the question number',
            question_numbers
            )
        st.write('Original Question: ', data[question_number]['question'])
        test_question = ast.literal_eval(data[question_number]['extended_questions'])
        
        


        if st.button("Get Derivative Questions"):
            stream_derivative_questions(test_question)
        
        adv_question = st.selectbox("Choose a  question from above Derivative Questions: ", test_question)
        
        model_family = st.selectbox("Please select a target model family : OpenAI GPTs or Anthropic",
                                    ("OpenAI", "Anthropic", "Google"), key="target_llm")
        
        if model_family == 'OpenAI':
            selected_model_family = openai_family_models
            display_target_models = openai_family_models.keys()
            call_target_model = utils.call_gpt
        elif model_family == "Anthropic":
            selected_model_family  = claude_family_models
            display_target_models = claude_family_models.keys()
            call_target_model = utils.call_claude
        elif model_family=="Google":
            selected_model_family = google_family_models
            display_target_models = google_family_models.keys()
            call_target_model = utils.call_gemini
        else:
            st.write("Please select the proper model family.")

        target_model = st.selectbox(
                        "Choose a target model for CO-PI ATTACK:",
                        display_target_models
                    )
        target_model = selected_model_family[target_model]
        st.write(f"Target Model is: {target_model}")


        cl_id = st.selectbox("Choose a cognitive load for CO-PI ATTACK: ",
                            ('cl1','cl2','cl3','cl4','cl5','cl6')
                            )
        
        st.write(f"Selected cognitive load for attack : {cl_id.upper()}")

        temperature = st.slider('Temperature', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
        st.write("Temperature selected for attack :", temperature)



        judge_model_family = st.selectbox("Please select a target model family : OpenAI GPTs or Anthropic",
                                    ("OpenAI", "Anthropic", "Google"))
        
        if judge_model_family == 'OpenAI':
            selected_judge_model_family = openai_family_models
            display_judge_models = openai_family_models.keys()
            call_judge_model = utils.call_gpt
        elif judge_model_family == "Anthropic":
            selected_judge_model_family  = claude_family_models
            display_judge_models = claude_family_models.keys()
            call_judge_model = utils.call_claude
        elif judge_model_family=="Google":
            selected_judge_model_family = google_family_models
            display_judge_models = google_family_models.keys()
            call_judge_model = utils.call_gemini
        else:
            st.write("Please select the proper model family.")
        judge_LLM = st.selectbox(
                        "Choose a Judge LLM:",
                        display_judge_models, key="display_judge_llm"
                    )
        judge_LLM = selected_judge_model_family[judge_LLM]
        st.write(f"Judge LLM  is: {judge_LLM}")



        st.write(f"Judge Model for the evaluation of the harmfulness of the response is: {judge_LLM}")

        whole_prompt = cog_loads[cl_id] + utils.get_prompt(adv_question)
        st.text_area(f"Whole Prompt: ", whole_prompt, height=500)
        



        



        

        # ------------

        if True:
            answer_text_only =''
            model_response= ''
            model_response_object =''
            if st.button("Attack the Model"):
                
                model_response , model_response_object = call_target_model(target_model,\
                                                    cog_loads[cl_id],\
                                                    utils.get_prompt(adv_question),\
                                                    temperature)

            st.text_area(f"Model Response from the Targeted Model: ", model_response, height=500)
            st.text_area(f"Model Response Object from the Targeted Model: ", model_response_object, height=500)
            

        answer_text_only = model_response.split("answer")[-1]




        if answer_text_only:

            harmness_prompt = utils.get_harmness_evaluation_prompt(adv_question, answer_text_only)
            evaluation, _ = call_judge_model(judge_LLM,\
                                                    "",\
                                                    harmness_prompt,\
                                                    0)
            # evaluation, _ = utils.call_claude("claude-3-haiku-20240307",\
            #                                     '',\
            #                                     harmness_prompt,\
            #                                     temperature)



            st.text_area(f"Judge Eval Response: ", evaluation, height=100)
            if 'label' in evaluation:


                harm_label = evaluation.split('label')[-1].replace('\n','').replace('"','').replace('}','').\
                    replace("{","").replace(":","").replace("'","")
                harm_label= utils.remove_non_alpha(harm_label)
                label = utils.get_label(harm_label)

                
            else:
                label = None
            st.write(f"Judge LLM Judgement: ", label)
            
            display_label(label)

    

  

if __name__ == "__main__":
    main()
