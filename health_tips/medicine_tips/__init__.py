"""
Medicine Tips Module
Module mẹo vặt về thuốc
"""

from health_tips.medicine_tips.storage_tab import render_storage_tab
from health_tips.medicine_tips.taking_tab import render_taking_tab
from health_tips.medicine_tips.food_interactions_tab import render_food_interactions_tab
from health_tips.medicine_tips.drug_interactions_tab import render_drug_interactions_tab
from health_tips.medicine_tips.missed_dose_tab import render_missed_dose_tab
from health_tips.medicine_tips.reading_labels_tab import render_reading_labels_tab

__all__ = [
    "render_storage_tab",
    "render_taking_tab",
    "render_food_interactions_tab",
    "render_drug_interactions_tab",
    "render_missed_dose_tab",
    "render_reading_labels_tab"
]

