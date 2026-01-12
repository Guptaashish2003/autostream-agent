from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



INTENT_PROMPT = PromptTemplate(
    input_variables=["message"],
    template="""
You are an intent classifier for a SaaS sales agent.

Classify the user message into exactly ONE of the following intents:
- GREETING (hello, hi, casual talk)
- INFO (pricing, features, plans, support, refund, questions)
- HIGH_INTENT (ready to sign up, wants to try, buy, subscribe)

User message:
{message}

Return ONLY the intent name.
"""
)


def detect_intent(llm: ChatGoogleGenerativeAI, message: str) -> str:
    # Create a chain: Prompt -> Model -> String Parser
    chain = INTENT_PROMPT | llm | StrOutputParser()
    
    # Run the chain
    response_text = chain.invoke({"message": message})
    return response_text.strip()
