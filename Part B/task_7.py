# Use enumerate on your tool list and print both index and tool name.

Testing_tools = ["Github", "JIRA", "Slack", "Postman", "Jenkins" ]

tools = dict((enumerate(Testing_tools)))
print("values of the list with thier index are : " )
for index, value in tools.items():
    print(index,value)