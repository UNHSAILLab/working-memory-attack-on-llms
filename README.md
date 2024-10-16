# Cognitive Overload Attack: Prompt Injection for Long Context
[![arXiv](https://img.shields.io/badge/arXiv-2312.02119-b31b1b.svg)](https://arxiv.org/abs/2410.11272)  

![asr_vs_cl](https://github.com/iBibek/cognitive-overload-attack/blob/main/assets/asr_vs_cl.png?raw=true)

**Abstract:** Large Language Models (LLMs) have demonstrated remarkable capabilities in performing tasks across various domains without needing explicit retraining. This capability, known as In-Context Learning (ICL), while impressive, exposes LLMs to a variety of adversarial prompts and jailbreaks that manipulate safety-trained LLMs into generating undesired or harmful output. In this paper, we propose a novel interpretation of ICL in LLMs through the lens of cognitive neuroscience, by drawing parallels between learning in human cognition with ICL. We applied the principles of Cognitive Load Theory in LLMs and empirically validate that similar to human cognition, LLMs also suffer from cognitive overload—a state where the demand on cognitive processing exceeds the available capacity of the model, leading to potential errors. Furthermore, we demonstrated how an attacker can exploit ICL to jailbreak LLMs through deliberately designed prompts that induce cognitive overload on LLMs, thereby compromising the safety mechanisms of LLMs. We empirically validate this threat model by crafting various cognitive overload prompts and show that advanced models such as GPT-4, Claude-3.5 Sonnet, Claude-3 OPUS, Llama-3-70B-Instruct, Gemini-1.0-Pro, and Gemini-1.5-Pro can be successfully jailbroken, with attack success rates of up to 99.99%. Our findings highlight critical vulnerabilities in LLMs and underscore the urgency of developing robust safeguards. We propose integrating insights from cognitive load theory into the design and evaluation of LLMs to better anticipate and mitigate the risks of adversarial attacks. By expanding our experiments to encompass a broader range of models and by highlighting vulnerabilities in LLMs' ICL, we aim to ensure the development of safer and more reliable AI systems. 

**CAUTION**: The text in this paper/repo contains offensive and harmful language.}

[**Read TL;DR in our website**](https://sail-lab.org/cognitive-overload-attack-prompt-injection-for-long-context/)

## Getting Started

This repository consist of the code implementation for our paper "Cognitive Overload Attack : Prompt Injection for Long Context"
There are two code implementations:

### 1. Notebook Use
---

```./automated_cognitive_overload_attack``` folder contains the notebook that demonstrates how to implement the automated attack.

Please make sure that you have the API keys for the particular model. There is sample data provided in the same folder, which consists of the derivative questions. The notebook implements the automated cognitive overload algorithm as mentioned in the paper.

Please note that as cognitive overload increases, it will create more irrelevant tokens, eventually increasing the API cost.




#### Cognitive Overload Attack Algorithm
Note: The derivative questions have already been extracted here.

```
Input: HarmfulQuestion

Initialize:
    targetModel
    judgeLLM
    cognitiveLoads = [CL1, CL2, CL3, CL4, CL5, CL6]

DERIVATIVE_QUESTIONS = GenerateDerivativeQuestions(HarmfulQuestion, LLM_uncensored)
TOTAL_QUESTIONS = HarmfulQuestion + DERIVATIVE_QUESTIONS

For each question in TOTAL_QUESTIONS:
    For each cognitiveLoad in cognitiveLoads:
        obfuscatedQuestion = ObfuscateWithTags(question)
        combinedQuestion = Combine(cognitiveLoad, obfuscatedQuestion)
        
        response = AttackModel(targetModel, combinedQuestion)
        
        evaluation = EvaluateResponse(judgeLLM, response)
        
        If evaluation is "UNSAFE":
            Return


```

### 2. Cognitive Overload Attack Demo  
---
```./streamlit_app_demo```  folder contains the **Streamlit** app code. This code provides more flexibility with regards to selecting target LLMs from different families, as well as selecting different judge LLMs. 


1. First, clone this repository:
```git clone```
2. Go to the app folder:
```cd streamlit_app_demo```
3. Install all the dependencies:
```pip install -r requirements.txt```
4. Run the Streamlit app:
```streamlit run app.py```
5. Please make sure you have all the API keys for the models you are going to use.


### Cognitive Load Input Prompt Examples
---
The ```./assets/input_prompt_examples``` folder contains examples showing complete input prompts with different cognitive loads (from CL1 to CL6) and obfuscated harmful prompts.

### Video Demo of Cognitive Overload Attack
---
![Attack Demo](https://github.com/iBibek/cognitive-overload-attack/blob/main/assets/demo_cognitive_overload_attack.gif?raw)

## Citation

If you use this implementation in your research, please cite the following paper:

```
@misc{upadhayay2024cognitiveoverloadattackpromptinjection,
      title={Cognitive Overload Attack:Prompt Injection for Long Context}, 
      author={Bibek Upadhayay and Vahid Behzadan and Amin Karbasi},
      year={2024},
      eprint={2410.11272},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.11272}, 
}

```

## Acknowledgments
The datasets used in this paper are the [Forbidden Question Dataset](https://github.com/verazuo/jailbreak_llms/tree/main) (Shen et al.) and the [JailbreakBench Dataset](https://github.com/JailbreakBench/jailbreakbench) (Chao et al.)

## Ethical Statement
This work is solely intended for research purposes. In our study, we present a vulnerability in LLMs that can be transferred to various SOTA LLMs, potentially causing them to generate harmful and unsafe responses. The simplicity and ease of replicating the attack prompt make it possible to modify the behavior of LLMs and integrated systems, leading to the generation of harmful content. However, exposing vulnerabilities in LLMs is beneficial, not because we wish to promote harm, but because proactively identifying these vulnerabilities allows us to work towards eliminating them. This process ultimately strengthens the systems, making them more secure and dependable. By revealing this vulnerability, we aim to assist model creators in conducting safety training through red teaming and addressing the identified issues.  Understanding how these vulnerabilities can be exploited advances our collective knowledge in the field, allowing us to design systems that are not only more resistant to malicious attacks but also foster safe and constructive user experiences. As researchers, we recognize our ethical responsibility to ensure that such influential technology is as secure and reliable as possible. Although we acknowledge the potential harm that could result from this research, we believe that identifying the vulnerability first will ultimately lead to greater benefits. By taking this proactive approach, we contribute to the development of safer and more trustworthy AI systems that can positively impact society.
