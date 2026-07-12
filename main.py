import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from project!")
    print("OpenAI Key:", os.getenv("openai_key"))
    information = """Virtusa Corporation, founded in 1996 in Sri Lanka, is headquartered in Westborough, Massachusetts, USA, and operates globally with delivery centers in the U.S., U.K., Singapore, Germany, Malaysia, Netherlands, India, and Sri Lanka 
    The company provides IT consulting, business consulting, digital engineering, application outsourcing, and platform engineering services, serving clients across industries such as banking, financial services, insurance, healthcare, telecommunications, media, technology, and travel
    """
    summary_templete = """ given the information {information} about some company i want you to create:
    1. A brief summary of the company in 2-3 sentences.
    2. A list of the company's core services and offerings.
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_templete,
    )
    print(information)

if __name__ == "__main__":
    main()
