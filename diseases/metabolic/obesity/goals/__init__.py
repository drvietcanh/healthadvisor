"""
Goals Module - Mục tiêu và động lực giảm cân
Split into manageable components
"""

from .goal_calculators import (
    create_weight_loss_goal,
    calculate_progress,
    calculate_bmi_goal
)
from .milestones import (
    get_milestones,
    get_milestone_benefits,
    get_celebration
)
from .motivation import (
    get_motivation_message,
    get_goal_recommendation,
    get_weekly_tips,
    get_daily_affirmations
)

__all__ = [
    'create_weight_loss_goal',
    'calculate_progress',
    'get_milestones',
    'get_motivation_message',
    'get_weekly_tips',
    'get_daily_affirmations',
    'calculate_bmi_goal',
    'get_milestone_benefits',
    'get_celebration',
    'get_goal_recommendation'
]
