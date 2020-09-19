# Travel Master

## Route search to get from one point to another.

You can add, edit and delete cities. There is also a page-by-page view of all available cities.

You can add, edit and delete trains. There is also a page-by-page view of all available trains. The train has a unique code (name), starting point, ending point, and duration time in conventional units. There can be several trains from one point to another.

You can select the starting and ending point of the route, as well as specify the maximum duration time. Also, the user can add any intermediate cities through which the route should run. The user gets routes satisfying the conditions. The user can save this route by giving it a name.

Route output is sorted according to the shortest duration time. Thus, the route with the shortest duration time is displayed first. The description of the route contains information about starting point, ending point, duration time, and also contains a list of all trains that are on this route.

If the route is not found, the user will receive a message: "Requested route does not exist". If the specified duration time is less than the minimum route time, then user will get the following message: "The duration time is longer than you entered. You should increase the duration time."

If logged in, users get access to adding and editing both trains and cities as well as deleting any records.

If not logged in, the route can only be saved, viewed and deleted. You cannot edit a saved route.
