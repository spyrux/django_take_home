# Remarcable Django Take Home

This project is a simple Django application that models products, categories, and tags. Users are able to search for keywords in the products descriptions, filter by tags, and filter by categories. 20 products, 5 categories, and 12 tags have been created with Django Admin and provided as an example database.

## Models Documentation

### Category Model

The `Category` model is used to represent categories that can group multiple products.

#### Fields

- **`name`**
  - Type: `CharField`
  - Description: The name of the category.
  - Attributes:
    - `max_length=40`: Restricts the length of the category name to 40 characters.
  - Example: `"Electronics"`

#### Methods

- **`__str__`**
  - Purpose: Returns the string representation of the category.
  - Output: `"Electronics"`

---

### Tag Model

The `Tag` model is used to represent tags that can be associated with one or more products.

#### Fields

- **`name`**
  - Type: `CharField`
  - Description: The name of the tag.
  - Attributes:
    - `max_length=40`: Restricts the length of the tag name to 40 characters.
  - Example: `"Wireless"`

#### Methods

- **`__str__`**
  - Purpose: Returns the string representation of the tag.
  - Output: `"Wireless"`

---

### Product Model

The `Product` model represents a product that belongs to a category and may have multiple or no tags.

#### Fields

- **`description`**

  - Type: `TextField`
  - Description: A detailed description of the product.
  - Attributes:
    - No length restriction (uses `TextField`).
  - Example: `"A pair of wireless earbuds with high sound quality."`

- **`name`**

  - Type: `CharField`
  - Description: The name of the product.
  - Attributes:
    - `max_length=40`: Restricts the length of the product name to 40 characters.
  - Example: `"Wireless Earbuds"`

- **`category`**

  - Type: `ForeignKey` (to `Category`)
  - Description: Links the product to a specific category.
  - Attributes:
    - `on_delete=models.CASCADE`: Deletes the product if the associated category is deleted.
  - Example: A product in the `"Electronics"` category.

- **`tags`**
  - Type: `ManyToManyField` (to `Tag`)
  - Description: Allows assigning multiple tags to a product.
  - Attributes:
    - `blank=True`: Makes this relationship optional.
  - Example: `"Portable", "Wireless"`

#### Methods

- **`__str__`**
  - Purpose: Returns the string representation of the product.
  - Output: `"Wireless Earbuds"`

## Local Setup

Clone the project

```bash
  git clone https://github.com/spyrux/django_take_home.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install django
```

Make migrations and migrate

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Load the example database

```bash
  python manage.py loaddata db.json
```

Run the server and view on your development port i.e http://127.0.0.1:8000/

```bash
  python manage.py runserver
```

## Additional Notes and Considerations

- Represented Categories and Tags as objects that only had a name field.
- Products could have many Tags or none.
- Products could only belong to one Category.
- The dataset and search volume are relatively small.
  
## Potential Improvements

### Search Optimization

- Full-text index search with rather than using a simple partial search with icontains.

### Interface Improvements

- User Interface could be improved by leveraging front-end frameworks like Angular or React.

### Database Scaling

- Adjustments would have to be made to the architecture of the database to account for large-scale read and writes.

