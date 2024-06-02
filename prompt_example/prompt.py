from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def generate_summary(info_type: str, information: str):
    summary_template = """
    given the {info_type} {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    3. Be no more than 50 words

    Do not add any other text, apart from this summary template
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information, "info_type": info_type})
    print(res)
