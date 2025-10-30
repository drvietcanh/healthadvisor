"""
Data models for HealthAdvisor - Multi-disease health consultation app.
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime


# ============= Common Symptom Models =============

class GeneralSymptoms(BaseModel):
    """General symptoms checker."""
    fever: bool = False
    fatigue: bool = False
    weight_loss: bool = False
    weight_gain: bool = False
    night_sweats: bool = False
    appetite_change: bool = False


class CardiovascularSymptoms(BaseModel):
    """Cardiovascular-related symptoms."""
    chest_pain: bool = False
    chest_pain_severity: Optional[int] = Field(None, ge=1, le=10)
    shortness_of_breath: bool = False
    palpitations: bool = False
    leg_swelling: bool = False
    fainting: bool = False
    irregular_heartbeat: bool = False


class StrokeSymptoms(BaseModel):
    """Stroke-specific symptoms (BE-FAST)."""
    balance_loss: bool = False
    vision_problems: bool = False
    facial_droop: bool = False
    arm_weakness: bool = False
    speech_difficulty: bool = False
    sudden_severe_headache: bool = False
    confusion: bool = False
    onset_time_hours: Optional[float] = None


class DiabetesSymptoms(BaseModel):
    """Diabetes-related symptoms."""
    excessive_thirst: bool = False
    frequent_urination: bool = False
    unexplained_hunger: bool = False
    blurred_vision: bool = False
    slow_healing_wounds: bool = False
    tingling_hands_feet: bool = False
    recurrent_infections: bool = False


class HypertensionSymptoms(BaseModel):
    """Hypertension-related symptoms."""
    headache: bool = False
    dizziness: bool = False
    nosebleeds: bool = False
    shortness_of_breath: bool = False
    chest_pain: bool = False
    visual_changes: bool = False


# ============= Patient Profile =============

class PatientProfile(BaseModel):
    """Patient demographic and risk factor profile."""
    age: int = Field(..., ge=0, le=120)
    gender: Literal["male", "female", "other"]
    weight_kg: Optional[float] = None
    height_cm: Optional[float] = None
    
    # Risk factors
    smoking: bool = False
    alcohol_use: Literal["none", "moderate", "heavy"] = "none"
    physical_activity: Literal["sedentary", "light", "moderate", "active"] = "sedentary"
    
    # Medical history
    family_history_heart_disease: bool = False
    family_history_stroke: bool = False
    family_history_diabetes: bool = False
    
    # Current conditions
    has_hypertension: bool = False
    has_diabetes: bool = False
    has_high_cholesterol: bool = False
    has_heart_disease: bool = False
    
    # Current medications
    on_blood_thinners: bool = False
    on_bp_medication: bool = False
    on_diabetes_medication: bool = False


# ============= Assessment Results =============

class RiskLevel(str):
    """Risk level categories."""
    EMERGENCY = "EMERGENCY"  # Call 115 immediately
    HIGH = "HIGH"            # See doctor within 24-48 hours
    MODERATE = "MODERATE"    # Schedule appointment within 1-2 weeks
    LOW = "LOW"              # Lifestyle modifications, routine checkup


class DiseaseAssessment(BaseModel):
    """Assessment result for a specific disease."""
    disease_name_vn: str
    disease_name_en: str
    risk_level: Literal["EMERGENCY", "HIGH", "MODERATE", "LOW"]
    risk_score: Optional[float] = Field(None, ge=0, le=100)
    
    # Messages
    summary_vn: str
    summary_en: str
    recommendations_vn: List[str] = Field(default_factory=list)
    recommendations_en: List[str] = Field(default_factory=list)
    
    # What to do next
    action_needed_vn: str
    action_needed_en: str
    
    # Warning signs
    warning_signs_vn: List[str] = Field(default_factory=list)
    warning_signs_en: List[str] = Field(default_factory=list)


# ============= Nutrition & Lifestyle =============

class NutritionPlan(BaseModel):
    """Personalized nutrition recommendations."""
    disease: str
    
    # Foods to eat
    recommended_foods_vn: List[str] = Field(default_factory=list)
    recommended_foods_en: List[str] = Field(default_factory=list)
    
    # Foods to avoid
    avoid_foods_vn: List[str] = Field(default_factory=list)
    avoid_foods_en: List[str] = Field(default_factory=list)
    
    # Meal suggestions
    meal_suggestions_vn: List[str] = Field(default_factory=list)
    meal_suggestions_en: List[str] = Field(default_factory=list)
    
    # Nutrients to focus on
    key_nutrients_vn: List[str] = Field(default_factory=list)
    key_nutrients_en: List[str] = Field(default_factory=list)
    
    # Daily targets
    calorie_target: Optional[str] = None
    sodium_limit_mg: Optional[int] = None
    sugar_limit_g: Optional[int] = None
    water_intake_liters: Optional[float] = None


class LifestylePlan(BaseModel):
    """Personalized lifestyle recommendations."""
    disease: str
    
    # Exercise recommendations
    exercise_type_vn: List[str] = Field(default_factory=list)
    exercise_type_en: List[str] = Field(default_factory=list)
    exercise_frequency: str = ""
    exercise_duration_minutes: int = 0
    
    # Sleep recommendations
    sleep_hours: str = ""
    sleep_tips_vn: List[str] = Field(default_factory=list)
    sleep_tips_en: List[str] = Field(default_factory=list)
    
    # Stress management
    stress_management_vn: List[str] = Field(default_factory=list)
    stress_management_en: List[str] = Field(default_factory=list)
    
    # Lifestyle modifications
    lifestyle_changes_vn: List[str] = Field(default_factory=list)
    lifestyle_changes_en: List[str] = Field(default_factory=list)
    
    # Things to avoid
    avoid_vn: List[str] = Field(default_factory=list)
    avoid_en: List[str] = Field(default_factory=list)


# ============= Clinical Scores =============

class ABCD2Score(BaseModel):
    """ABCD2 score for TIA risk assessment."""
    age_60_or_older: bool = False
    bp_elevated: bool = False
    clinical_weakness: bool = False
    clinical_speech_only: bool = False
    duration_60_plus: bool = False
    duration_10_59: bool = False
    diabetes: bool = False
    
    def calculate(self) -> int:
        score = 0
        if self.age_60_or_older: score += 1
        if self.bp_elevated: score += 1
        if self.clinical_weakness: score += 2
        elif self.clinical_speech_only: score += 1
        if self.duration_60_plus: score += 2
        elif self.duration_10_59: score += 1
        if self.diabetes: score += 1
        return score


class HeartDiseaseRisk(BaseModel):
    """10-year cardiovascular disease risk assessment."""
    age: int
    gender: Literal["male", "female"]
    total_cholesterol: Optional[float] = None  # mg/dL
    hdl_cholesterol: Optional[float] = None    # mg/dL
    systolic_bp: Optional[int] = None
    smoking: bool = False
    diabetes: bool = False
    on_bp_medication: bool = False


class DiabetesRisk(BaseModel):
    """Diabetes risk assessment."""
    age: int
    bmi: float
    waist_circumference_cm: Optional[float] = None
    physical_activity_regular: bool = False
    family_history: bool = False
    history_high_bp: bool = False
    history_gestational_diabetes: bool = False


# ============= Health Tips =============

class HealthTip(BaseModel):
    """Daily health tips."""
    category: Literal["nutrition", "exercise", "mental_health", "sleep", "prevention"]
    title_vn: str
    title_en: str
    content_vn: str
    content_en: str
    source: str = ""
