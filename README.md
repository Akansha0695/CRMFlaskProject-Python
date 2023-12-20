                                            Customer Relation Management - Flask Project - Python


This Flask project consists of a simple web application with multiple routes for managing customer information. The project uses Flask, a Python web framework, to handle HTTP requests and render HTML templates. The application interacts with a database (presumably defined in a module named Database) to perform CRUD (Create, Read, Update, Delete) operations on customer records.


                                                       The main routes include
                                                       
**Home**: Displays the main page of the application.

**About Us**: Renders a page providing information about the project or the company.

**Contact Us**: Displays a contact page.

**Customer List**: Retrieves all customer records from the database and displays them on a page.

**Add Customer**: Provides a form to add a new customer. Handles both GET and POST requests, adding a new customer to the database upon form submission.

**Delete Customer**: Allows for the deletion of a customer record based on the provided customer ID.

**Update Customer Detail**: Allows for updating customer details based on the provided customer ID.





**The application employs HTML templates for rendering pages and dynamically interacts with the database to manage customer information. It runs in debug mode, which is helpful during development for real-time updates. To run the application, execute the script, and the Flask development server will start, making the web application accessible locally.**
