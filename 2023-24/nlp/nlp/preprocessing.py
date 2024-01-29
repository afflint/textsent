import spacy


def to_record(token, document_id, metadata: dict=None):
    record = {'doc_id': document_id, 'lower': token.text.lower()}
    fields = ['idx', 'text', 'pos_', 'lemma_', 'dep_', 'tag_', 'is_alpha', 'is_stop']
    for field in fields:
        record[field] = getattr(token, field)
    if metadata is None:
        metadata = {}
    for k, v in metadata.items():
        record[k] = v
    return record

def to_records(nlp: spacy.language.Language, document_text: str, document_id: object, **metadata):
    return [to_record(token=token, document_id=document_id, metadata=metadata) for token in nlp(document_text)]