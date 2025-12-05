#!/bin/env python3
# MODULES ====================================================================
import pandas as pd
from shiny import reactive, render, ui
from shiny import Inputs, Outputs, Session
import shinyswatch
import sqlite3
# For pooled SQL connections
from sqlalchemy import create_engine, text

# Import global variables
from globals import NP_CLASS, DB_CHOICES, EXP_TYPE_MAPPING

# SERVER =====================================================================
def server(input: Inputs, output: Outputs, session: Session):

    # ------------------------------------------------------------------------
    # DYNAMIC SIDEBAR LOGIC 
    # ------------------------------------------------------------------------
    @reactive.effect
    @reactive.event(input.db_select) # React when db_select changes
    def update_exp_type():
        """
        Observes the selection of db_select and updates the choices
        for exp_type based on the mapping
        """
        db_selection = input.db_select()
        # Get the new list of choices from the mapping
        new_exp_choices = EXP_TYPE_MAPPING.get(db_selection, [])
        # Update the exp_type based on the selection
        ui.update_select(
            "exp_type",
            choices=new_exp_choices,
            selected=new_exp_choices[0] if new_exp_choices else None
        ) # END dynamic sidebar logic

    # ------------------------------------------------------------------------
    # THEME PICKER LOGIC 
    # ------------------------------------------------------------------------
    shinyswatch.theme_picker_server()

    # ------------------------------------------------------------------------
    # POOLED SQL CONNECTION LOGIC 
    # ------------------------------------------------------------------------
#    @reactive.Calc
#    def filtered_data():
#        selected_np_class = input.np_class()
#        selected_db = input.db_select()
#        selected_exp = input.exp_type()
#
#        # Acquire/borrow a connection from the pool using `with` statement
#        with sql_engine
