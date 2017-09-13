from .search import Search


class DocTypeAsyncMixin:
    @classmethod
    def search(cls, using=None, index=None):
        """
        Create an :class:`~elasticsearch_dsl_async.Search` instance that will search
        over this ``DocType``.
        """
        return Search(
            using=using or cls._doc_type.using,
            index=index or cls._doc_type.index,
            doc_type=[cls]
        )
