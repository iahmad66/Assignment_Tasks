# Convert the list into a set. Add a duplicate tool and show how the set handles it.
# Testing_tools = ["Github", "JIRA", "Slack", "Postman", "Jenkins" ]

Testing_Tool = ["Jira", "Selenium", "JMeter ", "Postman", " Cypress"]

testing_tool = set(Testing_Tool)
print("after conversion : ", testing_tool)

testing_tool.add("Postman")
print("Adding new element ", testing_tool)      # No changes after adding duplicate item in set