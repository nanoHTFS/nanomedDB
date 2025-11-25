# MODULES ====================================================================
import faicons as fa
import pandas as pd
from pathlib import Path
from shiny import App, Inputs, reactive, render, ui

# DEFINITIONS ================================================================
app_dir = Path(__file__).parent

data = pd.DataFrame({
    "col1":[1,2,3,], 
    "col2": ["A", "B", "C"]
})

## ICONS ---------------------------------------------------------------------
ICONS = {
    "icon_user": fa.icon_svg("user", "solid"),
    "icon_house": fa.icon_svg("house", "solid"),
    "icon_db": fa.icon_svg("database", "solid"),
    "icon_upload": fa.icon_svg("upload", "solid"),
    "icon_license": fa.icon_svg("file-contract", "solid")
}

# UI =========================================================================
app_ui = ui.page_fluid(
    ui.include_css(app_dir / "styles.css"), # Include CSS
    ui.page_navbar(
        #ui.nav_spacer(),
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
        ui.nav_panel(
            ICONS["icon_db"],
            ui.layout_columns(
                ui.column(6, #
                    ui.card_header("Some text here")
                ), # END column 
                ui.column(6, #
                    ui.card(
                        ui.output_data_frame("data")
                    ) # END card
                ) # END column
            ) # END ui.layout_columns
        ), # END ui.nav_panel # VIEW DB
        ui.nav_panel(
            ICONS["icon_upload"],
            ui.layout_columns(
            ) # END ui.layout_columns
        ), # END ui.nav_panel # UPLOAD
        sidebar=ui.sidebar(
            ui.input_select(
                "db_select",
                "Select Database",
                choices=[
                    "Formulation",
                    "Formulation",
                    "In vitro",
                    "In vivo"
                ] # END choices
            ) # END input_select # db_select
        ), # END sidebar
        id="tabs",
        title="nanomedDB",
        fillable=True,
    ) # END ui.page_navbar
) # END ui.page_fluid

#app_ui = ui.page_navbar(
#    ui.nav_spacer(),
#    ui.nav_panel(
#        "Home",
#        ui.card(ui.card_header("Training Scores")),
#    ),
#    ui.nav_panel(
#        "View Data",
#        ui.layout_columns(
#            ui.column(6, ui.card_header("Some text here")),
#            ui.column(6, ui.card(ui.output_data_frame("data"))),
#        ),
#    ),
#    sidebar=ui.sidebar(
#        ui.input_select(
#            "account",
#            "Account",
#            choices=[
#                "Berge & Berge",
#                "Fritsch & Fritsch",
#                "Hintz & Hintz",
#                "Mosciski and Sons",
#                "Wolff Ltd",
#            ],
#        )
#    ),
#    id="tabs",
#    title="nanomedDB",
#    fillable=True,
#    ui.include_css(app_dir / "styles.css")
#)
 
# SERVER =====================================================================
def server(input: Inputs):
    return None



# BUILD APP ==================================================================
app = App(app_ui, server)
