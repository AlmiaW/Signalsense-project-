print("SignalSense Communication Pattern Tracker")
print("This program helps you log communication patterns and notice changes over time.")

user = input("Enter your name: ")
print("Welcome,", user)

message_sent = input("What time did you send the message? ")
response_time = int(input("How many minutes did it take for them to respond? "))
messages_this_week = int(input("How many times did you communicate this week? "))

print("\n--- SignalSense Summary ---")
print("Message sent:", message_sent)
print("Response time:", response_time, "minutes")
print("Communication frequency this week:", messages_this_week, "times")

if response_time <= 30:
    print("Pattern insight: The response time appears fairly quick.")
else:
    print("Pattern insight: The response time appears delayed.")

if messages_this_week >= 5:
    print("Consistency insight: Communication appears consistent this week.")
else:
    print("Consistency insight: Communication appears less consistent this week.")

print("\nSignalSense helps turn communication patterns into something clear and measurable.")
print("End of program.")
