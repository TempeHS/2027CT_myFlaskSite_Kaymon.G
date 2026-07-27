# Website Name

| Field                          | Detail |
| ------------------------------ | ------ |
| **Website Title**              | Number Nexus       |
| **Student Name(s)**            | Kaymon Gurrala       |
| **Class / Course**             | 9CT1       |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Kaymon.G       |
| **Live Site / Codespaces URL** | N/A       |
| **Date**                       | 23/ 07/ 26       |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:** <!-- One or two sentences: what the site is and why it exists (from your Statement of Intent). -->
Number Nexus is an interactive math platform primarily designed for students aged 12-18, the site will serve as an educational tool that aims to improve skills, confidence and engagement through resources provided, practice questions and multiple video explanation. It is needed because currently we have realised that many people tend to struggle in speed, accuracy and confidence in maths.

**Target audience:** <!-- One sentence: who the site is for (from your personas). -->
The primary audience for this website is teenagers and students aged 12-18 who want to improve at math and excel in the topics that they're learning. This website’s main audience are for students who are very comfortable and familiar with technology, allowing them to access content easier through the user-interface. However, many students struggle with time, so the navigation controls must be quick and easy to use.

**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom CSS · pytest

---

## 2. Walkthrough Video (2 minutes)

This is the most important part of your documentation — it shows your website running.

<!--
  Embed a ~2 minute walkthrough. Replace VIDEO_ID with your YouTube video ID:
  [![Website Walkthrough](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

  OR link a screen recording stored in the repository:
  [Watch the Walkthrough](./docs/walkthrough.mp4)
-->

| Field            | Detail |
| ---------------- | ------ |
|<img width="476" height="267" alt="Homepage" src="https://github.com/user-attachments/assets/2fb52517-d629-4084-a27c-723f61cac3ae" /> |Hi, I'm Kaymon, and this is Number Nexus—a Flask-based web application designed to help students aged 12–18 build math speed and confidence. On the home page, students are greeted with a clean layout utilizing a mobile-responsive Bootstrap navbar and a 3-column grid system that instantly outlines how the platform tackles math anxiety.The homepage introduces Number Nexus with a clean Bootstrap layout and responsive navigation.        |
| <img width="476" height="267" alt="contact page" src="https://github.com/user-attachments/assets/5c677d47-fcab-4b34-bcc6-74a41e5d6ce5" />   | The Contact page features an embedded Google Map and a simple enquiry form for user communication.|
|<img width="476" height="267" alt="About Us" src="https://github.com/user-attachments/assets/66520804-cc91-428b-ba92-d5250ff97f4d" /> |The About Us page explains the purpose and goals behind the platform using structured Bootstrap containers.        |
| <img width="476" height="267" alt="Content and Practice Pages" src="https://github.com/user-attachments/assets/106c3770-11b0-4361-b10f-0c6f35688425" /> |The Content page uses Bootstrap cards to organise math subjects clearly for fast browsing. Which links to actual learning content taht includes a responsive video player and formula tips to support quick learning. After this, the page leads you to practice questions on the topic to review your knowledge.        |
| <img width="476" height="267" alt="Login page" src="https://github.com/user-attachments/assets/112171ce-1a00-4bb2-997c-d65e407de6c2" /> |The Login page demonstrates the authentication interface using Bootstrap form styling.        |
|<img width="476" height="267" alt="Dark mode enable and disable" src="https://github.com/user-attachments/assets/95871a0e-99f1-402b-beb5-b11db2787bca" /> | Dark mode is implemented using the CSS prefers-color-scheme media query. This allows the website to detect the user’s operating system colour preference and apply the correct theme automatically. Because the theme is selected before the page renders, users experience a seamless transition with no flashing or layout shift. This approach improves accessibility, reduces eye strain, and ensures the interface feels modern and responsive across all devices.|
|<img width="476" height="267" alt="Mobile Responsiveness" src="https://github.com/user-attachments/assets/b6fa9aab-5862-4e9b-80c0-18b6de39e2e2" /> | The layout scales smoothly to mobile, with the Bootstrap navbar collapsing into a hamburger menu for easy navigation.  |
| <img width="476" height="267" alt="Backend Testing" src="https://github.com/user-attachments/assets/39b63942-ff41-4f4d-bf0f-0fa5f9a69ca3" /> | Automated tests confirm stable Flask routing and clean 200 responses across all pages.  |
**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?

### Overall Delivery: Successful
Yes, the delivered website successfully satisfies the core requirements outlined in the original Statement of Intent. "Number Nexus" functions as a responsive, interactive educational tool that targets math confidence and accuracy for users aged 12–18. 

### Evidence of Success
* **Engagement & Resources (Intent: Improve Skills):** The website successfully serves instructional math content using dynamic **Jinja2 templates**. Video resources are integrated directly into the topic pages, lowering the barrier to entry for visual learners.
* **Speed & Navigation (Intent: Quick Controls for Busy Students):** By leveraging the **Bootstrap CDN**, the user interface is lightweight, highly responsive, and optimized for fast mobile or desktop navigation. Students can jump between topics instantly without clunky load times.
* **Platform Reliability (Intent: Functional Educational Tool):** Code stability was verified using **pytest**. Testing the Flask routes ensures that students do not encounter broken links or `404` errors when navigating through critical practice modules.

### Areas for Growth & Honest Reflection
While the core educational framework and navigation UI are fully delivered, the "speed training" aspect of the intent can be pushed further. In future iterations, implementing JavaScript-based countdown timers and an automated accuracy tracking scorecard would create a more robust feedback loop for students looking to measure their exact progress.

## 3.1 Your Statement of Intent

### 1. Statement of Intent 

1.1 What is the website? 

Number Nexus is an interactive math platform primarily designed for students aged 12-18, the site will serve as an educational tool that aims to improve skills, confidence and engagement through resources provided, practice questions and multiple video explanation. It has a homepage featuring new content and information, and a resource section for different year groups and levels of math, this page will also contain many of the additional features mentioned later. It will feature example questions for the user, to ensure that they learn about the content given to them. It will also contain a user-friendly interface that's easy to use. Not only that, but the website will help deepen their understanding and improve problem-solving efficiency. 

1.2 Why is it needed? 

Currently we have realised that many people tend to struggle in speed, accuracy and confidence in maths. This is often because they are lacking engaging learning tools which causes students to have dull and boring learning experiences, so they don't maintain their confidence and drive to complete their work. It causes a decrease in their motivation leading to a poorer academic performance over time. It creates problems for people who are at any level of content and causes many problems to people who are already struggling at math. 

  

We expect this website to make a huge change. Number Nexus is designed to make learning math a fun and enjoyable experience, building up confidence and motivation for students who have trouble with math. This website is designed to also improve the student’s academic performance. The website allows students to excel in their math classes and can help them out with structured sources and step-by-step videos explaining the content to help them understand what they're learning in much more depth. 

1.3 Who is it for? 

The primary audience for this website is teenagers and students aged 12-18 who want to improve at math and excel in the topics that they're learning. This website’s main audience are for students who are very comfortable and familiar with technology, allowing them to access content easier through the user-interface. However, many students struggle with time, so the navigation controls must be quick and easy to use. Metalanguage will be taught along the course on the website to allow the user to understand more complex words and terms. 

1.3 Summary 

Number Nexus will transform perspectives of how students view math by changing it from a boring and uninteresting subject to a fun, enjoyable and exciting course that many people will excel in. The website makes it easier for students to learn math in a simple and fun way, so they can learn and take everything they learn so they can use it later during math class and exams. With tips, tricks and videos to help the user understand math, the website gives more knowledge to the students by helping them achieve more through a simple website. We expect this website to make a huge change in many students' lives by helping them improve massively in maths while also helping them keep up to their peers and help them achieve much higher than their initial goal while having a comfortavble experience.

### 3.2 What You Delivered

| Page    | Route      | What it delivers |
| ------- | ---------- | ---------------- |
| Home    | `/`        | A responsive homepage featuring Bootstrap components (navbar, carousel, cards), and quick navigation for students aged 12–18. It introduces the purpose of Number Nexus and links to learning resources.                 |
| Contact | `/contact` | A contact page containing an embedded Google Map, a form, and Bootstrap layout elements. Allows users to reach out and demonstrates correct Flask routing and responsive design.                 |
| Login | `/login` | A functional login interface built with Flask and Bootstrap. Provides a simple authentication entry point and demonstrates form handling, responsive layout, and user‑flow preparation for future personalised features.                 |
| About Us | `/learn_more` | A detailed information page explaining the mission, purpose, and goals of Number Nexus. It expands on the site's intent, uses Bootstrap for layout, and provides students with background context about how the platform supports their learning.                 |
| Content | `/content` | A resource hub displaying responsive Bootstrap cards containing math topics, example questions, and embedded video explanations. This page delivers the core learning materials of Number Nexus and adapts to dark mode for improved accessibility and user comfort.                 |
| Stage 3 Math | `/stage-3` | A topic page containing Stage 3 math explanations, example questions, and embedded videos. Uses responsive cards and consistent Jinja2 templates. |
| Stage 4 Math | `/stage-4` | A topic page delivering Stage 4 math content with structured explanations, worked examples, and visual learning resources. Includes responsive Bootstrap cards and dark mode support. |
| Stage 5 Math | `/stage-5` | A Stage 5 learning page featuring curriculum‑aligned explanations, example problems, and embedded video walkthroughs. Designed with consistent Jinja2 templates for predictable navigation. |
| Stage 6 Math | `/stage-6` | An advanced topic page providing higher‑level mathematical explanations, worked examples, and video demonstrations. Uses responsive cards and supports dark mode for accessibility. |
| Stage 3 Questions | `/stage-3/questions` | A practice page containing Stage 3 questions with structured examples and Bootstrap formatting. Supports fast navigation for revision. |
| Stage 4 Questions | `/stage-4/questions` | A question page delivering Stage 4 practice problems and revision tasks using consistent Jinja2 templates and responsive layout. |
| Stage 5 Questions | `/stage-5/questions` | A Stage 5 question bank offering curriculum‑aligned practice questions designed to build confidence, speed, and accuracy. |
| Stage 6 Questions | `/stage-6/questions` | An advanced question page containing higher‑level problems for Stage 6 students, formatted for clarity and efficient study flow. |

### 3.3 Evaluation Against Your Intent

The delivered version of Number Nexus successfully fulfills its primary intent as an interactive, accessible math platform for students aged 12–18. The core goal of improving student skills and engagement was achieved by pairing visual learning materials with clear layout design. By utilizing Jinja2 templates, topic structures remain consistent, allowing students to study without being distracted by unpredictable layouts. This directly addresses the student persona requirements of reducing math anxiety and building confidence, as the application serves as a reliable, predictable central environment for revision.

Where the website meets its intent best is in its rapid navigation and streamlined user interface, which directly satisfies the target audience's need for fast, efficient controls. Built upon the Bootstrap CDN framework, the site features low page-load latencies and clean menus that allow time-restricted teenagers to jump into revision modules instantly. The structural health of these navigation pathways is backed by an automated `pytest` suite that strictly validates route status codes, ensuring students are never slowed down by broken pages or missing content links.

However, the implementation fell short of its initial intent regarding advanced speed and accuracy optimization tools. While static practice questions and resources are readily accessible, the platform lacks a built-in interactive feedback loop, such as a JavaScript countdown timer or a real-time tracking dashboard, to explicitly measure a user's problem-solving velocity. This omission occurred because project development prioritized backend stability and responsive layout scaling over complex script execution. Consequently, while the platform excels as an informative and stable resource hub, the simple time-pressure features remain an item for future development. I should've mentioned ideas of reducing strain for users through colours schemes, like dark mode, I should've mentioned this in my Statement of Intent as I have now built the skills to implement this idea, this is one thing I should've put in my Statement of Intent so the users experience will not be impacted by strain.


### 3.4 Overall Effectiveness (1–2 paragraphs)


Overall, Number Nexus serves as a highly effective baseline platform for its target audience of tech-savvy teenagers who need quick, reliable access to math revision resources. The application balances clean presentation with fast performance, allowing time-restricted students to locate video walkthroughs and review topics instantly without fighting complex interfaces. By providing a stable, distraction-free layout backed by a robust Flask architecture, the platform effectively reduces learning friction and supports students in building baseline confidence at their own pace. 

However, the website’s total effectiveness is currently constrained by its static nature, lacking the aggressive speed-building tools required to truly master mathematical velocity. To transition the site from a reliable resource library into a truly high-utility training hub, the next crucial step is implementing a dynamic quiz system featuring automated score tracking and immediate UI feedback. Introducing a localized achievement leaderboard would also leverage peer competition to increase daily engagement, turning the platform into a comprehensive, high-velocity tool that fully delivers on its promise of enhancing both math speed and accuracy.

---

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

| What you used | Source / Creator | Licence | What you used it for   |
| ------------- | ---------------- | ------- | ---------------------- |
| Bootstrap     | Bootstrap team   | MIT     | Layout and components  |
| Flask         | Pallets Projects | BSD     | Web server and routing |
| Images        | Magnific         | EULA    | Images and placeholders|
| Fonts         | Google Fonts     | OFL     | Fonts and text areas   |
|Youtube videos | Youtube          |No license| Tutorials and content |
---

> **Student Declaration:** All work submitted is my own except where explicitly acknowledged above.
