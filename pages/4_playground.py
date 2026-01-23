import streamlit as st
import streamlit.components.v1 as components
from st_screen_stats import ScreenData

from config import (
    PLAYGROUND_PAGE_URL_JUPYTERLITE,
    PLAYGROUND_PAGE_URL_MARIMO
)
from utils import page_config, check_password

page_config()

# 認証チェック
check_password()


def playground() -> None:
    st.title("playground")

    screenD = ScreenData(setTimeout=1000)
    data = screenD.st_screen_data()

    select_playground = st.segmented_control(
        "select type",
        ["JupyterLite", "Marimo"],
        selection_mode="single",
        default="JupyterLite"
    )

    if select_playground == "JupyterLite":
        components.iframe(
            src=PLAYGROUND_PAGE_URL_JUPYTERLITE,
            width=data["innerWidth"],
            height=int(data["innerHeight"]*0.9),
        )

    if select_playground == "Marimo":
        components.iframe(
            src=PLAYGROUND_PAGE_URL_MARIMO,
            width=data["innerWidth"],
            height=int(data["innerHeight"]*0.9),
        )


playground()
