from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow frontend to make API requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Word bank with different difficulty levels
word_bank = {
    "easy": [
        {"word": "Happy", "correct_answer": "Joyful", "options": ["Sad", "Angry", "Joyful"]},
        {"word": "Big", "correct_answer": "Large", "options": ["Tiny", "Large", "Narrow"]},
        {"word": "Fast", "correct_answer": "Quick", "options": ["Slow", "Quick", "Lazy"]},
        {"word": "Cold", "correct_answer": "Chilly", "options": ["Hot", "Chilly", "Warm"]},
        {"word": "Laugh", "correct_answer": "Giggle", "options": ["Cry", "Giggle", "Weep"]},
        {"word": "Small", "correct_answer": "Tiny", "options": ["Large", "Gigantic", "Tiny"]},
        {"word": "Kind", "correct_answer": "Nice", "options": ["Mean", "Nice", "Rude"]},
        {"word": "Soft", "correct_answer": "Gentle", "options": ["Harsh", "Gentle", "Rough"]},
        {"word": "Angry", "correct_answer": "Mad", "options": ["Calm", "Happy", "Mad"]},
        {"word": "Easy", "correct_answer": "Simple", "options": ["Hard", "Simple", "Complicated"]},
        {"word": "Bright", "correct_answer": "Shiny", "options": ["Dark", "Shiny", "Dull"]},
        {"word": "Wet", "correct_answer": "Damp", "options": ["Dry", "Damp", "Parched"]},
        {"word": "Funny", "correct_answer": "Amusing", "options": ["Boring", "Amusing", "Serious"]},
        {"word": "Strong", "correct_answer": "Powerful", "options": ["Weak", "Powerful", "Fragile"]},
        {"word": "Neat", "correct_answer": "Tidy", "options": ["Messy", "Tidy", "Cluttered"]},
        {"word": "Quiet", "correct_answer": "Silent", "options": ["Loud", "Silent", "Noisy"]},
        {"word": "Tired", "correct_answer": "Sleepy", "options": ["Energetic", "Sleepy", "Lively"]},
        {"word": "Brave", "correct_answer": "Courageous", "options": ["Fearful", "Courageous", "Timid"]},
        {"word": "Dark", "correct_answer": "Dim", "options": ["Bright", "Dim", "Glowing"]},
        {"word": "Sad", "correct_answer": "Unhappy", "options": ["Happy", "Unhappy", "Excited"]},
        {"word": "Fast", "correct_answer": "Swift", "options": ["Slow", "Swift", "Lazy"]},
        {"word": "Clean", "correct_answer": "Pure", "options": ["Dirty", "Pure", "Filthy"]},
        {"word": "Thin", "correct_answer": "Slim", "options": ["Fat", "Slim", "Chunky"]},
        {"word": "Rude", "correct_answer": "Impolite", "options": ["Kind", "Impolite", "Respectful"]},
        {"word": "Tall", "correct_answer": "High", "options": ["Short", "High", "Low"]},
        {"word": "Dirty", "correct_answer": "Filthy", "options": ["Clean", "Filthy", "Pure"]},
        {"word": "Strong", "correct_answer": "Sturdy", "options": ["Weak", "Sturdy", "Fragile"]},
        {"word": "Pretty", "correct_answer": "Beautiful", "options": ["Ugly", "Beautiful", "Plain"]},
        {"word": "Slow", "correct_answer": "Sluggish", "options": ["Quick", "Sluggish", "Swift"]},
        {"word": "Thirsty", "correct_answer": "Parched", "options": ["Hydrated", "Parched", "Wet"]},
        {"word": "Shy", "correct_answer": "Timid", "options": ["Bold", "Timid", "Loud"]},
        {"word": "Old", "correct_answer": "Ancient", "options": ["Young", "Ancient", "Modern"]},
        {"word": "Hot", "correct_answer": "Warm", "options": ["Cold", "Warm", "Chilly"]},
        {"word": "Silly", "correct_answer": "Foolish", "options": ["Wise", "Foolish", "Clever"]},
        {"word": "Sad", "correct_answer": "Gloomy", "options": ["Cheerful", "Gloomy", "Excited"]},
        {"word": "Friend", "correct_answer": "Pal", "options": ["Enemy", "Pal", "Stranger"]},
        {"word": "Hungry", "correct_answer": "Starving", "options": ["Full", "Starving", "Satisfied"]},
        {"word": "Weak", "correct_answer": "Frail", "options": ["Strong", "Frail", "Sturdy"]},
        {"word": "Scared", "correct_answer": "Afraid", "options": ["Brave", "Afraid", "Fearless"]},
        {"word": "Warm", "correct_answer": "Cozy", "options": ["Cold", "Cozy", "Freezing"]},
        {"word": "Easy", "correct_answer": "Effortless", "options": ["Difficult", "Effortless", "Complicated"]},
        {"word": "Angry", "correct_answer": "Furious", "options": ["Calm", "Furious", "Gentle"]},
        {"word": "Shiny", "correct_answer": "Bright", "options": ["Dull", "Bright", "Dark"]},
        {"word": "Brave", "correct_answer": "Fearless", "options": ["Cowardly", "Fearless", "Timid"]},
        {"word": "Happy", "correct_answer": "Cheerful", "options": ["Sad", "Cheerful", "Miserable"]},
        {"word": "Cold", "correct_answer": "Freezing", "options": ["Warm", "Freezing", "Hot"]},
        {"word": "Fast", "correct_answer": "Rapid", "options": ["Slow", "Rapid", "Lazy"]},
        {"word": "Big", "correct_answer": "Huge", "options": ["Tiny", "Huge", "Small"]},
        {"word": "Quiet", "correct_answer": "Hushed", "options": ["Loud", "Hushed", "Noisy"]},
        {"word": "Funny", "correct_answer": "Hilarious", "options": ["Serious", "Hilarious", "Sad"]},
    ],
    "medium": [
        {"word": "Abundant", "correct_answer": "Plentiful", "options": ["Scarce", "Plentiful", "Minimal"]},
        {"word": "Cautious", "correct_answer": "Wary", "options": ["Careless", "Wary", "Reckless"]},
        {"word": "Deceive", "correct_answer": "Mislead", "options": ["Clarify", "Mislead", "Guide"]},
        {"word": "Eager", "correct_answer": "Keen", "options": ["Apathetic", "Keen", "Indifferent"]},
        {"word": "Fragile", "correct_answer": "Delicate", "options": ["Sturdy", "Delicate", "Tough"]},
        {"word": "Genuine", "correct_answer": "Authentic", "options": ["Fake", "Authentic", "False"]},
        {"word": "Hostile", "correct_answer": "Unfriendly", "options": ["Friendly", "Unfriendly", "Kind"]},
        {"word": "Idle", "correct_answer": "Inactive", "options": ["Active", "Inactive", "Busy"]},
        {"word": "Jubilant", "correct_answer": "Overjoyed", "options": ["Miserable", "Overjoyed", "Gloomy"]},
        {"word": "Kin", "correct_answer": "Relative", "options": ["Stranger", "Relative", "Enemy"]},
        {"word": "Legible", "correct_answer": "Readable", "options": ["Unreadable", "Readable", "Illegible"]},
        {"word": "Malice", "correct_answer": "Hatred", "options": ["Love", "Hatred", "Kindness"]},
        {"word": "Neglect", "correct_answer": "Ignore", "options": ["Care", "Ignore", "Support"]},
        {"word": "Obscure", "correct_answer": "Unclear", "options": ["Clear", "Unclear", "Bright"]},
        {"word": "Ponder", "correct_answer": "Think", "options": ["Ignore", "Think", "Forget"]},
        {"word": "Quaint", "correct_answer": "Unusual", "options": ["Common", "Unusual", "Modern"]},
        {"word": "Reluctant", "correct_answer": "Hesitant", "options": ["Eager", "Hesitant", "Willing"]},
        {"word": "Seldom", "correct_answer": "Rarely", "options": ["Often", "Rarely", "Always"]},
        {"word": "Tranquil", "correct_answer": "Calm", "options": ["Noisy", "Calm", "Loud"]},
        {"word": "Unique", "correct_answer": "One-of-a-kind", "options": ["Common", "One-of-a-kind", "Ordinary"]},
        {"word": "Vague", "correct_answer": "Unclear", "options": ["Clear", "Unclear", "Obvious"]},
        {"word": "Wholesome", "correct_answer": "Healthy", "options": ["Unhealthy", "Healthy", "Harmful"]},
        {"word": "Yearn", "correct_answer": "Long for", "options": ["Avoid", "Long for", "Despise"]},
        {"word": "Zealous", "correct_answer": "Passionate", "options": ["Indifferent", "Passionate", "Apathetic"]},
        {"word": "Diligent", "correct_answer": "Hardworking", "options": ["Lazy", "Hardworking", "Careless"]},
        {"word": "Grim", "correct_answer": "Serious", "options": ["Cheerful", "Serious", "Funny"]},
        {"word": "Linger", "correct_answer": "Stay", "options": ["Leave", "Stay", "Disappear"]},
        {"word": "Murmur", "correct_answer": "Whisper", "options": ["Shout", "Whisper", "Talk"]},
        {"word": "Notorious", "correct_answer": "Infamous", "options": ["Famous", "Infamous", "Respected"]},
        {"word": "Ominous", "correct_answer": "Threatening", "options": ["Comforting", "Threatening", "Reassuring"]},
        {"word": "Prudent", "correct_answer": "Wise", "options": ["Foolish", "Wise", "Careless"]},
        {"word": "Reckless", "correct_answer": "Careless", "options": ["Cautious", "Careless", "Thoughtful"]},
        {"word": "Scorn", "correct_answer": "Disdain", "options": ["Respect", "Disdain", "Praise"]},
        {"word": "Tedious", "correct_answer": "Boring", "options": ["Exciting", "Boring", "Thrilling"]},
        {"word": "Unkempt", "correct_answer": "Messy", "options": ["Neat", "Messy", "Organized"]},
        {"word": "Vibrant", "correct_answer": "Lively", "options": ["Dull", "Lively", "Colorless"]},
        {"word": "Wary", "correct_answer": "Cautious", "options": ["Reckless", "Cautious", "Careless"]},
        {"word": "Astonish", "correct_answer": "Surprise", "options": ["Bore", "Surprise", "Ignore"]},
        {"word": "Benevolent", "correct_answer": "Kind", "options": ["Mean", "Kind", "Rude"]},
        {"word": "Conceal", "correct_answer": "Hide", "options": ["Reveal", "Hide", "Expose"]},
        {"word": "Deplete", "correct_answer": "Use up", "options": ["Save", "Use up", "Store"]},
        {"word": "Elated", "correct_answer": "Thrilled", "options": ["Sad", "Thrilled", "Depressed"]},
        {"word": "Flourish", "correct_answer": "Thrive", "options": ["Decline", "Thrive", "Fail"]},
        {"word": "Gracious", "correct_answer": "Polite", "options": ["Rude", "Polite", "Impolite"]},
        {"word": "Hesitant", "correct_answer": "Uncertain", "options": ["Certain", "Uncertain", "Sure"]},
        {"word": "Impulsive", "correct_answer": "Hasty", "options": ["Careful", "Hasty", "Cautious"]},
        {"word": "Jovial", "correct_answer": "Cheerful", "options": ["Gloomy", "Cheerful", "Miserable"]},
        {"word": "Lofty", "correct_answer": "Tall", "options": ["Short", "Tall", "Low"]},
    ],

    "hard": [
        {"word": "Abstruse", "correct_answer": "Obscure", "options": ["Clear", "Obscure", "Simple"]},
        {"word": "Belligerent", "correct_answer": "Aggressive", "options": ["Calm", "Aggressive", "Friendly"]},
        {"word": "Cacophony", "correct_answer": "Discord", "options": ["Harmony", "Discord", "Melody"]},
        {"word": "Deleterious", "correct_answer": "Harmful", "options": ["Beneficial", "Harmful", "Helpful"]},
        {"word": "Ebullient", "correct_answer": "Exuberant", "options": ["Depressed", "Exuberant", "Reserved"]},
        {"word": "Fastidious", "correct_answer": "Meticulous", "options": ["Careless", "Meticulous", "Lazy"]},
        {"word": "Garrulous", "correct_answer": "Talkative", "options": ["Silent", "Talkative", "Quiet"]},
        {"word": "Hubris", "correct_answer": "Arrogance", "options": ["Humility", "Arrogance", "Modesty"]},
        {"word": "Intransigent", "correct_answer": "Unyielding", "options": ["Flexible", "Unyielding", "Compromising"]},
        {"word": "Juxtapose", "correct_answer": "Compare", "options": ["Separate", "Compare", "Ignore"]},
        {"word": "Lugubrious", "correct_answer": "Mournful", "options": ["Cheerful", "Mournful", "Excited"]},
        {"word": "Munificent", "correct_answer": "Generous", "options": ["Stingy", "Generous", "Greedy"]},
        {"word": "Nebulous", "correct_answer": "Vague", "options": ["Clear", "Vague", "Obvious"]},
        {"word": "Obfuscate", "correct_answer": "Confuse", "options": ["Clarify", "Confuse", "Explain"]},
        {"word": "Parsimonious", "correct_answer": "Stingy", "options": ["Generous", "Stingy", "Lavish"]},
        {"word": "Quixotic", "correct_answer": "Unrealistic", "options": ["Practical", "Unrealistic", "Sensible"]},
        {"word": "Recalcitrant", "correct_answer": "Defiant", "options": ["Obedient", "Defiant", "Submissive"]},
        {"word": "Sycophant", "correct_answer": "Flatterer", "options": ["Critic", "Flatterer", "Leader"]},
        {"word": "Trepidation", "correct_answer": "Fear", "options": ["Confidence", "Fear", "Calm"]},
        {"word": "Ubiquitous", "correct_answer": "Omnipresent", "options": ["Rare", "Omnipresent", "Scarce"]},
        {"word": "Verbose", "correct_answer": "Wordy", "options": ["Concise", "Wordy", "Silent"]},
        {"word": "Wistful", "correct_answer": "Yearning", "options": ["Content", "Yearning", "Joyful"]},
        {"word": "Xenophobia", "correct_answer": "Fear of foreigners", "options": ["Acceptance", "Fear of foreigners", "Love"]},
        {"word": "Yen", "correct_answer": "Desire", "options": ["Disgust", "Desire", "Hatred"]},
        {"word": "Zealot", "correct_answer": "Fanatic", "options": ["Moderate", "Fanatic", "Indifferent"]},
        {"word": "Acrimonious", "correct_answer": "Bitter", "options": ["Sweet", "Bitter", "Friendly"]},
        {"word": "Beguile", "correct_answer": "Deceive", "options": ["Clarify", "Deceive", "Guide"]},
        {"word": "Chicanery", "correct_answer": "Deception", "options": ["Honesty", "Deception", "Truth"]},
        {"word": "Didactic", "correct_answer": "Instructive", "options": ["Confusing", "Instructive", "Misleading"]},
        {"word": "Esoteric", "correct_answer": "Mysterious", "options": ["Obvious", "Mysterious", "Common"]},
        {"word": "Fortuitous", "correct_answer": "Accidental", "options": ["Intentional", "Accidental", "Planned"]},
        {"word": "Grandiloquent", "correct_answer": "Pompous", "options": ["Simple", "Pompous", "Humble"]},
        {"word": "Harangue", "correct_answer": "Lecture", "options": ["Praise", "Lecture", "Encourage"]},
        {"word": "Ineffable", "correct_answer": "Indescribable", "options": ["Ordinary", "Indescribable", "Plain"]},
        {"word": "Jargon", "correct_answer": "Specialized language", "options": ["Common speech", "Specialized language", "Simple words"]},
        {"word": "Lackadaisical", "correct_answer": "Lethargic", "options": ["Energetic", "Lethargic", "Active"]},
        {"word": "Mellifluous", "correct_answer": "Sweet-sounding", "options": ["Harsh", "Sweet-sounding", "Rough"]},
        {"word": "Nonplussed", "correct_answer": "Confused", "options": ["Certain", "Confused", "Sure"]},
        {"word": "Obstreperous", "correct_answer": "Noisy", "options": ["Quiet", "Noisy", "Silent"]},
        {"word": "Pernicious", "correct_answer": "Harmful", "options": ["Beneficial", "Harmful", "Helpful"]},
        {"word": "Quagmire", "correct_answer": "Difficult situation", "options": ["Easy task", "Difficult situation", "Solution"]},
        {"word": "Reverberate", "correct_answer": "Echo", "options": ["Mute", "Echo", "Silence"]},
        {"word": "Sagacious", "correct_answer": "Wise", "options": ["Foolish", "Wise", "Ignorant"]},
        {"word": "Tenuous", "correct_answer": "Weak", "options": ["Strong", "Weak", "Firm"]},
        {"word": "Undulate", "correct_answer": "Wave-like motion", "options": ["Still", "Wave-like motion", "Rigid"]},
        {"word": "Venerate", "correct_answer": "Respect", "options": ["Disrespect", "Respect", "Ignore"]},
        {"word": "Winsome", "correct_answer": "Charming", "options": ["Unattractive", "Charming", "Repulsive"]},
    ]
}

@app.get("/", include_in_schema=False)
@app.head("/")
def root():
    return {"message": "Welcome to the Synonym Game!"}


@app.get("/get_words/{difficulty}")
def get_words(difficulty: str):
    if difficulty not in word_bank:
        return {"error": "Invalid difficulty level"}
    
    selected_words = random.sample(word_bank[difficulty], 10)  # Pick 10 random words
    
    for word in selected_words:
        options = word["options"][:]  # Copy options list
        random.shuffle(options)  # Shuffle options
        
        # Find the correct answer's new index after shuffling
        correct_index = options.index(word["correct_answer"])
        
        # Store the shuffled options and correct index
        word["options"] = options
        word["correct_index"] = correct_index  

    return selected_words