<h1>BrightDocs</h1>
In a nutshell, BrightDocs is a web-based document automation app. The process
is envisioned as follows:

* User creates a blueprint
* User uploads documents (currently docx, pdf, xslx and email) for the blueprint
* User creates "triggers" (conditional statements) using variables
embedded in the uploaded documents. User can also define their own variables
outside of the documents. As an example, variable `plaintiff_gender`
can be created. The user can then combine this variable with another
variable like `plaintiff_he_she` to create a trigger that goes something
like:

```IF plaintiff_gender EQUALS "female", THEN plaintiff_he_she BECOMES "she"```

* This trigger would, if the user assigns "female" to the
`plaintiff_gender` variable, would simply replace all instances of
`plaintiff_he_she` with "she". In an excel spreadsheet, this applies
to all cells in rows or columns with an initial cell value of
`plaintiff_he_she`. In a pdf, it fills in all form fields with that
name.

* User clicks a big shiny `Run Blueprint` button. He/she fills in
whichever variables he/she chooses, then clicks an even bigger and
shinier `Create documents` button. Variables are automatically filled
based on the manually assigned variables as well as the values of the
variables filled in the preceding statements.

* Documents are bundled into a zip, which is then served to the user.

* ??

* Exponential user growth, profit, and a multi-billion dollar buyout
from Facebook/Google/Amazon.