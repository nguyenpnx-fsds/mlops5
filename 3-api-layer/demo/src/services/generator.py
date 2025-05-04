from src.schemas import State
from src.services import llm
from src.constants.prompt import template


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = template.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}
