import hashlib

import streamlit as st

from logger import get_logger
from model import DEFAULT_MAX_LEN, MAX_LEN, MIN_LEN, MODEL
from topics import QUESTION_TO_OPTIONS


logger = get_logger(__name__)


def get_hash(text: str) -> int:
    hash_obj = hashlib.sha256(text.encode())
    return int(hash_obj.hexdigest(), base=16) & 0xFFFFFFFFFFFFFFFF


st.set_page_config(
    page_title="Perfect project topic!",
    page_icon="https://raw.githubusercontent.com/VonNeumann47/perfect-project-topic/main/icon.png",
)

st.title("Узнай идеальную тему своего проекта!")
st.markdown(r"""
    Мы не будем спрашивать твой знак Зодиака или какой рукой ты пишешь.
    Достаточно ответить на следующие 5 вопросов, чтобы узнать,
    чем **на самом деле** нужно было заниматься в Яндекс.Лицее.

    Удачи!
""")

parts = []
for question, options in QUESTION_TO_OPTIONS.items():
    answer = st.text_input(
        label=question,
    ).strip()
    parts.append(options[get_hash(answer) % len(options)])

max_length = st.slider(
    "Максимальная длина аннотации (в словах)",
    MIN_LEN,
    MAX_LEN,
    DEFAULT_MAX_LEN,
    help="Обычный слайдер длины текста, что такого?",
)

button = st.button("Хочу ИДЕАЛЬНУЮ тему!")

MODEL.clear_output()
if button:
    topic = " ".join(parts).replace(" :", ":")
    MODEL.run_model(topic, max_length=max_length)
    description = MODEL.get_last_output()

    logger.info(f"TOPIC = {topic}")
    logger.info(f"DESCRIPTION = {description}")

    st.markdown("_" * 10)
    st.markdown(f"**Тема проекта**: {topic}")
    st.markdown("**Аннотация**")
    st.markdown(description)
