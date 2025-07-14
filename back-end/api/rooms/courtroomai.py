from flask import Blueprint, request, jsonify
import random
import pandas as pd

courtroom_bp = Blueprint("courtroom", __name__)

@courtroom_bp.route("/debate", methods=["POST"])
def courtroom_debate():
    debate_scripts = [
        {
            "title": "🔍 Theft at the Office",
            "summary": "A case of suspected theft at a corporate office. Lawyer A defends an employee accused of stealing company data. Lawyer B represents the prosecution.",
            "A": [
                "My client had no access to the secure servers.",
                "There is no CCTV evidence showing any wrongdoing.",
                "The logs were manipulated after the fact.",
                "He was on approved leave during the incident.",
                "He reported suspicious behavior earlier.",
                "Other employees had stronger motives.",
                "No stolen data was ever found on his devices.",
                "The IT department failed to follow protocol.",
                "Anonymous tips don’t hold legal ground.",
                "The accusation is built on speculation."
            ],
            "B": [
                "He had admin-level access to internal systems.",
                "Logs show activity from his credentials.",
                "Multiple coworkers raised concerns.",
                "A USB was found at his desk with sensitive info.",
                "He wiped his machine hours after the incident.",
                "Why would he report others but not provide proof?",
                "All evidence points to insider theft.",
                "We traced login attempts to his IP.",
                "He was under performance review — motive is clear.",
                "There’s no plausible alternative suspect."
            ]
        },
        {
            "title": "🏠 Land Dispute Between Neighbors",
            "summary": "A property boundary case between two neighbors disputing a 3-meter strip of land. Lawyer A defends the long-time owner. Lawyer B represents the recent buyer.",
            "A": [
                "My client has lived there for over 20 years.",
                "They have maintained the land continuously.",
                "They paid taxes on it without fail.",
                "Old surveys support their claim.",
                "They built a fence over 10 years ago.",
                "Witnesses confirm their occupation.",
                "They have legal precedence through adverse possession.",
                "The recent buyer ignored property records.",
                "Municipal documents show no new claim filed.",
                "They even planted trees years ago!"
            ],
            "B": [
                "The deed clearly includes the disputed land.",
                "They were never challenged during purchase.",
                "Property markers align with our claim.",
                "Their fence crosses our boundary line.",
                "The survey was outdated and inaccurate.",
                "Paying taxes doesn’t equal ownership.",
                "They never registered their claim formally.",
                "Their argument is based on assumption.",
                "The city plan shows the land as part of our lot.",
                "We're the legal title holders, case closed."
            ]
        },
        {
            "title": "📱 Defamation via Social Media",
            "summary": "A defamation suit where Lawyer A defends a celebrity accused of spreading false info. Lawyer B represents the affected party.",
            "A": [
                "The statement was opinion, not fact.",
                "There’s no intent to harm — it was commentary.",
                "The post was deleted within an hour.",
                "The account was compromised briefly.",
                "My client issued an apology.",
                "There's no financial damage proven.",
                "Freedom of speech must be upheld.",
                "The statements were based on public reports.",
                "We request expert analysis on media manipulation.",
                "No lawsuit was filed until weeks later."
            ],
            "B": [
                "The tweet had 1 million views — damage was done.",
                "They tagged the victim directly.",
                "Screenshots continue to circulate.",
                "They have influence and responsibility.",
                "The apology came only after backlash.",
                "The harm was both emotional and professional.",
                "Endorsement of false claims is still defamation.",
                "Intent can be inferred by context.",
                "Sponsorships were lost as a result.",
                "A public platform requires public accountability."
            ]
        }
    ]

    script = random.choice(debate_scripts)

    count = random.randint(5, 7)
    lines_a = random.sample(script["A"], count)
    lines_b = random.sample(script["B"], count)

    df = pd.DataFrame({"A": lines_a, "B": lines_b})
    score_a = df["A"].str.count(r"no|not|false|lack|innocent|report|alibi|error|unfounded").sum()
    score_b = df["B"].str.count(r"found|motive|proof|evidence|confirmed|records|damage").sum()

    if score_a > score_b:
        verdict = "Lawyer A wins! Defense made a compelling argument."
    elif score_b > score_a:
        verdict = "Lawyer B wins! Prosecution presented stronger evidence."
    else:
        verdict = "It's a tie! The case remains unresolved."

    return jsonify({
        "summary": script["summary"],
        "lawyer_a": lines_a,
        "lawyer_b": lines_b,
        "verdict": verdict
    })
