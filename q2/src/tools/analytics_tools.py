from datetime import datetime, timedelta
from typing import Dict, List, Any
from collections import defaultdict
from .helper import data_manager, get_ai_suggestions

def analyze_meeting_patterns(user_id: str, period: Dict[str, str]) -> Dict[str, Any]:
    """Analyze meeting patterns for a user over a given period"""
    user = data_manager.get_user(user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")
    
    start_date = datetime.fromisoformat(period["start"])
    end_date = datetime.fromisoformat(period["end"])
    
    # Get user's meetings in the period
    meetings = data_manager.get_user_meetings(user_id)
    period_meetings = [
        meeting for meeting in meetings
        if start_date <= datetime.fromisoformat(meeting["start_time"]) <= end_date
    ]
    
    # Calculate metrics
    total_meetings = len(period_meetings)
    total_duration = sum(
        (datetime.fromisoformat(m["end_time"]) - datetime.fromisoformat(m["start_time"])).total_seconds() / 3600
        for m in period_meetings
    )
    
    # Analyze patterns
    day_distribution = defaultdict(int)
    hour_distribution = defaultdict(int)
    effectiveness_scores = []
    
    for meeting in period_meetings:
        start_time = datetime.fromisoformat(meeting["start_time"])
        day_distribution[start_time.strftime("%A")] += 1
        hour_distribution[start_time.hour] += 1
        if meeting.get("effectiveness_score"):
            effectiveness_scores.append(meeting["effectiveness_score"])
    
    return {
        "total_meetings": total_meetings,
        "total_hours": round(total_duration, 2),
        "avg_daily_meetings": round(total_meetings / ((end_date - start_date).days + 1), 2),
        "day_distribution": dict(day_distribution),
        "hour_distribution": dict(hour_distribution),
        "avg_effectiveness": round(sum(effectiveness_scores) / len(effectiveness_scores), 2) if effectiveness_scores else None,
        "most_common_day": max(day_distribution.items(), key=lambda x: x[1])[0] if day_distribution else None,
        "most_common_hour": max(hour_distribution.items(), key=lambda x: x[1])[0] if hour_distribution else None
    }

def calculate_workload_balance(team_members: List[str]) -> Dict[str, Any]:
    """Calculate meeting workload distribution across team"""
    workload_data = {}
    total_team_hours = 0
    
    for user_id in team_members:
        user = data_manager.get_user(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        # Get user's meetings for the next week
        start_date = datetime.now()
        end_date = start_date + timedelta(days=7)
        
        meetings = data_manager.get_user_meetings(user_id)
        upcoming_meetings = [
            meeting for meeting in meetings
            if start_date <= datetime.fromisoformat(meeting["start_time"]) <= end_date
        ]
        
        # Calculate hours in meetings
        meeting_hours = sum(
            (datetime.fromisoformat(m["end_time"]) - datetime.fromisoformat(m["start_time"])).total_seconds() / 3600
            for m in upcoming_meetings
        )
        
        workload_data[user_id] = {
            "name": user["name"],
            "meeting_hours": round(meeting_hours, 2),
            "meeting_count": len(upcoming_meetings)
        }
        total_team_hours += meeting_hours
    
    # Calculate workload distribution and recommendations
    avg_hours = total_team_hours / len(team_members)
    for user_id in workload_data:
        workload_data[user_id]["relative_load"] = round(workload_data[user_id]["meeting_hours"] / avg_hours, 2)
        workload_data[user_id]["status"] = (
            "Overloaded" if workload_data[user_id]["relative_load"] > 1.2
            else "Underutilized" if workload_data[user_id]["relative_load"] < 0.8
            else "Balanced"
        )
    
    return {
        "team_workload": workload_data,
        "total_team_hours": round(total_team_hours, 2),
        "avg_hours_per_member": round(avg_hours, 2)
    }

def score_meeting_effectiveness(meeting_id: str) -> Dict[str, Any]:
    """Score meeting effectiveness and provide improvement suggestions"""
    meeting = data_manager.get_meeting(meeting_id)
    if not meeting:
        raise ValueError(f"Meeting {meeting_id} not found")
    
    # Analyze meeting characteristics
    duration = (datetime.fromisoformat(meeting["end_time"]) - 
               datetime.fromisoformat(meeting["start_time"])).total_seconds() / 3600
    participant_count = len(meeting["participants"])
    has_agenda = bool(meeting.get("agenda"))
    
    # Calculate base score (0-10)
    score = 7  # Start with neutral score
    
    # Adjust score based on factors
    if duration <= 1:  # Shorter meetings are generally more focused
        score += 1
    elif duration > 2:
        score -= 1
    
    if 3 <= participant_count <= 8:  # Optimal group size
        score += 1
    elif participant_count > 12:
        score -= 1
    
    if has_agenda:
        score += 1
    
    # Get AI suggestions for improvement
    prompt = f"""
    Analyze this meeting and suggest improvements:
    - Duration: {duration} hours
    - Participants: {participant_count}
    - Has Agenda: {has_agenda}
    - Title: {meeting['title']}
    
    Provide 3 specific suggestions to improve meeting effectiveness.
    Format: Return suggestions as a comma-separated list.
    """
    
    improvement_suggestions = get_ai_suggestions(prompt).split(",")
    
    return {
        "meeting_id": meeting_id,
        "effectiveness_score": score,
        "factors": {
            "duration": duration,
            "participant_count": participant_count,
            "has_agenda": has_agenda
        },
        "improvement_suggestions": [s.strip() for s in improvement_suggestions]
    }

def optimize_meeting_schedule(user_id: str) -> Dict[str, Any]:
    """Generate schedule optimization recommendations"""
    user = data_manager.get_user(user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")
    
    # Analyze current schedule
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    
    meetings = data_manager.get_user_meetings(user_id)
    upcoming_meetings = [
        meeting for meeting in meetings
        if start_date <= datetime.fromisoformat(meeting["start_time"]) <= end_date
    ]
    
    # Analyze patterns
    daily_meeting_counts = defaultdict(int)
    daily_meeting_hours = defaultdict(float)
    back_to_back_count = 0
    
    for meeting in upcoming_meetings:
        meeting_date = datetime.fromisoformat(meeting["start_time"]).date()
        daily_meeting_counts[meeting_date] += 1
        
        duration = (datetime.fromisoformat(meeting["end_time"]) - 
                   datetime.fromisoformat(meeting["start_time"])).total_seconds() / 3600
        daily_meeting_hours[meeting_date] += duration
    
    # Check for back-to-back meetings
    sorted_meetings = sorted(upcoming_meetings, key=lambda x: x["start_time"])
    for i in range(len(sorted_meetings) - 1):
        current_end = datetime.fromisoformat(sorted_meetings[i]["end_time"])
        next_start = datetime.fromisoformat(sorted_meetings[i + 1]["start_time"])
        if (next_start - current_end).total_seconds() / 60 < 15:  # Less than 15 min break
            back_to_back_count += 1
    
    # Generate optimization recommendations
    recommendations = []
    
    # Check for overloaded days
    overloaded_days = [
        date for date, count in daily_meeting_counts.items()
        if count > 5 or daily_meeting_hours[date] > 6
    ]
    if overloaded_days:
        recommendations.append(f"Consider redistributing meetings from overloaded days: {', '.join(str(d) for d in overloaded_days)}")
    
    # Check for back-to-back meetings
    if back_to_back_count > 0:
        recommendations.append(f"You have {back_to_back_count} back-to-back meetings. Consider adding buffer time between meetings.")
    
    # Get AI suggestions for optimization
    prompt = f"""
    Analyze this schedule and suggest optimizations:
    - Average daily meetings: {sum(daily_meeting_counts.values()) / len(daily_meeting_counts) if daily_meeting_counts else 0}
    - Back-to-back meetings: {back_to_back_count}
    - Overloaded days: {len(overloaded_days)}
    
    Provide 2-3 specific suggestions to optimize the schedule.
    Format: Return suggestions as a comma-separated list.
    """
    
    ai_suggestions = get_ai_suggestions(prompt).split(",")
    recommendations.extend([s.strip() for s in ai_suggestions])
    
    return {
        "schedule_metrics": {
            "total_meetings": len(upcoming_meetings),
            "avg_daily_meetings": round(sum(daily_meeting_counts.values()) / len(daily_meeting_counts), 2) if daily_meeting_counts else 0,
            "back_to_back_meetings": back_to_back_count,
            "overloaded_days": len(overloaded_days)
        },
        "optimization_recommendations": recommendations
    } 