from fastmcp import FastMCP
from tools.meeting_tools import create_meeting
from tools.scheduling_tools import find_optimal_slots, detect_scheduling_conflicts
from tools.analytics_tools import (
    analyze_meeting_patterns,
    calculate_workload_balance,
    score_meeting_effectiveness,
    optimize_meeting_schedule
)

app = FastMCP("Meeting Planner MCP")

# Register MCP tools
@app.tool("create_meeting")
def mcp_create_meeting(title: str, participants: list, duration: int, preferences: dict = None) -> dict:
    """Schedule a new meeting with given parameters"""
    return create_meeting(title, participants, duration, preferences)

@app.tool("find_optimal_slots")
def mcp_find_optimal_slots(participants: list, duration: int, date_range: dict) -> list:
    """Find optimal meeting time slots based on participant availability"""
    return find_optimal_slots(participants, duration, date_range)

@app.tool("detect_conflicts")
def mcp_detect_conflicts(user_id: str, time_range: dict) -> list:
    """Identify scheduling conflicts for a user in given time range"""
    return detect_scheduling_conflicts(user_id, time_range)

@app.tool("analyze_patterns")
def mcp_analyze_patterns(user_id: str, period: dict) -> dict:
    """Analyze meeting patterns for a user over a given period"""
    return analyze_meeting_patterns(user_id, period)

@app.tool("suggest_agenda")
def mcp_suggest_agenda(meeting_topic: str, participants: list) -> list:
    """Generate AI-powered agenda suggestions"""
    return generate_agenda_suggestions(meeting_topic, participants)

@app.tool("balance_workload")
def mcp_balance_workload(team_members: list) -> dict:
    """Calculate meeting workload distribution across team"""
    return calculate_workload_balance(team_members)

@app.tool("score_meeting")
def mcp_score_meeting(meeting_id: str) -> dict:
    """Score meeting effectiveness and provide improvement suggestions"""
    return score_meeting_effectiveness(meeting_id)

@app.tool("optimize_schedule")
def mcp_optimize_schedule(user_id: str) -> dict:
    """Generate schedule optimization recommendations"""
    return optimize_meeting_schedule(user_id)

if __name__ == "__main__":
    app.run() 