import json
from datetime import datetime
from typing import Dict, List, Any
import pytz
from dateutil import parser
import google.generativeai as genai
from pathlib import Path
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

class MeetingDataManager:
    def __init__(self):
        # Get the project root directory (2 levels up from this file)
        project_root = Path(__file__).parent.parent.parent
        self.data_file = project_root / "data" / "sample_content.json"
        self.load_data()

    def load_data(self) -> None:
        """Load meeting and user data from JSON file"""
        with open(self.data_file, 'r') as f:
            self.data = json.load(f)
            self.users = {user['user_id']: user for user in self.data['users']}
            self.meetings = {meeting['meeting_id']: meeting for meeting in self.data['meetings']}

    def save_data(self) -> None:
        """Save current data back to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get_user(self, user_id: str) -> Dict[str, Any]:
        """Get user details by ID"""
        return self.users.get(user_id)

    def get_meeting(self, meeting_id: str) -> Dict[str, Any]:
        """Get meeting details by ID"""
        return self.meetings.get(meeting_id)

    def get_user_meetings(self, user_id: str) -> List[Dict[str, Any]]:
        """Get all meetings for a specific user"""
        return [meeting for meeting in self.meetings.values() 
                if user_id in meeting['participants']]

def convert_to_utc(time_str: str, timezone: str) -> datetime:
    """Convert local time to UTC"""
    local_tz = pytz.timezone(timezone)
    local_time = parser.parse(time_str)
    if local_time.tzinfo is None:
        local_time = local_tz.localize(local_time)
    return local_time.astimezone(pytz.UTC)

def get_ai_suggestions(prompt: str) -> str:
    """Get AI-powered suggestions using Gemini"""
    response = model.generate_content(prompt)
    return response.text

# Initialize global data manager
data_manager = MeetingDataManager() 