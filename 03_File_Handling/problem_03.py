#To replace the content of a file with new content, you can use the following code:
new_content = "Growth is not always about achieving big milestones; often, it is found in the small, " \
              "consistent steps we take each day. Whether it’s learning a new skill, overcoming a challenge, or simply " \
              "staying committed to our goals, progress builds quietly but powerfully. The key lies in patience and persistence—understanding " \
              "that setbacks are part of the journey and that resilience transforms obstacles into opportunities. In the end, success is less " \
              " about speed and more about steady determination."
with open("message", "w") as f:
    f.write(new_content)
    f.write("\n")  # Add a newline for better readability

with open("message", "r") as f:
    data = f.read()
    print("Original data:", data)
    new_data = data.replace("Growth", "Success")
    print("New data:", new_data)

with open("message", "w") as f:
    f.write(new_data)