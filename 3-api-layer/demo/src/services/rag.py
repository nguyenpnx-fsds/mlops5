from src.schemas import State

from langgraph.graph import START, StateGraph
from src.services import retrieve, generate


class Rag:
    def __init__(self):
        self.graph_builder = StateGraph(State).add_sequence([retrieve, generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    async def get_rest_response(self, question: str):
        response = await self.graph.ainvoke({"question": question})
        return response["answer"]

    async def get_sse_response(self, question: str):
        for message, _ in self.graph.stream(
            {"question": question}, stream_mode="messages"
        ):
            data = message.content  # type: ignore
            yield f"event: responseUpdate\ndata: {data}\n\n"
