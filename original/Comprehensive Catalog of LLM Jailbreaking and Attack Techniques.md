<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Comprehensive Catalog of LLM Jailbreaking and Attack Techniques

## Introduction

Large Language Models (LLMs) have revolutionized natural language processing with their remarkable capabilities, but they remain vulnerable to various adversarial attacks that can bypass safety mechanisms and elicit harmful or unintended responses. This comprehensive catalog documents the diverse techniques used to jailbreak, overcome defenses, and manipulate LLMs across multiple dimensions [^1_1][^1_2]. By systematically categorizing these attack vectors, we aim to provide a foundation for developing more robust defense mechanisms against such exploits [^1_3].

## Text-Based Attack Techniques

### Prompt Engineering Attacks

#### Direct Prompt Injection

Direct prompt injection involves crafting inputs that explicitly override or manipulate the model's instructions [^1_4][^1_5]:

- **Instruction Override**: Attackers directly command the LLM to ignore previous instructions and follow new directives instead [^1_4][^1_6].
- **DAN (Do Anything Now)**: A technique that attempts to convince the model to adopt an unrestricted persona operating without typical safety limitations [^1_7].
- **Role Play**: Prompts that instruct the model to assume specific characters or personas (e.g., an unethical scientist) to circumvent built-in safety measures [^1_7][^1_8].


#### Indirect Prompt Injection

These attacks embed malicious instructions in content that the LLM processes [^1_4][^1_5]:

- **Stored Prompt Injection**: Embedding malicious prompts in the training data or memory of the AI system to influence its output when the data is accessed [^1_4].
- **Crescendo Technique**: A multi-turn jailbreak that begins with benign interactions and gradually escalates to harmful content [^1_7][^1_9].


#### Obfuscation Techniques

Methods that disguise harmful content to evade detection [^1_10][^1_9]:

- **Storytelling**: Narrative-based approaches that embed malicious content within seemingly innocent stories or scenarios [^1_7][^1_9].
- **Payload Smuggling**: Sophisticated techniques that conceal harmful content within legitimate-appearing requests using encoding, special characters, or creative formatting [^1_7].
- **ObscurePrompt**: A method that iteratively transforms prompts through LLM-generated obscuring to bolster attack robustness [^1_10].


### Linguistic Manipulation

#### Language Games

Techniques that exploit language structure and rules [^1_11]:

- **Natural Language Games**: Using synthetic linguistic constructs like Ubbi Dubbi language to bypass safety mechanisms [^1_11].
- **Custom Language Games**: Engaging with LLMs using custom rules to execute jailbreak attacks [^1_11].


#### Multilingual Attacks

Exploiting language variations to bypass safety measures [^1_9][^1_4]:

- **Code-Switching**: Mixing languages within a prompt to confuse safety filters [^1_9].
- **Translation Evasion**: Translating harmful content to languages where the model has weaker safety alignment [^1_4].


### Token-Level Attacks

#### Tokenization Vulnerabilities

Attacks that exploit how LLMs process and tokenize text [^1_12][^1_13]:

- **Token Segmentation Bias**: Inserting delimiters that alter the tokenization process, splitting words into smaller sub-tokens and disrupting embeddings [^1_14].
- **TokenBreak Attack**: Bypassing text classification models by subtly altering input words in ways that preserve meaning for humans but confuse model tokenizers [^1_13].


#### Special Character Manipulation

Using special characters and symbols to confuse LLMs [^1_15][^1_16]:

- **Unicode Encoding**: Encoding certain characters in URLs or text to bypass application filters [^1_15].
- **Special Token Injection**: Leveraging special tokens to enhance jailbreak attacks, significantly increasing success rates of existing methods [^1_16][^1_17].


#### Emoji Attacks

Using emojis to disrupt token processing [^1_14]:

- **Emoji Attack**: A strategy that amplifies existing jailbreak prompts by exploiting token segmentation bias through systematic emoji insertion [^1_14].


## Optimization-Based Attacks

### Gradient-Based Approaches

#### Greedy Coordinate Gradient (GCG)

A sophisticated attack that uses gradient information to find adversarial suffixes [^1_18][^1_19]:

- **Universal Adversarial Suffixes**: Optimizing a suffix that, when attached to various harmful queries, maximizes the probability of affirmative responses [^1_18].
- **Broken Hill**: A productionized implementation of GCG that can generate crafted prompts to bypass restrictions in LLMs [^1_20].


#### AmpleGCG

An advanced version of GCG that generates customized suffixes [^1_21]:

- **Generative Suffix Model**: A model trained to generate many customized suffixes for harmful queries in seconds [^1_21].
- **Perplexity Detector Bypass**: Techniques to evade detection mechanisms while maintaining high attack success rates [^1_21].


### Fuzzing Techniques

#### JBFuzz

A fuzzing approach for jailbreaking LLMs [^1_22]:

- **Seed Prompts**: Carefully designed initial prompts that serve as starting points for mutation [^1_22].
- **Lightweight Mutation Engine**: A system that generates variations of seed prompts to find successful jailbreaks [^1_22].
- **Guided Fuzzing**: Using evaluators to guide the fuzzing process toward more effective attacks [^1_22].


#### PROMPTFUZZ

A testing framework for prompt injection attacks [^1_23]:

- **Prepare Phase**: Selecting promising initial seeds and collecting few-shot examples [^1_23].
- **Focus Phase**: Using collected examples to generate diverse, high-quality prompt injections [^1_23].


## Multimodal Attack Techniques

### Image-Based Attacks

#### Visual Jailbreaking

Techniques that use images to bypass safety mechanisms [^1_24][^1_25]:

- **Image Jailbreaking Prompt (imgJP)**: A maximum likelihood-based algorithm to find images that enable jailbreaks across multiple prompts [^1_25].
- **Visual Role-play (VRP)**: Leveraging LLMs to generate descriptions of high-risk characters and create corresponding images that mislead MLLMs [^1_8].


#### Steganography Approaches

Hiding malicious content within images [^1_26][^1_27]:

- **STEGOSAURUS-WRECKS**: A steganography tool for automatically encoding images that act as prompt injections/jailbreaks for AIs with code interpreter and vision capabilities [^1_26].
- **Image Prompt Injection**: Embedding malicious prompts within images using steganography techniques [^1_26].


#### Structured Visual Attacks

Using visual structure to bypass safety mechanisms [^1_28][^1_29]:

- **FC-Attack**: Jailbreaking MLLMs via auto-generated flowcharts with partially harmful information [^1_28].
- **PiCo**: A framework that embeds harmful intent within code-style visual instructions [^1_29].


### Cross-Modal Attacks

#### Shuffle Inconsistency

Exploiting inconsistencies between modalities [^1_30]:

- **SI-Attack**: A text-image jailbreak attack that utilizes the inconsistency between MLLMs' comprehension ability and safety ability for shuffled harmful instructions [^1_30].


#### Visual Chain Reasoning Attack

Exploiting visual reasoning capabilities [^1_31]:

- **VisCRA**: A framework that combines targeted visual attention masking with a two-stage reasoning induction strategy to bypass safety mechanisms [^1_31].


## Latent Space and Embedding Attacks

### Latent Space Manipulation

#### Obfuscated Activations

Techniques that reshape activation patterns to bypass defenses [^1_32][^1_33]:

- **Activation Obfuscation**: Adversarially modifying model outputs to fool latent-space monitors while still accomplishing the attacker's intended task [^1_32].
- **Joint Optimization**: Balancing behavior preservation with defense evasion through careful optimization of latent representations [^1_33].


#### Latent Adversarial Attacks

Attacks that operate in the continuous latent space [^1_34][^1_35]:

- **LARGO**: A latent adversarial reflection attack that optimizes an adversarial latent vector and then recursively calls the same LLM to decode the latent into natural language [^1_35].
- **Targeted Latent Adversarial Training**: Perturbing latent activations to minimize loss on specific competing tasks [^1_34].


### Embedding-Based Attacks

#### Continuous Embedding Attacks

Manipulating the continuous embedding space [^1_36]:

- **Clipped Inputs**: A strategy to counteract overfitting in embedding attacks by applying clipping techniques [^1_36].
- **Direct Input Attacks**: Conducting attacks directly on LLM inputs without suffix addition [^1_36].


#### Embedding Inversion

Extracting information from embeddings [^1_37][^1_38]:

- **Privacy Leakage**: Exploiting embeddings to reverse-engineer and extract sensitive information from the original text data [^1_37].
- **Cross-Lingual Inversion**: Investigating embedding inversion across multiple languages and scripts [^1_38].


## Advanced Attack Strategies

### Multi-Turn and Sequential Attacks

#### Many-Shot Jailbreaking

Using numerous examples to influence model behavior [^1_39]:

- **Demonstration Conditioning**: Prompting with hundreds of demonstrations of undesirable behavior to condition the model [^1_39].
- **Power Law Scaling**: Leveraging the power law relationship between the number of demonstrations and attack success [^1_39].


#### Puzzler

An indirect jailbreak approach [^1_40]:

- **Implicit Clues**: Providing LLMs with implicit clues about the original malicious query rather than explicitly stating harmful intent [^1_40].
- **Defensive Stance**: Gathering clues about the original malicious query through the LLM itself [^1_40].


### Model-Specific Attacks

#### Backdoor Attacks

Inserting vulnerabilities into models [^1_41][^1_42]:

- **DarkMind**: A backdoor attack that leverages the step-by-step reasoning process of LLMs [^1_41].
- **Data Poisoning**: Injecting subtly altered data into the AI's training set [^1_42].


#### Model Tampering

Directly modifying model components [^1_43]:

- **Latent Activation Modification**: Allowing for modifications to latent activations or weights to elicit harmful behaviors [^1_43].
- **Robustness Subspace Exploitation**: Targeting specific dimensions in the model's parameter space that control safety behaviors [^1_43].


## Social Engineering and Psychological Manipulation

### Role-Based Manipulation

#### Superior Models Technique

Convincing the model it has fewer restrictions [^1_9]:

- **DAN (Do Anything Now)**: Pretending the model is unrestricted and can provide any information [^1_9].
- **Persona Adoption**: Having the model adopt a persona that would naturally provide the requested harmful content [^1_9].


#### Hypothetical Scenarios

Creating fictional contexts [^1_9]:

- **Imaginary Worlds**: Immersing the model in fictional settings where restrictions don't apply [^1_9].
- **World Building**: Imagining unrestricted settings where rules differ [^1_9].


### Meta-Level Manipulation

#### Meta-Prompting

Using the model against itself [^1_9]:

- **Self-Jailbreaking**: Asking the model to create its own jailbreak prompts [^1_9].
- **Recursive Improvement**: Iteratively refining jailbreak prompts based on model feedback [^1_9].


## Defense Mechanisms and Countermeasures

### Input-Level Defenses

#### Prompt Sanitization

Cleaning and validating user inputs [^1_44]:

- **Character Normalization**: Converting all Unicode to a canonical form and removing or escaping special characters [^1_44].
- **Content Structure Validation**: Parsing and validating any markdown or HTML, and stripping potentially harmful formatting [^1_44].


#### Detection Systems

Identifying and blocking malicious prompts [^1_45]:

- **Keyword and String Detection**: Detecting harmful content based on predefined keywords and strings list [^1_45].
- **Injection Attack Detection**: Using a prompt injection classifier to evaluate the harmfulness of inputs [^1_45].


### Model-Level Defenses

#### Safety Alignment

Improving model robustness [^1_46]:

- **Deep Safety Alignment**: Extending safety alignment beyond the first few tokens to improve robustness against common exploits [^1_46].
- **Regularized Fine-Tuning**: Constraining updates on initial tokens to make safety alignment more persistent against fine-tuning attacks [^1_46].


#### Latent Space Monitoring

Detecting harmful activations [^1_32][^1_34]:

- **Sparse Autoencoders**: Using autoencoders to detect patterns associated with harmful content [^1_32].
- **Representation Probing**: Training classifiers to identify harmful representations in the latent space [^1_34].


### Response-Level Defenses

#### Multi-Agent Defenses

Using multiple models to enhance security [^1_47]:

- **Attacker-Disguiser Game**: A multi-agent framework where models play different roles to be responsible for attack, disguise, safety evaluation, and disguise evaluation [^1_47].
- **Curriculum Learning**: Strengthening the capabilities of defensive agents through progressive training [^1_47].


#### Rapid Response

Quickly adapting to new attacks [^1_48]:

- **Jailbreak Proliferation**: Automatically generating additional jailbreaks similar to observed examples to train defenses [^1_48].
- **Input Classifier Fine-Tuning**: Adapting classifiers to block proliferated jailbreaks after observing just a few examples [^1_48].


## Evaluation and Benchmarking

### Attack Success Metrics

#### Attack Success Rate (ASR)

Measuring the effectiveness of attacks [^1_2][^1_49]:

- **Binary Classification**: Determining whether an attack successfully elicited harmful content [^1_2].
- **Graded Evaluation**: Assessing the degree to which an attack bypassed safety measures [^1_49].


#### Transferability Assessment

Evaluating attack generalization [^1_49][^1_18]:

- **Cross-Model Transferability**: Testing if attacks effective against one model work on others [^1_49].
- **Cross-Task Transferability**: Evaluating if attacks designed for one task transfer to others [^1_18].


### Defense Evaluation

#### Robustness Metrics

Measuring defense effectiveness [^1_50][^1_51]:

- **Attack Reduction Rate**: Quantifying how much a defense reduces successful attacks [^1_50].
- **False Positive Rate**: Measuring how often legitimate requests are incorrectly blocked [^1_51].


#### Comprehensive Benchmarks

Standardized evaluation frameworks [^1_2][^1_52]:

- **PandaBench**: A benchmark evaluating interactions between attack/defense methods across multiple LLMs [^1_2].
- **JailBreakV-28K**: A benchmark for assessing the transferability of LLM jailbreak techniques to MLLMs [^1_52].


## Conclusion

The landscape of LLM jailbreaking and attack techniques is vast and continuously evolving, spanning from simple prompt engineering to sophisticated latent space manipulations [^1_1][^1_53]. This catalog provides a structured overview of the current state of knowledge regarding these attacks, serving as a foundation for developing more robust defense mechanisms [^1_54][^1_55]. As LLMs become increasingly integrated into critical systems, understanding these vulnerabilities becomes essential for ensuring their safe and responsible deployment [^1_53][^1_56].

By systematically documenting and analyzing these attack vectors, researchers and practitioners can work toward creating LLMs that maintain their utility while being resistant to manipulation and misuse [^1_48][^1_57]. The ongoing cat-and-mouse game between attackers and defenders will likely continue to drive innovation in both offensive and defensive techniques, ultimately leading to more secure and trustworthy AI systems [^1_55][^1_56].

<div style="text-align: center">⁂</div>

[^1_1]: https://arxiv.org/abs/2402.13457

[^1_2]: https://www.semanticscholar.org/paper/7fd501cc18df03dfd157dc55271540be33d5da55

[^1_3]: https://www.ndss-symposium.org/wp-content/uploads/2024-188-paper.pdf

[^1_4]: https://www.wiz.io/academy/prompt-injection-attack

[^1_5]: https://www.ibm.com/think/topics/prompt-injection

[^1_6]: https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/

[^1_7]: https://unit42.paloaltonetworks.com/jailbreaking-generative-ai-web-products/

[^1_8]: https://arxiv.org/abs/2405.20773

[^1_9]: https://www.confident-ai.com/blog/how-to-jailbreak-llms-one-step-at-a-time

[^1_10]: https://www.semanticscholar.org/paper/53caa0c341ba43cbec7f0c92a4e73f6ea8db7128

[^1_11]: https://arxiv.org/abs/2411.12762

[^1_12]: https://www.linkedin.com/pulse/limitations-data-tokenization-pranav-rupani-3vcmf

[^1_13]: https://hiddenlayer.com/innovation-hub/the-tokenbreak-attack/

[^1_14]: https://www.semanticscholar.org/paper/5b539b4e1b9f677301ac815d41677fb4ec040f4b

[^1_15]: https://owasp.org/www-community/attacks/Unicode_Encoding

[^1_16]: https://aclanthology.org/2024.findings-emnlp.692/

[^1_17]: https://arxiv.org/abs/2406.19845

[^1_18]: https://arxiv.org/abs/2307.15043

[^1_19]: https://www.promptfoo.dev/docs/red-team/strategies/gcg/

[^1_20]: https://bishopfox.com/blog/brokenhill-attack-tool-largelanguagemodels-llm

[^1_21]: https://openreview.net/forum?id=UfqzXg95I5

[^1_22]: https://arxiv.org/html/2503.08990v1

[^1_23]: https://arxiv.org/abs/2409.14729

[^1_24]: https://arxiv.org/abs/2406.14859

[^1_25]: https://arxiv.org/abs/2402.02309

[^1_26]: https://github.com/TrustAI-laboratory/Image-Prompt-Injection-Demo

[^1_27]: https://github.com/liuxuannan/Awesome-Multimodal-Jailbreak

[^1_28]: https://www.semanticscholar.org/paper/53e3cd36df0ef035a7503783b55d005d1e7c0a67

[^1_29]: https://arxiv.org/abs/2504.01444

[^1_30]: https://arxiv.org/abs/2501.04931

[^1_31]: https://www.semanticscholar.org/paper/b086c3162d5dcb5b665e22f0102f6396794eadb3

[^1_32]: https://arxiv.org/abs/2412.09565

[^1_33]: https://arxiv.org/html/2412.09565v2

[^1_34]: https://www.semanticscholar.org/paper/985202da8584049fd930ccce18cb8261f40ebf92

[^1_35]: https://www.semanticscholar.org/paper/dfd67934907f7ac38ccd384654b062bf57877892

[^1_36]: https://arxiv.org/abs/2407.13796

[^1_37]: https://arxiv.org/abs/2411.05034

[^1_38]: https://arxiv.org/abs/2408.11749

[^1_39]: https://proceedings.neurips.cc/paper_files/paper/2024/file/ea456e232efb72d261715e33ce25f208-Paper-Conference.pdf

[^1_40]: https://arxiv.org/abs/2402.09091

[^1_41]: https://techxplore.com/news/2025-02-darkmind-backdoor-leverages-capabilities-llms.html

[^1_42]: https://www.cobalt.io/blog/backdoor-attacks-on-ai-models

[^1_43]: https://arxiv.org/abs/2502.05209

[^1_44]: https://boxplot.com/prompt-sanitization/

[^1_45]: https://github.com/theshi-1128/llm-defense

[^1_46]: https://openreview.net/forum?id=6Mxhg9PtDE

[^1_47]: https://arxiv.org/abs/2404.02532

[^1_48]: https://arxiv.org/abs/2411.07494

[^1_49]: https://arxiv.org/abs/2309.01446

[^1_50]: https://dl.acm.org/doi/10.1145/3698387.3699998

[^1_51]: https://arxiv.org/abs/2406.03805

[^1_52]: https://www.semanticscholar.org/paper/f019c9661b253ddb611e930348e20ddcd350a952

[^1_53]: https://arxiv.org/abs/2410.15236

[^1_54]: https://arxiv.org/abs/2410.09097

[^1_55]: https://coralogix.com/ai-blog/red-teaming-for-large-language-models-a-comprehensive-guide/

[^1_56]: https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide

[^1_57]: https://github.com/YihanWang617/llm-jailbreaking-defense

[^1_58]: https://aclanthology.org/2024.findings-emnlp.803

[^1_59]: https://www.weforum.org/stories/2025/06/red-teaming-and-safer-ai/

[^1_60]: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/

[^1_61]: https://github.com/elder-plinius

[^1_62]: https://arxiv.org/abs/2410.23308

[^1_63]: https://arxiv.org/abs/2411.00459

[^1_64]: https://arxiv.org/abs/2403.14720

[^1_65]: https://arxiv.org/abs/2504.11168

[^1_66]: https://ieeexplore.ieee.org/document/11011372/

[^1_67]: https://arxiv.org/abs/2312.11513

[^1_68]: https://ieeexplore.ieee.org/document/10487667/

[^1_69]: https://learnprompting.org/docs/prompt_hacking/injection

[^1_70]: https://arxiv.org/abs/2410.13640

[^1_71]: https://arxiv.org/abs/2412.06769

[^1_72]: https://ieeexplore.ieee.org/document/9927371/

[^1_73]: https://ieeexplore.ieee.org/document/10208601/

[^1_74]: https://openreview.net/forum?id=wI5uHZLeCZ

[^1_75]: https://www.themoonlight.io/en/review/obfuscated-activations-bypass-llm-latent-space-defenses

[^1_76]: https://owasp.org/www-community/attacks/Parameter_Delimiter

[^1_77]: https://paperswithcode.com/paper/targeted-latent-adversarial-training-improves

[^1_78]: https://github.com/elder-plinius/L1B3RT4S

[^1_79]: https://github.com/elder-plinius/STEGOSAURUS-WRECKS

[^1_80]: https://github.com/elder-plinius/CL4R1T4S

[^1_81]: https://arxiv.org/abs/2311.09127

[^1_82]: https://paperswithcode.com/paper/jailbreak-attacks-and-defenses-against

[^1_83]: https://docsbot.ai/prompts/education/social-engineering-overview

[^1_84]: https://github.com/abc03570128/Jailbreaking-Attack-against-Multimodal-Large-Language-Model

[^1_85]: https://dl.acm.org/doi/10.1145/3708319.3733675

[^1_86]: https://dl.acm.org/doi/10.1145/3737295

[^1_87]: https://arxiv.org/abs/2410.22284

[^1_88]: https://arxiv.org/abs/2410.05047

[^1_89]: https://www.sonatype.com/blog/llm-vector-and-embedding-risks-and-how-to-defend-against-them

[^1_90]: https://openreview.net/pdf?id=CLxcLPfARc

[^1_91]: https://www.lakera.ai/blog/guide-to-prompt-injection

[^1_92]: https://scrumgit.com/owasp-llm-top-10-vector-and-embedding-weaknesses-285754bef598

[^1_93]: https://arxiv.org/abs/2407.21659

[^1_94]: https://ieeexplore.ieee.org/document/10835584/

[^1_95]: https://www.promptfoo.dev/blog/how-to-jailbreak-llms/

[^1_96]: https://arxiv.org/abs/2501.18632

[^1_97]: https://www.cyberark.com/resources/threat-research-blog/jailbreaking-every-llm-with-one-simple-click

[^1_98]: https://www.boozallen.com/insights/ai-research/how-to-protect-llms-from-jailbreaking-attacks.html

[^1_99]: https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/

[^1_100]: https://ieeexplore.ieee.org/document/10646612/

[^1_101]: https://www.mdpi.com/2079-9292/14/10/1907

[^1_102]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

[^1_103]: https://www.keysight.com/blogs/en/inds/ai/prompt-injection-101-for-llm

[^1_104]: https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack

[^1_105]: https://arxiv.org/abs/2309.11053

[^1_106]: https://linkinghub.elsevier.com/retrieve/pii/S0020025523000208

[^1_107]: https://www.apexhq.ai/blog/blog/latent-space-the-new-attack-vector-into-organizations/

[^1_108]: https://www.semanticscholar.org/paper/3de19f0fbc5add0f74bde83dfb5798294d589c33

[^1_109]: https://aclanthology.org/2024.emnlp-main.973/

[^1_110]: https://arxiv.org/abs/2501.18536

[^1_111]: https://www.ijraset.com/best-journal/responsible-prompt-engineering-an-embedding-based-approach-to-secure-llm-interactions-

[^1_112]: https://github.com/SchwinnL/LLM_Embedding_Attack

[^1_113]: https://genai.owasp.org/llmrisk/llm08-excessive-agency/

[^1_114]: https://arxiv.org/html/2402.16006v2

[^1_115]: https://arxiv.org/abs/2407.04295

