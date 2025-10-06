# ai_analysis.py
import pandas as pd
import numpy as np
import json
from datetime import datetime

# Generate realistic AI usage data (2000-2025)
def generate_ai_data():
    years = list(range(2000, 2026))
    
    # AI adoption phases
    # 2000-2010: Early research & limited applications
    # 2011-2016: Deep learning breakthrough & early commercial use
    # 2017-2021: AI boom & widespread adoption
    # 2022-2025: Generative AI explosion & integration
    
    # Simulate AI adoption rate (% of companies using AI)
    adoption_rate = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 12,  # 2000-2009
        15, 18, 22, 28, 35, 42, 50,      # 2010-2016 (Deep learning impact)
        58, 65, 72, 78, 83, 87, 90,      # 2017-2023
        92, 94, 95                        # 2024-2025
    ]
    
    # AI investment in billions
    investment = [
        0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 2.2, 2.7,  # 2000-2009
        3.5, 4.5, 6.0, 8.5, 12.0, 18.0, 26.0,              # 2010-2016
        40.0, 58.0, 78.0, 95.0, 125.0, 156.0, 200.0,       # 2017-2023
        280.0, 350.0, 420.0                                # 2024-2025
    ]
    
    # AI research papers published (thousands)
    research_papers = [
        3, 3.2, 3.5, 3.8, 4.2, 4.6, 5.1, 5.7, 6.4, 7.2,   # 2000-2009
        8.1, 9.2, 10.5, 12.2, 14.5, 17.5, 21.5,           # 2010-2016
        27.0, 34.0, 42.0, 52.0, 64.0, 78.0, 95.0,         # 2017-2023
        115.0, 138.0, 165.0                               # 2024-2025
    ]
    
    # AI-related job postings (thousands)
    job_postings = [
        5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10,            # 2000-2009
        12, 15, 20, 28, 40, 60, 90,                       # 2010-2016
        140, 210, 320, 480, 650, 850, 1100,               # 2017-2023
        1400, 1750, 2100                                  # 2024-2025
    ]
    
    # Significant AI events
    events = [
        {"year": 2000, "event": "MIT's AI Lab becomes CSAIL"},
        {"year": 2006, "event": "Geoffrey Hinton coins 'Deep Learning'"},
        {"year": 2011, "event": "IBM Watson wins Jeopardy!"},
        {"year": 2012, "event": "AlexNet revolutionizes computer vision"},
        {"year": 2014, "event": "GANs (Generative Adversarial Networks) introduced"},
        {"year": 2016, "event": "AlphaGo defeats Lee Sedol"},
        {"year": 2017, "event": "Transformer architecture published"},
        {"year": 2018, "event": "GPT-1 released by OpenAI"},
        {"year": 2020, "event": "GPT-3 demonstrates remarkable capabilities"},
        {"year": 2022, "event": "ChatGPT launch sparks generative AI boom"},
        {"year": 2023, "event": "AI regulation discussions intensify globally"},
        {"year": 2024, "event": "Multimodal AI models become mainstream"},
        {"year": 2025, "event": "AI integration reaches most industries"}
    ]
    
    # AI hype phases
    hype_phases = [
        {"period": "2000-2006", "phase": "Early Research", "description": "Limited to academia and specialized applications"},
        {"period": "2007-2012", "phase": "Machine Learning Adoption", "description": "ML becomes practical for business applications"},
        {"period": "2013-2018", "phase": "Deep Learning Boom", "description": "Neural networks revolutionize AI capabilities"},
        {"period": "2019-2022", "phase": "AI Integration", "description": "AI becomes embedded in products and services"},
        {"period": "2023-2025", "phase": "Generative AI Era", "description": "Creative AI models transform content creation"}
    ]
    
    return {
        "years": years,
        "adoption_rate": adoption_rate,
        "investment": investment,
        "research_papers": research_papers,
        "job_postings": job_postings,
        "events": events,
        "hype_phases": hype_phases
    }

# Generate and save the data
ai_data = generate_ai_data()

# Save as JSON for the frontend
with open('ai_data.json', 'w') as f:
    json.dump(ai_data, f, indent=2)

print("AI data generated and saved to ai_data.json")