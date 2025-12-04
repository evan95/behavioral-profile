ANIMALS = ["Lion", "Owl", "Dolphin", "Beaver", "Falcon", "Deer"]

# 16 questions with 6 options each mapped to animals in order [Lion,Owl,Dolphin,Beaver,Falcon,Deer]
QUESTIONS = [
    {
        "id": 1,
        "text": "When I need to make an important decision, I:",
        "options": [
            "Take the lead and decide quickly.",
            "Gather data and follow the plan.",
            "Talk to colleagues to hear opinions.",
            "Follow the procedure that always worked.",
            "Act fast and take calculated risks.",
            "Avoid decisions until I feel sure."
        ]
    },
    {
        "id": 2,
        "text": "In team meetings, I usually:",
        "options": [
            "Direct the focus and keep things objective.",
            "Ask technical questions and seek clarification.",
            "Bring energy, encourage and connect people.",
            "Record actions and ensure follow-up.",
            "Challenge ideas to see which one prevails.",
            "Listen more than I speak."
        ]
    },
    {
        "id": 3,
        "text": "When a conflict appears, I:",
        "options": [
            "Make a decisive decision to end it.",
            "Analyze reasons before acting.",
            "Facilitate communication between the parties.",
            "Look for practical, step-by-step solutions.",
            "Face the problem directly.",
            "Try to calm everyone and seek harmony."
        ]
    },
    {
        "id": 4,
        "text": "In a project with tight deadlines, my role tends to be:",
        "options": [
            "Coordinator who defines priorities.",
            "Risk and quality analyst.",
            "Motivator who keeps morale high.",
            "Methodical executor — I complete tasks reliably.",
            "Driver — I accelerate deliveries.",
            "Support — ensuring no one becomes overloaded."
        ]
    },
    {
        "id": 5,
        "text": "I prefer a work environment that is:",
        "options": [
            "Competitive and goal-oriented.",
            "Structured and predictable.",
            "Collaborative and social.",
            "Stable with clear processes.",
            "Dynamic and challenging.",
            "Safe and low in conflict."
        ]
    },
    {
        "id": 6,
        "text": "When I receive critical feedback, I:",
        "options": [
            "Accept it if it is useful for achieving results.",
            "Want examples and data on how to improve.",
            "Thank the person and try to harmonize.",
            "Create a practical action plan.",
            "Initially react by defending my choices.",
            "Take it into consideration and try to adjust."
        ]
    },
    {
        "id": 7,
        "text": "My ideal working style is:",
        "options": [
            "Setting clear goals and delegating.",
            "Detailed planning before starting.",
            "Working in pairs or teams.",
            "Predictable routine with checklists.",
            "Acting quickly, adjusting later.",
            "Going slow and carefully."
        ]
    },
    {
        "id": 8,
        "text": "How do I deal with sudden changes?",
        "options": [
            "Reassume control and redesign priorities.",
            "Evaluate the impact before acting.",
            "Talk with the team to realign.",
            "Follow processes to minimize errors.",
            "Adapt quickly and take advantage of opportunities.",
            "Feel insecure and seek support."
        ]
    },
    {
        "id": 9,
        "text": "In long projects, my strength is:",
        "options": [
            "Maintaining focus on the final objective.",
            "Maintaining technical quality.",
            "Keeping the team motivated.",
            "Consistency and continuous delivery.",
            "Overcoming obstacles through action.",
            "Sensitivity to others' needs."
        ]
    },
    {
        "id": 10,
        "text": "When someone proposes a new idea, I:",
        "options": [
            "Evaluate if it brings competitive advantage.",
            "Want to see the logic behind it.",
            "Ask how it affects people.",
            "Check whether it fits the process.",
            "Test it quickly if possible.",
            "Worry about risks to stability."
        ]
    },
    {
        "id": 11,
        "text": "My role in a team that is missing deadlines:",
        "options": [
            "Organize, lead, and define priorities.",
            "Diagnose technical problems.",
            "Provide emotional and moral support.",
            "Work extra hours to catch up.",
            "Push for faster decisions.",
            "Try to reduce team stress."
        ]
    },
    {
        "id": 12,
        "text": "How close colleagues describe me:",
        "options": [
            "Confident and decisive.",
            "Rational and precise.",
            "Friendly and empathetic.",
            "Reliable and dedicated.",
            "Ambitious and driven.",
            "Calm and attentive."
        ]
    },
    {
        "id": 13,
        "text": "What motivates me most at work:",
        "options": [
            "Achieving goals and recognition.",
            "Solving complex problems.",
            "Relationships and environment.",
            "Doing things well with a healthy routine.",
            "Overcoming competition and challenges.",
            "Working in a safe environment."
        ]
    },
    {
        "id": 14,
        "text": "How I organize my day:",
        "options": [
            "Priorities tied to results.",
            "Time blocks for analysis.",
            "Flexible schedule with interaction.",
            "Task lists and checklists.",
            "Adjust according to urgency.",
            "Include plenty of breaks."
        ]
    },
    {
        "id": 15,
        "text": "When a failure occurs, I:",
        "options": [
            "Make changes to prevent recurrence.",
            "Investigate the root cause.",
            "Communicate and support the team.",
            "Fix the error step-by-step.",
            "Take quick corrective action.",
            "Feel shaken but try to help."
        ]
    },
    {
        "id": 16,
        "text": "If I could choose my ideal professional function, it would be:",
        "options": [
            "Manager / Project Leader",
            "Analyst / Technical Specialist",
            "HR / Facilitator / Customer Success",
            "Operations / Execution",
            "Sales / Strategy",
            "Support / Counseling"
        ]
    }
]

# helper: map question idx and chosen option idx to scoring vector
def map_option_to_vector(question_idx, option_idx):
    # each option corresponds directly to animal in ANIMALS order
    vec = [0] * len(ANIMALS)
    if 0 <= option_idx < len(ANIMALS):
        vec[option_idx] = 3  # award 3 points to chosen animal
    return vec
