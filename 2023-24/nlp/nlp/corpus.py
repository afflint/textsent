import pymongo


class SpacyDbCorpus:
    def __init__(self, db_name: str, collection: str) -> None:
        self.db = pymongo.MongoClient()[db_name][collection]
    
    def get_corpus(self, filters: list = None, metadata: list = None, limit: int = None):
        pipeline = []
        if filters is not None:
            for f in filters:
                pipeline.append({'$match': f})
        if metadata is None:
            gid = "$doc_id"
        else:
            gid = {"doc_id": "$doc_id"}
            for m in metadata:
                gid[m] = "${}".format(m)
        pipeline.append({'$group': {"_id": gid, "tokens": {"$push": {
            "text": "$text", "lower": "$lower", "idx": "$idx", "pos": "$pos_", "lemma": "$lemma_",
            "dep": "$dep_", "tag": "$tag_" 
        }}}})
        if limit is not None:
            pipeline.append({'$limit': limit})
        for record in self.db.aggregate(pipeline, allowDiskUse=True):
            yield record