from src.schema import State
from langchain_core.documents import Document
from src.utils import logger


# Define the retrieval function
def retrieve(state: State):
    """Generate tool call for retrieval or respond."""

    # Perform the retrieval using the vector store
    # retrieved_docs = vector_store.similarity_search(state["question"])
    logger.info(f"Retrieving documents for question: {state['question']}")
    retrieved_docs = [
        Document(
            page_content="Beetles are herbivores and eat plants, leaves, and flowers."
        ),
        Document(
            page_content="Beetles are omnivores and eat a variety of foods, including other insects."
        ),
        Document(
            page_content="Some beetles are scavengers and eat decaying organic matter."
        ),
    ]
    return {"context": retrieved_docs}
