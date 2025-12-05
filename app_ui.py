#!/bin/env python3
# MODULES ====================================================================
import faicons as fa
from shiny import Inputs, reactive, render, ui
import shinyswatch 

from globals import ICONS, NP_CLASS, DB_CHOICES, EXP_TYPE_MAPPING

# UI =========================================================================
app_ui = ui.page_fluid(
#    ui.include_css(app_dir / "styles.css"), # Include CSS
    ui.page_navbar(
        #ui.nav_spacer(),
## --- HOMEPAGE --------------------------------------------------------------
        ui.nav_panel(
            ICONS["icon_house"],
            ui.layout_columns(
                ui.column(8,
                    ui.card(
                    ui.card_header("Welcome to the nanomedDB"),
                    ui.p("The nanomedDB Open Database is an initiative to curate nanomedicine formulation data in a systematic and  open manner. These data are freely accessible to the nanomedicine community to explore structure-function relationships between nanomaterial physico-chemical properties, formulation parameters, and biological interactions."),
                    ui.p("Users can also contribute their data, which will then be evaluated and integrated into the database."),
                    ui.p("The nanomedDB platform and data herein are distributed under a GNU General Public License v3.0 (GPL 3.0). You are free to share (copy and redistribute), as well as adapt (remix, transform, and build upon) with proper attribution, and with the caveat that ... ")
                    )
                ), # END ui.column
            ), # END ui.layout_columns
        ), # END ui.nav_panel # HOME
## --- DATABASE --------------------------------------------------------------
        ui.nav_panel(
            ICONS["icon_db"],
            ui.layout_columns(
                ui.column(6, #
                ), # END column 
                ui.column(6, #
                    ui.card(
                    ) # END card
                ) # END column
            ) # END ui.layout_columns
        ), # END ui.nav_panel # VIEW DB
## --- UPLOAD USER DATA ------------------------------------------------------
        ui.nav_panel(
            ICONS["icon_upload"],
            ui.layout_columns(
                ui.column(3,
                # FIRST NAME
                    ui.input_text(
                        "input_fname",
                        "First Name",
                        value=''
                    )
                ), # END column
                ui.column(3,
                # Surname
                    ui.input_text(
                        "input_lname",
                        "Surname",
                        value=''
                    )
                ), # END column
            ) # END ui.layout_columns
        ), # END ui.nav_panel # UPLOAD
## --- SIDEBAR ---------------------------------------------------------------
        sidebar=ui.sidebar(
            ui.input_select(
                "np_class",
                "Select NP Class",
                choices=NP_CLASS,
                selected=NP_CLASS[0]
            ), # END input_select # np_class
            ui.input_select(
                "db_select",
                "Select Database",
                choices=DB_CHOICES,
                selected=DB_CHOICES[0]
            ), # END input_select # db_select
            ui.input_select(
                "exp_type",
                "Select Experiment Type",
                choices=[],
                selected=None
            ), # END input_select # exp_type
            ui.div(style="flex-grow: 1;"),
            shinyswatch.theme_picker_ui(),
        ), # END sidebar
        id="tabs",
        title="nanomedDB",
        fillable=True,
    ) # END ui.page_navbar
) # END ui.page_fluid
