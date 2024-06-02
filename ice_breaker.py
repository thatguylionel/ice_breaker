from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()

    information = """
    Jamie Lee Curtis (born November 22, 1958) is an American actress, producer, and children's author. 
    Known for her performances in the horror and slasher genres, she is regarded as a scream queen, in addition to roles 
    in comedies.[1] Curtis has received multiple accolades, including an Academy Award, a BAFTA Award, and two 
    Golden Globe Awards,as well as nominations for an Emmy Award and a Grammy Award.

    The youngest daughter of actors Janet Leigh and Tony Curtis, she made her television debut in a 1977 episode of the 
    NBC drama series Quincy, M.E..[2] Curtis made her film debut and rose to prominence with her portrayal of 
    Laurie Strode in John Carpenter's slasher film Halloween (1978). A critical and commercial success, the film 
    established Curtis as a scream queen and led to starring roles in the horror films The Fog, Prom Night, Terror Train
     (all 1980), and Roadgames (1981). She would reprise the role in six of the Halloween sequels, concluding with 
     Halloween Ends in 2022.

    Curtis's film work spans many genres outside of horror, including the comedies Trading Places (1983), for which she 
    won the BAFTA for Best Supporting Actress, and A Fish Called Wanda (1988), for which she received a nomination for 
    the BAFTA for Best Actress. Her role as a workout instructor in the film Perfect (1985) earned her a reputation 
    as a sex symbol. She won a Golden Globe Award for Best Actress for her portrayal of Helen Tasker in James Cameron's 
    True Lies (1994). Her other film credits include Freaky Friday (2003), Knives Out (2019), and 
    Everything Everywhere All at Once (2022). Her performance in the latter earned Curtis multiple accolades, 
    including the Academy Award for Best Supporting Actress.[7][8][9] As of 2023, her films have grossed over 
    $2.5 billion at the box office.
    
    Curtis received another Golden Globe for her portrayal of Hannah Miller on ABC's sitcom Anything but 
    Love (1989–1992), and earned a nomination for a Primetime Emmy Award for Outstanding Lead Actress for the television
     film Nicholas' Gift (1998). She also starred in the Fox series Scream Queens (2015–2016), for which she received 
     her seventh Golden Globe nomination.[6] Curtis has written numerous children's books, including Today I Feel Silly, 
     and Other Moods That Make My Day (1998), which made The New York Times's best-seller list. She is married to 
     British-American filmmaker Christopher Guest, with whom she has two adopted children.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
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
    res = chain.invoke(input={"information": information})

    print(res)
