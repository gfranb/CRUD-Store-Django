# store-crud
**🏬 Store-CRUD**

A Store CRUD with Django.

This CRUD application is designed to practice and demonstrate the basic concepts of Django, including:

    🔗 URLs

    🗄️ Models

    👁️ Views

    📄 Templates

    📝 Forms

The request responses are returned as HTML.


**📁 Project Structure**

The CRUD consists of 3 main classes:


    📦 Category
    🚩 Campaign
    🛍️ Product
    
    
Relationships between classes:


    📦 Category is a superclass of 🚩 Campaign.

    🚩 Campaign is a superclass of 🛍️ Product.

    Each 📦 Category can have one or more 🚩 Campaigns.

    Each 🚩 Campaign can have one or more 🛍️ Products.


In order to create a new entry, both a 📦 Category and a 🚩 Campaign are required.


Models in this project utilize Foreign Keys to establish relationships and enable filtering.


**🚀 Getting Started**

To get started with this Store CRUD project:


Ensure you have Django installed.

Clone this repository to your local machine.

Run the Django development server.

Access the application in your web browser.

Feel free to modify and enhance the project as needed!



If you have any questions or need further assistance, please don't hesitate to reach out.
