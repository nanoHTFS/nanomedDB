# MODULES ====================================================================
import faicons as fa

## ICONS ---------------------------------------------------------------------
ICONS = {
    "icon_user": fa.icon_svg("user", "solid"),
    "icon_house": fa.icon_svg("house", "solid"),
    "icon_db": fa.icon_svg("database", "solid"),
    "icon_upload": fa.icon_svg("upload", "solid"),
    "icon_license": fa.icon_svg("file-contract", "solid")
}

## TOP MATTER STRUCTURE ------------------------------------------------------
NP_CLASS = ["All",
            "Lipid-based Nanoparticles",
            "Polymer@Lipid Hybrid Nanoparticles",
            "Polymeric Nanoparticles"]

DB_CHOICES = ["Formulation", "In Vitro", "In Vivo"]

EXP_TYPE_MAPPING = {
  "Formulation": ["Nanoprecipitation", "Emulsion", "Microfluidic"],
  "In Vitro": ["Cell Viability", "NP Uptake", "Therapeutic EFficacy"],
  "In Vivo": ["Biodistribution", "Pharmacokinetics", "Toxicity", "Therapeutic Efficacy"]
}


