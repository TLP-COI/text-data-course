# Syllabus ({{course}} {{semester}})

```{warning}
:class: dropdown
This syllabus is a draft, and subject to change. 
Use it as a guide for course expectations, but always clarify with a question if something seems uncertain!

```



##  Text as Data for Technical Language Processing

::::{sidebar} Course and Conact Information
:::{admonition} Course Information
{{info_panel}}
:::

:::{admonition} Instructor Contact
:class: tip
{{instructor_panel}}
:::
::::

This course is intended for those wanting to apply various modern text analysis techniques to gain domain-specific insights from their natural language data. 
Natural Language Processing (NLP) requires special care to apply in a useful, reprocucible, and ethical way. 
This is especially true when context becomes a large factor in how the text is written or understood --- for instance, technical fields like Social Science, Medicine, Engineering, Policy, Digital Humanities, and many more.


With that in mind, this course does not take a traditional, theory-heavy approach to the subject matter. 
Instead, the goal is to guide newcomers through the plethora of tools, theoretical assumptions, data types, and ethical questions that arise when NLP is used as descision-support for experts and decision makers. 
This is a class about how the broader NLP Socio-technical system can or even _should_ function: Technical Language Processing. 

This course is meant to be enjoyable and thought-provoking! 
I have tried to set the tone with "fun" titles and examples, since it's important to experiment and ask questions in a comfortable environment. 
But, it will also address some key ethical questions and hopefully get us thinking critically about the power our assumptions and decisions have when using these techniques. 

## Prerequisites

- Comfortable with Python and Jupyter Notebooks. Other languages are acceptable for submission of work (e.g. R, Julia, Octave), especially if the language has a working kernel interface to Jupyter Notebooks, but the course examples and software overviews will be demonstrated exclusively in Python. 
  Experience using the foundational data science tools in Python (numpy, pandas, scikit-learn, etc.) will be immensely helpful. 
- Comfort using version control systems (git), and plain-text markup for project and homework tracking and submission. 
- Familiar with basic statistics concepts (discrete and continuous distributions, Bayes' rule, sampling, etc.); Some exposure to machine learning concepts (classification, clustering, regression, supervised vs un/semi-supervised learning). 
- Those unfamiliar with one or more of the above are welcome to take the course! Links to resources might be available, but responsibility for catching up will rest with *you*, and all students will be held to the same standard of work. 

## Course Schedule

The Sections are broken down slightly different from most NLP or text analysis courses. 
By using problem-solving frameworks from e.g. engineering disciplines, I hope to bring a flavor of just how _important_ context is to your applications of these technicques to technical text. 

```{margin}
Bring a laptop every week, as the section material will be largely interactive and essential to follow along with, yourself.
```

- Week 1: Introduction and Logistics 
  - Why "TLP"?
  - Tools of the Trade
- Week 2-4: Unit 1 --- Assumptions ("P" the "NL")
  - Follow the rules: Keywords, Ontologies, and Rule-based Methods
  - The company you keep: Bags-of-wording, matrices, & topic models 
  - Fill in the blank: Markov models, sometimes hidden
  - Fantastic Nets and Where to Find Them: semantic embeddings 
- Week 5-6: Unit 2 --- Goals & Approaches in Text Analyses
  - A thousand words: Clustering, Classifying, & Entity Recognition
  - Day-in-the-life: putting the "pipeline" together
- Week 7-8: Unit 3 --- Measuring & Evaluating NLP "Systems"
  - Measuring Up: Similarity, Quality, and Importance metrics
  - You're the Translator: communicating transparent evaluation
- Week 9: Unit 4 --- Validation (and the role of expertise)
  - Finish the Owl: reasessing the "pipleline" 
  - What is "TLP", exactly? 
- Week 10-12: Case Studies, Special topics, & Guest Lectures (TBD)
- Week 13-14: Project Discussions, Q&A, and Final Presentations

## Evaluation

Participation - 20%
: Bring a laptop, participate in class discussions and exercises, and analyse the impacts and nuance of various techniques and datasets we use or read about. 
  Much of the lecture is intented to operate similar to a lab, getting hands-on experience using the data, tools, and techniques described. 
  I expect everyone who attends and engages with the class discussions to do well here!

Homework - 40%
: Apply concepts to your own data using methods from each of the four units. 
  A lot of the this course centers around not only applying NLP and other analysis types, but interpreting and critically engaging with assumptions, flaws, and possibilities they present in the context of your text's domain. 
  
  - Unit 1 HW - 10%
  - Unit 2 HW - 10%
  - Unit 3 HW - 10%
  - Unit 4 HW - 10%

  Every homework report should outline your assumptions, key decisions, and methods; think outside-the-box, and get help ahead-of-time if you're feeling stuck. 

Project - 40%
: Intended to allow free-form exploration and decision support using your dataset of choice, to emulate the ways NLP gets applied in technical domains. 

  - One project, two staged "submissions" 
    - Mid-semester report (due start of week 9) - 10% 
    - Final report (due start of week 14) - 20%
  - final presentation to class (week 14) - 10% 

Extra Credit - 5%
: There will be extra credit available for those that are willing/able to create interactive presentations or visualizations from their homeworks. 
  These must be presented to the class at the beginning of the lecture, and used to guide a short (15-min) class discussion about homework experiences and observations. 
  Email or talk with me about your planned presentation idea *at least 48 hours prior* to the start of class so I can provide feedback or direction. 

 ```{margin}
 In other words, an on-time submission graded 90% will be worth 81% the next day, and 73% the day after that. 
```
  
 Late work will be accepted, at a cost of 10% the remaining point value per day. 



## Important Information for {{institution}} Students 

Disability
:  If you believe you have a disability, then you should contact the Academic Resource Center (arc@georgetown.edu) for further information. The Center is located in the Leavey Center, Suite 335 (202-687-8354). The Academic Resource Center is the campus office responsible for reviewing documentation provided by students with disabilities and for determining reasonable accommodations in accordance with the Americans with Disabilities Act (ASA) and University policies. For more information, go to http://academicsupport.georgetown.edu/disability/.

Important Academic Policies and Academic Integrity
:  McCourt School students are expected to uphold the academic policies set forth by Georgetown University and the Graduate School of Arts and Sciences. Students should therefore familiarize themselves with all the rules, regulations, and procedures relevant to their pursuit of a Graduate School degree. The policies are located at: http://grad.georgetown.edu/academics/policies/


Statement on Sexual Misconduct
:  Please know that as a faculty member I am committed to supporting survivors of sexual misconduct, including relationship violence, sexual harassment and sexual assault.  However, university policy also requires me to report any disclosures about sexual misconduct to the Title IX Coordinator, whose role is to coordinate the University’s response to sexual misconduct. 

   Georgetown has a number of fully confidential professional resources who can provide support and assistance to survivors of sexual assault and other forms of sexual misconduct.  These resources include:
   
   ````{panels}
   Jen Schweer, MA, LPC
   ^^^
   Associate Director of Health Education Services for Sexual Assault Response and Prevention
   - (202) 687-0323
   - jls242@georgetown.edu

   ---
   Erica Shirley, Trauma Specialist
   ^^^
   Counseling and Psychiatric Services (CAPS)
   - (202) 687-6985
   - els54@georgetown.edu

   ````

   More information about campus resources and reporting sexual misconduct can be found at http://sexualassault.georgetown.edu.

Provost’s Policy Accommodating Students’ Religious Observances
:  Georgetown University promotes respect for all religions.  Any student who is unable to attend classes or to participate in any examination, presentation, or assignment on a given day because of the observance of a major religious holiday or related travel shall be excused and provided with the opportunity to make up, without unreasonable burden, any work that has been missed for this reason and shall not in any other way be penalized for the absence or rescheduled work. Students will remain responsible for all assigned work. Students should notify professors in writing at the beginning of the semester of religious observances that conflict with their classes. The Office of the Provost, in consultation with Campus Ministry and the Registrar, will publish, before classes begin for a given term, a list of major religious holidays likely to affect Georgetown students.  The Provost and the Main Campus Executive Faculty encourage faculty to accommodate students whose bona fide religious observances in other ways impede normal participation in a course.  Students who cannot be accommodated should discuss the matter with an advising dean.
