**Text Mining and Sentiment Analysis - Master Degree in Data Science and Economics**

**Prof. Alfio Ferrara**

*Department of Computer Science, Università degli Studi di Milano
Room 7012 via Celoria 18, 20133 Milano, Italia <a href="mailto:alfio.ferrara@unimi.it">alfio.ferrara@unimi.it</a>*



# Ideas for final projects

[TOC]

## Instructions

The final project consists in the preparation of a short study on one of the topics of the course, identifying a precise research question and measurable objectives. The project will propose a methodology for solving the research question and provide an experimental verification of the results obtained according to results evaluation metrics. The emphasis is not on obtaining high performance but rather on the critical discussion of the results obtained in order to understand the potential effectiveness of the proposed methodology.

The results must be documented in a short article of not less than 4 pages and no more than 8, composed according to the guidelines available here: [template](https://preview.springer.com/gp/livingreviews/latex-templates) and using the corresponding $\LaTeX$ or MS Word templates. Students have also to provide access to a <a href="https://github.com/">GitHub</a> repository containing the code and reproducible experimental results.

Finally, the project will be discussed after a 10 minutes presentation in English with slides. 



## Procedure

Exam dates are just for the registration of the final grade. The project discussion will be set by appointment, according to the following procedure:

1. Subscribe to any available date
2. Contact Prof. Ferrara as soon as
   1. The project is finished and ready to be discussed
   2. After the date of your subscription is expired

3. Setup an appointment and discuss your work

**Example**: you subscribe the exam date of [Month] [Day]. **Anytime after [Month] [Day]**, when the **project is ready**, you will contact Prof. Ferrara and set an appointment. You discuss the project during the appointment.

If you are **interested in doing your final master thesis on these topics**, the final project may be a preliminary work in view of the thesis. In this case, discuss the contents with Prof. Ferrara.



## Structure of the paper

1. **Introduction**

   Provides an overview of the project and a short dicsussion on the pertinent literature 

2. **Research question and methodology**

   Provides a clear statement on the goals of the project, an overview of the proposed approach, and a formal definition of the problem

3. **Experimental results**

   Provides an overview of the dataset used for experiments, the metrics used for evaluating performances, and the experimental methodology. Presents experimental results as plots and/or tables

4. **Concluding remarks**

   Provides a critical discussion on the experimental results and some ideas for future work



## Project ideas

The following are ideas for projects. For each idea, a short description, example of datasets that can be used, and bibliographic references are provided. Students may **choose one of the following** as their project theme or **they can propose their own idea**, structuring the proposal as those presented in this document. In the latter case, just send the project description to Prof. Ferrara.



### Hidden concepts (P1)

Entailments are inferences which logically follow from a given claim. It is a purely logical concept (not strictly speaking a pragmatic one). 

Examples:

`Tim has bought fish tonight` entails that 

- Tim has spent money tonight
- Tim has bought something

`Tim managed to stop the car` entails that 

- Tim stopped the car
- Tim tried to stop the car
- Tim did something to the car 

The project aims at defining a model that detects possible entailments given an input utterance. Machine learning methods for representing language context and hidden knowledge in text may be exploited to this end as well as knowledge bases (such as WordNet or Wikidata) in order to link logical propositions and concepts to the utterance text.

A particularly interesting idea is that of extracting from a pair of sentences the set of concepts associated with them and then attempting to reconstruct the network of concepts which connects those of the first sentence with those of the second. For this purpose semantic networks of concepts can be used such as for example [ConceptNet](https://conceptnet.io/).

#### Dataset

Samuel R. Bowman, Gabor Angeli, Christopher Potts, and Christopher D. Manning. 2015. A large annotated corpus for learning natural language inference. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP). [[pdf](http://nlp.stanford.edu/pubs/snli_paper.pdf)] [[webpage](https://nlp.stanford.edu/projects/snli/)]

#### References

Stephen Levinson, 1983. Pragmatics, Cambridge: CUP

Poliak, A. (2020). A survey on recognizing textual entailment as an nlp evaluation. arXiv preprint [arXiv:2010.03061](https://arxiv.org/abs/2010.03061).

Belinkov, Y., & Glass, J. (2017). Analyzing hidden representations in end-to-end automatic speech recognition systems. arXiv preprint [arXiv:1709.04482](https://arxiv.org/abs/1709.04482).

### What do you like in boardgames (P2) 

Playing boardgames is a wonderfull hobby that is growing in popularity in the last years. Since 2000, the website [BoardGameGeek (BGG)](https://boardgamegeek.com)  provides a complete database about boardgames and users playing boardgames around the world. Users provide also stats and ratings that evaluate the popularity of each game according to several criteria, including a rating and the number of users voting the game, the community opinion about the playability of the game with respect to the number of players, the community opinion about how much the game is language dependant, the game complexity (called weight) (see for example the stats for the game [Gloomhaven](https://boardgamegeek.com/boardgame/174430/gloomhaven)). Moreover, BGG provide access to users comments on games that are often associated with a review score given to the game through their [BGG API](https://boardgamegeek.com/wiki/page/BGG_XML_API2).

Goal of the project is to study the user comments in order to undertand the polarity of users with respect to the following **aspects** of boardgaming (definitions a taken from the Italian [Goblinpedia](https://www.goblins.net/goblinpedia):

- **luck** or **alea**: all those game elements independent of player intervention, introduced by game mechanics outside the control of the players.
- **bookkeeping**: manual recording of data and potentially automatic or semi-automatic game processes, including also the need of continuosly accessing the rulebook for reference.
- **downtime**: unproductive waiting time between one player turn and the next. By unproductive we mean not only having nothing (or little) to do, but also nothing (or little) to think about.
- **interaction**: the degree of influence that one player's actions have on the actions of the other participants.
- **bash the leader**: when, to prevent the victory of whoever is first, the players are forced to take actions against him, often to the detriment of their own advantage or in any case without gaining anything directly. At the table, the unfortunate situation can arise whereby one or more must "sacrifice" themselves to curb the leader and let the others benefit from this conduct.
- **complicated vs complex**: A game is complicated the more the rules are quantitatively many and qualitatively equipped with exceptions. Once you understand and learn all the variables, a game (that is only) complicated is not difficult to master. In a complicated game, solving a problem leads to immediate, certain and predictable results.
  A game is as complex as the repercussions of one's actions are difficult to predict and master. Even once you understand and learn all the variables, a complex game is still difficult to master. In a complex game, solving one problem leads to other problems. 

For each aspect, the project will develop a method to find references to that aspect in user comments in order to associate a polarity and, potentially, an opinion to the aspect of interest.

#### Datasets

Game metadata as well as users comments and evaluation score may be accessed through thee [BGG API](https://boardgamegeek.com/wiki/page/BGG_XML_API2).

#### References

Schouten, K., & Frasincar, F. (2015). Survey on aspect-level sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28(3), 813-830. [link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7286808&casa_token=RXxN0Mq3OGYAAAAA:WrsjDCF3kBc_W64DMB51CJQ0h8BLbBdn4MAo6S4pDLI377bxFtqAWBOyBRZAVGh_N8ebztVX&tag=1)

Rana, T. A., & Cheah, Y. N. (2016). Aspect extraction in sentiment analysis: comparative analysis and survey. Artificial Intelligence Review, 46(4), 459-483. [link](https://link.springer.com/article/10.1007/s10462-016-9472-z)

Nazir, A., Rao, Y., Wu, L., & Sun, L. (2020). Issues and challenges of aspect-based sentiment analysis: A comprehensive survey. IEEE Transactions on Affective Computing. [link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8976252&casa_token=25ETa60ccgQAAAAA:V1MiSCJCoGOg0YX-F0M9KFod7JLSl-k9w2LxnRYXjZPz-XJJzu2XGNHJTwDolMfo0rNvgLxI)

### How do you cultivate your field (P3)

> In collaboration with Prof. [Luca Bechini](https://www.unimi.it/it/ugov/person/luca-bechini), Department of Agricultural and Environmental Sciences - Production, Landscape, Agroenergy, Università degli Studi di Milano 

Most of our food comes from annual crops like wheat, rice and maize. The growing cycle of each annual crop starts with planting seeds into the soil. Before planting, the soil is normally prepared to ensure a good seed-soil contact and homogeneous seed placement. Soil preparation is carried out with tillage tools. In the conventional tillage methods, the first tool used is the plough (which reverses and loosens the soil), followed by other passes with tools (like harrows) that reduce the sizes of soil aggregates remaining after ploughing. 

However, these methods involve a great consumption of tractor fuel and may involve a deterioration of soil quality. For this reason, alternative methods (“minimum tillage”) are adopted, that avoid ploughing and make use of simpler and shallower tillage tools. Minimum tillage techniques reduce the consumption of fuel and time, and, depending on how they are implemented, may provide additional benefits (e.g. improvement of soil quality). One of the most debated advantages of minimum tillage practices is the increase of soil organic carbon. Soil organic carbon (SOC) is an essential component of soil fertility. In general, the higher the SOC, the better soil quality is.

The purpose of the project is to analyse the content of published research (abstracts of scientific publications), by evaluating the effects on SOC of minimum tillage practices. Frequently, the change in SOC over time after the adoption of the practice is expressed in relation to the change in SOC observed under conventional tillage in similar conditions (same soil type, same climate, same crop rotation, etc.).
More in general, the project is a first exercise that could potentially be generalized to the analysis of the effects of an agricultural practice on a number of soil, crop or atmosphere variables, like for example crop yield, crop quality, soil quality, gaseous emissions, and water pollution.

#### Dataset

- AGRONOMY. About 18 000 scientific paper abstracts in the field of *agronomy* research, provided as RIS bibliographic records. [dataset](http://island.ricerca.di.unimi.it/~alfio/shared/agrotech.zip) - [RIS](https://en.wikipedia.org/wiki/RIS_(file_format)).
- Concepts and seed terminology [link](https://unimibox.unimi.it/index.php/s/d4eEitbyczLdjwd). An ontology containing the relavant terminology for the identification of soil  preparation methods, effects on soil (including SOC), type of soils and crops, climate.

- Agronomy Ontologies: Further terminology and a formal descritpion of concept may be found in [VALERIE](http://www.foodvoc.org/page/Valerie-9), [AGROVOC](http://aims.fao.org/vest-registry/vocabularies/agrovoc), [EUROVOC](https://op.europa.eu/en/web/eu-vocabularies/th-concept/-/resource/eurovoc/100156?target=Browse)

#### References

- Bechini, L., Koenderink, N., Ten Berge, H. F., Corre, W., Van Evert, F. K., Facchi, A., ... & Hily, Y. (2016). Improving access to research outcomes for innovation in agriculture and forestry: the VALERIE project. In Convegno della Società italiana di agronomia (SIA). [link](https://air.unimi.it/handle/2434/481444#.Xq7I8ZpS_0Q)
- Rink, B., Bejan, C. A., & Harabagiu, S. (2010, May). Learning textual graph patterns to detect causal event relations. In *Twenty-Third International FLAIRS Conference*. [link](https://www.aaai.org/ocs/index.php/FLAIRS/2010/paper/viewPaper/1380)

### What text are you? (P4)

> Instructor, Martin Ruskov, Department of Languages, Literatures, Cultures and Mediations, Università degli Studi di Milano

Text is everywhere around us. Yet, much like human thought, texts are very different, to the extent that two texts might not have anything in common. Consider a sports report, a description of an archeological artifact or a scientific publication. Whereas the first is expected to contain a summary of key events and results, the second would need to contain a physical description of the object. The third might not even have parts with any of the above. Commonly, from the above the first is called a narrative, the second descriptive text, and the third an expository text.

Recent advances in computational linguistics have allowed for the modeling of a number of tasks such as part-of-speech annotation, dependency parsing and sentiment analysis. Attempts have been made to replicate these successes to classification of text types, but with mixed results. Further experimentation and comparative analysis might be interesting.

#### Dataset

Caselli, Tommaso; Sprugnoli, Rachele; Moretti, Giovanni, 2021, "Content Type Dataset - v1.5", https://doi.org/10.34894/TYB4PF, DataverseNL, V1

#### References

- Caselli, T., Sprugnoli, R., & Moretti, G. (2022). Identifying communicative functions in discourse with content types. *Language Resources and Evaluation*, *56*(2), 417–450. https://doi.org/10.1007/s10579-021-09554-4 
- Asher, N., & Lascarides, A. (1994) Intentions and information in discourse. In: *Proceedings of the 32nd Annual Meeting of the Association for Computational Linguistics, Association for Computational Linguistics*, Las Cruces, New Mexico, USA, pp. 34–41, https://doi.org/10.3115/981732.981738, https://www.aclweb.org/anthology/P94-1006.
- Banisakher, D., Yarlott, W. V., Aldawsari, M., Rishe, N., & Finlayson, M. (2020). Improving the identification of the discourse function of news article paragraphs. In: *Proceedings of the First Joint Workshop on Narrative Understanding, Storylines, and Events, Association for Computational Linguistics*, Online, pp. 17–25, https://doi.org/10.18653/v1/2020.nuse-1.3, https://www.aclweb.org/anthology/2020.nuse-1.3.

### Explain you opinion (P5)

> In collaboration with Emanuele Guidotti, University of Neuchâtel

[Born Classifier](https://bornrule.eguidotti.com/) is a text classification algorithm inspired by the notion of superposition of states in quantum physics. Born provides good classification performance, explainability, and computational efficiency. In this project, the goal is to exploit the Born explanation in order to use it for Aspect Based Sentiment Analysis. In particular, the main idea to to proceed as follows:

1. Perform a sentiment analysis classification of documents using Born
2. Extract the explanation features for each pair of documents and predicted labels
3. Analyze the explanatory features in order to group them in candidate aspects
4. Associate each aspect to a specific sentence or portion of the text
5. Predict the sentiment for the sentence or text portion using the trained Born classifier
6. Associate then a (potentially different) sentiment to each sentence or text portion according to the aspect

Finally, evaluate the quality of the results for each aspect.

#### Dataset

Any dataset supporting ABSA. See for example [here](https://paperswithcode.com/datasets?task=aspect-based-sentiment-analysis&page=1).

#### References

- Emanuele Guidotti and Alfio Ferrara. Text Classification with Born’s Rule. *Advances in Neural Information Processing Systems*, 2022.
- Schouten, K., & Frasincar, F. (2015). Survey on aspect-level sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28(3), 813-830. [link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7286808&casa_token=RXxN0Mq3OGYAAAAA:WrsjDCF3kBc_W64DMB51CJQ0h8BLbBdn4MAo6S4pDLI377bxFtqAWBOyBRZAVGh_N8ebztVX&tag=1)
- Rana, T. A., & Cheah, Y. N. (2016). Aspect extraction in sentiment analysis: comparative analysis and survey. Artificial Intelligence Review, 46(4), 459-483. [link](https://link.springer.com/article/10.1007/s10462-016-9472-z)

### Who you are? (P6)

> In collaboration with Emanuele Guidotti, University of Neuchâtel

Entity Disambiguation is the task of linking mentions of ambiguous entities to their referent entities in a knowledge base such as Wikipedia. [Born Classifier](https://bornrule.eguidotti.com/) is a text classification algorithm inspired by the notion of superposition of states in quantum physics. Born provides good classification performance, explainability, and computational efficiency. In this project, the goal is to exploit the Born explanation in order to try to perform entity disambiguation. In particular, the main idea to to proceed as follows:

1. Perform Named Entity Recognition as a classification process with Born, where the text is the input and the entities mentioned in the text are the target
2. Extract the explanation features for each pair of documents and predicted entities
3. Analyze the explanatory features in order to group see if ambiguous entities (i.e., entities with the same name) are associated with different explanatory features in different documents
4. Try to use the explanatory features in order to distinguish different classes of equivalence referring to the same ambiguous entity
5. You can also collect different Wikipedia pages potentially corresponding to the same ambiguous entities (e.g., [Berlin](https://en.wikipedia.org/wiki/Berlin) as the capital city of Germany or [Berlin](https://en.wikipedia.org/wiki/Berlin_(TV_series)) as the TV series) and run the classification on these documents to match the explanations of the original dataset with those of the Wikipedia pages and select the right sense for the entity 
6. Finally, evaluate the quality of the results for the disambiguation task.

#### Dataset

Any dataset supporting Entity Disambiguation. See for example [WikilinksNED](https://aclanthology.org/K17-1008/), [AIDA CoNLL-YAGO](https://paperswithcode.com/dataset/aida-conll-yago), or [AQUAINT](https://paperswithcode.com/dataset/aquaint).

#### References

- Emanuele Guidotti and Alfio Ferrara. Text Classification with Born’s Rule. *Advances in Neural Information Processing Systems*, 2022.
- Yotam Eshel, Noam Cohen, Kira Radinsky, Shaul Markovitch, Ikuya Yamada, and Omer Levy. 2017. [Named Entity Disambiguation for Noisy Text](https://aclanthology.org/K17-1008). In *Proceedings of the 21st Conference on Computational Natural Language Learning (CoNLL 2017)*, pages 58–68, Vancouver, Canada. Association for Computational Linguistics.
- Hoffart, J., Yosef, M. A., Bordino, I., Fürstenau, H., Pinkal, M., Spaniol, M., ... & Weikum, G. (2011, July). Robust disambiguation of named entities in text. In *Proceedings of the 2011 conference on empirical methods in natural language processing* (pp. 782-792).

### I hate you (P7)

Hate speech detection on is critical for applications like controversial event extraction, building AI chatterbots, content recommendation, and sentiment analysis. We define this task as being able to classify a text comment as racist, sexist or neither. The complexity of the natural language constructs makes this task very challenging. 

The goal of the project is to create models for classifying text contents as offensive (e.g., racist, sexist or other) and to determine the most relevant terminology for each category and to extract relevant aspects in the hate speech. By working on datasets in different languages, such as English and Italian, it is also possible to study the main differences in the lexicon of hate in the two languages.

The goal of the project can also be adapted to other tasks or text phenomena, such as sarcasm, moral values, political opinions and so on. In general, the idea is to find a lexical explanation with respect to the decision of a classifier.

#### Dataset

Any dataset suitable for hate speech detection (see for example [here](https://hatespeechdata.com/) and [here](https://paperswithcode.com/dataset/hate-speech)).

#### References

- Mathew, B., Saha, P., Yimam, S. M., Biemann, C., Goyal, P., & Mukherjee, A. (2021, May). Hatexplain: A benchmark dataset for explainable hate speech detection. In *Proceedings of the AAAI Conference on Artificial Intelligence* (Vol. 35, No. 17, pp. 14867-14875).
- Arango, A., Pérez, J., & Poblete, B. (2019, July). Hate speech detection is not as easy as you may think: A closer look at model validation. In *Proceedings of the 42nd international acm sigir conference on research and development in information retrieval* (pp. 45-54).
- Fortuna, P.; and Nunes, S. 2018. A survey on automatic detection of hate speech in text. ACM Computing Surveys (CSUR) 51(4): 85.

### Safe Clinical NLI (P8)

> Instructor: Darya Shlyk, *Department of Computer Science, Università degli Studi di Milano*

Natural Language Inference (NLI) is a pivotal task in natural language understanding, aiming to ascertain if a statement logically follows from a given premise. 

For instance, given the premise: "*He returned to the clinic three weeks later and was prescribed antibiotics*" an NLI system should deduce that the statement "*The patient has an infection*" is entailed by the premise.

In recent years, there has been a significant surge in the publication of Clinical Trial Reports (CTRs). As a result, it has become increasingly challenging for clinical practitioners to keep pace with the ever-growing literature to offer personalized evidence-based care. In this context, NLI presents an opportunity to aid in the large-scale interpretation and retrieval of medical evidence.

In this project, we propose to tackle a textual entailment task using clinical trial data. The task is based on a dataset comprising breast cancer CTRs, statements, and labels annotated by domain expert annotators. The annotated statements represent sentences that make a claim about the information within one of the sections in the CTR. The objective is to determine the inference relation (entailment vs. contradiction) between CTR-statement pairs. Additionally, we encourage the exploration of evidence-based retrieval, wherein the NLI system extracts a set of supporting facts from the premise to justify its predictions.

#### Dataset

The available datasets are [nli4ct](https://sites.google.com/view/nli4ct/semeval-2024/get-data-and-starting-kit), [mednli](https://huggingface.co/datasets/bigbio/mednli).

#### References

- Jullien, Maël, et al. "NLI4CT: Multi-Evidence Natural Language Inference for Clinical Trial Reports." arXiv preprint arXiv:2305.03598 (2023).
- Mulyar, Andriy, Ozlem Uzuner, and Bridget McInnes. "MT-clinical BERT: scaling clinical information extraction with multitask learning." Journal of the American Medical Informatics Association 28.10 (2021): 2108-2115.
- Lee, Jinhyuk, et al. "BioBERT: a pre-trained biomedical language representation model for biomedical text mining." Bioinformatics 36.4 (2020): 1234-1240.
- DeYoung, Jay, et al. "Evidence inference 2.0: More data, better models." arXiv preprint arXiv:2005.04177 (2020).
- Romanov, Alexey and Shivade, Chaitanya. "Lessons from Natural Language Inference in the Clinical Domain" Proceedings of EMLP (2018).

### Bio Linking (P9)

> Instructor: Darya Shlyk, *Department of Computer Science, Università degli Studi di Milano*

Much of the world's healthcare data is stored in free-text documents, such as medical records and clinical notes. Analyzing and extracting meaningful insights from this unstructured data can be challenging. One approach for extracting structured knowledge from a vast corpus of biomedical literature is to annotate the text with concepts from existing knowledge bases. 

In the context of biomedical information extraction, Concept Recognition (CR) is defined as a two-step process, that consists in identifying and linking textual mentions of biomedical entities, such as genes, diseases, and phenotypes, to corresponding concepts in domain-specific ontologies.  The objective of this project is to devise effective strategies for automating the extraction of concepts from unstructured biomedical resources. When developing your CR system, you may decide to focus on a specific class of entities such as diseases or genes and link to any target ontology within the biomedical domain, such as MONDO, Human Phenotype Ontology, etc. 

For clinical CR, SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms) is a viable option. SNOMED CT is a systematically organized clinical terminology that encompasses a wide range of clinical concepts, including diseases, symptoms, procedures, and body structures.

#### Dataset

Possible datasets include, PubMed abstracts and Clinical [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/2.2/) available on request.

#### References

- Vuokko, Riikka, Anne Vakkuri, and Sari Palojoki. "Systematized Nomenclature of Medicine–Clinical Terminology (SNOMED CT) Clinical Use Cases in the Context of Electronic Health Record Systems: Systematic Literature Review." JMIR medical informatics 11 (2023): e43750.
- Lossio-Ventura, Juan Antonio, et al. "Clinical concept recognition: Evaluation of existing systems on EHRs." Frontiers in Artificial Intelligence 5 (2023): 1051724.
- Toonsi, Sumyyah, Şenay Kafkas, and Robert Hoehndorf. "BORD: A Biomedical Ontology based method for concept Recognition using Distant supervision: Application to Phenotypes and Diseases." bioRxiv (2023): 2023-02.
- Hailu, Negacy D., et al. "Biomedical concept recognition using deep neural sequence models." bioRxiv (2019): 530337.

### KG+LLM : A Happy Marriage (P10)

> Instructor: Darya Shlyk, *Department of Computer Science, Università degli Studi di Milano*

A Knowledge Graph (KG) serves as a semantic network of entities, concepts, and relations, playing a pivotal role in numerous knowledge-driven applications across various domains. Often, KGs are curated by human experts who extract and interconnect factual knowledge from unstructured textual data. The construction of a KG typically involves a series of natural language processing tasks, including Named Entity Recognition (NER), Relation and Event Extraction (RE and EE), and Entity Linking (EL). While, Link Prediction (LP) is a critical aspect of KG reasoning, that aims to unveil latent relationships between entities, thereby enhancing the KG with additional knowledge.
The latest generation of language models, such as GPT+ and LLAMA2, showcase remarkable natural language understanding capabilities, achieving near-human-level performance across a wide spectrum of extractive and generative tasks. 

The project aims to explore the integration of large language models in knowledge-base construction and reasoning tasks. The goal is to investigate how these models can be leveraged to streamline and augment the KG creation process, thereby advancing the state-of-the-art in knowledge representation and reasoning.

#### Dataset

Any annotated dataset for NER, EL, RE, LP, QA (see for example [here](https://code.google.com/archive/p/relation-extraction-corpus/downloads))

#### References

- Zhu, Yuqi, et al. "Llms for knowledge graph construction and reasoning: Recent capabilities and future opportunities." *arXiv preprint arXiv:2305.13168* (2023).
- Xu, Derong, et al. "Large language models for generative information extraction: A survey." *arXiv preprint arXiv:2312.17617* (2023).
- Pan, Shirui, et al. "Unifying large language models and knowledge graphs: A roadmap." *IEEE Transactions on Knowledge and Data Engineering* (2024).

