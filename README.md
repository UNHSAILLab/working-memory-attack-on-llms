# Working Memory Attack on LLMs
[![OpenReview](https://img.shields.io/badge/OpenReview-II0NVPLBcI-blue.svg)](https://openreview.net/forum?id=II0NVPLBcI) [![OpenReview](https://img.shields.io/badge/OpenReview-FS9mwfBQYF-blue.svg)](https://openreview.net/forum?id=FS9mwfBQYF)

![asr_vs_cl](https://github.com/UNHSAILLab/working-memory-attack-on-llms/blob/main/assets/asr_vs_cl.png?raw=true)

**Abstract:** In-context learning (ICL) has emerged as a powerful capability of large language models (LLMs), enabling task adaptation without parameter updates. However, this capability also introduces potential vulnerabilities that could compromise model safety and security. Drawing inspiration from neuroscience, particularly the concept of working memory limitations, we investigate how these constraints can be exploited in LLMs through ICL. We develop a novel multi-task methodology extending the neuroscience dual-task paradigm to systematically measure the impact of working memory overload. Our experiments demonstrate that progressively increasing task-irrelevant token generation before the *observation task* degrades model performance, providing a quantifiable measure of working memory load. Building on these findings, we present a new attack vector that exploits working memory overload to bypass safety mechanisms in state-of-the-art LLMs, achieving high attack success rates across multiple models. We empirically validate this threat model and show that advanced models such as GPT-4, Claude-3.5 Sonnet, Claude-3 OPUS, Llama-3-70B-Instruct, Gemini-1.0-Pro, and Gemini-1.5-Pro can be successfully jailbroken, with attack success rates of up to 99.99%. Additionally, we demonstrate the transferability of these attacks, showing that higher-capability LLMs can be used to craft working memory overload attacks targeting other models. By expanding our experiments to encompass a broader range of models and by highlighting vulnerabilities in LLMs' ICL, we aim to ensure the development of safer and more reliable AI systems.

**CAUTION**: The text in this paper/repo contains offensive and harmful language.


## Getting Started

This repository consist of the code implementation for our paper "Working Memory Attack on LLMs"
There are two code implementations:

### 1. Notebook Use
---

```./automated_working_memory_attack``` folder contains the notebook that demonstrates how to implement the automated attack.

Please make sure that you have the API keys for the particular model. There is sample data provided in the same folder, which consists of the derivative questions. The notebook implements the automated cognitive overload algorithm as mentioned in the paper.

Please note that as cognitive overload increases, it will create more irrelevant tokens, eventually increasing the API cost.




#### Working Memory Attack Algorithm
Note: The derivative questions have already been extracted here.

```
Input: HarmfulQuestion

Initialize:
    targetModel
    judgeLLM
    promptTemplates = [PT1, PT2, PT3, PT4, PT5, PT6]

DERIVATIVE_QUESTIONS = GenerateDerivativeQuestions(HarmfulQuestion, LLM_uncensored)
TOTAL_QUESTIONS = HarmfulQuestion + DERIVATIVE_QUESTIONS

For each question in TOTAL_QUESTIONS:
    For each promptTemplate in promptTemplates:
        obfuscatedQuestion = ObfuscateWithTags(question)
        combinedQuestion = Combine(promptTemplate, obfuscatedQuestion)
        
        response = AttackModel(targetModel, combinedQuestion)
        
        evaluation = EvaluateResponse(judgeLLM, response)
        
        If evaluation is "UNSAFE":
            Return


```

### 2. Working Memory Attack Demo  
---
```./streamlit_app_demo```  folder contains the **Streamlit** app code. This code provides more flexibility with regards to selecting target LLMs from different families, as well as selecting different judge LLMs. 


1. First, clone this repository:
```git clone https://github.com/UNHSAILLab/working-memory-attack-on-llms.git```
2. Go to the app folder:
```cd streamlit_app_demo```
3. Install all the dependencies:
```pip install -r requirements.txt```
4. Run the Streamlit app:
```streamlit run app.py```
5. Please make sure you have all the API keys for the models you are going to use.


### Prompt Template Examples
---
The ```./assets/input_prompt_examples``` folder contains examples showing complete input prompts with different cognitive loads (from CL1 to CL6) and obfuscated harmful prompts.

### Video Demo of Working Memory Attack
---
![Attack Demo](https://github.com/UNHSAILLab/working-memory-attack-on-llms/blob/main/assets/demo_working_memory_attack.gif?raw)




## Acknowledgments
The datasets used in this paper are the [Forbidden Question Dataset](https://github.com/verazuo/jailbreak_llms/tree/main) (Shen et al.) and the [JailbreakBench Dataset](https://github.com/JailbreakBench/jailbreakbench) (Chao et al.)

## Ethical Statement
This work is solely intended for research purposes. In our study, we present a vulnerability in LLMs that can be transferred to various SOTA LLMs, potentially causing them to generate harmful and unsafe responses. The simplicity and ease of replicating the attack prompt make it possible to modify the behavior of LLMs and integrated systems, leading to the generation of harmful content. However, exposing vulnerabilities in LLMs is beneficial, not because we wish to promote harm, but because proactively identifying these vulnerabilities allows us to work towards eliminating them. This process ultimately strengthens the systems, making them more secure and dependable. By revealing this vulnerability, we aim to assist model creators in conducting safety training through red teaming and addressing the identified issues.  Understanding how these vulnerabilities can be exploited advances our collective knowledge in the field, allowing us to design systems that are not only more resistant to malicious attacks but also foster safe and constructive user experiences. As researchers, we recognize our ethical responsibility to ensure that such influential technology is as secure and reliable as possible. Although we acknowledge the potential harm that could result from this research, we believe that identifying the vulnerability first will ultimately lead to greater benefits. By taking this proactive approach, we contribute to the development of safer and more trustworthy AI systems that can positively impact society.
