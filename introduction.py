import streamlit as st


# Creating markdown for the introduction page
def intro():
    markdown_info = st.markdown(
        """
    
    # What this tool is about?
    This tool is designed to compare, find the usecases of models provided by openai. Thanks for using this tool.

    ## What is openai?
    OpenAI is a non-profit artificial intelligence research company founded in 2015 by Elon Musk, Sam Altman, and Greg Brockman. It is based in San Francisco, California, and is funded by Musk, Amazon, Microsoft, and other investors. OpenAI's mission is to ensure that artificial general intelligence benefits all of humanity. OpenAI's first product is an API that provides access to its GPT-3 language model. The company also develops other AI technologies, such as a robot that can play the video game Dota 2.

    ## Model comparisions and usecases. 
    | **Models**   | **Description**                                                                                               |
    |--------------|---------------------------------------------------------------------------------------------------------------|
    |    GPT-3.5   | A set of models that improve on GPT-3 and can understand as well as generate natural language or code         |
    |    DALL·E    | A model that can generate and edit images given a natural language prompt                                     |
    |    Whisper   | A model that can convert audio into text                                                                      |
    |  Embeddings  | A set of models that can convert text into a numerical form                                                   |
    | CodexLimited | beta    A set of models that can understand and generate code, including translating natural language to code |
    |  Moderation  | A fine-tuned model that can detect whether text may be sensitive or unsafe                                    |
    |     GPT-3    | A set of models that can understand and generate natural language                                             |

    source- [https://platform.openai.com/docs/models](https://platform.openai.com/docs/models)

    ## What does this demo offers? 
    checkbox markdown 

    Question answering 
    - [ ] Image generation 
    - [ ] Speech to text
    - [ ] Code generation
    - [ ] Content moderation
    - [ ] Numerical embeddings
    - [ ] GPT3 models

    ## How to use this tool?
    * Enter your openai api key in the sidebar
    * Select the task you want to perform
    * Enter the required input 
    * Click on the submit button
    * The output will be displayed in the main window
    """
    )
