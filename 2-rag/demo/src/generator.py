from src.schema import State
from src.llm import llm
from src.prompt import template


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = template.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}
