from dotenv import load_dotenv

from prompt_example.prompt import generate_summary
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True)
    generate_summary("LinkedIn", linkedin_data)
