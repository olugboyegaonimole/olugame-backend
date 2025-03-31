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


"Level 1": [
    {"word": "big", "options": ["huge", "small", "tiny"], "answer": "huge"},
    {"word": "happy", "options": ["joyful", "sad", "angry"], "answer": "joyful"},
    {"word": "fast", "options": ["quick", "slow", "lazy"], "answer": "quick"},
    {"word": "hot", "options": ["warm", "cold", "freezing"], "answer": "warm"},
    {"word": "small", "options": ["tiny", "large", "gigantic"], "answer": "tiny"},
    {"word": "cold", "options": ["chilly", "hot", "warm"], "answer": "chilly"},
    {"word": "soft", "options": ["fluffy", "hard", "rough"], "answer": "fluffy"},
    {"word": "strong", "options": ["powerful", "weak", "slow"], "answer": "powerful"},
    {"word": "light", "options": ["bright", "dark", "heavy"], "answer": "bright"},
    {"word": "clean", "options": ["neat", "dirty", "messy"], "answer": "neat"},
    {"word": "loud", "options": ["noisy", "quiet", "silent"], "answer": "noisy"},
    {"word": "new", "options": ["fresh", "old", "ancient"], "answer": "fresh"},
    {"word": "tall", "options": ["huge", "short", "long"], "answer": "huge"},
    {"word": "funny", "options": ["hilarious", "boring", "sad"], "answer": "hilarious"},
    {"word": "sad", "options": ["miserable", "happy", "joyful"], "answer": "miserable"},
    {"word": "easy", "options": ["simple", "hard", "difficult"], "answer": "simple"},
    {"word": "kind", "options": ["nice", "mean", "rude"], "answer": "nice"},
    {"word": "fat", "options": ["chubby", "thin", "slim"], "answer": "chubby"},
    {"word": "wet", "options": ["damp", "dry", "soaked"], "answer": "damp"},
    {"word": "early", "options": ["soon", "late", "on time"], "answer": "soon"},
    {"word": "full", "options": ["stuffed", "empty", "hungry"], "answer": "stuffed"},
    {"word": "old", "options": ["ancient", "young", "new"], "answer": "ancient"},
    {"word": "weak", "options": ["frail", "strong", "powerful"], "answer": "frail"},
    {"word": "slow", "options": ["leisurely", "fast", "lazy"], "answer": "leisurely"},
    {"word": "hungry", "options": ["starving", "thirsty", "full"], "answer": "starving"},
    {"word": "dark", "options": ["dim", "bright", "gloomy"], "answer": "dim"},
    {"word": "rich", "options": ["wealthy", "poor", "famous"], "answer": "wealthy"},
    {"word": "fat", "options": ["plump", "slim", "skinny"], "answer": "plump"},
    {"word": "lazy", "options": ["inactive", "energetic", "slow"], "answer": "inactive"},
    {"word": "dry", "options": ["parched", "wet", "moist"], "answer": "parched"},
    {"word": "round", "options": ["circular", "square", "flat"], "answer": "circular"},
    {"word": "long", "options": ["lengthy", "short", "tall"], "answer": "lengthy"},
    {"word": "thin", "options": ["slim", "fat", "chubby"], "answer": "slim"},
    {"word": "simple", "options": ["easy", "complicated", "hard"], "answer": "easy"},
    {"word": "safe", "options": ["secure", "dangerous", "harmful"], "answer": "secure"},
    {"word": "smooth", "options": ["silky", "rough", "bumpy"], "answer": "silky"},
    {"word": "dirty", "options": ["messy", "clean", "tidy"], "answer": "messy"},
    {"word": "angry", "options": ["mad", "calm", "furious"], "answer": "mad"},
    {"word": "short", "options": ["tiny", "long", "small"], "answer": "tiny"},
    {"word": "happy", "options": ["cheerful", "excited", "joyful"], "answer": "cheerful"},
    {"word": "quiet", "options": ["silent", "calm", "peaceful"], "answer": "silent"},
    {"word": "thin", "options": ["skinny", "fat", "chubby"], "answer": "skinny"},
    {"word": "cheap", "options": ["affordable", "expensive", "costly"], "answer": "affordable"},
    {"word": "heavy", "options": ["massive", "light", "huge"], "answer": "massive"},
    {"word": "cold", "options": ["freezing", "chilly", "warm"], "answer": "freezing"},
    {"word": "soft", "options": ["fluffy", "hard", "smooth"], "answer": "fluffy"},
    {"word": "hard", "options": ["tough", "difficult", "rough"], "answer": "tough"}
],

"Level 2": [
    {"word": "rapid", "options": ["fast", "slow", "steady"], "answer": "fast"},
    {"word": "silent", "options": ["quiet", "noisy", "loud"], "answer": "quiet"},
    {"word": "angry", "options": ["furious", "calm", "happy"], "answer": "furious"},
    {"word": "brave", "options": ["courageous", "fearful", "scared"], "answer": "courageous"},
    {"word": "clever", "options": ["smart", "dull", "foolish"], "answer": "smart"},
    {"word": "polite", "options": ["courteous", "rude", "harsh"], "answer": "courteous"},
    {"word": "bright", "options": ["radiant", "dim", "gloomy"], "answer": "radiant"},
    {"word": "strong", "options": ["sturdy", "weak", "frail"], "answer": "sturdy"},
    {"word": "fragile", "options": ["delicate", "hard", "tough"], "answer": "delicate"},
    {"word": "wealthy", "options": ["rich", "poor", "broke"], "answer": "rich"},
    {"word": "quick", "options": ["swift", "slow", "lazy"], "answer": "swift"},
    {"word": "delicious", "options": ["tasty", "bland", "awful"], "answer": "tasty"},
    {"word": "huge", "options": ["gigantic", "tiny", "small"], "answer": "gigantic"},
    {"word": "tired", "options": ["exhausted", "energetic", "awake"], "answer": "exhausted"},
    {"word": "friendly", "options": ["kind", "mean", "rude"], "answer": "kind"},
    {"word": "honest", "options": ["truthful", "dishonest", "lying"], "answer": "truthful"},
    {"word": "narrow", "options": ["thin", "wide", "broad"], "answer": "thin"},
    {"word": "calm", "options": ["peaceful", "nervous", "tense"], "answer": "peaceful"},
    {"word": "messy", "options": ["untidy", "clean", "neat"], "answer": "untidy"},
    {"word": "happy", "options": ["cheerful", "miserable", "gloomy"], "answer": "cheerful"},
    {"word": "sad", "options": ["unhappy", "joyful", "excited"], "answer": "unhappy"},
    {"word": "fearful", "options": ["scared", "brave", "courageous"], "answer": "scared"},
    {"word": "damp", "options": ["moist", "dry", "parched"], "answer": "moist"},
    {"word": "cold", "options": ["chilly", "hot", "warm"], "answer": "chilly"},
    {"word": "soft", "options": ["cushiony", "rough", "hard"], "answer": "cushiony"},
    {"word": "hardworking", "options": ["diligent", "lazy", "careless"], "answer": "diligent"},
    {"word": "important", "options": ["significant", "trivial", "unimportant"], "answer": "significant"},
    {"word": "interesting", "options": ["fascinating", "boring", "dull"], "answer": "fascinating"},
    {"word": "precise", "options": ["accurate", "wrong", "incorrect"], "answer": "accurate"},
    {"word": "smooth", "options": ["silky", "rough", "coarse"], "answer": "silky"},
    {"word": "gigantic", "options": ["enormous", "tiny", "minute"], "answer": "enormous"},
    {"word": "painful", "options": ["agonizing", "comfortable", "relaxing"], "answer": "agonizing"},
    {"word": "sleepy", "options": ["drowsy", "alert", "awake"], "answer": "drowsy"},
    {"word": "bright", "options": ["luminous", "dark", "dim"], "answer": "luminous"},
    {"word": "quick", "options": ["speedy", "slow", "lazy"], "answer": "speedy"},
    {"word": "generous", "options": ["kind", "selfish", "greedy"], "answer": "kind"},
    {"word": "bumpy", "options": ["rough", "smooth", "flat"], "answer": "rough"},
    {"word": "dirty", "options": ["filthy", "clean", "spotless"], "answer": "filthy"},
    {"word": "early", "options": ["prompt", "late", "delayed"], "answer": "prompt"},
    {"word": "heavy", "options": ["massive", "light", "airy"], "answer": "massive"},
    {"word": "cozy", "options": ["comfortable", "cold", "chilly"], "answer": "comfortable"},
    {"word": "expensive", "options": ["costly", "cheap", "affordable"], "answer": "costly"},
    {"word": "famous", "options": ["well-known", "unknown", "obscure"], "answer": "well-known"},
    {"word": "tricky", "options": ["difficult", "easy", "simple"], "answer": "difficult"},
    {"word": "weird", "options": ["strange", "normal", "usual"], "answer": "strange"},
    {"word": "wild", "options": ["untamed", "domesticated", "calm"], "answer": "untamed"},
    {"word": "worried", "options": ["anxious", "calm", "relaxed"], "answer": "anxious"}
],


"Level 3": [
    {"word": "ancient", "options": ["old", "modern", "new"], "answer": "old"},
    {"word": "fragile", "options": ["delicate", "strong", "tough"], "answer": "delicate"},
    {"word": "complicated", "options": ["complex", "simple", "easy"], "answer": "complex"},
    {"word": "genuine", "options": ["authentic", "fake", "artificial"], "answer": "authentic"},
    {"word": "brilliant", "options": ["intelligent", "dull", "foolish"], "answer": "intelligent"},
    {"word": "tranquil", "options": ["peaceful", "chaotic", "noisy"], "answer": "peaceful"},
    {"word": "immense", "options": ["huge", "tiny", "small"], "answer": "huge"},
    {"word": "peculiar", "options": ["strange", "normal", "usual"], "answer": "strange"},
    {"word": "timid", "options": ["shy", "bold", "confident"], "answer": "shy"},
    {"word": "perilous", "options": ["dangerous", "safe", "harmless"], "answer": "dangerous"},
    {"word": "rigid", "options": ["stiff", "flexible", "loose"], "answer": "stiff"},
    {"word": "hasty", "options": ["quick", "slow", "careful"], "answer": "quick"},
    {"word": "prudent", "options": ["cautious", "reckless", "careless"], "answer": "cautious"},
    {"word": "weary", "options": ["tired", "energetic", "awake"], "answer": "tired"},
    {"word": "reliable", "options": ["trustworthy", "untrustworthy", "dishonest"], "answer": "trustworthy"},
    {"word": "dismal", "options": ["gloomy", "bright", "cheerful"], "answer": "gloomy"},
    {"word": "arrogant", "options": ["conceited", "humble", "modest"], "answer": "conceited"},
    {"word": "nimble", "options": ["agile", "clumsy", "slow"], "answer": "agile"},
    {"word": "vivid", "options": ["colorful", "dull", "faded"], "answer": "colorful"},
    {"word": "stern", "options": ["strict", "lenient", "easygoing"], "answer": "strict"},
    {"word": "lavish", "options": ["extravagant", "cheap", "modest"], "answer": "extravagant"},
    {"word": "coarse", "options": ["rough", "smooth", "silky"], "answer": "rough"},
    {"word": "meager", "options": ["scarce", "abundant", "plentiful"], "answer": "scarce"},
    {"word": "reluctant", "options": ["hesitant", "eager", "willing"], "answer": "hesitant"},
    {"word": "fickle", "options": ["unpredictable", "steady", "reliable"], "answer": "unpredictable"},
    {"word": "vulnerable", "options": ["weak", "strong", "resistant"], "answer": "weak"},
    {"word": "tedious", "options": ["boring", "exciting", "thrilling"], "answer": "boring"},
    {"word": "exquisite", "options": ["beautiful", "ugly", "plain"], "answer": "beautiful"},
    {"word": "indignant", "options": ["angry", "calm", "content"], "answer": "angry"},
    {"word": "meticulous", "options": ["precise", "careless", "hasty"], "answer": "precise"},
    {"word": "grueling", "options": ["exhausting", "easy", "effortless"], "answer": "exhausting"},
    {"word": "subtle", "options": ["delicate", "obvious", "clear"], "answer": "delicate"},
    {"word": "thrifty", "options": ["frugal", "wasteful", "lavish"], "answer": "frugal"},
    {"word": "ominous", "options": ["threatening", "harmless", "comforting"], "answer": "threatening"},
    {"word": "elated", "options": ["joyful", "miserable", "depressed"], "answer": "joyful"},
    {"word": "rigorous", "options": ["strict", "lenient", "lax"], "answer": "strict"},
    {"word": "erratic", "options": ["unpredictable", "consistent", "steady"], "answer": "unpredictable"},
    {"word": "abundant", "options": ["plentiful", "scarce", "limited"], "answer": "plentiful"},
    {"word": "graceful", "options": ["elegant", "awkward", "clumsy"], "answer": "elegant"},
    {"word": "exuberant", "options": ["enthusiastic", "dull", "lifeless"], "answer": "enthusiastic"},
    {"word": "melancholy", "options": ["gloomy", "cheerful", "joyful"], "answer": "gloomy"},
    {"word": "scrupulous", "options": ["honest", "dishonest", "careless"], "answer": "honest"},
    {"word": "plausible", "options": ["believable", "unlikely", "doubtful"], "answer": "believable"},
    {"word": "versatile", "options": ["adaptable", "inflexible", "rigid"], "answer": "adaptable"},
    {"word": "notorious", "options": ["infamous", "unknown", "respected"], "answer": "infamous"},
    {"word": "somber", "options": ["serious", "cheerful", "happy"], "answer": "serious"},
    {"word": "resilient", "options": ["strong", "weak", "delicate"], "answer": "strong"},
    {"word": "tedious", "options": ["monotonous", "exciting", "engaging"], "answer": "monotonous"}
]
,


"Level 4": [
    {"word": "convoluted", "options": ["complicated", "simple", "clear"], "answer": "complicated"},
    {"word": "authentic", "options": ["genuine", "fake", "fraudulent"], "answer": "genuine"},
    {"word": "astute", "options": ["shrewd", "foolish", "ignorant"], "answer": "shrewd"},
    {"word": "pristine", "options": ["immaculate", "dirty", "tainted"], "answer": "immaculate"},
    {"word": "incessant", "options": ["constant", "interrupted", "sporadic"], "answer": "constant"},
    {"word": "erroneous", "options": ["incorrect", "accurate", "factual"], "answer": "incorrect"},
    {"word": "cohesive", "options": ["unified", "disjointed", "scattered"], "answer": "unified"},
    {"word": "elusive", "options": ["hard to catch", "obvious", "clear"], "answer": "hard to catch"},
    {"word": "ephemeral", "options": ["short-lived", "eternal", "lasting"], "answer": "short-lived"},
    {"word": "imperative", "options": ["crucial", "optional", "trivial"], "answer": "crucial"},
    {"word": "profound", "options": ["deep", "superficial", "shallow"], "answer": "deep"},
    {"word": "ambiguous", "options": ["unclear", "explicit", "definite"], "answer": "unclear"},
    {"word": "resolute", "options": ["determined", "hesitant", "indecisive"], "answer": "determined"},
    {"word": "frivolous", "options": ["trivial", "important", "serious"], "answer": "trivial"},
    {"word": "deviate", "options": ["stray", "follow", "adhere"], "answer": "stray"},
    {"word": "prolific", "options": ["productive", "unproductive", "barren"], "answer": "productive"},
    {"word": "candid", "options": ["honest", "deceptive", "misleading"], "answer": "honest"},
    {"word": "meticulous", "options": ["careful", "careless", "reckless"], "answer": "careful"},
    {"word": "dubious", "options": ["doubtful", "certain", "sure"], "answer": "doubtful"},
    {"word": "copious", "options": ["abundant", "scarce", "limited"], "answer": "abundant"},
    {"word": "lethargic", "options": ["sluggish", "energetic", "active"], "answer": "sluggish"},
    {"word": "affluent", "options": ["wealthy", "poor", "destitute"], "answer": "wealthy"},
    {"word": "stoic", "options": ["unemotional", "expressive", "dramatic"], "answer": "unemotional"},
    {"word": "esoteric", "options": ["obscure", "common", "well-known"], "answer": "obscure"},
    {"word": "trivial", "options": ["insignificant", "important", "crucial"], "answer": "insignificant"},
    {"word": "tedious", "options": ["monotonous", "exciting", "stimulating"], "answer": "monotonous"},
    {"word": "ostentatious", "options": ["flashy", "modest", "understated"], "answer": "flashy"},
    {"word": "contrived", "options": ["artificial", "natural", "authentic"], "answer": "artificial"},
    {"word": "scrupulous", "options": ["honest", "corrupt", "dishonest"], "answer": "honest"},
    {"word": "placid", "options": ["calm", "agitated", "anxious"], "answer": "calm"},
    {"word": "auspicious", "options": ["favorable", "unlucky", "ominous"], "answer": "favorable"},
    {"word": "somber", "options": ["serious", "cheerful", "joyful"], "answer": "serious"},
    {"word": "tedious", "options": ["boring", "thrilling", "exciting"], "answer": "boring"},
    {"word": "coherent", "options": ["logical", "confusing", "nonsensical"], "answer": "logical"},
    {"word": "inadvertent", "options": ["unintentional", "deliberate", "planned"], "answer": "unintentional"},
    {"word": "insatiable", "options": ["greedy", "content", "satisfied"], "answer": "greedy"},
    {"word": "reclusive", "options": ["isolated", "social", "outgoing"], "answer": "isolated"},
    {"word": "stringent", "options": ["strict", "lenient", "relaxed"], "answer": "strict"},
    {"word": "nuance", "options": ["subtlety", "obviousness", "clarity"], "answer": "subtlety"},
    {"word": "transient", "options": ["temporary", "permanent", "lasting"], "answer": "temporary"},
    {"word": "eccentric", "options": ["unusual", "ordinary", "typical"], "answer": "unusual"},
    {"word": "nonchalant", "options": ["indifferent", "anxious", "nervous"], "answer": "indifferent"},
    {"word": "mundane", "options": ["ordinary", "extraordinary", "unique"], "answer": "ordinary"},
    {"word": "quintessential", "options": ["perfect", "imperfect", "flawed"], "answer": "perfect"},
    {"word": "impetuous", "options": ["hasty", "thoughtful", "careful"], "answer": "hasty"},
    {"word": "fortuitous", "options": ["lucky", "unfortunate", "unlucky"], "answer": "lucky"},
    {"word": "indispensable", "options": ["essential", "unnecessary", "optional"], "answer": "essential"},
    {"word": "trepidation", "options": ["fear", "courage", "confidence"], "answer": "fear"},
    {"word": "benevolent", "options": ["kind", "cruel", "mean"], "answer": "kind"}
]
,


"Level 5": [
    {"word": "ambivalent", "options": ["uncertain", "decisive", "clear"], "answer": "uncertain"},
    {"word": "impeccable", "options": ["flawless", "imperfect", "defective"], "answer": "flawless"},
    {"word": "ubiquitous", "options": ["omnipresent", "rare", "scarce"], "answer": "omnipresent"},
    {"word": "enervate", "options": ["weaken", "strengthen", "invigorate"], "answer": "weaken"},
    {"word": "insidious", "options": ["sly", "obvious", "transparent"], "answer": "sly"},
    {"word": "defenestrate", "options": ["throw out", "invite", "receive"], "answer": "throw out"},
    {"word": "ephemeral", "options": ["short-lived", "eternal", "permanent"], "answer": "short-lived"},
    {"word": "magnanimous", "options": ["generous", "selfish", "greedy"], "answer": "generous"},
    {"word": "conspicuous", "options": ["obvious", "hidden", "subtle"], "answer": "obvious"},
    {"word": "paucity", "options": ["scarcity", "abundance", "plenty"], "answer": "scarcity"},
    {"word": "quixotic", "options": ["idealistic", "practical", "realistic"], "answer": "idealistic"},
    {"word": "assiduous", "options": ["diligent", "lazy", "apathetic"], "answer": "diligent"},
    {"word": "rescind", "options": ["revoke", "confirm", "approve"], "answer": "revoke"},
    {"word": "vitriolic", "options": ["bitter", "kind", "gentle"], "answer": "bitter"},
    {"word": "cacophony", "options": ["discord", "melody", "harmony"], "answer": "discord"},
    {"word": "antithesis", "options": ["opposite", "similarity", "resemblance"], "answer": "opposite"},
    {"word": "austere", "options": ["severe", "gentle", "soft"], "answer": "severe"},
    {"word": "morose", "options": ["gloomy", "happy", "cheerful"], "answer": "gloomy"},
    {"word": "epitome", "options": ["embodiment", "partial", "imperfect"], "answer": "embodiment"},
    {"word": "plethora", "options": ["abundance", "scarcity", "lack"], "answer": "abundance"},
    {"word": "histrionic", "options": ["dramatic", "subdued", "calm"], "answer": "dramatic"},
    {"word": "perfunctory", "options": ["casual", "meticulous", "thorough"], "answer": "casual"},
    {"word": "intrepid", "options": ["brave", "timid", "fearful"], "answer": "brave"},
    {"word": "elucidate", "options": ["clarify", "confuse", "complicate"], "answer": "clarify"},
    {"word": "perspicacious", "options": ["perceptive", "unaware", "ignorant"], "answer": "perceptive"},
    {"word": "imprudent", "options": ["reckless", "wise", "careful"], "answer": "reckless"},
    {"word": "cacophony", "options": ["discord", "melody", "harmony"], "answer": "discord"},
    {"word": "disparate", "options": ["different", "similar", "identical"], "answer": "different"},
    {"word": "tenuous", "options": ["weak", "strong", "firm"], "answer": "weak"},
    {"word": "antagonize", "options": ["provoke", "calm", "appease"], "answer": "provoke"},
    {"word": "mellifluous", "options": ["sweet-sounding", "harsh", "abrasive"], "answer": "sweet-sounding"},
    {"word": "equanimity", "options": ["composure", "panic", "disorder"], "answer": "composure"},
    {"word": "recalcitrant", "options": ["stubborn", "compliant", "obedient"], "answer": "stubborn"},
    {"word": "concise", "options": ["brief", "verbose", "lengthy"], "answer": "brief"},
    {"word": "flabbergasted", "options": ["astonished", "bored", "unimpressed"], "answer": "astonished"},
    {"word": "effervescent", "options": ["bubbly", "flat", "dull"], "answer": "bubbly"},
    {"word": "capricious", "options": ["whimsical", "predictable", "steady"], "answer": "whimsical"},
    {"word": "adroit", "options": ["skillful", "clumsy", "awkward"], "answer": "skillful"},
    {"word": "insular", "options": ["isolated", "connected", "open"], "answer": "isolated"},
    {"word": "juxtapose", "options": ["compare", "contrast", "align"], "answer": "contrast"},
    {"word": "ebullient", "options": ["enthusiastic", "apathetic", "uninterested"], "answer": "enthusiastic"},
    {"word": "fortuitous", "options": ["lucky", "unfortunate", "tragic"], "answer": "lucky"},
    {"word": "sagacious", "options": ["wise", "foolish", "ignorant"], "answer": "wise"},
    {"word": "recalcitrant", "options": ["stubborn", "obedient", "docile"], "answer": "stubborn"},
    {"word": "propitious", "options": ["favorable", "unlucky", "unfavorable"], "answer": "favorable"},
    {"word": "noxious", "options": ["harmful", "harmless", "safe"], "answer": "harmful"},
    {"word": "sedulous", "options": ["diligent", "lazy", "apathetic"], "answer": "diligent"}
]
,

"Level 6": [
    {"word": "abstruse", "options": ["complex", "simple", "obvious"], "answer": "complex"},
    {"word": "ineffable", "options": ["indescribable", "clear", "predictable"], "answer": "indescribable"},
    {"word": "insouciant", "options": ["carefree", "worried", "anxious"], "answer": "carefree"},
    {"word": "laconic", "options": ["brief", "verbose", "wordy"], "answer": "brief"},
    {"word": "nadir", "options": ["low point", "high point", "peak"], "answer": "low point"},
    {"word": "obfuscate", "options": ["confuse", "clarify", "simplify"], "answer": "confuse"},
    {"word": "panacea", "options": ["solution", "problem", "issue"], "answer": "solution"},
    {"word": "polemical", "options": ["controversial", "agreeable", "peaceful"], "answer": "controversial"},
    {"word": "quixotic", "options": ["idealistic", "pragmatic", "realistic"], "answer": "idealistic"},
    {"word": "recondite", "options": ["obscure", "clear", "easy"], "answer": "obscure"},
    {"word": "sophomoric", "options": ["juvenile", "mature", "wise"], "answer": "juvenile"},
    {"word": "sublime", "options": ["exalted", "mundane", "common"], "answer": "exalted"},
    {"word": "taciturn", "options": ["silent", "talkative", "chatty"], "answer": "silent"},
    {"word": "tenuous", "options": ["weak", "strong", "secure"], "answer": "weak"},
    {"word": "trenchant", "options": ["sharp", "blunt", "dull"], "answer": "sharp"},
    {"word": "veracity", "options": ["truthfulness", "falsehood", "deception"], "answer": "truthfulness"},
    {"word": "vituperative", "options": ["abusive", "kind", "gentle"], "answer": "abusive"},
    {"word": "wheedle", "options": ["coax", "force", "demand"], "answer": "coax"},
    {"word": "ameliorate", "options": ["improve", "worsen", "deteriorate"], "answer": "improve"},
    {"word": "ascetic", "options": ["self-denying", "indulgent", "pleasure-seeking"], "answer": "self-denying"},
    {"word": "bellicose", "options": ["hostile", "peaceful", "calm"], "answer": "hostile"},
    {"word": "capitulate", "options": ["surrender", "fight", "resist"], "answer": "surrender"},
    {"word": "diatribe", "options": ["tirade", "praise", "compliment"], "answer": "tirade"},
    {"word": "equivocate", "options": ["prevaricate", "clarify", "confirm"], "answer": "prevaricate"},
    {"word": "impecunious", "options": ["poor", "wealthy", "affluent"], "answer": "poor"},
    {"word": "inexorable", "options": ["unyielding", "flexible", "relenting"], "answer": "unyielding"},
    {"word": "mendacious", "options": ["dishonest", "truthful", "genuine"], "answer": "dishonest"},
    {"word": "obsequious", "options": ["submissive", "dominant", "defiant"], "answer": "submissive"},
    {"word": "opprobrium", "options": ["disgrace", "honor", "respect"], "answer": "disgrace"},
    {"word": "perfidy", "options": ["treachery", "loyalty", "fidelity"], "answer": "treachery"},
    {"word": "phlegmatic", "options": ["calm", "emotional", "anxious"], "answer": "calm"},
    {"word": "recalcitrant", "options": ["stubborn", "compliant", "obedient"], "answer": "stubborn"},
    {"word": "reprehensible", "options": ["blameworthy", "praiseworthy", "honorable"], "answer": "blameworthy"},
    {"word": "sagacious", "options": ["wise", "ignorant", "unwise"], "answer": "wise"},
    {"word": "specious", "options": ["deceptive", "genuine", "truthful"], "answer": "deceptive"},
    {"word": "tacit", "options": ["implicit", "explicit", "clear"], "answer": "implicit"},
    {"word": "trenchant", "options": ["sharp", "dull", "blunt"], "answer": "sharp"},
    {"word": "virulent", "options": ["poisonous", "harmless", "safe"], "answer": "poisonous"},
    {"word": "voracious", "options": ["insatiable", "satisfied", "content"], "answer": "insatiable"},
    {"word": "winsome", "options": ["charming", "unattractive", "ugly"], "answer": "charming"},
    {"word": "wrought", "options": ["created", "destroyed", "ruined"], "answer": "created"},
    {"word": "zealous", "options": ["passionate", "apathetic", "disinterested"], "answer": "passionate"},
    {"word": "insidious", "options": ["sly", "transparent", "obvious"], "answer": "sly"},
    {"word": "exonerate", "options": ["absolve", "accuse", "blame"], "answer": "absolve"},
    {"word": "pragmatic", "options": ["practical", "idealistic", "visionary"], "answer": "practical"}
],


"Level 7": [
    {"word": "abrogate", "options": ["revoke", "confirm", "validate"], "answer": "revoke"},
    {"word": "anathema", "options": ["curse", "blessing", "favor"], "answer": "curse"},
    {"word": "antipathy", "options": ["hatred", "love", "affection"], "answer": "hatred"},
    {"word": "apocryphal", "options": ["false", "genuine", "authentic"], "answer": "false"},
    {"word": "augury", "options": ["omen", "certainty", "assurance"], "answer": "omen"},
    {"word": "cajole", "options": ["coax", "force", "demand"], "answer": "coax"},
    {"word": "calumny", "options": ["slander", "praise", "commendation"], "answer": "slander"},
    {"word": "concatenation", "options": ["link", "separation", "division"], "answer": "link"},
    {"word": "consternation", "options": ["alarm", "calm", "peace"], "answer": "alarm"},
    {"word": "contumacious", "options": ["rebellious", "obedient", "submissive"], "answer": "rebellious"},
    {"word": "dearth", "options": ["shortage", "abundance", "plenty"], "answer": "shortage"},
    {"word": "effulgent", "options": ["radiant", "dull", "dim"], "answer": "radiant"},
    {"word": "ephemeral", "options": ["fleeting", "permanent", "lasting"], "answer": "fleeting"},
    {"word": "equanimity", "options": ["composure", "anxiety", "distress"], "answer": "composure"},
    {"word": "excoriate", "options": ["criticize", "praise", "laud"], "answer": "criticize"},
    {"word": "exigent", "options": ["urgent", "trivial", "unimportant"], "answer": "urgent"},
    {"word": "fatuous", "options": ["silly", "intelligent", "wise"], "answer": "silly"},
    {"word": "fastidious", "options": ["meticulous", "careless", "reckless"], "answer": "meticulous"},
    {"word": "forlorn", "options": ["desolate", "joyful", "content"], "answer": "desolate"},
    {"word": "garrulous", "options": ["talkative", "silent", "quiet"], "answer": "talkative"},
    {"word": "harangue", "options": ["rant", "compliment", "praise"], "answer": "rant"},
    {"word": "imbroglio", "options": ["confusion", "clarity", "order"], "answer": "confusion"},
    {"word": "inchoate", "options": ["incomplete", "perfect", "finished"], "answer": "incomplete"},
    {"word": "inculcate", "options": ["teach", "ignore", "forget"], "answer": "teach"},
    {"word": "inexorable", "options": ["unyielding", "flexible", "changeable"], "answer": "unyielding"},
    {"word": "inscrutable", "options": ["mysterious", "clear", "obvious"], "answer": "mysterious"},
    {"word": "lachrymose", "options": ["tearful", "joyful", "cheerful"], "answer": "tearful"},
    {"word": "magnanimous", "options": ["generous", "petty", "selfish"], "answer": "generous"},
    {"word": "malfeasance", "options": ["wrongdoing", "good deed", "virtue"], "answer": "wrongdoing"},
    {"word": "nefarious", "options": ["wicked", "good", "honorable"], "answer": "wicked"},
    {"word": "noisome", "options": ["foul", "pleasant", "aromatic"], "answer": "foul"},
    {"word": "obfuscate", "options": ["confuse", "clarify", "simplify"], "answer": "confuse"},
    {"word": "pecuniary", "options": ["financial", "emotional", "psychological"], "answer": "financial"},
    {"word": "perfidious", "options": ["treacherous", "loyal", "honest"], "answer": "treacherous"},
    {"word": "proclivity", "options": ["tendency", "aversion", "dislike"], "answer": "tendency"},
    {"word": "recalcitrant", "options": ["stubborn", "obedient", "compliant"], "answer": "stubborn"},
    {"word": "recondite", "options": ["obscure", "clear", "simple"], "answer": "obscure"},
    {"word": "sententious", "options": ["moralizing", "careless", "indifferent"], "answer": "moralizing"},
    {"word": "supercilious", "options": ["arrogant", "humble", "modest"], "answer": "arrogant"},
    {"word": "taciturn", "options": ["silent", "talkative", "loquacious"], "answer": "silent"},
    {"word": "tergiversate", "options": ["evade", "clarify", "state"], "answer": "evade"},
    {"word": "vituperative", "options": ["abusive", "kind", "gentle"], "answer": "abusive"},
    {"word": "winsome", "options": ["charming", "unattractive", "ugly"], "answer": "charming"},
    {"word": "zealous", "options": ["enthusiastic", "apathetic", "disinterested"], "answer": "enthusiastic"},
    {"word": "zenith", "options": ["peak", "valley", "bottom"], "answer": "peak"},
    {"word": "ubiquitous", "options": ["everywhere", "rare", "uncommon"], "answer": "everywhere"},
    {"word": "vituperate", "options": ["criticize", "praise", "commend"], "answer": "criticize"},
    {"word": "yoke", "options": ["bind", "release", "separate"], "answer": "bind"}
]

}

@app.get("/", include_in_schema=False)
@app.head("/")
def root():
    return {"message": "Welcome to the Synonym Game!"}


@app.get("/words/{level}")
def get_words(level: str):
    if level not in words_data:
        return {"error": "Invalid level"}
    
    selected_words = random.sample(words_data[level], 10)  # Pick 10 random words

    for word in selected_words:
        options = word["options"][:]  # Copy options list
        random.shuffle(options)  # Shuffle options
        
        # Find the correct answer's new index after shuffling
        correct_index = options.index(word["answer"])
        
        # Update word object with shuffled options and correct index
        word["options"] = options
        word["correct_index"] = correct_index  

    return selected_words