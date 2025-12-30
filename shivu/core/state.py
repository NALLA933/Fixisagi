import asyncio

locks = {}
message_counts = {}
sent_characters = {}
last_characters = {}
first_correct_guesses = {}
spawn_messages = {}
spawn_message_links = {}
currently_spawning = {}

MESSAGE_FREQUENCY = 40
DESPAWN_TIME = 180
AMV_ALLOWED_GROUP_ID = -1003100468240