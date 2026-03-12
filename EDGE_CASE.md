# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified
The spec does not specify what should happen when GET /stats is called 
with no students in the database.

2) How you have accounted for this in your implementation
If there are no students, the endpoint returns:
{"count": 0, "average": null, "min": null, "max": null}

Without this check, calculating average/min/max on an empty list would 
cause a division by zero error and crash the server.