# Binary Independence Model
Python implementation of Binary Independence Model (BIM) system for Information Retrieval 

### Example of Usage 

Import TIME dataset, initialize the system, formulate a query, tell the system which documents are relevent, see more retrieved documents, read the entire text of a retrieved document.

articles = import_dataset()

bim  = BIM(articles)

bim.answer_query('Italy and Great Britain fight the enemy')

bim.relevance_feedback(5,6,8)

bim.show_more()

bim.read_document(6)
