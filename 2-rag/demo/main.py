from src.schema import State

from langgraph.graph import START, StateGraph
from src.retrieval import retrieve
from src.generator import generate


graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

response = graph.invoke({"question": "What do beetles eat?"})
print(response["answer"])
