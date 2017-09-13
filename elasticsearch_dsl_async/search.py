import asyncio
from elasticsearch_dsl import search
from elasticsearch_dsl.connections import connections


class Search(search.Search):
    @asyncio.coroutine
    def execute_async(self, ignore_cache=False):
        """
        Execute the search asynchronously and return an instance of ``Response`` wrapping all
        the data.

        :arg response_class: optional subclass of ``Response`` to use instead.
        """
        if ignore_cache or not hasattr(self, '_response'):
            es = connections.get_connection(self._using)

            result = yield from es.search(
                index=self._index,
                doc_type=self._doc_type,
                body=self.to_dict(),
                **self._params
            )

            self._response = self._response_class(self, result)
        return self._response
