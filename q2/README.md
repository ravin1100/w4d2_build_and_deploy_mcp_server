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

1. Clone the repository and navigate to the project directory
2. Create and activate a virtual environment
3. Install dependencies using requirements.txt
4. Configure environment variables in .env file
5. Run the server using src/main.py

## 📚 MCP Tools Documentation

### Meeting Management Tools

#### 1. Create Meeting (mcp_create_meeting)
Creates a new meeting with intelligent scheduling features. Takes meeting title, participant list, duration, and optional preferences as input. The tool:
- Validates participant availability
- Finds optimal meeting time
- Generates AI-powered agenda
- Handles time zone differences
- Creates a unique meeting ID
- Saves meeting details

#### 2. Find Optimal Slots (mcp_find_optimal_slots)
Discovers the best available time slots for meetings. Considers:
- Participant working hours
- Time zone differences
- Existing commitments
- No-meeting preferences
- Team workload balance
Returns a list of available time slots ranked by suitability.

#### 3. Detect Scheduling Conflicts (mcp_detect_conflicts)
Identifies potential scheduling conflicts for users. Features:
- Time zone aware conflict detection
- Working hours validation
- Overlap analysis
- Buffer time consideration
Returns detailed conflict information including affected meetings.

### Analytics and Insights Tools

#### 4. Analyze Meeting Patterns (mcp_analyze_patterns)
Examines meeting behavior and trends. Analyzes:
- Meeting frequency
- Duration patterns
- Participant engagement
- Time slot preferences
- Productivity metrics
Provides insights for better meeting planning.

#### 5. Generate Agenda Suggestions (mcp_suggest_agenda)
AI-powered tool for creating meeting agendas. Considers:
- Meeting topic
- Participant roles
- Historical meeting data
- Previous agenda patterns
- Team dynamics
Generates contextually relevant agenda items.

#### 6. Calculate Workload Balance (mcp_balance_workload)
Assesses meeting load distribution across team members. Features:
- Meeting hour calculations
- Workload comparison
- Overload detection
- Balance recommendations
- Team capacity analysis

#### 7. Score Meeting Effectiveness (mcp_score_meeting)
Evaluates meeting productivity and provides improvement suggestions. Analyzes:
- Duration efficiency
- Participant count
- Agenda completion
- Meeting objectives
- Follow-up actions
Provides a numerical score and actionable recommendations.

#### 8. Optimize Schedule (mcp_optimize_schedule)
Generates schedule optimization recommendations. Considers:
- Meeting patterns
- Break times
- Focus periods
- Team availability
- Workload distribution
Provides personalized scheduling improvements.

## 📊 Data Models

### User Profile
Stores user-specific information including:
- Personal details (name, email)
- Time zone preferences
- Working hours
- Meeting preferences
- No-meeting periods

### Meeting Record
Contains meeting-related data including:
- Meeting details (ID, title)
- Participant information
- Timing information
- Agenda and notes
- Effectiveness metrics

## 🔧 Configuration

### Environment Variables
- GOOGLE_API_KEY: For AI features
- HOST: Server host address
- PORT: Server port number
- DEBUG: Debug mode toggle

### Sample Data
Includes comprehensive test data:
- Multiple users across time zones
- Various meeting types
- Different scheduling patterns
- Preference examples

## 🤝 Best Practices

### Time Management
- Use ISO format with timezone
- Consider global time differences
- Maintain buffer periods
- Respect working hours

### Meeting Optimization
- Keep meetings focused
- Include necessary breaks
- Balance team workload
- Monitor effectiveness

### AI Feature Usage
- Provide clear contexts
- Review AI suggestions
- Update preferences regularly
- Monitor effectiveness scores

## 🔍 Troubleshooting

### Common Issues
1. API Key Problems
   - Configuration issues
   - Permission settings
   - Key validation

2. Scheduling Conflicts
   - Time zone mismatches
   - Preference conflicts
   - Availability issues

3. Performance Concerns
   - Query optimization
   - Data management
   - Response times

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 