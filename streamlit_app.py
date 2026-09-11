import streamlit as st
import language_tool_python

st.set_page_config(page_title="Grammar Error Detection", page_icon="📝")

st.title("📝 Grammar Error Detection System")

tool = language_tool_python.LanguageTool('en-US')

text = st.text_area("Enter an English sentence")

if st.button("Check Grammar"):

    if text.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        matches = tool.check(text)
        corrected = language_tool_python.utils.correct(text, matches)

        st.subheader("✅ Corrected Sentence")
        st.success(corrected)

        st.subheader("❌ Errors Found")

        if len(matches) == 0:
            st.success("No grammar errors found!")
        else:
            for i, m in enumerate(matches, 1):
                # Safe extraction without errorLength
                wrong = text[m.offset : m.offset + len(m.context.strip())]

                st.write(f"**Error {i}:**")
                st.write("Wrong text:", wrong)
                st.write("Suggestion:", ", ".join(m.replacements[:3]))
                st.write("Message:", m.message)
                st.divider()