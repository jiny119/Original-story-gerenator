import streamlit as st
from transformers import pipeline
from gtts import gTTS

# Streamlit App Title
st.title("📖 Urdu Story Generator with Voiceover")

# User Input: Story Title
story_title = st.text_input("Enter a Title for the Story (Urdu Allowed)")

if st.button("Generate Story"):
    if story_title:
        with st.spinner("Generating story... Please wait..."):
            # AI Story Generation
            generator = pipeline("text-generation", model="openai-community/gpt2")
            prompt = f"{story_title} کے بارے میں ایک کہانی لکھیے۔"
            story = generator(prompt, max_length=500, num_return_sequences=1)[0]["generated_text"]

            # Display Story Text
            st.subheader("Generated Story:")
            st.write(story)

            # Convert Story to Speech (TTS)
            tts = gTTS(text=story, lang="ur")
            tts.save("story.mp3")

            # Play Audio
            st.subheader("Listen to the Story:")
            st.audio("story.mp3", format="audio/mp3")

            # Download Button for Audio
            with open("story.mp3", "rb") as file:
                st.download_button(
                    label="Download Story Audio",
                    data=file,
                    file_name="urdu_story.mp3",
                    mime="audio/mp3"
                )

    else:
        st.warning("Please enter a title for the story!")
