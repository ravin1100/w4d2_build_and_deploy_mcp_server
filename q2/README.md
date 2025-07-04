# Smart Meeting Assistant with AI Scheduling

An intelligent MCP server that revolutionizes meeting management with AI-powered features for scheduling, optimization, and analytics. The system handles complex scheduling scenarios across multiple time zones while considering user preferences and workload balance.

## 🌟 Features

### Intelligent Scheduling
- Smart meeting scheduling with automatic conflict detection
- Time zone aware scheduling across global teams
- Respects user preferences and working hours
- Optimal time slot recommendations based on participant availability

### AI-Powered Analytics
- Meeting pattern analysis (frequency, duration, productivity)
- Automatic agenda generation using historical data
- Participant workload balancing
- Meeting effectiveness scoring with improvement suggestions
- Schedule optimization recommendations

### User-Centric Design
- Customizable user preferences
- No-meeting time blocks
- Preferred meeting days/times
- Working hours respect
- Virtual/physical location management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)
- Google API Key for Gemini AI features

### Installation

1. Clone the repository and navigate to the project:
   ```bash
   git clone <repository-url>
   cd project-directory
   ```

2. Create and activate virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Unix/MacOS
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   # Create .env file
   touch .env

   # Add the following to .env
   GOOGLE_API_KEY=your_api_key_here
   HOST=0.0.0.0
   PORT=8000
   DEBUG=True
   ```

5. Run the server:
   ```bash
   python src/main.py
   ```

## 📚 API Documentation

### Meeting Management

#### 1. Create Meeting
```python
mcp_create_meeting(
    title: str,
    participants: List[str],
    duration: int,
    preferences: Dict = None
) -> Dict

# Example
response = mcp_create_meeting(
    title="Q2 Planning Review",
    participants=["u1", "u2", "u3"],
    duration=60,
    preferences={"preferred_time": "morning"}
)
```

#### 2. Find Optimal Slots
```python
mcp_find_optimal_slots(
    participants: List[str],
    duration: int,
    date_range: Dict[str, str]
) -> List[Dict]

# Example
slots = mcp_find_optimal_slots(
    participants=["u1", "u2"],
    duration=45,
    date_range={
        "start": "2025-07-10T00:00:00+00:00",
        "end": "2025-07-11T23:59:59+00:00"
    }
)
```

#### 3. Detect Scheduling Conflicts
```python
mcp_detect_conflicts(
    user_id: str,
    time_range: Dict[str, str]
) -> List[Dict]

# Example
conflicts = mcp_detect_conflicts(
    user_id="u1",
    time_range={
        "start": "2025-07-01T00:00:00+00:00",
        "end": "2025-07-02T23:59:59+00:00"
    }
)
```

### Analytics and Insights

#### 4. Analyze Meeting Patterns
```python
mcp_analyze_patterns(
    user_id: str,
    period: Dict[str, str]
) -> Dict

# Example
patterns = mcp_analyze_patterns(
    user_id="u1",
    period={
        "start": "2025-06-01T00:00:00+00:00",
        "end": "2025-06-30T23:59:59+00:00"
    }
)
```

#### 5. Generate Agenda Suggestions
```python
mcp_suggest_agenda(
    meeting_topic: str,
    participants: List[str]
) -> List[str]

# Example
agenda = mcp_suggest_agenda(
    meeting_topic="Product Launch Strategy",
    participants=["u1", "u2", "u3"]
)
```

#### 6. Calculate Workload Balance
```python
mcp_balance_workload(
    team_members: List[str]
) -> Dict

# Example
workload = mcp_balance_workload(
    team_members=["u1", "u2", "u3", "u4"]
)
```

#### 7. Score Meeting Effectiveness
```python
mcp_score_meeting(
    meeting_id: str
) -> Dict

# Example
score = mcp_score_meeting(meeting_id="m1")
```

#### 8. Optimize Schedule
```python
mcp_optimize_schedule(
    user_id: str
) -> Dict

# Example
optimization = mcp_optimize_schedule(user_id="u1")
```

## 📊 Data Models

### User Schema
```json
{
  "user_id": "u1",
  "name": "John Doe",
  "email": "john@example.com",
  "timezone": "America/New_York",
  "working_hours": {
    "start": "09:00",
    "end": "17:00"
  },
  "preferences": {
    "no_meetings": ["12:00-13:00"],
    "preferred_days": ["Monday", "Wednesday"]
  }
}
```

### Meeting Schema
```json
{
  "meeting_id": "m1",
  "title": "Project Review",
  "participants": ["u1", "u2"],
  "start_time": "2025-03-15T10:00:00-04:00",
  "end_time": "2025-03-15T11:00:00-04:00",
  "agenda": ["Status Update", "Next Steps"],
  "location": "Virtual",
  "notes": "",
  "effectiveness_score": 8
}
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Required for AI-powered features
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `DEBUG`: Debug mode (default: True)

### Sample Data
The system comes with sample data in `data/sample_content.json`:
- 10+ users across different time zones
- 60+ meetings with various patterns
- Different meeting types and configurations

## 🤝 Best Practices

### Time Handling
- Always use ISO format with timezone offset
- Consider participant time zones when scheduling
- Use UTC for internal operations

### Meeting Optimization
- Keep meetings under 60 minutes when possible
- Include breaks between meetings
- Respect lunch hours and no-meeting preferences
- Balance workload across team members

### AI Features Usage
- Provide clear meeting topics for better agenda suggestions
- Include relevant participants for context
- Review and adjust AI suggestions as needed

## 🔍 Troubleshooting

### Common Issues
1. **API Key Issues**
   - Ensure GOOGLE_API_KEY is set in .env
   - Verify API key has required permissions

2. **Scheduling Conflicts**
   - Check time zone configurations
   - Verify working hours settings
   - Review no-meeting preferences

3. **Performance Issues**
   - Optimize date range queries
   - Limit participant list size
   - Use appropriate time slots

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 