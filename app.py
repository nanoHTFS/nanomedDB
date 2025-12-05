#!/bin/env python3
# MODULES ====================================================================
from shiny import App
from app_ui import app_ui
from app_server import server
from pathlib import Path
from sqlalchemy import create_engine

# DEFINITIONS ================================================================
app_dir = Path(__file__).parent


## SQL -----------------------------------------------------------------------
DB_URL = "sqlite:///"
sql_engine = create_engine(
  DB_URL
)


# BUILD APP ==================================================================
app = App(app_ui, server)
