import asyncio

from elasticsearch_async import AsyncTransport
from elasticsearch_dsl import search
from elasticsearch_dsl.connections import connections


class Search(search.Search):
    def execute_future(self):
        """
        Execute the search asynchronously and return an instance of ``Response`` wrapping all
        the data.

        :arg response_class: optional subclass of ``Response`` to use instead.
        """
        es = connections.get_connection(self._using)
        transport = es.transport
        assert isinstance(transport, AsyncTransport)
        loop = transport.loop

        @asyncio.coroutine
        def coroutine():
            result = yield from es.search(
                index=self._index,
                doc_type=self._doc_type,
                body=self.to_dict(),
                **self._params
            )

            self._response = self._response_class(self, result)

        return asyncio.ensure_future(coroutine(), loop=loop)
