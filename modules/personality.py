ANIMAL_DESCRIPTIONS = {
    "Lion": """Lions are natural leaders who thrive in fast-paced and competitive environments.
They are confident, assertive, and take responsibility without hesitation. Their strength lies in their ability to make quick decisions, mobilize teams, and keep projects focused on clear objectives. Lions communicate directly and value efficiency, clarity, and results. They may become impatient with slow progress or excessive analysis, but their determination pushes teams forward. They excel in roles requiring direction, strategy, and high-impact decision-making.""",

    "Owl": """Owls are analytical, precise, and deeply logical. They feel most comfortable in structured environments where they can research, evaluate, and reduce risks. Their attention to detail and commitment to accuracy make them excellent problem-solvers. Owls prefer well-defined processes and take time to analyze a situation before making decisions. Their communication is calm, objective, and fact-based. They excel in roles involving data, investigation, engineering, planning, and quality assurance.""",

    "Dolphin": """Dolphins are creative, adaptable, and deeply attuned to human emotions. They thrive in collaborative and inspiring environments, where innovation and imagination are appreciated. Dolphins are excellent communicators who bring harmony to groups, encouraging connection and teamwork. They value authenticity, emotional well-being, and meaningful interactions. Their optimism and flexibility allow them to handle change gracefully. Dolphins often uplift those around them with positivity and empathy, making them uniquely gifted at building strong relationships and fostering supportive communities.""",

    "Beaver": """Beavers are organized, methodical, and committed to structure. They believe that success is built through discipline, consistency, and well-defined processes. They are reliable executors who follow procedures carefully and ensure that work is done correctly. Beavers bring stability to long-term projects, maintain order, and reduce uncertainty. They excel in areas such as operations, compliance, financial processes, and systematic workflow execution.""",

    "Falcon": """Falcons are dynamic, fast-thinking, and action-oriented. They love challenges, competition, and innovation. Falcons adapt quickly, make decisions rapidly, and embrace opportunities with confidence. They prefer experimentation over long analysis and often break through stagnation with their energy. Falcons are ideal for entrepreneurial roles, sales, strategy, growth teams, and any context where speed and initiative drive success.""",

    "Deer": """Deer are gentle, calm, and emotionally intuitive. They value stability, understanding, and respectful environments. Their natural empathy allows them to support others, detect emotional needs, and create safe spaces for communication. They avoid conflict and focus on cooperation. Deers thrive in roles requiring patience, emotional intelligence, service orientation, and supportive functions such as counseling, care, customer empathy, and coordination.""" 
}

ANIMAL_RECOMMENDATIONS = {
    "Lion": "Practical tips: ask for regular feedback, delegate clear tasks, and practice patience when others need time to analyze.",
    "Owl": "Practical tips: share your conclusions early, practice concise summaries, and set time limits to avoid analysis paralysis.",
    "Dolphin": "Practical tips: balance creativity with simple plans, create rituals for follow-through, and practice boundaries to avoid overload.",
    "Beaver": "Practical tips: allow small changes occasionally, document wins visibly, and practice flexibility exercises.",
    "Falcon": "Practical tips: test ideas in small steps, communicate expectations clearly, and include checkpoints for risk control.",
    "Deer": "Practical tips: build assertiveness practice, set safe deadlines, and use scheduled check-ins to reduce anxiety."
}

ANIMAL_STRENGTHS_WEAKNESSES = {
    "Lion": {
        "strengths": ["Decisive", "Goal-oriented", "Confident"],
        "weaknesses": ["Impatient", "Can overlook details", "Direct communication may feel blunt"]
    },
    "Owl": {
        "strengths": ["Analytical", "Thorough", "Dependable"],
        "weaknesses": ["Overthinks", "Slow to decide", "May seem distant"]
    },
    "Dolphin": {
        "strengths": ["Empathetic", "Creative", "Great communicator"],
        "weaknesses": ["Can be disorganized", "May avoid difficult decisions", "People-pleasing"]
    },
    "Beaver": {
        "strengths": ["Organized", "Consistent", "Process-driven"],
        "weaknesses": ["Resistant to change", "Can be rigid", "May prefer routine over innovation"]
    },
    "Falcon": {
        "strengths": ["Fast", "Bold", "Innovative"],
        "weaknesses": ["Risk-prone", "May rush planning", "Can be perceived as aggressive"]
    },
    "Deer": {
        "strengths": ["Sensitive", "Supportive", "Calm"],
        "weaknesses": ["Conflict-avoidant", "May be indecisive", "Can take criticism personally"]
    }
}

def map_option_to_vector(option: int):
    """
    Maps the numeric answer (1–6) to the correct animal.
    """
    mapping = {
        0: "Beaver",
        1: "Deer",
        2: "Dolphin",
        3: "Falcon",
        4: "Lion",
        5: "Owl"
    }

    return mapping.get(option)