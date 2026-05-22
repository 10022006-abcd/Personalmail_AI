def build_prompt(data):

    prompt = f"""
You are an expert AI email writer.

Generate a realistic, human-like, and well-structured email.

USER PROFILE:
- Name: {data.name}
- Age: {data.age}
- Gender: {data.gender}
- Location: {data.location}
- Profession: {data.profession}
- Income Level: {data.income_level}

EMAIL DETAILS:
- Purpose: {data.purpose}
- Recipient Type: {data.recipient_type}
- Relationship With Recipient: {data.relationship}
- Tone: {data.tone}
- Length: {data.length}
- Urgency: {data.urgency}
- Language: {data.language}

ADDITIONAL CONTEXT:
{data.additional_context}

INSTRUCTIONS:
- Generate a professional and contextual email
- Adapt writing style intelligently
- Generate a subject line
- Ensure proper formatting
- Make the email detailed and realistic
- Avoid repetitive text
- Make the tone match the requested style

OUTPUT FORMAT:

Subject:
<generated subject>

Email:
<generated email>
"""

    return prompt