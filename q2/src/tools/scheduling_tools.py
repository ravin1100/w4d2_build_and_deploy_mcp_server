from datetime import datetime, timedelta
from typing import Dict, List, Any
from .helper import data_manager, convert_to_utc

def find_optimal_slots(participants: List[str], duration: int, date_range: Dict[str, str]) -> List[Dict[str, str]]:
    """Find optimal meeting time slots based on participant availability"""
    # Convert date range to UTC
    start_date = datetime.fromisoformat(date_range["start"])
    end_date = datetime.fromisoformat(date_range["end"])
    
    # Get all participants' schedules and preferences
    schedules = {}
    for user_id in participants:
        user = data_manager.get_user(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        # Get user's timezone and working hours
        tz = user["timezone"]
        work_start = convert_to_utc(f"{start_date.date()} {user['working_hours']['start']}", tz)
        work_end = convert_to_utc(f"{start_date.date()} {user['working_hours']['end']}", tz)
        
        # Get user's meetings
        meetings = data_manager.get_user_meetings(user_id)
        
        schedules[user_id] = {
            "work_hours": (work_start, work_end),
            "meetings": meetings,
            "preferences": user["preferences"]
        }
    
    # Find common available slots
    available_slots = []
    current_time = start_date
    slot_duration = timedelta(minutes=duration)
    
    while current_time < end_date:
        slot_end = current_time + slot_duration
        is_available = True
        
        for user_id, schedule in schedules.items():
            # Check if within working hours
            if not is_within_working_hours(current_time, schedule["work_hours"]):
                is_available = False
                break
                
            # Check if conflicts with existing meetings
            if has_meeting_conflict(current_time, slot_end, schedule["meetings"]):
                is_available = False
                break
                
            # Check if conflicts with no-meeting preferences
            if conflicts_with_preferences(current_time, schedule["preferences"]):
                is_available = False
                break
        
        if is_available:
            available_slots.append({
                "start": current_time.isoformat(),
                "end": slot_end.isoformat()
            })
        
        # Move to next 30-minute slot
        current_time += timedelta(minutes=30)
    
    return available_slots

def detect_scheduling_conflicts(user_id: str, time_range: Dict[str, str]) -> List[Dict[str, Any]]:
    """Identify scheduling conflicts for a user in given time range"""
    user = data_manager.get_user(user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")
    
    start_time = datetime.fromisoformat(time_range["start"])
    end_time = datetime.fromisoformat(time_range["end"])
    
    # Get user's meetings in the time range
    meetings = data_manager.get_user_meetings(user_id)
    conflicts = []
    
    for meeting in meetings:
        meeting_start = datetime.fromisoformat(meeting["start_time"])
        meeting_end = datetime.fromisoformat(meeting["end_time"])
        
        # Check if meeting overlaps with the time range
        if (meeting_start <= end_time and meeting_end >= start_time):
            conflicts.append({
                "meeting_id": meeting["meeting_id"],
                "title": meeting["title"],
                "start_time": meeting["start_time"],
                "end_time": meeting["end_time"],
                "participants": meeting["participants"]
            })
    
    return conflicts

def is_within_working_hours(time: datetime, work_hours: tuple) -> bool:
    """Check if time is within working hours"""
    work_start, work_end = work_hours
    current_time = time.time()
    return work_start.time() <= current_time <= work_end.time()

def has_meeting_conflict(start: datetime, end: datetime, meetings: List[Dict]) -> bool:
    """Check if time slot conflicts with existing meetings"""
    for meeting in meetings:
        meeting_start = datetime.fromisoformat(meeting["start_time"])
        meeting_end = datetime.fromisoformat(meeting["end_time"])
        if (start < meeting_end and end > meeting_start):
            return True
    return False

def conflicts_with_preferences(time: datetime, preferences: Dict) -> bool:
    """Check if time conflicts with user preferences"""
    if "no_meetings" in preferences:
        for no_meeting_time in preferences["no_meetings"]:
            start_str, end_str = no_meeting_time.split("-")
            no_meeting_start = datetime.strptime(start_str, "%H:%M").time()
            no_meeting_end = datetime.strptime(end_str, "%H:%M").time()
            if no_meeting_start <= time.time() <= no_meeting_end:
                return True
    return False 