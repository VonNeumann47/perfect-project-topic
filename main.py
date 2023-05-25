import streamlit as st

from model import MODEL
from topics import QUESTION_TO_OPTIONS


def main():
    st.set_page_config(
        page_title="Perfect project topic!",
        page_icon=(
            "https://raw.githubusercontent.com/"
        ),
    )

    st.title("Узнай идеальную тему своего проекта!")
    st.markdown(r"""
        Мы не будем спрашивать твой знак Зодиака или размер ноги.
        Достаточно ответить на следующие 5 вопросов, чтобы узнать,
        чем **на самом деле** нужно было заниматься в Яндекс.Лицее.

        Удачи!
    """)

    parts = []
    for question, options in QUESTION_TO_OPTIONS.items():
        answer = st.text_input(
            label=question,
        ).strip()
        parts.append(options[hash(answer) % len(options)])

    button = st.button("Хочу ИДЕАЛЬНУЮ тему!")

    MODEL.clear_output()
    if button:
        topic = " ".join(parts).replace(" :", ":")
        MODEL.run_model(topic)
        description = MODEL.get_last_output()

        st.markdown("_" * 10)
        st.markdown(f"""
            **Тема проекта**: {topic}

            **Аннотация**

            {description}
        """)


if __name__ == "__main__":
    main()
