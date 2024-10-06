# Car selling platform project

## Business Requirements

### Project to build a platform where owners can announce their cars for selling directly

## Functionalities
- The users should be able to:
  - As a seller. make a post announcing their car to sell and manage its content
  - Exchange messages between the sellers and the potential buyers 

## Entities and attributes:
- Users
  - Sellers
  - Buyers
  
- Seller
  - Name
  - Location
  - Contacts

 - Buyer
  - Name
  - Contacts

  Unregistered users can contact sellers.
  - This option should be able to be disabled in the Buyers' profile

- Car
  - Pictures - various
  - Initial picture
  - Model
  - Brand / automaker
  - Number os seats
  - Year of manufacture
  - Type
    - Familiar
    - Van
    - Truck
  - Owner / Seller - Default to current user
  - Date of creation auto to today
  - Date published - default to today
  - Display - Yes/No - The add may not be visible in listings
  
- Messages
Note: We can opt to use a pre-existing application, like django-postman  
For a local application attributes would be:
  - From
  - To
  - Subject
  - Body content
  - Delivered date
  - Read date

--------
