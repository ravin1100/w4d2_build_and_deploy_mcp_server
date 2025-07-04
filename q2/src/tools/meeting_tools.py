from datetime import datetime, timedelta
from typing import Dict, List, Any
import uuid
from .helper import data_manager, convert_to_utc, get_ai_suggestions
from .scheduling_tools import find_optimal_slots

def create_meeting(title: str, participants: List[str], duration: int, preferences: Dict = None) -> Dict[str, Any]:
    """Create a new meeting with given parameters"""
    # Validate participants exist
    for participant in participants:
        if not data_manager.get_user(participant):
            raise ValueError(f"User {participant} not found")

    # Generate meeting ID
    meeting_id = f"m{str(uuid.uuid4())[:8]}"

    # Get optimal time slot based on preferences
    time_slots = find_optimal_slots(participants, duration, {
        "start": datetime.now().isoformat(),
        "end": (datetime.now() + timedelta(days=7)).isoformat()
    })

    if not time_slots:
        raise ValueError("No suitable time slots found for all participants")

    # Use the first optimal slot
    start_time = time_slots[0]["start"]
    end_time = time_slots[0]["end"]

    # Generate AI-powered agenda suggestions
    suggested_agenda = generate_agenda_suggestions(title, participants)

    # Create meeting object
    meeting = {
        "meeting_id": meeting_id,
        "title": title,
        "participants": participants,
        "start_time": start_time,
        "end_time": end_time,
        "agenda": suggested_agenda,
        "location": "Virtual",  # Default to virtual
        "notes": "",
        "effectiveness_score": None  # Will be updated after the meeting
    }

    # Add to data and save
    data_manager.data["meetings"].append(meeting)
    data_manager.meetings[meeting_id] = meeting
    data_manager.save_data()

    return meeting

def generate_agenda_suggestions(meeting_topic: str, participants: List[str]) -> List[str]:
    """Generate AI-powered agenda suggestions based on topic and participants"""
    # Get participant roles and past meetings
    participant_info = []
    for p_id in participants:
        user = data_manager.get_user(p_id)
        past_meetings = data_manager.get_user_meetings(p_id)
        participant_info.append({
            "name": user["name"],
            "past_meetings": [m["title"] for m in past_meetings[-5:]]  # Last 5 meetings
        })

    # Create prompt for AI
    prompt = f"""
    Generate a structured agenda for a meeting with the following details:
    Topic: {meeting_topic}
    Participants: {', '.join([p['name'] for p in participant_info])}
    
    Consider their recent meetings:
    {participant_info}
    
    Generate 3-5 key agenda items that would make this meeting effective.
    Format: Return only the agenda items as a comma-separated list.
    """

    # Get AI suggestions
    suggestions = get_ai_suggestions(prompt)
    
    # Parse and clean suggestions
    agenda_items = [item.strip() for item in suggestions.split(",")]
    return agenda_items[:5]  # Limit to 5 items 