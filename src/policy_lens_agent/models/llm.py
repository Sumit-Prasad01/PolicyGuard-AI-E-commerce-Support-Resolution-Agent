import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_groq import ChatGroq

load_dotenv()


class LLMFactory:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

    def get_llm(self, temperature=0.2):
        return ChatGroq(
            groq_api_key=self.api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=temperature
        )


def build_chain(system_prompt: str, user_prompt: str, temperature: float = 0.2):
    llm = LLMFactory().get_llm(temperature=temperature)

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", user_prompt)
    ])

    chain = prompt | llm | StrOutputParser()
    return chain