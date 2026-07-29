starting = 1500
new_chat = 500
maxPrice = 8000

old_chat = []
total_chat = []


def chat_prediction(n, overhead, new_chat, maxPrice, old_chat = None, total_chat = None):
    nth_chat = 0
    if old_chat is None and total_chat is None:
        old_chat = []
        total_chat = []
    while nth_chat < n:
        chat_cost = overhead + sum(old_chat) + new_chat 
        current_cost = min(chat_cost, maxPrice) # capped at 8000
        nth_chat += 1
        old_chat.append(new_chat)
        total_chat.append(current_cost)
    return f"total cost {sum(total_chat):,} Token in {nth_chat}th`"

print(chat_prediction(1000, starting, new_chat, 32000))
