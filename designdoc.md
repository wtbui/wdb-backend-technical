Husband Calling Backend Design Doc

Overview:
The features implemented in this API include a POST endpoint to register contestants, a GET endpoint to observe all contestants and functionality to sort by name, and a GET endpoint to calculate the score of a single contestant.

Structure:
The project structure is compartmentalized into three different parts, the controller files, the model files, and the route files. The controller folder contains files which define logic wihtin the API and interact directly with the database. The model folder contains schema data. The routes folder contains routes to the different endpoints.

For this API, only one schema was used. This contains fields for the "contestant" class which includes the name, husbandName, vocalRange, and location. 

(ASSUMPTION) For this case, vocalRange and location were assumed to be Integers.

Error Codes:
For error/response codes, a couple were used throughout the project. 
For success, 200 (success) was used for any GET endpoints and 201 (successful create) for the POST endpoints. 
To validate the request data in the POST endpoint, code 422 (Unprocessable Content) was used in the event that the request data is invalid. 
For the "husbandCall" endpoint, code 406 (Not Acceptable) was used in the event that either the vocal range of a contestant is too small or a contestant is not registered.
To handle any general larger errors, code 500 was used. 

Difficulty:
For me personally, the most difficult endpoint to implement in this API to implement was the POST request. This was because it had the most interactions with the database and needed to have the request validated before it could be entered into the database. These extra steps added to the overall complexity. The way I handled it was by building it one part at a time, by doing so I could reduce the complexity of each individual problem which made it more manageable. 

    
