## Testing 

Rigorous manual and automated testing was conducted throughout the development lifecycle of **ApplyTrack** to ensure high standards of quality, reliability, performance, and cross-device accessibility. 

The primary objective of the testing process was to confirm that all core functionality aligns with user requirements, that secure data handling is enforced across views, and that the application delivers a seamless, responsive user experience on mobile, tablet, and desktop viewports.

The following sections detail the code validation steps, performance and accessibility audits, manual feature test cases, and bug resolutions executed prior to production release.

### User Stories/features

**US1: Register an account:**

As a new user, I want to register for an account, so that I can use ApplyTrack to manage my job applications.

Acceptance criteria:

- [x] User can enter a username.
- [x] User can enter an email address.
- [x] User can create a password.
- [x] User must confirm their password.
- [x] Account is created when valid information is submitted.
- [x] User receives an appropriate error if the information is invalid.

Feature:

![Register feature](docs/user-stories/us1.png)

**US2:Login:**

As a registered user, I want to log in to my account, so that I can access my job applications.

Acceptance criteria:

- [x] User can enter their username/email and password.
- [x] Valid credentials allow access.
- [x] Invalid credentials display an error.
- [x] User is redirected to their dashboard after logging in.

Feature:

![Login feature](docs/user-stories/us2.png)

**US3:Logout:**

As a logged-in user, I want to log out, so that my account remains secure when I finish using the application.

Acceptance criteria:

- [x] User can find a logout option.
- [x] User is logged out successfully.
- [x] User cannot access protected pages after logging out.

Feature:

![Logout feature](docs/user-stories/us3.png)

**US4: Add and application:**

As a job seeker, I want to add a job application, so that I can keep a record of jobs I have applied for.

Acceptance criteria:

- [x] User can enter company name.
- [x] User can enter job title.
- [x] User can enter location.
- [x] User can enter application date.
- [x] User can select an application status.
- [x] Application is saved to the database.

Feature:

![Add application ](docs/user-stories/us4.png)

**US5: View my applications**

As a job seeker, I want to view my applications, so that I can see the jobs I am currently tracking.

Acceptance criteria:

- [x] User can see their applications on the dashboard.
- [x] Each application displays important information such as company, job title and status.
- [x] Applications belonging to other users are not displayed.

Feature:

![View application ](docs/user-stories/us5.png)

**US6: Edit an application**

As a job seeker, I want to edit my job applications, so that I can keep the information up to date.

Acceptance criteria:

- [x] User can access an edit option.
- [x] Existing information is displayed in the form.
- [x] User can change the information.
- [x] Changes are saved to the database.
- [x] Users cannot edit another user's application

Feature:

![Edit application ](docs/user-stories/us6.png)

**US7: Delete an application**

As a job seeker, I want to delete an application, so that I can remove applications I no longer want to track.

Acceptance criteria:

- [x] User can select delete.
- [x] User is asked to confirm deletion.
- [x] Application is removed after confirmation.
- [x] User can cancel deletion.
- [x] Users cannot delete another user's application.

Feature:

![Delete application ](docs/user-stories/us7.png)

**US8: Track application status**

As a job seeker, I want to assign a status to each application, so that I can easily track my progress.


Acceptance criteria:

- [x] User can select a status when creating an application.
- [x] User can change the status later.
- [x] Current status is displayed on the dashboard.
- [x] Status options are consistent throughout the application.

Feature:

![Track application status ](docs/user-stories/us8.png)

**US9: Track interview dates**

As a job seeker, I want to record an interview date, so that I can keep track of upcoming interviews.

Acceptance criteria:

- [x] User can optionally add an interview date.
- [x] Interview date can be edited.
- [x] Interview information is displayed on the application details page.

Feature:

![Track interview date ](docs/user-stories/us9.png)

**US10: Add notes**

As a job seeker, I want to add notes to an application, so that I can record useful information about the recruitment process.

Acceptance criteria:

- [x] User can add notes.
- [x] Notes can be edited.
- [x] Notes are displayed on the application details page.

Feature:

![Add notes](docs/user-stories/us10.png)

**US11: Responsive application**

As a user, I want ApplyTrack to work on different screen sizes, so that I can use it on my computer, tablet or phone.

Acceptance criteria:

- [x] Navigation works on smaller screens.
- [x] Forms are usable on mobile.
- [x] Application cards/tables adapt to smaller screens.
- [x] Text remains readable.

Feature:

Tablet:
![Responsive Design tablet view](docs/readme-images/tablet.png)

Mobile:
![Responsive Design mobile view](docs/readme-images/mobile.png)

Desktop:
![Responsive Design desktop view](docs/readme-images/desktop.png)

**US12: Clear feedback**

As a user, I want to receive feedback when I perform an action, so that I know whether it was successful.

Acceptance Criteria:

- [x] Users receive an on screen notification when they have completed an action

Feature:

![Notification](docs/user-stories/us12.png)

**US13: Security**

As a registered user, I want my applications to be private, so that other users cannot access or modify my information.

Acceptance criteria:

- [x] Users can only see their own applications.
- [x] Users cannot edit another user's application.
- [x] Users cannot delete another user's application.
- [x] Unauthenticated users cannot access the dashboard

![Security](docs/user-stories/us13.png)




### Mobile Lighthouse Testing


| Page | Result Screenshot |
| :--- | :--- |
| Home / Landing Page (Logged out view) | ![Lighthouse result](docs/lighthouse/mobile-1.png) |
| Login Page | ![Lighthouse result](docs/lighthouse/mobile-2.png) |
| Registration Page | ![Lighthouse result](docs/lighthouse/mobile-3.png) |
| Applications Page | ![Lighthouse result](docs/lighthouse/mobile-4.png) |
| View Applications Page | ![Lighthouse result](docs/lighthouse/mobile-5.png) |
| Contact Page | ![Lighthouse result](docs/lighthouse/mobile-6.png) |


### Desktop Lighthouse Testing


| Page | Result Screenshot |
| :--- | :--- |
| Home / Landing Page (Logged out view) | ![Lighthouse result](docs/lighthouse/desktop-1.png) |
| Login Page | ![Lighthouse result](docs/lighthouse/desktop-2.png) |
| Registration Page | ![Lighthouse result](docs/lighthouse/desktop-3.png) |
| Applications Page | ![Lighthouse result](docs/lighthouse/desktop-4.png) |
| View Applications Page | ![Lighthouse result](docs/lighthouse/desktop-5.png) |
| Contact Page | ![Lighthouse result](docs/lighthouse/desktop-6.png) |

