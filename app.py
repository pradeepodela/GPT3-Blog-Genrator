import streamlit as st
import openai

openai.api_key = 'your key'

def generateBlogTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
st.title('AI Blog Generator')
st.write('This is a simple blog generator that uses OpenAI\'s API to generate blog topics and sections.')
st.title('Genrate blog Topics')

topic = st.text_input('Enter a topic to generate blog Topic on: ')
button_blogtopics = st.button('Generate Blog Topics')
if button_blogtopics:
    st.write(generateBlogTopics(topic))
    print(generateBlogTopics(topic))

topic_blog = st.text_input('Enter a topic to generate blog sections on: ')
button_blogsection = st.button('Generate Blog sections')
if button_blogsection:
    st.write(generateBlogSections(topic_blog))
    print(generateBlogSections(topic_blog))


topic_content = st.text_input('Enter a topic to generate blog content: ')
button_blogcontent = st.button('Generate Blog content')
if button_blogcontent:
    st.write(blogSectionExpander(topic_content))
    print(blogSectionExpander(topic_content))
