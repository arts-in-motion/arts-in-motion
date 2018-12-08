# Documentation





## Users and User Groups
Users in this application are admin users, or people that will be able to sign in and access this database.

To see a list of all users go to '.../auth/user/'

Edit a current user:

The main thing you will probably need is to make someone a 'superuser'. Superuser status designates that the user has all permissions without explicitly assigning them.

Add a new user:

'.../auth/user/add/'

Groups:

Using groups is a way to group together different users with similar permissions.

## Classes
To see a list of classes on the admin site go to '.../classes/class/'.

You can filter classes by which classes are 'active' or 'inactive'.

You can order 'start_date' and 'description' by clicking on that title. You can search by description by entering in the description into the 'search field' on the top right of the page.

Scroll to the bottom of the page and you will be able to select 'export' or 'delete' selected classes. This let's you delete multple classes at once. It also let's you export the selected classes to a csv.

If you click on the 'Report Link' on the right side of the row for each class, you will be taken to a Class report page for that class. More on reports below.

To add a new class, you can click the button 'add class' which will take you to '.../classes/class/add'.

Required fields are in bold, other fields are optional. For example, 'description' is required, whereas 'end_date' is not.

'Instructors' can be chosen from 'Individuals' by clicking on the magnifying glass in the Instructor's field. A window will pop up with a list of Individuals to choose from. If the Individual you want to add isn't listed, you can click 'Add Individual' in the top right of that popup window and follow instructions.

Students can be added to this class at the bottom of the page. click 'Add another student-class relationship' and you will be able to choose from a list of Individuals that are Students.

If the student isn't on the list, you will need to add them at '.../contacts/individual/add/' and be sure to mark them as 'student'.

Continue adding students by repeating those steps. When all students are entered, you can click 'Save' at the bottom of the page.

## Class Reports

To see a list of classes that isn't on the admin page you can visit '.../class-reports'. There is a table with a list of classes. You can click on each of these classes and it will take you to a detailed view.

For example:
'../class-reports/1' will take you to a class with id number that is 1. You can see all the students information that are enrolled in the class. You can also print this page.

There are links on the top of the page to go back to the class list, admin list or admin edit page for this class.

## Donations

Visit '.../donations/donation/' to se a list of donations. You can search donations by donor name.

To add a new donation:

Click 'Add Donation' and it will take you to '.../donations/donation/add/'